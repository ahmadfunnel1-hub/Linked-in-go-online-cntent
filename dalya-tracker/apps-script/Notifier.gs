/******************************************************************
 * Notifier.gs — تراكر داليا ← مهام وتنبيهات GoHighLevel
 * ضيفه كملف جديد بنفس مشروع Apps Script (جنب Code.gs).
 * بيستعمل من Code.gs: getTargetSheet, getLayout, getTaskRows, cell,
 *                    DEFAULT_GID, SPREADSHEET_ID
 *
 * شو بيعمل حسب التايم لاين:
 *  1) قبل Start بـ LEAD_DAYS يوم ← Task بـ GHL للشخص (عمود Owner التاني)،
 *     وموعد التسليم = يوم End. (المهام اللي بلّشت وما خلصت بتنعمل فوراً)
 *  2) الحالة صارت Done (من التراكر أو من الشيت) ← المهمة بتنسكّر بـ GHL.
 *  3) للمهمة Dependency وخلص اللي قبلها ← بتنعمل فوراً «دورك الآن» + إيميل.
 *  4) عدّى End وما خلصت ← Task «متأخرة» للمدير (MANAGER).
 *  5) إيميل الصبح لكل شخص: شو بيبدأ اليوم/بكرا، شو بينتهي اليوم، وشو متأخر.
 *
 * Script Properties (⚙️ Project Settings ← Script Properties):
 *   GHL_TOKEN        Private Integration token (pit-…)
 *   GHL_LOCATION_ID  ID الساب أكاونت
 *   GHL_CONTACT_ID   (اختياري) الكونتاكت اللي بتنحط عليه المهام — إذا فاضي بينعمل لحاله
 *
 * الترتيب: setupNotifier ← testNotifier ← installNotifier
 ******************************************************************/

const NOTIFY = {
  PROJECT_LABEL: "داليا",
  TRACKER_URL: "",          // رابط صفحة التراكر بـ GHL — بينحط جوّا كل مهمة (اختياري)
  GIDS: [],                 // تابات الشيت اللي منتابعها (فاضي = DEFAULT_GID)
  YEAR: 2026,               // للتواريخ اللي ما فيها سنة مثل «02 نوفمبر»
  LEAD_DAYS: 1,             // كم يوم قبل Start تنعمل المهمة (0 = يوم البداية نفسه)
  DUE_HOUR: 17,             // ساعة التسليم بيوم End
  RUN_HOUR: 9,              // ساعة التشغيل اليومي (حسب Time zone المشروع)
  TEAM: {                   // اسم بالشيت ← مستخدم GHL (userId أو إيميل أو اسمه بـ GHL)
    // "Otaibi": "name@adscope.com",
    // "Shabib": "aBcD1234userId",
  },                        // اللي مش مكتوب هون بيتطابق لحاله بالاسم
  CLIENT_NAMES: ["Dalya"],  // أسماء فريق العميل (مش مستخدمين بـ GHL)
  CLIENT_FOLLOWUP: "",      // مين من فريقك بيتابع مهام العميل (اسم أو إيميل) — لازم تعبّيه
  MANAGER: "",              // مين بيوصله تنبيه التأخير (فاضي = بلا تنبيه تأخير)
  EMAIL_DIGEST: true,       // إيميل الصبح + إيميل «دورك الآن» (false = بس مهام GHL)
  GHL_VERSION: "2021-07-28",
};

let NOTIFY_DRY_ = false;

/* ======================= خطوات التركيب ======================= */

// 1) بيتأكد من التوكن وبيطابق أسماء الشيت مع مستخدمين GHL. ما بيعمل ولا مهمة.
function setupNotifier() {
  requireProps_();
  CacheService.getScriptCache().remove("ghl_users");
  const users = ghlUsers_();
  const out = ["مستخدمين GHL (" + users.length + "):"];
  users.forEach(u => out.push("  • " + u.name + "  <" + u.email + ">  id=" + u.id));
  out.push("", "مطابقة الأسماء من الشيت:");
  let bad = 0;
  gids_().forEach(gid => {
    const { tasks } = readTasks_(getTargetSheet(gid));
    uniq_([].concat.apply([], tasks.map(t => t.people))).forEach(n => {
      const a = resolveAssignee_(n, users);
      if (a.error) bad++;
      out.push(a.error ? "  ❌ " + n + " ← " + a.error
                       : "  ✅ " + n + " ← " + a.user.name + (a.isClient ? "  (متابعة العميل)" : ""));
    });
  });
  if (NOTIFY.MANAGER) {
    const m = resolveName_(NOTIFY.MANAGER, users);
    out.push("المدير: " + (m.user ? "✅ " + m.user.name : "❌ " + m.error));
  } else out.push("المدير: (فاضي — ما في تنبيه تأخير)");
  out.push("", bad ? "⚠️ صلّح الأسماء اللي عليها ❌ (بـ NOTIFY.TEAM أو CLIENT_FOLLOWUP) وشغّل setupNotifier كمان مرة."
                   : "👌 كل الأسماء تمام. الخطوة الجاية: testNotifier");
  console.log(out.join("\n"));
}

// 2) تجربة بدون تنفيذ: بيطبع شو كان رح يصير اليوم.
function testNotifier() {
  requireProps_();
  NOTIFY_DRY_ = true;
  try {
    gids_().forEach(gid => {
      const r = processSheet_(getTargetSheet(gid), { escalate: true });
      console.log("🧪 تجربة (ولا شي انبعت):\n" + (r.log.join("\n") || "(ولا شي اليوم)"));
      if (NOTIFY.EMAIL_DIGEST) sendDigests_(r);
    });
  } finally { NOTIFY_DRY_ = false; }
}

// 3) بيركّب التشغيل اليومي + مزامنة تعديلات الشيت، وبيشغّل أول دورة حقيقية.
function installNotifier() {
  requireProps_();
  removeNotifier();
  ScriptApp.newTrigger("dailyRun").timeBased().everyDays(1).atHour(NOTIFY.RUN_HOUR).create();
  try { ScriptApp.newTrigger("onSheetEdit").forSpreadsheet(SPREADSHEET_ID).onEdit().create(); }
  catch (e) { console.warn("ما قدرت أركّب تريغر تعديل الشيت (" + e.message + ") — التعديل اليدوي بالشيت رح يتزامن الصبح بس."); }
  console.log("✅ تركّب: كل يوم الساعة " + NOTIFY.RUN_HOUR + " + مزامنة لما يتعدّل الشيت. هلق أول دورة…");
  dailyRun();
}

// بيوقف كل شي (المهام الموجودة بـ GHL بتضل).
function removeNotifier() {
  ScriptApp.getProjectTriggers().forEach(t => {
    if (["dailyRun", "onSheetEdit"].indexOf(t.getHandlerFunction()) > -1) ScriptApp.deleteTrigger(t);
  });
}

/* ======================= التشغيل ======================= */

function dailyRun() {
  if (!notifierReady_()) return;
  const lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    gids_().forEach(gid => {
      const r = processSheet_(getTargetSheet(gid), { escalate: true });
      console.log(r.log.join("\n") || "ولا تغيير");
      if (NOTIFY.EMAIL_DIGEST) sendDigests_(r);
    });
  } finally { lock.releaseLock(); }
}

// بتنادى من doPost (Code.gs) بعد ما تتغير الحالة من التراكر.
function notifyAfterStatusChange_(sheet) {
  if (!notifierReady_()) return;
  SpreadsheetApp.flush();
  const r = processSheet_(sheet, { escalate: false });
  if (r.log.length) console.log(r.log.join("\n"));
}

// تريغر installable: لما حدا يعدّل الحالة/الشخص/التواريخ بالشيت مباشرة.
function onSheetEdit(e) {
  try {
    if (!e || !e.range || !notifierReady_()) return;
    const sh = e.range.getSheet();
    if (gids_().indexOf(sh.getSheetId()) < 0) return;
    const L = getLayout(sh);
    if (e.range.getLastRow() <= L.headerRow) return;
    const c1 = e.range.getColumn() - 1, c2 = e.range.getLastColumn() - 1;
    if (![L.status, L.assignee, L.start, L.end].some(c => c >= c1 && c <= c2)) return;
    const lock = LockService.getScriptLock();
    if (!lock.tryLock(20000)) return;
    try { console.log(processSheet_(sh, { escalate: false }).log.join("\n")); }
    finally { lock.releaseLock(); }
  } catch (err) { console.error("onSheetEdit: " + err); }
}

/* ======================= المنطق ======================= */

function processSheet_(sheet, opts) {
  opts = opts || {};
  const gid = sheet.getSheetId(), users = ghlUsers_(), st = loadState_(), T = today_();
  const tasks = readTasks_(sheet).tasks, byId = {}, log = [], assigned = [];
  tasks.forEach(t => { byId[t.id] = t; });
  let contact = null;
  const cid = () => contact || (contact = projectContactId_());

  tasks.forEach(t => {
    try {
      const key = gid + "|" + hash_(t.phase + "|" + t.task), done = t.status === "Done";
      if (!t.S) { if (!done) log.push("• #" + t.id + " ما إلها Start — تخطّيتها"); return; }
      if (!t.people.length) { if (!done) log.push("• #" + t.id + " ما في اسم بعمود Owner التاني"); return; }
      const depsDone = t.deps.length > 0 && t.deps.every(d => byId[d] && byId[d].status === "Done");
      const inWindow = T >= addDays_(t.S, -NOTIFY.LEAD_DAYS);
      const seen = {};
      let allResolved = true;

      t.people.forEach(p => {
        const a = resolveAssignee_(p, users);
        if (a.error) { allResolved = false; if (!done) log.push("❌ #" + t.id + " " + p + ": " + a.error); return; }
        const uid = a.user.id;
        if (seen[uid]) return;
        seen[uid] = 1;
        assigned.push({ t: t, a: a });
        const k = key + "|" + uid, rec = st[k];

        if (done) {
          if (rec && !rec.done) { setDone_(rec, true); rec.done = true; saveRec_(k, rec); log.push("✔️ #" + t.id + " انسكّرت بـ GHL (" + a.user.name + ")"); }
          return;
        }
        if (rec) {
          if (rec.done) { setDone_(rec, false); rec.done = false; saveRec_(k, rec); log.push("↩️ #" + t.id + " رجعت انفتحت (" + a.user.name + ")"); }
          return;
        }
        if (!inWindow && !depsDone) return;            // لسا بكير
        const handoff = depsDone && !inWindow;          // خلص اللي قبلها قبل موعدها
        const c = cid();
        st[k] = { id: createTask_(c, t, a, handoff), c: c, uid: uid, done: false };
        saveRec_(k, st[k]);
        log.push("➕ #" + t.id + " " + t.task + " ← " + a.user.name + (handoff ? " (دورك الآن)" : ""));
        if (handoff && NOTIFY.EMAIL_DIGEST && a.user.email) {
          mail_(a.user.email, "🔔 [" + NOTIFY.PROJECT_LABEL + "] دورك الآن: #" + t.id + " " + t.task,
            "<p>المهام السابقة اكتملت ✅ — يمكنك البدء في <b>#" + t.id + " " + esc_(t.task) + "</b>.</p>" +
            "<p>" + fmtDay_(t.S) + " ← " + fmtDay_(t.E) + "</p>" + trackerLink_());
        }
      });

      // شخص انشال من المهمة (أو انسكّرت والشخص تغيّر) ← سكّر مهمته القديمة
      if (allResolved) Object.keys(st).forEach(k => {
        if (k.indexOf(key + "|") !== 0 || k === key + "|late") return;
        const rec = st[k];
        if (rec.done || seen[rec.uid]) return;
        setDone_(rec, true); rec.done = true; saveRec_(k, rec);
        log.push("✖️ #" + t.id + " انسكّرت لمستخدم ما عاد مسؤول عنها");
      });

      // التأخير ← تنبيه للمدير (مرة وحدة لكل مهمة)
      const lk = key + "|late", lrec = st[lk];
      if (done) {
        if (lrec && !lrec.done) { setDone_(lrec, true); lrec.done = true; saveRec_(lk, lrec); }
      } else if (!lrec && opts.escalate && NOTIFY.MANAGER && t.E < T) {
        const m = resolveName_(NOTIFY.MANAGER, users);
        if (!m.user) log.push("❌ المدير: " + m.error);
        else {
          const c = cid();
          st[lk] = { id: createLateTask_(c, t, m.user, T), c: c, uid: m.user.id, done: false };
          saveRec_(lk, st[lk]);
          log.push("⚠️ #" + t.id + " متأخرة " + daysWord_(diffDays_(t.E, T)) + " ← تنبيه لـ " + m.user.name);
        }
      }
    } catch (e) { log.push("❗ #" + t.id + ": " + e.message); }
  });
  return { gid: gid, today: T, tasks: tasks, assigned: assigned, log: log };
}

function createTask_(contactId, t, a, handoff) {
  const prefix = handoff ? "🔔 دورك الآن: " : a.isClient ? "👤 متابعة مع العميل: " : "";
  const body = [
    "المشروع: " + NOTIFY.PROJECT_LABEL + " · المرحلة: " + t.phase,
    "المسؤول في الشيت: " + t.assignee + (t.owner ? " (" + t.owner + ")" : ""),
    "من " + fmtDay_(t.S) + " إلى " + fmtDay_(t.E) + " · " + daysWord_(diffDays_(t.S, t.E) + 1),
    t.deps.length ? "بعد المهام: " + t.deps.map(d => "#" + d).join("، ") : "",
    handoff ? "✅ المهام السابقة اكتملت — يمكنك البدء الآن." : "",
    NOTIFY.TRACKER_URL ? "التراكر: " + NOTIFY.TRACKER_URL : "",
    "عند الانتهاء: غيّر الحالة في التراكر إلى «مكتمل» وستُغلق هذه المهمة تلقائياً.",
  ].filter(Boolean).join("\n");
  return postTask_(contactId, {
    title: prefix + "[" + NOTIFY.PROJECT_LABEL + "] #" + t.id + " " + t.task,
    body: body, dueDate: dueIso_(t.E), completed: false, assignedTo: a.user.id,
  });
}

function createLateTask_(contactId, t, mgr, T) {
  return postTask_(contactId, {
    title: "⚠️ متأخرة: [" + NOTIFY.PROJECT_LABEL + "] #" + t.id + " " + t.task + " — " + t.assignee,
    body: [
      "كان موعد التسليم " + fmtDay_(t.E) + " · متأخرة " + daysWord_(diffDays_(t.E, T)),
      "المسؤول: " + t.assignee + " · الحالة: " + t.status,
      NOTIFY.TRACKER_URL ? "التراكر: " + NOTIFY.TRACKER_URL : "",
    ].filter(Boolean).join("\n"),
    dueDate: dueIso_(T), completed: false, assignedTo: mgr.id,
  });
}

function sendDigests_(r) {
  const T = r.today, tomorrow = addDays_(T, 1), per = {};
  r.assigned.forEach(x => {
    const t = x.t;
    if (t.status === "Done" || !t.S) return;
    let tag = null;
    if (t.E < T) tag = "⚠️ متأخرة " + daysWord_(diffDays_(t.E, T));
    else if (+t.E === +T) tag = "⏰ تنتهي اليوم";
    else if (+t.S === +T) tag = "🟢 تبدأ اليوم";
    else if (+t.S === +tomorrow) tag = "⏭️ تبدأ غداً";
    if (!tag) return;
    const u = x.a.user;
    (per[u.id] = per[u.id] || { user: u, items: [] }).items.push({ t: t, tag: tag, client: x.a.isClient });
  });
  Object.keys(per).forEach(id => {
    const p = per[id];
    if (!p.user.email) return;
    const li = p.items.map(i => "<li><b>" + i.tag + "</b> — #" + i.t.id + " " + esc_(i.t.task) +
      (i.client ? " (متابعة مع العميل)" : "") + "<br><small>" + fmtDay_(i.t.S) + " ← " + fmtDay_(i.t.E) +
      " · " + esc_(i.t.status) + "</small></li>").join("");
    mail_(p.user.email, "[" + NOTIFY.PROJECT_LABEL + "] مهامك اليوم (" + p.items.length + ")",
      "<p>صباح الخير " + esc_(p.user.firstName || p.user.name) + " 👋</p><ul>" + li + "</ul>" + trackerLink_());
  });
}

/* ======================= الشيت ======================= */

function readTasks_(sheet) {
  const L = getLayout(sheet), rows = getTaskRows(sheet, L);
  if (!rows.length) return { L: L, tasks: [] };
  const first = rows[0].row, n = rows[rows.length - 1].row - first + 1;
  const raw = sheet.getRange(first, 1, n, L.lastCol).getValues();
  const tz = sheet.getParent().getSpreadsheetTimeZone();
  const tasks = rows.map((r, k) => {
    const rv = raw[r.row - first];
    let S = parseSheetDate_(rv[L.start], cell(r.v, L.start), tz);
    let E = parseSheetDate_(rv[L.end], cell(r.v, L.end), tz) || S;
    if (S && E && E < S) { const x = S; S = E; E = x; }
    const assignee = cell(r.v, L.assignee);
    return {
      id: k + 1, row: r.row,                       // نفس الترقيم تبع doGet والتراكر
      phase: cell(r.v, L.phase) || "عام",
      task: cell(r.v, L.task) || ("مهمة #" + (k + 1)),
      owner: cell(r.v, L.owner), assignee: assignee, people: splitPeople_(assignee),
      status: normStatus_(cell(r.v, L.status)), S: S, E: E,
      deps: (digits_(cell(r.v, L.dependency)).match(/\d+/g) || []).map(Number),
    };
  });
  return { L: L, tasks: tasks };
}

const MONTHS_ = {"يناير":0,"كانون الثاني":0,"jan":0,"january":0,"فبراير":1,"شباط":1,"feb":1,"february":1,"مارس":2,"آذار":2,"mar":2,"march":2,"أبريل":3,"ابريل":3,"إبريل":3,"نيسان":3,"apr":3,"april":3,"مايو":4,"أيار":4,"may":4,"يونيو":5,"يونيه":5,"حزيران":5,"jun":5,"june":5,"يوليو":6,"يوليه":6,"تموز":6,"jul":6,"july":6,"أغسطس":7,"اغسطس":7,"آب":7,"aug":7,"august":7,"سبتمبر":8,"أيلول":8,"sep":8,"sept":8,"september":8,"أكتوبر":9,"اكتوبر":9,"تشرين الأول":9,"oct":9,"october":9,"نوفمبر":10,"تشرين الثاني":10,"nov":10,"november":10,"ديسمبر":11,"كانون الأول":11,"dec":11,"december":11};

function parseSheetDate_(raw, disp, tz) {
  if (raw instanceof Date && !isNaN(raw)) {
    const p = Utilities.formatDate(raw, tz, "yyyy-M-d").split("-");
    return new Date(+p[0], +p[1] - 1, +p[2]);
  }
  const s = digits_(disp || raw || "").trim().toLowerCase(), Y = NOTIFY.YEAR || new Date().getFullYear();
  if (!s || s === "—" || s === "-") return null;
  let m = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/);
  if (m) return new Date(+m[1], +m[2] - 1, +m[3]);
  m = s.match(/^(\d{1,2})[\/.](\d{1,2})(?:[\/.](\d{2,4}))?$/);
  if (m) return new Date(m[3] ? (+m[3] < 100 ? 2000 + +m[3] : +m[3]) : Y, +m[2] - 1, +m[1]);
  m = s.match(/^(\d{1,2})\s+([^\d]+?)\s*(\d{4})?$/);
  if (m && MONTHS_[m[2].trim()] != null) return new Date(m[3] ? +m[3] : Y, MONTHS_[m[2].trim()], +m[1]);
  m = s.match(/^([^\d]+?)\s+(\d{1,2}),?\s*(\d{4})?$/);
  if (m && MONTHS_[m[1].trim()] != null) return new Date(m[3] ? +m[3] : Y, MONTHS_[m[1].trim()], +m[2]);
  return null;
}

function splitPeople_(s) {
  return String(s || "").split(/\s*(?:\+|,|،|&|\/| و )\s*/).map(x => x.trim()).filter(Boolean);
}
function normStatus_(s) {
  s = String(s || "").trim().toLowerCase();
  if (s === "done" || s === "مكتمل") return "Done";
  if (s === "pending" || s === "in progress" || s === "قيد التنفيذ") return "Pending";
  return "Not Started";
}

/* ======================= GHL ======================= */

function ghl_(method, path, body) {
  const token = PropertiesService.getScriptProperties().getProperty("GHL_TOKEN");
  const opt = {
    method: method, muteHttpExceptions: true,
    headers: { Authorization: "Bearer " + token, Version: NOTIFY.GHL_VERSION, Accept: "application/json" },
  };
  if (body) { opt.contentType = "application/json"; opt.payload = JSON.stringify(body); }
  for (let i = 0; i < 3; i++) {
    const r = UrlFetchApp.fetch("https://services.leadconnectorhq.com" + path, opt);
    const code = r.getResponseCode(), txt = r.getContentText();
    if (code === 429 || code >= 500) { Utilities.sleep(1500 * (i + 1)); continue; }
    if (code >= 300) throw new Error("GHL " + method.toUpperCase() + " " + path + " → " + code + ": " + txt.slice(0, 300));
    try { return JSON.parse(txt || "{}"); } catch (_) { return {}; }
  }
  throw new Error("GHL مشغول (429/5xx) " + path);
}

function ghlUsers_() {
  const cache = CacheService.getScriptCache(), hit = cache.get("ghl_users");
  if (hit) return JSON.parse(hit);
  const loc = PropertiesService.getScriptProperties().getProperty("GHL_LOCATION_ID");
  const j = ghl_("get", "/users/?locationId=" + encodeURIComponent(loc));
  const users = (j.users || []).filter(u => !u.deleted).map(u => ({
    id: u.id, email: u.email || "", firstName: u.firstName || "", lastName: u.lastName || "",
    name: u.name || [u.firstName, u.lastName].filter(Boolean).join(" ") || u.email || u.id,
  }));
  cache.put("ghl_users", JSON.stringify(users), 21600);
  return users;
}

function projectContactId_() {
  const p = PropertiesService.getScriptProperties();
  let id = p.getProperty("GHL_CONTACT_ID");
  if (id) return id;
  if (NOTIFY_DRY_) return "DRY_CONTACT";
  const j = ghl_("post", "/contacts/", {
    locationId: p.getProperty("GHL_LOCATION_ID"), firstName: "مشروع", lastName: NOTIFY.PROJECT_LABEL,
    tags: ["project-tracker"], source: "Project Tracker",
  });
  id = j.contact && j.contact.id;
  if (!id) throw new Error("ما قدرت أعمل كونتاكت المشروع: " + JSON.stringify(j).slice(0, 200));
  p.setProperty("GHL_CONTACT_ID", id);
  return id;
}

function postTask_(contactId, payload) {
  if (NOTIFY_DRY_) return "DRY";
  const j = ghl_("post", "/contacts/" + contactId + "/tasks", payload);
  const id = (j.task && (j.task.id || j.task._id)) || j.id;
  if (!id) throw new Error("GHL ما رجّع id للمهمة: " + JSON.stringify(j).slice(0, 200));
  return id;
}

function setDone_(rec, done) {
  if (NOTIFY_DRY_) return;
  try { ghl_("put", "/contacts/" + rec.c + "/tasks/" + rec.id + "/completed", { completed: !!done }); }
  catch (e) {
    if (/→ (400|404)/.test(e.message)) console.warn("المهمة " + rec.id + " مش موجودة بـ GHL (يمكن انمسحت) — تجاهلتها");
    else throw e;
  }
}

/* ======================= الأسماء ======================= */

function norm_(s) { return String(s || "").toLowerCase().replace(/[^a-z0-9؀-ۿ]+/g, " ").trim(); }

function findUser_(q, users) {
  q = String(q || "").trim();
  if (!q) return null;
  const byId = users.filter(u => u.id === q)[0];
  if (byId) return byId;
  if (q.indexOf("@") > -1) return users.filter(u => u.email.toLowerCase() === q.toLowerCase())[0] || null;
  const n = norm_(q), compact = n.replace(/ /g, "");
  const hits = users.filter(u => {
    const tokens = norm_([u.name, u.firstName, u.lastName, u.email.split("@")[0]].join(" ")).split(" ");
    const full = norm_(u.name).replace(/ /g, "");
    return full === compact || tokens.indexOf(n) > -1 || (compact.length >= 4 && full.indexOf(compact) > -1);
  });
  return hits.length === 1 ? hits[0] : hits.length > 1 ? { ambiguous: hits } : null;
}

// بيطبّق NOTIFY.TEAM وبعدين بيدوّر بمستخدمين GHL.
function resolveName_(q, users) {
  const key = Object.keys(NOTIFY.TEAM).filter(k => norm_(k) === norm_(q))[0];
  const want = key ? NOTIFY.TEAM[key] : q;
  const u = findUser_(want, users);
  if (!u) return { error: "ما لقيت مستخدم GHL «" + want + "» — حطه بـ NOTIFY.TEAM" };
  if (u.ambiguous) return { error: "في أكتر من مستخدم: " + u.ambiguous.map(x => x.name).join("، ") + " — حدد واحد بـ NOTIFY.TEAM" };
  return { user: u };
}

function resolveAssignee_(person, users) {
  const isClient = NOTIFY.CLIENT_NAMES.some(c => norm_(c) === norm_(person));
  if (isClient && !NOTIFY.CLIENT_FOLLOWUP) return { isClient: true, error: "من فريق العميل — اكتب مين بيتابع معه بـ NOTIFY.CLIENT_FOLLOWUP" };
  const r = resolveName_(isClient ? NOTIFY.CLIENT_FOLLOWUP : person, users);
  r.isClient = isClient;
  return r;
}

/* ======================= الحالة (عشان ما يتكرر شي) ======================= */

function loadState_() {
  const all = PropertiesService.getScriptProperties().getProperties(), st = {};
  Object.keys(all).forEach(k => { if (k.indexOf("nt:") === 0) { try { st[k.slice(3)] = JSON.parse(all[k]); } catch (_) {} } });
  return st;
}
function saveRec_(k, rec) { if (!NOTIFY_DRY_) PropertiesService.getScriptProperties().setProperty("nt:" + k, JSON.stringify(rec)); }

/* ======================= أدوات ======================= */

function notifierReady_() {
  const p = PropertiesService.getScriptProperties();
  return !!(p.getProperty("GHL_TOKEN") && p.getProperty("GHL_LOCATION_ID"));
}
function requireProps_() {
  if (!notifierReady_()) throw new Error("ناقص GHL_TOKEN أو GHL_LOCATION_ID — حطهم من ⚙️ Project Settings ← Script Properties");
}
function gids_() { return (NOTIFY.GIDS && NOTIFY.GIDS.length ? NOTIFY.GIDS : [DEFAULT_GID]).map(Number); }
function hash_(s) {
  return Utilities.base64EncodeWebSafe(Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, s, Utilities.Charset.UTF_8)).slice(0, 12);
}
function today_() { const n = new Date(); return new Date(n.getFullYear(), n.getMonth(), n.getDate()); }
function addDays_(d, k) { return new Date(d.getFullYear(), d.getMonth(), d.getDate() + k); }
function diffDays_(a, b) { return Math.round((b - a) / 86400000); }
function dueIso_(d) { return new Date(d.getFullYear(), d.getMonth(), d.getDate(), NOTIFY.DUE_HOUR, 0, 0).toISOString(); }
const WD_ = ["الأحد", "الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"];
const MO_ = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"];
function fmtDay_(d) { return d ? WD_[d.getDay()] + " " + d.getDate() + " " + MO_[d.getMonth()] : "؟"; }
function daysWord_(n) { return n <= 0 ? "أقل من يوم" : n === 1 ? "يوم واحد" : n === 2 ? "يومين" : n <= 10 ? n + " أيام" : n + " يومًا"; }
function digits_(s) {
  return String(s).replace(/[٠-٩]/g, d => "٠١٢٣٤٥٦٧٨٩".indexOf(d)).replace(/[۰-۹]/g, d => "۰۱۲۳۴۵۶۷۸۹".indexOf(d));
}
function uniq_(a) { return a.filter((x, i) => x && a.indexOf(x) === i); }
function esc_(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]); }
function trackerLink_() { return NOTIFY.TRACKER_URL ? '<p><a href="' + NOTIFY.TRACKER_URL + '">افتح التراكر</a></p>' : ""; }
function mail_(to, subject, html) {
  if (NOTIFY_DRY_) { console.log("✉️ (تجربة) لـ " + to + ": " + subject); return; }
  try {
    MailApp.sendEmail({ to: to, subject: subject, name: "تراكر " + NOTIFY.PROJECT_LABEL,
      htmlBody: '<div dir="rtl" style="font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:1.8">' + html + "</div>" });
  } catch (e) { console.warn("الإيميل ما انبعت لـ " + to + ": " + e.message); }
}

const DEFAULT_GID = 125509369;
const SPREADSHEET_ID = "1Lgjpc5DvoYd3bRELQrYfkw1fQs2twcZ_Kyhw6H81U3Y";
const MAX_HEADER_SEARCH = 30;
const MAX_DATA_ROWS = 60;
const LEGEND_WORDS = ["client team","adscope","both teams","both","launch"];

function json(o) {
  return ContentService.createTextOutput(JSON.stringify(o))
    .setMimeType(ContentService.MimeType.JSON);
}
function getSpreadsheet() {
  try { return SpreadsheetApp.openById(SPREADSHEET_ID); }
  catch (e) { const ss = SpreadsheetApp.getActiveSpreadsheet(); if (ss) return ss; throw e; }
}
function getTargetSheet(gid) {
  const sheets = getSpreadsheet().getSheets();
  const want = (gid != null && gid !== "") ? Number(gid) : DEFAULT_GID;
  return sheets.find(s => s.getSheetId() === want)
      || sheets.find(s => s.getSheetId() === DEFAULT_GID)
      || sheets[0];
}
// Reads the header row once and maps each field to its column index (0-based).
function getLayout(sheet) {
  const lastCol = Math.max(sheet.getLastColumn(), 8);
  const top = sheet.getRange(1, 1, MAX_HEADER_SEARCH, lastCol).getDisplayValues();
  let h = -1;
  for (let r = 0; r < top.length; r++) {
    if (String(top[r][0]).trim().toLowerCase() === "phase" &&
        String(top[r][1]).trim().toLowerCase() === "task") { h = r; break; }
  }
  if (h < 0) h = 2;
  const heads = top[h].map(x => String(x).trim().toLowerCase());
  const owners = [];
  heads.forEach((x, i) => { if (x === "owner") owners.push(i); });
  const idx = name => heads.indexOf(name);
  return {
    headerRow: h + 1, lastCol,
    phase: 0, task: 1,
    owner: owners[0] != null ? owners[0] : 2,
    assignee: owners[1] != null ? owners[1] : -1,
    status: idx("status") >= 0 ? idx("status") : 3,
    start: idx("start") >= 0 ? idx("start") : 4,
    end: idx("end") >= 0 ? idx("end") : 5,
    dependency: idx("dependency") >= 0 ? idx("dependency") : 6,
  };
}
// Returns [{row, values}] for real task rows (one batch read, fast).
function getTaskRows(sheet, L) {
  const lastRow = sheet.getLastRow();
  if (lastRow <= L.headerRow) return [];
  const n = Math.min(lastRow - L.headerRow, MAX_DATA_ROWS);
  const vals = sheet.getRange(L.headerRow + 1, 1, n, L.lastCol).getDisplayValues();
  const out = [];
  for (let i = 0; i < vals.length; i++) {
    const v = vals[i];
    const p = String(v[L.phase]).trim(), t = String(v[L.task]).trim();
    const pl = p.toLowerCase(), tl = t.toLowerCase();
    if (pl === "legend" || tl === "legend") break;
    if (LEGEND_WORDS.includes(pl) && (!t || LEGEND_WORDS.includes(tl))) break;
    if (!p && !t) continue;               // skip empty spacer rows
    out.push({ row: L.headerRow + 1 + i, v });
  }
  return out;
}
function cell(v, i) { return i >= 0 ? String(v[i] || "").trim() : ""; }
function doGet(e) {
  const sheet = getTargetSheet(e && e.parameter ? e.parameter.gid : null);
  const L = getLayout(sheet);
  const tasks = getTaskRows(sheet, L).map((r, k) => ({
    id: k + 1,
    phase: cell(r.v, L.phase) || "عام",
    task: cell(r.v, L.task) || ("مهمة #" + (k + 1)),
    owner: cell(r.v, L.owner),
    assignee: cell(r.v, L.assignee),
    status: cell(r.v, L.status) || "Not Started",
    start: cell(r.v, L.start),
    end: cell(r.v, L.end),
    dependency: cell(r.v, L.dependency),
  }));
  return json({ tasks, count: tasks.length, headerRow: L.headerRow, gid: sheet.getSheetId() });
}
function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(10000);
    let data = {};
    if (e.postData && e.postData.contents) data = JSON.parse(e.postData.contents);
    else if (e.parameter) data = e.parameter;
    const allowed = ["Not Started", "Pending", "Done"];
    if (!data.id || allowed.indexOf(String(data.status)) < 0)
      return json({ success: false, error: "invalid id or status" });
    const sheet = getTargetSheet(data.gid);
    const L = getLayout(sheet);
    const rows = getTaskRows(sheet, L);
    const target = rows[Number(data.id) - 1];
    if (!target) return json({ success: false, error: "task not found" });
    sheet.getRange(target.row, L.status + 1).setValue(String(data.status));
    // ⬇️ جديد: يزامن مهام GHL (يسكّر/يفتح/«دورك الآن»). أي خطأ هون ما بيوقّف الحفظ.
    try { if (typeof notifyAfterStatusChange_ === "function") notifyAfterStatusChange_(sheet); }
    catch (n) { console.error("GHL notify: " + n); }
    return json({ success: true, id: Number(data.id), status: data.status });
  } catch (err) {
    return json({ success: false, error: String(err) });
  } finally {
    try { lock.releaseLock(); } catch (_) {}
  }
}

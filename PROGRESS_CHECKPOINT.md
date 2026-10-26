# SolidCraft 繁體中文全介面中文化與安裝進度記錄

**存檔時間**：2026-10-26 01:18  
**專案路徑**：`H:\我的雲端硬碟\Agent\project\soildcraft`

---

## 📌 今日已完成工作 (Completed)

1. **專案原始碼同步**：
   - 已成功從官方 GitHub 倉庫 Clone 最新版 SolidCraft 完整 Rust 專案。

2. **100% 繁體中文介面字典建置 (`assets/locales/zh-TW.json`)**：
   - 原先 `zh-TW.json` 僅有 1,966 條翻譯，缺失 1,176 條（英文混雜嚴重）。
   - 現已**全數補齊至 3,142 條**，實現 100% 覆蓋率（與 `en.json` 完全一致）。
   - 套用台灣正體 CAD 專業術語標準化：
     - 約束 ➔ **拘束**
     - 渲染 ➔ **彩現**
     - 拉伸 ➔ **擠出**
     - 插件 ➔ **外掛**
     - 保存 ➔ **儲存**
     - 默認 ➔ **預設**
     - 導出 / 導入 ➔ **匯出 / 匯入**
     - 窗口 / 光標 ➔ **視窗 / 游標**
     - 項目 / 本體 ➔ **專案 / 實體**
   - 透過 `cargo xtask lists --fix` 排序與規範化校驗通過。
   - 執行 `cargo xtask i18n` 檢核通過：所有 Complete 語系均無遺漏字串。

3. **預設啟動繁體中文環境**：
   - 修改 [crates/ui-egui/src/prefs.rs](file:///H:/我的雲端硬碟/Agent/project/soildcraft/crates/ui-egui/src/prefs.rs)：將預設語言改為 `zh-TW`。
   - 修改 [crates/ui-egui/src/i18n.rs](file:///H:/我的雲端硬碟/Agent/project/soildcraft/crates/ui-egui/src/i18n.rs)：渲染預設 Locale 設為 `CHINESE_TRADITIONAL`，並將 `zh-TW` 加入完整語系列表。
   - 修改 [xtask/src/i18n.rs](file:///H:/我的雲端硬碟/Agent/project/soildcraft/xtask/src/i18n.rs)：將 `zh-TW` 列為必檢項目。

4. **繁體中文字型渲染優化 (`crates/ui-egui/src/fonts.rs`)**：
   - 於 Windows 字型候選清單中新增 **微軟正黑體 (`msjh.ttc`, `msjh.ttf`)** 與 `jhenghei` / `mingliu` 關鍵字，確保介面高解析度字體清晰優美。

---

## 🚀 明天繼續進行項目 (Next Steps)

1. **編譯安裝**：
   - 執行 `cargo build --release -p solidcraft` 或 `cargo install --path apps/solidcraft`。
2. **桌面捷徑與一鍵啟動**：
   - 建立桌面捷徑與 `啟動SolidCraft.bat`，方便雙擊直接啟動繁體中文 3D CAD。
3. **驗收與展示**：
   - 啟動程式確認全部選單、工具列、特徵樹、對話方塊皆為純正繁體中文。

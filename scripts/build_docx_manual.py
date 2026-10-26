import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_callout(doc, text, title="重點提示", fill_hex="F0F9FF", border_hex="0284C7"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, fill_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    run_title = p.add_run(f"📌 {title}：")
    run_title.font.bold = True
    run_title.font.name = "Microsoft JhengHei"
    run_title.font.size = Pt(10.5)
    run_title.font.color.rgb = RGBColor.from_string(border_hex)
    
    run_text = p.add_run(text)
    run_text.font.name = "Microsoft JhengHei"
    run_text.font.size = Pt(10)
    run_text.font.color.rgb = RGBColor(50, 60, 75)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

doc = Document()

# Set page margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# Normal style font
style_normal = doc.styles['Normal']
style_normal.font.name = 'Microsoft JhengHei'
style_normal.font.size = Pt(10.5)
style_normal.font.color.rgb = RGBColor(30, 41, 59)

# ----------------- COVER PAGE -----------------
if os.path.exists('docs/images/manual_cover.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_after = Pt(12)
    p_img.add_run().add_picture('docs/images/manual_cover.png', width=Inches(6.5))

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(4)
r_t = p_title.add_run("SolidCraft 3D CAD 參數化建模系統")
r_t.font.name = "Microsoft JhengHei"
r_t.font.size = Pt(24)
r_t.font.bold = True
r_t.font.color.rgb = RGBColor(15, 23, 42)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(16)
r_s = p_sub.add_run("官方繁體中文全功能使用手冊與實務指引 (v0.22.1)")
r_s.font.name = "Microsoft JhengHei"
r_s.font.size = Pt(14)
r_s.font.color.rgb = RGBColor(2, 132, 199)

# Meta Table
tbl_meta = doc.add_table(rows=4, cols=2)
tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_data = [
    ("核心技術", "純 Rust 原生開發 · Truck B-Rep 幾何拓撲核心 · 零商業依賴"),
    ("語系標準", "100% 繁體中文全介面 · 台灣標準 CAD 工程術語 · 微軟正黑體優化"),
    ("硬體整合", "Bambu Lab A1 mini 3D 列印公差規格支援 · 輕量化拓撲結構"),
    ("發行版本", "v0.22.1 繁體中文正式版（含 Windows 獨立安裝檔與免安裝綠色版）")
]
for i, (k, v) in enumerate(meta_data):
    c0 = tbl_meta.cell(i, 0)
    c1 = tbl_meta.cell(i, 1)
    set_cell_background(c0, "F1F5F9")
    set_cell_background(c1, "F8FAFC")
    set_cell_margins(c0, 60, 60, 100, 100)
    set_cell_margins(c1, 60, 60, 100, 100)
    p0 = c0.paragraphs[0]
    p1 = c1.paragraphs[0]
    p0.paragraph_format.space_after = Pt(2)
    p1.paragraph_format.space_after = Pt(2)
    r0 = p0.add_run(k)
    r0.font.bold = True
    r0.font.size = Pt(9.5)
    r0.font.color.rgb = RGBColor(71, 85, 105)
    r1 = p1.add_run(v)
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = RGBColor(30, 41, 59)

doc.add_page_break()

# ----------------- SECTION 1 -----------------
h1 = doc.add_heading(level=1)
h1.paragraph_format.space_before = Pt(14)
h1.paragraph_format.space_after = Pt(6)
r = h1.add_run("第一章：SolidCraft 系統架構與專案介紹")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(15, 23, 42)

p = doc.add_paragraph()
p.add_run("SolidCraft 是一款全新世代、乾淨架構（Clean-room）、純 Rust 語言打造的開源參數化 3D CAD 電腦輔助設計軟體。相較於依賴商業授權或老舊架構的傳統 CAD 工具，SolidCraft 具備極速啟動、記憶體安全保證、跨平台原生渲染以及強大的 AI 代理人驅動介面（Model Context Protocol）。")

p = doc.add_paragraph()
p.add_run("本專案已由工程團隊進行深度在地化調校，將全系統 3,142 條操作文字、圖表說明與選單標籤全部轉換為標準「台灣繁體中文」，並將所有幾何約束、特徵生成、歷史樹與檔案操作術語，嚴格依照台灣機械與工業設計慣用標準統一。")

add_callout(doc, "SolidCraft 內部數值計算完全以公釐（mm）與弧度（rad）為基準，Z 軸垂直朝上，完全契合現代 3D 列印機與 CNC 切削機台的座標系規範。", "幾何核心標準", "F0FDF4", "16A34A")

# ----------------- SECTION 2 -----------------
h1 = doc.add_heading(level=1)
h1.paragraph_format.space_before = Pt(16)
h1.paragraph_format.space_after = Pt(6)
r = h1.add_run("第二章：安裝方式與快速啟動指南")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(15, 23, 42)

p = doc.add_paragraph()
p.add_run("為方便在新電腦或不同作業環境中快速部署，本版本提供兩種安裝與執行模式：")

h2 = doc.add_heading(level=2)
r = h2.add_run("1. Windows 一鍵安裝檔 (Setup Wizard)")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(2, 132, 199)

p = doc.add_paragraph()
p.add_run("• 安裝檔案：SolidCraft-v0.22.1-繁體中文安裝檔.exe\n"
          "• 特點：具備標準 Windows 繁體中文安裝精靈，自動將程式安裝至 Program Files、建立桌面捷徑與開始功能表捷徑，並自動將 solidcraft 與 solidcraft-cli 加入系統 PATH 環境變數，亦支援 .solidcraft 設計檔案關聯。")

h2 = doc.add_heading(level=2)
r = h2.add_run("2. 綠色免安裝可攜版 (Portable Edition)")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(2, 132, 199)

p = doc.add_paragraph()
p.add_run("• 封裝檔案：SolidCraft-v0.22.1-繁體中文免安裝版.zip\n"
          "• 特點：隨插即用，解壓縮至隨身碟或任意磁碟資料夾即可使用。內附「啟動SolidCraft.bat」與「一鍵建立桌面捷徑.bat」，適合校園電腦教室或無系統管理員權限之環境。")

# ----------------- SECTION 3 -----------------
h1 = doc.add_heading(level=1)
h1.paragraph_format.space_before = Pt(16)
h1.paragraph_format.space_after = Pt(6)
r = h1.add_run("第三章：繁體中文操作介面全景導覽")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(15, 23, 42)

p = doc.add_paragraph()
p.add_run("SolidCraft 採用極簡且直覺的現代深色介面佈局，整體操作環境劃分為四大主要核心區域：")

if os.path.exists('docs/images/cad_ui_layout.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture('docs/images/cad_ui_layout.png', width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(8)
    r_c = p_cap.add_run("▲ 圖 3-1：SolidCraft 繁體中文版操作介面四大核心佈局圖解")
    r_c.font.size = Pt(9)
    r_c.font.color.rgb = RGBColor(100, 116, 139)

tbl_ui = doc.add_table(rows=5, cols=2)
tbl_ui.alignment = WD_TABLE_ALIGNMENT.CENTER
ui_desc = [
    ("上方功能區 (Ribbon)", "依建模情境劃分標籤頁：【實體】、【草圖】、【曲面】、【鈑金】、【組裝】、【彩現】與【工具】，圖示下方附帶中文功能名稱。"),
    ("左側零件瀏覽器 (Browser)", "階層化樹狀結構：原點基準面（XY、XZ、YZ）、實體本體（Bodies）、草圖集合（Sketches）與模型全局參數變數清單。"),
    ("中央 3D 視圖畫布 (Viewport)", "提供即時硬體加速 3D 視角渲染，內建右上角視圖方塊（Nav Cube）、原點三軸指示器（RGB 對應 XYZ），支援透視與正交投影切換。"),
    ("下方參數化特徵時間軸 (Timeline)", "記錄模型從無到有的所有特徵步驟（草圖、擠出、倒角等）。可自由拖曳「回溯標記」回到過去步驟編輯，並自動聯動更新後續特徵。")
]
for i, (k, v) in enumerate(ui_desc):
    c0 = tbl_ui.cell(i+1, 0)
    c1 = tbl_ui.cell(i+1, 1)
    set_cell_background(c0, "F8FAFC")
    set_cell_margins(c0, 60, 60, 100, 100)
    set_cell_margins(c1, 60, 60, 100, 100)
    c0.paragraphs[0].add_run(k).font.bold = True
    c0.paragraphs[0].runs[0].font.size = Pt(9.5)
    c1.paragraphs[0].add_run(v).font.size = Pt(9.5)

# Header row for table
c0 = tbl_ui.cell(0, 0)
c1 = tbl_ui.cell(0, 1)
set_cell_background(c0, "0284C7")
set_cell_background(c1, "0284C7")
set_cell_margins(c0, 80, 80, 100, 100)
set_cell_margins(c1, 80, 80, 100, 100)
r0 = c0.paragraphs[0].add_run("介面分區")
r0.font.bold = True
r0.font.color.rgb = RGBColor(255, 255, 255)
r1 = c1.paragraphs[0].add_run("功能說明與操作指引")
r1.font.bold = True
r1.font.color.rgb = RGBColor(255, 255, 255)

doc.add_page_break()

# ----------------- SECTION 4 -----------------
h1 = doc.add_heading(level=1)
h1.paragraph_format.space_before = Pt(16)
h1.paragraph_format.space_after = Pt(6)
r = h1.add_run("第四章：參數化建模核心工作流程")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(15, 23, 42)

p = doc.add_paragraph()
p.add_run("參數化 CAD 的精髓在於「幾何關係與數值驅動」。當設計變更時，只需要修改初始草圖的尺寸或幾何條件，整個下游的 3D 實體模型將全自動智慧重新運算重建。")

if os.path.exists('docs/images/parametric_workflow.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture('docs/images/parametric_workflow.png', width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(8)
    r_c = p_cap.add_run("▲ 圖 4-1：SolidCraft 標準參數化特徵建模流程")
    r_c.font.size = Pt(9)
    r_c.font.color.rgb = RGBColor(100, 116, 139)

steps_content = [
    ("步驟一：基準面選取與 2D 草圖繪製", "點選頂部功能區「新建草圖」，選擇 XY、XZ、YZ 基準面或既有實體的平坦表面。使用直線、兩點矩形、中心圓或樣條曲線繪製零件基本截面。"),
    ("步驟二：施加幾何拘束與尺寸驅動標註", "為草圖線條添加幾何拘束：水平/垂直拘束、重合、相切、平行、垂直、同心與相等長度。接著使用標註工具給定精確長度或角度，使草圖線條達到完全拘束狀態。"),
    ("步驟三：3D 特徵成型（擠出 / 旋轉 / 掃略）", "點選「擠出」工具，將封閉草圖輪廓拉伸為 3D 實體；或使用「旋轉」繞基準軸旋轉 360 度成型旋轉體；或沿著導引路徑「掃略」產生管件與複雜曲面。"),
    ("步驟四：細部修飾（圓角 / 倒角 / 薄殼）", "選取實體邊緣施加「圓角」以減少應力集中；使用「倒角」進行組裝導引斜角修飾；利用「薄殼」將實體掏空並指定均勻壁厚。"),
    ("步驟五：參數回溯與設計修改", "隨時在下方特徵時間軸上雙擊任意先前特徵（如「草圖1」），修改任意數值後退出，SolidCraft 會在毫秒內自動重新生成最新 3D 工件。")
]

for title, desc in steps_content:
    h3 = doc.add_heading(level=3)
    r = h3.add_run(f"✦ {title}")
    r.font.name = "Microsoft JhengHei"
    r.font.color.rgb = RGBColor(15, 23, 42)
    p = doc.add_paragraph()
    p.add_run(desc)

# ----------------- SECTION 5 -----------------
h1 = doc.add_heading(level=1)
h1.paragraph_format.space_before = Pt(16)
h1.paragraph_format.space_after = Pt(6)
r = h1.add_run("第五章：3D 列印與 Bambu Lab A1 mini 切片整合實務")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(15, 23, 42)

p = doc.add_paragraph()
p.add_run("針對 Bambu Lab A1 mini 高精度 FDM 列印機，SolidCraft 提供了極佳的模型匯出與拓撲支援。設計工件時請嚴格遵循以下列印規範：")

if os.path.exists('docs/images/a1_mini_print_spec.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture('docs/images/a1_mini_print_spec.png', width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(8)
    r_c = p_cap.add_run("▲ 圖 5-1：Bambu Lab A1 mini 列印安全邊界與卡榫配合公差規格")
    r_c.font.size = Pt(9)
    r_c.font.color.rgb = RGBColor(100, 116, 139)

add_callout(doc, "Bambu Lab A1 mini 最大成型體積為 180×180×180 mm。單一零件之長寬高務必控制在 ≤ 175 mm 以內，預留擦嘴、感應排線與 Brim 裙邊之安全間隙。若超出尺寸，請使用「分割」工具拆件，並建立定位卡榫。", "A1 mini 列印尺寸安全邊界", "FFFBEB", "D97706")

tbl_print = doc.add_table(rows=5, cols=3)
tbl_print.alignment = WD_TABLE_ALIGNMENT.CENTER
print_data = [
    ("固定組裝 / 卡榫", "單邊間隙 0.12 ~ 0.15 mm（總間隙 0.25 ~ 0.30 mm）", "緊配合，免膠水即可牢固扣合"),
    ("旋轉軸孔 / 滑槽", "單邊間隙 0.20 ~ 0.25 mm（總間隙 0.40 ~ 0.50 mm）", "活動機構平滑運轉不卡死"),
    ("推薦匯出格式", "STEP (.step) 或 3MF (.3mf)", "STEP 完整保留數學曲面，切片圓弧極度光滑"),
    ("切片參數建議", "層高 0.20mm、壁厚 3~4 圈、Gyroid 填充 15~20%", "兼顧列印強度與耗材節省")
]
for i, (col1, col2, col3) in enumerate(print_data):
    r_idx = i + 1
    c0 = tbl_print.cell(r_idx, 0)
    c1 = tbl_print.cell(r_idx, 1)
    c2 = tbl_print.cell(r_idx, 2)
    set_cell_background(c0, "F8FAFC")
    set_cell_margins(c0, 60, 60, 80, 80)
    set_cell_margins(c1, 60, 60, 80, 80)
    set_cell_margins(c2, 60, 60, 80, 80)
    c0.paragraphs[0].add_run(col1).font.bold = True
    c0.paragraphs[0].runs[0].font.size = Pt(9)
    c1.paragraphs[0].add_run(col2).font.size = Pt(9)
    c2.paragraphs[0].add_run(col3).font.size = Pt(9)

# Header
for idx, text in enumerate(["項目", "規格與參數設定", "設計效益說明"]):
    c = tbl_print.cell(0, idx)
    set_cell_background(c, "10B981")
    set_cell_margins(c, 80, 80, 80, 80)
    r_h = c.paragraphs[0].add_run(text)
    r_h.font.bold = True
    r_h.font.color.rgb = RGBColor(255, 255, 255)

doc.add_page_break()

# ----------------- SECTION 6 -----------------
h1 = doc.add_heading(level=1)
h1.paragraph_format.space_before = Pt(16)
h1.paragraph_format.space_after = Pt(6)
r = h1.add_run("第六章：AI 代理人協同建模 (Model Context Protocol)")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(15, 23, 42)

p = doc.add_paragraph()
p.add_run("SolidCraft 領先全球原生內建 Model Context Protocol (MCP) 伺服器，可直接銜接現代大型語言模型（LLM）。AI 代理人可透過背景通訊埠或命令列，直接調用 SolidCraft 建立幾何、修改尺寸或導出分析報告。")

p = doc.add_paragraph()
p.add_run("本安裝版本已自動為您的系統註冊 MCP 支援：\n"
          "• 註冊平台：Gemini、VS Code、Claude Desktop、Opencode 等 AI 工具。\n"
          "• 調用範例：只需在 AI 對話中輸入「幫我建立一個 50x50x20mm 底座並挖出 M4 螺絲孔」，AI 即可自動調用 solidcraft-cli 執行腳本並將 3D 模型繪製完成。")

# ----------------- SECTION 7 -----------------
h1 = doc.add_heading(level=1)
h1.paragraph_format.space_before = Pt(16)
h1.paragraph_format.space_after = Pt(6)
r = h1.add_run("第七章：常用快捷鍵與操作技巧速查表")
r.font.name = "Microsoft JhengHei"
r.font.color.rgb = RGBColor(15, 23, 42)

tbl_keys = doc.add_table(rows=9, cols=3)
tbl_keys.alignment = WD_TABLE_ALIGNMENT.CENTER
key_data = [
    ("滑鼠右鍵拖曳", "旋轉視角 (Orbit)", "3D 空間自由環顧旋轉工件"),
    ("滑鼠滾輪按下拖曳 / Shift + 右鍵", "平移視圖 (Pan)", "平行移動視角視野"),
    ("滑鼠滾輪滾動", "縮放視圖 (Zoom)", "預設朝向游標所在位置放大縮小"),
    ("空白鍵 (Space)", "快捷工具搜尋箱", "彈出快速鍵指令輸入方塊"),
    ("Ctrl + Z / Ctrl + Y", "復原 / 重做", "多層級操作步驟復原與重複"),
    ("L / R / C", "直線 / 矩形 / 圓形", "草圖繪製模式下的即時工具切換"),
    ("D", "尺寸標註 (Dimension)", "為選取之線段或兩點添加精確尺寸"),
    ("E", "實體擠出 (Extrude)", "快速將目前草圖輪廓拉伸為 3D 實體")
]

for idx, text in enumerate(["快捷按鍵 / 滑鼠手勢", "操作功能", "說明"]):
    c = tbl_keys.cell(0, idx)
    set_cell_background(c, "6366F1")
    set_cell_margins(c, 80, 80, 80, 80)
    r_h = c.paragraphs[0].add_run(text)
    r_h.font.bold = True
    r_h.font.color.rgb = RGBColor(255, 255, 255)

for i, (col1, col2, col3) in enumerate(key_data):
    r_idx = i + 1
    c0 = tbl_keys.cell(r_idx, 0)
    c1 = tbl_keys.cell(r_idx, 1)
    c2 = tbl_keys.cell(r_idx, 2)
    set_cell_background(c0, "F8FAFC")
    set_cell_margins(c0, 60, 60, 80, 80)
    set_cell_margins(c1, 60, 60, 80, 80)
    set_cell_margins(c2, 60, 60, 80, 80)
    c0.paragraphs[0].add_run(col1).font.bold = True
    c0.paragraphs[0].runs[0].font.size = Pt(9)
    c1.paragraphs[0].add_run(col2).font.size = Pt(9)
    c2.paragraphs[0].add_run(col3).font.size = Pt(9)

# Save document
out_path = 'SolidCraft_3D_CAD_繁體中文使用說明書.docx'
doc.save(out_path)
print(f"Saved {out_path} successfully!")

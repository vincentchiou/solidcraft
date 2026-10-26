import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

os.makedirs('docs/images', exist_ok=True)

# Set font for matplotlib
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'PingFang TC', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 1. UI Layout Diagram (cad_ui_layout.png)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Background
bg = patches.Rectangle((0, 0), 100, 60, facecolor='#1e1e24', edgecolor='#33333d', linewidth=2)
ax.add_patch(bg)

# Top Bar (Menu & Title)
top_bar = patches.Rectangle((0, 54), 100, 6, facecolor='#25252d', edgecolor='#3a3a48', linewidth=1)
ax.add_patch(top_bar)
ax.text(2, 57, "SolidCraft 3D CAD [繁體中文版] - 專案1.solidcraft", color='#ffffff', fontsize=12, fontweight='bold', va='center')
ax.text(80, 57, "說明 | 偏好設定 | 登出", color='#8e8ea0', fontsize=10, va='center')

# Ribbon Bar (Tools)
ribbon = patches.Rectangle((0, 44), 100, 10, facecolor='#2b2b36', edgecolor='#3a3a48', linewidth=1)
ax.add_patch(ribbon)
tabs = ["【實體】", "草圖", "曲面", "鈑金", "組裝", "彩現", "工具"]
for i, tab in enumerate(tabs):
    t_bg = patches.Rectangle((2 + i*13, 50), 12, 4, facecolor='#3d3d4e' if i==0 else '#2b2b36', edgecolor='#525266')
    ax.add_patch(t_bg)
    ax.text(8 + i*13, 52, tab, color='#00d2ff' if i==0 else '#d1d1db', fontsize=9, ha='center', va='center')

tools = ["新建草圖", "擠出", "旋轉", "掃略", "放樣", "圓角", "倒角", "薄殼", "拔模", "分割", "鏡射", "矩形陣列"]
for i, tool in enumerate(tools):
    tool_box = patches.Rectangle((2 + i*8, 44.5), 7.5, 5, facecolor='#363645', edgecolor='#4f4f66', linewidth=0.8)
    ax.add_patch(tool_box)
    ax.text(5.75 + i*8, 47, tool, color='#f0f0f5', fontsize=7.5, ha='center', va='center')

# Left Sidebar (Browser / Feature Tree)
sidebar = patches.Rectangle((0, 8), 24, 36, facecolor='#23232b', edgecolor='#3a3a48', linewidth=1)
ax.add_patch(sidebar)
ax.text(2, 41, "📂 零件瀏覽器 (Browser)", color='#ffb703', fontsize=9.5, fontweight='bold')
browser_items = [
    "▼ 原點 (Origin)",
    "   ├─ XY 基準面",
    "   ├─ XZ 基準面",
    "   └─ YZ 基準面",
    "▼ 實體本體 (Bodies)",
    "   ├─ 實體 1 (Body1)",
    "   └─ 實體 2 (Body2)",
    "▼ 草圖集合 (Sketches)",
    "   ├─ 草圖 1 (底座輪廓)",
    "   └─ 草圖 2 (定位卡榫)"
]
for i, item in enumerate(browser_items):
    ax.text(2, 38 - i*3, item, color='#a0a0b2', fontsize=8)

# Central 3D Viewport
viewport = patches.Rectangle((24, 8), 76, 36, facecolor='#18181f', edgecolor='#3a3a48', linewidth=1)
ax.add_patch(viewport)

# Isometric 3D Model Wireframe / Shaded Box inside Viewport
cube_front = patches.Polygon([[54, 18], [68, 14], [68, 28], [54, 32]], facecolor='#3a86ff', edgecolor='#60a5fa', alpha=0.85, linewidth=1.5)
cube_top = patches.Polygon([[54, 32], [68, 28], [60, 36], [46, 40]], facecolor='#60a5fa', edgecolor='#93c5fd', alpha=0.9, linewidth=1.5)
cube_left = patches.Polygon([[46, 26], [54, 18], [54, 32], [46, 40]], facecolor='#1d4ed8', edgecolor='#3b82f6', alpha=0.85, linewidth=1.5)
ax.add_patch(cube_front)
ax.add_patch(cube_top)
ax.add_patch(cube_left)

# Cylinder Extrusion on top of cube
cyl_patch = patches.Circle((57, 34), 3.5, facecolor='#38bdf8', edgecolor='#7dd3fc', linewidth=1.2)
ax.add_patch(cyl_patch)
ax.text(57, 34, "擠出柱", color='#ffffff', fontsize=7, ha='center', va='center')

# Origin coordinate axes widget
ax.arrow(28, 12, 5, 0, head_width=1.2, head_length=1, fc='#ef4444', ec='#ef4444')
ax.arrow(28, 12, 0, 5, head_width=1.2, head_length=1, fc='#10b981', ec='#10b981')
ax.arrow(28, 12, -3, -2.5, head_width=1.2, head_length=1, fc='#3b82f6', ec='#3b82f6')
ax.text(34, 12, "X", color='#ef4444', fontsize=9, fontweight='bold')
ax.text(28, 18, "Z (向上)", color='#10b981', fontsize=9, fontweight='bold')
ax.text(24, 9, "Y", color='#3b82f6', fontsize=9, fontweight='bold')

# Navigation Cube in Top-Right
nav_box = patches.Rectangle((90, 34), 8, 8, facecolor='#2c2c38', edgecolor='#6366f1', linewidth=1.5)
ax.add_patch(nav_box)
ax.text(94, 38, "上視\n俯瞰", color='#c7d2fe', fontsize=7, ha='center', va='center', fontweight='bold')

# Bottom Timeline (Parametric History)
timeline = patches.Rectangle((0, 0), 100, 8, facecolor='#23232c', edgecolor='#3a3a48', linewidth=1)
ax.add_patch(timeline)
ax.text(2, 4.5, "⏱️ 參數化特徵時間軸 (Timeline)", color='#10b981', fontsize=8.5, fontweight='bold')

steps = ["1. 草圖1", "2. 擠出1", "3. 草圖2", "4. 擠出柱", "5. 圓角", "6. 薄殼", "7. 倒角"]
for i, step in enumerate(steps):
    step_patch = patches.Rectangle((26 + i*10, 1.5), 9, 5, facecolor='#312e81', edgecolor='#6366f1', linewidth=1)
    ax.add_patch(step_patch)
    ax.text(30.5 + i*10, 4, step, color='#e0e7ff', fontsize=7, ha='center', va='center')

plt.tight_layout()
plt.savefig('docs/images/cad_ui_layout.png', dpi=200, bbox_inches='tight')
plt.close()
print("Generated cad_ui_layout.png")

# ==========================================
# 2. Parametric Workflow Diagram (parametric_workflow.png)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 4.2), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 40)
ax.axis('off')

# Title
ax.text(50, 36, "SolidCraft 核心參數化建模流程 (Parametric Design Pipeline)", fontsize=13, fontweight='bold', color='#1e293b', ha='center')

stages = [
    ("步驟一\n選擇基準面\n繪製草圖", "#3b82f6", "2D 幾何圖形\n(線段/矩形/圓形)"),
    ("步驟二\n施加幾何拘束\n與尺寸標註", "#8b5cf6", "幾何約束與數值\n(水平/垂直/共線/相切)"),
    ("步驟三\n3D 特徵成型\n實體建立", "#06b6d4", "特徵動作\n(擠出/旋轉/掃略/放樣)"),
    ("步驟四\n特徵歷史調整\n與幾何修飾", "#10b981", "圓角/倒角/薄殼\n時間軸隨時回溯"),
    ("步驟五\nCAD 成果匯出\n與 3D 列印", "#f59e0b", "STEP / 3MF / STL\n切片至 A1 mini")
]

for i, (title, color, desc) in enumerate(stages):
    x = 3 + i*19.5
    # Card
    card = patches.FancyBboxPatch((x, 6), 17, 24, boxstyle="round,pad=0.6", facecolor='#f8fafc', edgecolor=color, linewidth=2)
    ax.add_patch(card)
    # Header box
    hdr = patches.FancyBboxPatch((x, 20), 17, 10, boxstyle="round,pad=0.3", facecolor=color, edgecolor='none')
    ax.add_patch(hdr)
    ax.text(x + 8.5, 25, title, color='#ffffff', fontsize=8.5, fontweight='bold', ha='center', va='center')
    ax.text(x + 8.5, 13, desc, color='#475569', fontsize=7.5, ha='center', va='center')
    
    # Arrow to next
    if i < 4:
        ax.annotate('', xy=(x + 19, 18), xytext=(x + 17.5, 18),
                    arrowprops=dict(facecolor='#94a3b8', edgecolor='none', width=2, headwidth=6))

plt.tight_layout()
plt.savefig('docs/images/parametric_workflow.png', dpi=200, bbox_inches='tight')
plt.close()
print("Generated parametric_workflow.png")

# ==========================================
# 3. 3D Print Spec Diagram (a1_mini_print_spec.png)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis('off')

# Title
ax.text(50, 46, "Bambu Lab A1 mini 列印規格與公差設計指引", fontsize=13, fontweight='bold', color='#0f172a', ha='center')

# Left Box: Build Volume
card_vol = patches.FancyBboxPatch((4, 4), 42, 38, boxstyle="round,pad=0.5", facecolor='#f1f5f9', edgecolor='#0284c7', linewidth=2)
ax.add_patch(card_vol)
ax.text(25, 38, "🖨️ 成型體積與安全邊界", color='#0369a1', fontsize=10.5, fontweight='bold', ha='center')

# Outer build plate 180x180
outer_plate = patches.Rectangle((12, 10), 26, 24, facecolor='#e0f2fe', edgecolor='#0284c7', linestyle='--', linewidth=1.5)
ax.add_patch(outer_plate)
ax.text(25, 31, "最大體積 180×180×180 mm", color='#0284c7', fontsize=8, ha='center')

# Safe print boundary <= 175mm
inner_plate = patches.Rectangle((14, 12), 22, 20, facecolor='#bae6fd', edgecolor='#0369a1', linewidth=2)
ax.add_patch(inner_plate)
ax.text(25, 22, "★ 安全排版邊界\n長寬高 ≤ 175 mm\n(預留擦嘴與裙邊)", color='#0c4a6e', fontsize=8.5, fontweight='bold', ha='center', va='center')

# Right Box: Tolerance & Split Mechanism
card_tol = patches.FancyBboxPatch((52, 4), 44, 38, boxstyle="round,pad=0.5", facecolor='#f8fafc', edgecolor='#10b981', linewidth=2)
ax.add_patch(card_tol)
ax.text(74, 38, "🧩 拆件與卡榫組裝公差規範", color='#047857', fontsize=10.5, fontweight='bold', ha='center')

# Peg and socket graphic
socket_box = patches.Rectangle((56, 17), 16, 16, facecolor='#dcfce7', edgecolor='#16a34a', linewidth=1.5)
ax.add_patch(socket_box)
# Hole in socket
hole = patches.Rectangle((62, 22), 6, 8, facecolor='#f8fafc', edgecolor='#16a34a', linestyle=':')
ax.add_patch(hole)
ax.text(64, 19, "母卡榫 (槽)", color='#166534', fontsize=7.5, ha='center')

peg_box = patches.Rectangle((78, 17), 14, 16, facecolor='#fee2e2', edgecolor='#dc2626', linewidth=1.5)
ax.add_patch(peg_box)
# Peg protrusion
peg = patches.Rectangle((74, 22.4), 4, 7.2, facecolor='#f87171', edgecolor='#dc2626')
ax.add_patch(peg)
ax.text(85, 19, "公卡榫 (柱)", color='#991b1b', fontsize=7.5, ha='center')

# Tolerances bullet points
ax.text(56, 12, "• 緊配合 (固定卡榫)：單邊間隙 0.12 ~ 0.15 mm", color='#1e293b', fontsize=8)
ax.text(56, 8, "• 旋轉/活動滑槽：單邊間隙 0.20 ~ 0.25 mm", color='#1e293b', fontsize=8)
ax.text(56, 4.5, "• 超出 175mm 自動拆件並預留定位 Peg/Socket", color='#059669', fontsize=8, fontweight='bold')

plt.tight_layout()
plt.savefig('docs/images/a1_mini_print_spec.png', dpi=200, bbox_inches='tight')
plt.close()
print("Generated a1_mini_print_spec.png")

# ==========================================
# 4. Cover Banner (manual_cover.png)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 4), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 40)
ax.axis('off')

# Gradient-like background
bg = patches.Rectangle((0, 0), 100, 40, facecolor='#0f172a')
ax.add_patch(bg)
accent = patches.Rectangle((0, 0), 100, 3, facecolor='#38bdf8')
ax.add_patch(accent)

ax.text(50, 27, "SolidCraft 3D CAD", fontsize=24, fontweight='bold', color='#ffffff', ha='center')
ax.text(50, 19, "純 Rust 開源參數化建模軟體 · 官方繁體中文完整使用手冊", fontsize=12, color='#38bdf8', ha='center', fontweight='bold')
ax.text(50, 11, "100% 繁中化介面 · 台灣標準 CAD 術語 · Bambu Lab 3D 列印整合 · AI 代理人協同驅動", fontsize=9, color='#94a3b8', ha='center')

plt.tight_layout()
plt.savefig('docs/images/manual_cover.png', dpi=200, bbox_inches='tight')
plt.close()
print("Generated manual_cover.png")

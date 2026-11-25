#!/usr/bin/env python3
"""Draw the news-image-20261124 poster: one image summing up Tuesday 24 November 2026.

Local build tool (Pillow). The competition program itself (main.py) is stdlib-only
and copies the rendered entry.png byte-for-byte, per the kit's simplest valid route.
Deterministic: fixed canvas, fixed fonts, no randomness, no network.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 242, 231)       # newsprint cream
INK = (20, 20, 20)
RED = (179, 32, 44)
BLUE = (29, 78, 137)
DARKBLUE = (16, 42, 74)
CELL_BG = (255, 253, 247)
TICKER_BG = (20, 20, 20)
GOLD = (196, 148, 22)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def text_block(x, y, text, font, fill, max_w, leading, max_lines=None):
    lines = wrap(text, font, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        d.text((x, y), line, font=font, fill=fill)
        y += leading
    return y

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 96], fill=INK)
d.text((28, 12), "THE WORLD IN ONE IMAGE", font=F(SERIF_B, 42), fill=(255, 253, 247))
d.text((28, 64), "One picture of the day's world news  •  30 stories  •  every continent",
       font=F(SANS_R, 22), fill=(212, 205, 188))

d.rectangle([0, 96, W, 148], fill=RED)
d.text((28, 104), "TUESDAY  24 NOVEMBER 2026", font=F(SANS_B, 38), fill=(255, 255, 255))
tw = d.textlength("TUESDAY  24 NOVEMBER 2026", font=F(SANS_B, 38))
d.text((28 + tw + 24, 114), "— the day in full, below", font=F(SANS_R, 21), fill=(255, 220, 220))

# ---------------------------------------------------------------- icons
def icon_ship(cx, cy, s, color=DARKBLUE):
    d.polygon([(cx - s, cy + 6), (cx + s, cy + 6), (cx + s - 12, cy + 20), (cx - s + 8, cy + 20)], fill=color)
    d.rectangle([cx - 22, cy - 12, cx + 6, cy + 4], fill=color)
    d.rectangle([cx + 12, cy - 6, cx + 26, cy + 4], fill=color)
    for i in range(3):
        x0 = cx - s + i * 26
        d.arc([x0, cy + 20, x0 + 22, cy + 34], 0, 180, fill=BLUE, width=3)

def icon_burst(cx, cy, s, color=RED):
    pts = []
    for i in range(16):
        r = s if i % 2 == 0 else s * 0.45
        a = math.pi * i / 8
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=color)

def icon_court(cx, cy, s):
    d.polygon([(cx - s, cy - 20), (cx + s, cy - 20), (cx, cy - 38)], fill=DARKBLUE)
    for i in range(4):
        x = cx - s + 7 + i * ((2 * s - 14) // 3)
        d.rectangle([x, cy - 14, x + 8, cy + 20], fill=DARKBLUE)
    d.rectangle([cx - s, cy + 22, cx + s, cy + 29], fill=DARKBLUE)

def icon_talk(cx, cy, s):
    d.rounded_rectangle([cx - s, cy - 26, cx + 4, cy + 6], 9, outline=DARKBLUE, width=5)
    d.polygon([(cx - 18, cy + 6), (cx - 7, cy + 6), (cx - 16, cy + 19)], fill=DARKBLUE)
    d.rounded_rectangle([cx - 3, cy - 10, cx + s, cy + 19], 9, outline=RED, width=5)
    d.polygon([(cx + 19, cy + 19), (cx + 30, cy + 19), (cx + 23, cy + 30)], fill=RED)

def icon_building(cx, cy, s):
    d.rectangle([cx - 22, cy - 32, cx + 8, cy + 30], fill=(70, 70, 70))
    d.rectangle([cx + 12, cy - 15, cx + 32, cy + 30], fill=(110, 106, 96))
    for r in range(3):
        for c in range(2):
            d.rectangle([cx - 16 + c * 13, cy - 24 + r * 17, cx - 8 + c * 13, cy - 15 + r * 17],
                        fill=(250, 220, 120))
    d.ellipse([cx - 2, cy - 54, cx + 22, cy - 32], fill=(150, 146, 138))
    d.ellipse([cx + 10, cy - 60, cx + 38, cy - 38], fill=(170, 166, 158))

def icon_trophy(cx, cy, s):
    d.polygon([(cx - 20, cy - 30), (cx + 20, cy - 30), (cx + 15, cy + 2), (cx - 15, cy + 2)], fill=GOLD)
    d.arc([cx - 36, cy - 28, cx - 12, cy - 2], 90, 270, fill=GOLD, width=5)
    d.arc([cx + 12, cy - 28, cx + 36, cy - 2], 270, 90, fill=GOLD, width=5)
    d.rectangle([cx - 4, cy + 2, cx + 4, cy + 15], fill=GOLD)
    d.rectangle([cx - 15, cy + 15, cx + 15, cy + 24], fill=GOLD)

def icon_heli(cx, cy, s):
    d.ellipse([cx - 26, cy - 8, cx + 18, cy + 15], fill=DARKBLUE)
    d.polygon([(cx + 16, cy - 1), (cx + 42, cy - 9), (cx + 42, cy - 2), (cx + 18, cy + 5)], fill=DARKBLUE)
    d.rectangle([cx + 40, cy - 15, cx + 44, cy + 1], fill=DARKBLUE)
    d.line([cx - 36, cy - 19, cx + 24, cy - 19], fill=INK, width=5)
    d.line([cx - 5, cy - 19, cx - 5, cy - 10], fill=INK, width=4)
    d.line([cx - 20, cy + 21, cx + 14, cy + 21], fill=INK, width=4)

def icon_shop(cx, cy, s):
    d.rectangle([cx - 32, cy - 6, cx + 32, cy + 30], outline=INK, width=4)
    for i in range(5):
        x = cx - 32 + i * 13
        d.polygon([(x, cy - 22), (x + 13, cy - 22), (x + 10, cy - 6), (x + 3, cy - 6)],
                  fill=RED if i % 2 == 0 else (255, 253, 247), outline=INK)
    d.rectangle([cx - 8, cy + 7, cx + 8, cy + 30], fill=DARKBLUE)

def icon_tower(cx, cy, s):
    d.polygon([(cx - 13, cy + 32), (cx - 8, cy - 34), (cx + 8, cy - 34), (cx + 13, cy + 32)], fill=DARKBLUE)
    for r in range(4):
        d.line([cx - 11 + r, cy - 19 + r * 12, cx + 11 - r, cy - 19 + r * 12], fill=(250, 220, 120), width=3)
    icon_burst(cx + 26, cy - 26, 15)

def icon_flame(cx, cy, s):
    d.polygon([(cx, cy - 36), (cx + 17, cy - 5), (cx + 20, cy + 14), (cx + 10, cy + 30),
               (cx - 10, cy + 30), (cx - 20, cy + 14), (cx - 15, cy - 7)], fill=(224, 110, 30))
    d.polygon([(cx, cy - 10), (cx + 9, cy + 7), (cx + 7, cy + 26), (cx - 7, cy + 26),
               (cx - 9, cy + 7)], fill=(245, 180, 40))

def icon_jet(cx, cy, s):
    d.polygon([(cx + 38, cy), (cx - 5, cy - 10), (cx - 26, cy - 29), (cx - 19, cy - 3),
               (cx - 38, cy), (cx - 19, cy + 3), (cx - 26, cy + 29), (cx - 5, cy + 10)], fill=DARKBLUE)
    d.ellipse([cx + 14, cy - 4, cx + 24, cy + 4], fill=(250, 220, 120))

def icon_flag(cx, cy, s):
    d.line([cx - 22, cy - 34, cx - 22, cy + 32], fill=INK, width=5)
    d.polygon([(cx - 22, cy - 34), (cx + 28, cy - 24), (cx - 22, cy - 12)], fill=(0, 130, 80))

def icon_drone_ship(x, y):
    icon_ship(x, y + 12, 34)
    d.line([x - 18, y - 30, x + 18, y - 30], fill=INK, width=4)
    d.line([x, y - 30, x, y - 20], fill=INK, width=3)
    d.ellipse([x - 9, y - 24, x + 9, y - 12], fill=INK)
    d.ellipse([x - 24, y - 36, x - 12, y - 24], outline=INK, width=3)
    d.ellipse([x + 12, y - 36, x + 24, y - 24], outline=INK, width=3)

ICONS = {
    "ship": lambda x, y: (icon_ship(x, y, 34), icon_burst(x + 28, y - 26, 14)),
    "drone_ship": icon_drone_ship,
    "court": lambda x, y: icon_court(x, y, 36),
    "talk": lambda x, y: icon_talk(x, y, 34),
    "building": lambda x, y: icon_building(x, y, 34),
    "trophy": lambda x, y: icon_trophy(x, y, 34),
    "heli": lambda x, y: icon_heli(x, y, 34),
    "shop": lambda x, y: icon_shop(x, y, 34),
    "tower": lambda x, y: icon_tower(x, y, 34),
    "flame": lambda x, y: icon_flame(x, y, 34),
    "jet": lambda x, y: icon_jet(x, y, 34),
    "flag": lambda x, y: icon_flag(x, y, 34),
}

# ---------------------------------------------------------------- cells
CELLS = [
    ("STRAIT OF HORMUZ", "ship", "4 TANKERS HIT MINES, IRAN SAYS",
     "Tankers ablaze; Tehran may shut the strait"),
    ("UKRAINE AT SEA", "drone_ship", "UKRAINE HITS RUSSIAN SHIPS",
     "Strikes in Finland gulf & off Libya"),
    ("UNITED STATES • COURT", "court", "HUAWEI GUILTY ON 10 COUNTS",
     "Bank fraud & trade secrets; no racketeering"),
    ("UKRAINE TALKS", "talk", "ZELENSKY URGES 4-WAY TALKS",
     "US envoys push for a deal by January"),
    ("GAZA", "building", "ISRAEL KILLS HAMAS SECURITY CHIEF",
     "Naeem Abu Nahel + 6 killed"),
    ("SENEGAL • SPORT", "trophy", "SENEGAL WIN BACK AFRICA CUP",
     "Court restores title stripped after final"),
    ("TÜRKIYE", "heli", "HELICOPTER CRASH KILLS 5 CREW",
     "Down on a training flight"),
    ("COLOMBIA", "shop", "25 HELD HOSTAGE IN SUPERMARKET",
     "Cartagena store seized; 5 women freed"),
    ("SAUDI ARABIA", "tower", "DRONE HITS RIYADH TOWER",
     "PIF HQ tower; at least 11 wounded"),
    ("VIETNAM", "flame", "RESTAURANT BLAST KILLS 6",
     "Hanoi restaurant; suspected gas leak"),
    ("SOUTH KOREA", "jet", "RUSSIAN JETS ENTER AIR ZONE",
     "Fighters up; islanders told to shelter"),
    ("BANGLADESH", "flag", "HASINA VOWS RETURN DEC 16",
     "Ex-PM in exile, under a death sentence"),
]

GX, GY, GW, GH, GAP = 16, 156, 325, 148, 7
for i, (kicker, icon, head, sub) in enumerate(CELLS):
    col, row = i % 3, i // 3
    x, y = GX + col * (GW + GAP), GY + row * (GH + GAP)
    d.rectangle([x, y, x + GW, y + GH], fill=CELL_BG, outline=INK, width=2)
    d.rectangle([x, y, x + GW, y + 5], fill=RED)
    ICONS[icon](x + 46, y + 76)
    tx = x + 94
    d.text((tx, y + 11), kicker, font=F(SANS_B, 15), fill=BLUE)
    head_lines = wrap(head, F(SANS_B, 23), GW - 106)
    yy = text_block(tx, y + 32, head, F(SANS_B, 23), INK, GW - 106, 27, max_lines=3)
    sub_max = 1 if len(head_lines) >= 3 else 2
    text_block(tx, yy + 3, sub, F(SANS_R, 16), (60, 56, 48), GW - 106, 20, max_lines=sub_max)

# ---------------------------------------------------------------- ticker
TY = 772
d.rectangle([0, TY, W, H], fill=TICKER_BG)
d.text((28, TY + 9), "ALSO ON TUESDAY — 18 MORE STORIES", font=F(SANS_B, 25), fill=(250, 220, 120))
TICKER = [
    "Zaporizhzhia: Russian strike kills 2, wounds 40",
    "Iran's IRGC attacks a ship in Hormuz",
    "NATO vows space defence on satellite reports",
    "Pentagon rebukes Canada on defence, F-35s",
    "US blacklists Singapore chip firm Megaspeed",
    "Nvidia reinstates CEO Jensen Huang",
    "S. Korea: $375k rewards to catch AI exam cheats",
    "Bangladesh garment workers clash with police",
    "175 migrants missing from a Senegal boat",
    "Israel: Eisenkot signs first coalition deal",
    "Iraq orders control of Kurdish oilfields",
    "UK sanctions Houthis & 4 senior officials",
    "Houthis 60 km from Aden, Yemen warns",
    "Colombia car bomb injures 23 in Villavicencio",
    "China sentences an official to death for spying",
    "Mexico captures cartel boss 'El Chapo Isidro'",
    "Indonesia nominates two to replace VP",
    "Malaysia to return migrants to Myanmar",
]
tf = F(SANS_R, 19)
col_w = (W - 56) // 2
for i, line in enumerate(TICKER):
    col, row = i // 9, i % 9
    x = 28 + col * col_w
    y = TY + 50 + row * 22
    d.rectangle([x, y + 6, x + 7, y + 13], fill=RED)
    d.text((x + 14, y), line, font=tf, fill=(240, 236, 226))

img.save("entry.png", optimize=True)
print("saved entry.png")

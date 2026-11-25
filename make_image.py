#!/usr/bin/env python3
"""Draw the one-image summary of Wednesday 25 November 2026 world news.

Run this on a development machine with Pillow installed. Its only output is
entry.png, which is committed to the repository and copied by main.py at grade
time; the grader itself needs no third-party packages.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (11, 17, 33)
PANEL = (20, 30, 53)
WHITE = (245, 248, 255)
MUTED = (157, 174, 202)
DARK = (12, 18, 32)
AMBER = (255, 186, 32)
CORAL = (255, 108, 94)
CYAN = (60, 212, 226)
GREEN = (92, 219, 143)
VIOLET = (187, 153, 255)
BLUE = (116, 171, 255)

BOLD = "C:/Windows/Fonts/arialbd.ttf"
REG = "C:/Windows/Fonts/arial.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text(d, xy, s, f, fill, anchor=None):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)


def backdrop(d):
    d.rectangle((0, 0, W, H), fill=BG)
    for x in range(0, W, 32):
        for y in range(0, H, 32):
            d.ellipse((x, y, x + 2, y + 2), fill=(27, 38, 63))


def header(d):
    text(d, (36, 26), "THE WORLD IN ONE IMAGE", font(REG, 22), MUTED)
    text(d, (34, 54), "WORLD NEWS", font(BOLD, 88), WHITE)
    d.rounded_rectangle((656, 36, 988, 118), radius=16, fill=AMBER)
    text(d, (822, 52), "WEDNESDAY", font(BOLD, 21), DARK, "mm")
    text(d, (822, 80), "25 NOV 2026", font(BOLD, 43), DARK, "mm")
    d.line((36, 152, 988, 152), fill=AMBER, width=4)


def card(d, box, accent, tag, lines, sub, icon):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=18, fill=PANEL, outline=accent, width=3)
    d.rounded_rectangle((x0 + 3, y0 + 3, x1 - 3, y0 + 13), radius=5, fill=accent)
    text(d, (x0 + 20, y0 + 24), tag, font(BOLD, 18), accent)
    icon(d, x0 + (x1 - x0) / 2, y0 + 100, accent)
    yy = y0 + 174
    for line in lines:
        text(d, (x0 + 20, yy), line, font(BOLD, 34), WHITE)
        yy += 40
    text(d, (x0 + 20, y1 - 40), sub, font(REG, 18), MUTED)


def icon_chip(d, cx, cy, c):
    d.rounded_rectangle((cx - 43, cy - 36, cx + 43, cy + 36), radius=8, outline=c, width=5)
    for i in (-28, -14, 0, 14, 28):
        d.line((cx + i, cy - 36, cx + i, cy - 48), fill=c, width=4)
        d.line((cx + i, cy + 36, cx + i, cy + 48), fill=c, width=4)
    d.polygon([(cx - 34, cy + 12), (cx, cy - 14), (cx + 34, cy + 12)], fill=c)
    for i in (-24, -8, 8, 24):
        d.rectangle((cx + i - 4, cy + 10, cx + i + 4, cy + 24), fill=c)


def icon_store(d, cx, cy, c):
    d.rectangle((cx - 54, cy - 10, cx + 54, cy + 42), outline=c, width=4)
    for i in range(6):
        x = cx - 54 + i * 18
        d.polygon([(x, cy - 10), (x + 9, cy - 28), (x + 18, cy - 10)], fill=c if i % 2 == 0 else WHITE)
    for dx in (-32, 0, 32):
        d.ellipse((cx + dx - 9, cy + 2, cx + dx + 9, cy + 20), outline=c, width=4)
        d.line((cx + dx, cy + 20, cx + dx, cy + 34), fill=c, width=4)
        d.line((cx + dx - 14, cy + 10, cx + dx - 24, cy - 4), fill=c, width=4)
        d.line((cx + dx + 14, cy + 10, cx + dx + 24, cy - 4), fill=c, width=4)


def icon_tower(d, cx, cy, c):
    d.rectangle((cx - 24, cy - 54, cx + 24, cy + 50), outline=c, width=4)
    for yy in (-36, -12, 12, 36):
        for dx in (-13, 4):
            d.rectangle((cx + dx, cy + yy, cx + dx + 9, cy + yy + 11), fill=c)
    d.line((cx, cy - 54, cx, cy - 74), fill=c, width=4)
    d.polygon([(cx + 34, cy - 34), (cx + 62, cy - 54), (cx + 54, cy - 22),
               (cx + 74, cy - 8), (cx + 44, cy - 4), (cx + 30, cy + 20),
               (cx + 24, cy - 14)], fill=CORAL)


def icon_ship(d, cx, cy, c):
    d.polygon([(cx - 58, cy + 10), (cx + 58, cy + 10), (cx + 36, cy + 40),
               (cx - 38, cy + 40)], fill=c)
    d.rectangle((cx - 8, cy - 42, cx + 8, cy + 10), fill=c)
    d.polygon([(cx + 8, cy - 42), (cx + 44, cy - 12), (cx + 8, cy - 12)], fill=WHITE)
    d.ellipse((cx - 62, cy - 62, cx - 38, cy - 38), outline=c, width=4)
    d.line((cx - 50, cy - 62, cx - 50, cy - 38), fill=c, width=3)
    d.line((cx - 62, cy - 50, cx - 38, cy - 50), fill=c, width=3)


def icon_islands(d, cx, cy, c):
    d.polygon([(cx - 72, cy + 34), (cx - 42, cy - 16), (cx - 12, cy + 34)], fill=c)
    d.polygon([(cx + 12, cy + 34), (cx + 42, cy - 6), (cx + 72, cy + 34)], fill=c)
    d.arc((cx - 48, cy - 26, cx + 48, cy + 54), 200, 340, fill=WHITE, width=4)
    d.line((cx - 42, cy - 16, cx - 42, cy - 50), fill=WHITE, width=3)
    d.line((cx + 42, cy - 6, cx + 42, cy - 40), fill=WHITE, width=3)
    d.polygon([(cx - 42, cy - 50), (cx - 12, cy - 42), (cx - 42, cy - 34)], fill=AMBER)
    d.polygon([(cx + 42, cy - 40), (cx + 12, cy - 32), (cx + 42, cy - 24)], fill=CYAN)


def icon_rocket(d, cx, cy, c):
    d.polygon([(cx, cy - 62), (cx + 20, cy - 18), (cx + 20, cy + 30),
               (cx - 20, cy + 30), (cx - 20, cy - 18)], fill=c)
    d.ellipse((cx - 10, cy - 32, cx + 10, cy - 12), fill=BG, outline=WHITE, width=3)
    d.polygon([(cx - 20, cy + 8), (cx - 36, cy + 36), (cx - 20, cy + 30)], fill=WHITE)
    d.polygon([(cx + 20, cy + 8), (cx + 36, cy + 36), (cx + 20, cy + 30)], fill=WHITE)
    d.polygon([(cx - 12, cy + 30), (cx, cy + 62), (cx + 12, cy + 30)], fill=AMBER)
    d.line((cx + 44, cy - 40, cx + 76, cy - 40), fill=WHITE, width=4)
    d.line((cx + 60, cy - 56, cx + 60, cy - 24), fill=WHITE, width=4)


def ticker(d):
    d.rounded_rectangle((32, 806, 988, 990), radius=18, fill=PANEL)
    d.line((32, 806, 988, 806), fill=AMBER, width=4)
    text(d, (52, 820), "ALSO TODAY", font(BOLD, 22), AMBER)
    left = [
        "NORTH KOREA EXPELS SWISS DIPLOMAT",
        "US READIES TARIFFS ON CHINA, EU",
        "EBOLA BURIAL TEAMS SWAMPED",
    ]
    right = [
        "TURKEY: 5 KILLED IN HELICOPTER CRASH",
        "RUSSIA FIGURES: ~500,000 WAR DEATHS",
        "CIA SYSTEM BREACHED, REPORT SAYS",
    ]
    for i, line in enumerate(left):
        text(d, (52, 858 + i * 40), line, font(REG, 21), WHITE)
    for i, line in enumerate(right):
        text(d, (516, 858 + i * 40), line, font(REG, 21), WHITE)


def main():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    backdrop(d)
    header(d)
    xs = [32, 357, 682]
    ys = [170, 488]
    cards = [
        (CORAL, "US / TECHNOLOGY", ["HUAWEI", "GUILTY"], "US court: trade-secret theft", icon_chip),
        (AMBER, "COLOMBIA", ["CARTAGENA", "HOSTAGES"], "Gunmen seize 25 in store", icon_store),
        (CORAL, "MIDDLE EAST", ["RIYADH", "TOWER HIT"], "Houthi strike injures eleven", icon_tower),
        (CYAN, "RUSSIA / UKRAINE", ["WARSHIP", "STRUCK"], "Corvette hit in Gulf of Finland", icon_ship),
        (GREEN, "PACIFIC", ["SOLOMONS", "SWITCH"], "Swaps China pact for Australia", icon_islands),
        (VIOLET, "SCIENCE / SPACE", ["SHENZHOU-24", "LAUNCH"], "First astronaut from Pakistan", icon_rocket),
    ]
    for i, (accent, tag, lines, sub, icon) in enumerate(cards):
        col, row = i % 3, i // 3
        box = (xs[col], ys[row], xs[col] + 309, ys[row] + 296)
        card(d, box, accent, tag, lines, sub, icon)
    ticker(d)
    im.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", im.size)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Draw the news-image-20261121 entry: six stories of Saturday 21 November 2026.

Hand-drawn with Pillow only (no AI generation, no network, no downloaded
artwork). Every pictogram is a few geometric shapes; every word is set in
DejaVu Sans. Running this script writes a deterministic 1024x1024 PNG.
"""

import hashlib
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)      # warm paper background
CARD = (255, 255, 255)       # card face
INK = (26, 26, 26)           # headline / body text
NAVY = (27, 42, 74)          # header + footer band
RULE = (192, 57, 43)         # red rule under the header
FOOT = (215, 222, 235)       # footer text

FONT_DIR = "/usr/share/fonts/truetype/dejavu"

# Six stories, strongest first. Every figure was checked against at least
# two independent news sources before it was written here.
STORIES = [
    {
        "kicker": "MARKETS  •  NEW YORK",
        "accent": (178, 34, 34),
        "glyph": "chart",
        "headline": "Wall Street slides into correction",
        "body": "S&P 500 falls 3.7% and Nasdaq 5.3% in an AI-led rout. Nvidia drops 14% as the SEC probes its accounting.",
    },
    {
        "kicker": "SECURITY  •  POLAND",
        "accent": (176, 124, 18),
        "glyph": "missile",
        "headline": "Russian missiles crash in Poland",
        "body": "A Kh-101 and two more objects come down in the south-east. No one is hurt; NATO jets scramble and Warsaw seeks reinforcements.",
    },
    {
        "kicker": "CLIMATE  •  ANTALYA, TURKEY",
        "accent": (31, 92, 140),
        "glyph": "globe",
        "headline": "COP31 talks run into overtime",
        "body": "The deadline passes with no deal. The draft drops all fossil-fuel language and the $120bn adaptation goal.",
    },
    {
        "kicker": "DISASTER  •  PERU",
        "accent": (46, 125, 72),
        "glyph": "quake",
        "headline": "6.8 quake shakes central Peru",
        "body": "The tremor strikes Junin and is felt in Lima, sending residents into the streets. No casualties are reported.",
    },
    {
        "kicker": "ENERGY  •  THE GULF",
        "accent": (94, 52, 130),
        "glyph": "tanker",
        "headline": "Iran masses tankers to test blockade",
        "body": "More than 14 tankers gather at Kharg Island as the US widens its blockade. Tehran says it 'must be broken'.",
    },
    {
        "kicker": "DIPLOMACY  •  BRUSSELS",
        "accent": (18, 122, 120),
        "glyph": "rings",
        "headline": "UK and EU seal Brexit reset",
        "body": "Food checks are scrapped, carbon markets linked, and 100,000 young people a year can live and work on each side.",
    },
]


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


F_TITLE = lambda: font("DejaVuSans-Bold.ttf", 46)
F_SUB = lambda: font("DejaVuSans-Bold.ttf", 20)
F_KICK = lambda: font("DejaVuSans-Bold.ttf", 17)
F_HEAD = lambda: font("DejaVuSans-Bold.ttf", 29)
F_BODY = lambda: font("DejaVuSans.ttf", 19)
F_FOOT = lambda: font("DejaVuSans.ttf", 15)


def wrap(text, fnt, max_w):
    """Split text into lines that fit max_w pixels, word by word."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def glyph_chart(d, cx, cy, col):
    pts = [(cx - 15, cy + 2), (cx - 5, cy - 6), (cx + 2, cy - 1), (cx + 9, cy - 8),
           (cx + 15, cy + 9)]
    d.line(pts, fill=col, width=4, joint="curve")
    d.polygon([(cx + 15, cy + 9), (cx + 7, cy + 7), (cx + 15, cy + 1)], fill=col)


def glyph_missile(d, cx, cy, col):
    # A small upright rocket: body, nose cone, two fins, flame.
    d.polygon([(cx, cy - 15), (cx + 6, cy - 6), (cx + 6, cy + 6),
               (cx - 6, cy + 6), (cx - 6, cy - 6)], fill=col)
    d.polygon([(cx - 6, cy + 6), (cx - 11, cy + 13), (cx - 6, cy + 11)], fill=col)
    d.polygon([(cx + 6, cy + 6), (cx + 11, cy + 13), (cx + 6, cy + 11)], fill=col)
    d.polygon([(cx - 3, cy + 12), (cx + 3, cy + 12), (cx, cy + 18)], fill=col)


def glyph_globe(d, cx, cy, col):
    d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline=col, width=3)
    d.arc([cx - 14, cy - 6, cx + 14, cy + 6], 0, 360, fill=col, width=2)
    d.arc([cx - 6, cy - 14, cx + 6, cy + 14], 0, 360, fill=col, width=2)


def glyph_quake(d, cx, cy, col):
    for j, amp in enumerate((4, 8, 12)):
        y = cy - 10 + j * 10
        pts = [(cx - 15, y), (cx - 8, y - amp), (cx - 2, y + amp),
               (cx + 5, y - amp), (cx + 11, y), (cx + 15, y)]
        d.line(pts, fill=col, width=3, joint="curve")


def glyph_tanker(d, cx, cy, col):
    d.polygon([(cx - 16, cy + 2), (cx + 16, cy + 2), (cx + 11, cy + 11),
               (cx - 11, cy + 11)], fill=col)
    for x in (-12, -4, 4):
        d.rectangle([cx + x, cy - 8, cx + x + 6, cy + 1], fill=col)
    d.line([(cx - 16, cy + 16), (cx - 8, cy + 13), (cx, cy + 16),
            (cx + 8, cy + 13), (cx + 16, cy + 16)], fill=col, width=2)


def glyph_rings(d, cx, cy, col):
    # A ring of eight small stars, the way the EU flag reads at a glance.
    import math
    for k in range(8):
        a = math.pi / 4 * k - math.pi / 2
        sx, sy = cx + 11 * math.cos(a), cy + 11 * math.sin(a)
        star = []
        for j in range(10):
            r = 3.2 if j % 2 == 0 else 1.4
            ang = a - math.pi / 2 + j * math.pi / 5
            star.append((sx + r * math.cos(ang), sy + r * math.sin(ang)))
        d.polygon(star, fill=col)


GLYPHS = {
    "chart": glyph_chart,
    "missile": glyph_missile,
    "globe": glyph_globe,
    "quake": glyph_quake,
    "tanker": glyph_tanker,
    "rings": glyph_rings,
}


def draw_card(d, story, x, y, w, h):
    accent = story["accent"]
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD)
    d.rounded_rectangle([x, y, x + w, y + 8], radius=4, fill=accent)
    d.rectangle([x, y + 4, x + w, y + 8], fill=accent)

    pad = 22
    ix, iy, r = x + pad + 26, y + 40, 26
    d.ellipse([ix - r, iy - r, ix + r, iy + r], fill=accent)
    GLYPHS[story["glyph"]](d, ix, iy, (255, 255, 255))

    kx = ix + r + 14
    d.text((kx, iy - 10), story["kicker"], font=F_KICK(), fill=accent)

    tx = x + pad
    tw = w - 2 * pad
    head_lines = wrap(story["headline"], F_HEAD(), tw)
    by = y + 82
    for line in head_lines:
        d.text((tx, by), line, font=F_HEAD(), fill=INK)
        by += 36
    body_lines = wrap(story["body"], F_BODY(), tw)
    by += 8
    for line in body_lines:
        d.text((tx, by), line, font=F_BODY(), fill=INK)
        by += 25
    return len(head_lines), len(body_lines)


def build_image():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Header band.
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.text((24, 16), "SATURDAY 21 NOVEMBER 2026", font=F_TITLE(), fill=(255, 255, 255))
    d.text((24, 66), "THE WORLD IN ONE IMAGE  •  SIX STORIES FROM ONE DAY",
           font=F_SUB(), fill=(190, 200, 220))
    d.rectangle([0, 100, W, 104], fill=RULE)

    # 2 x 3 grid of story cards.
    margin, gutter = 24, 16
    cw = (W - 2 * margin - gutter) // 2
    ch = 278
    counts = []
    for i, story in enumerate(STORIES):
        cx = margin + (i % 2) * (cw + gutter)
        cy = 118 + (i // 2) * (ch + 14)
        counts.append(draw_card(d, story, cx, cy, cw, ch))

    # Footer band.
    d.rectangle([0, 984, W, H], fill=NAVY)
    d.text((24, 996),
           "Saturday's news as reported on 21 November 2026  •  Sources: Reuters, AP, CNN, WSJ, UN News, The Times",
           font=F_FOOT(), fill=FOOT)
    return img, counts


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img, counts = build_image()
    for i, (hl, bl) in enumerate(counts):
        print(f"card {i}: headline {hl} lines, body {bl} lines")
    img.save(out, "PNG")
    data = open(out, "rb").read()
    print(f"wrote {out}: {len(data)} bytes, sha256 "
          f"{hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()

"""Generates the pixel-art SVG assets for the danielrdg profile README.

Usage: python tools/generate_assets.py assets
Needs fonttools and the OFL font files in tools/fonts (not committed):
PixelifySans[wght].ttf and Silkscreen-Regular.ttf, from
https://github.com/google/fonts (ofl/pixelifysans, ofl/silkscreen).
Text is converted to paths (no font files ship with the SVGs).
Fonts: Pixelify Sans and Silkscreen, both SIL OFL 1.1.
"""
import math
import os
import sys
from xml.sax.saxutils import escape

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
if len(sys.argv) != 2:
    sys.exit("usage: python tools/generate_assets.py <output-dir>")
OUT = sys.argv[1]

OURO, LUZ, TINTA = "#d9a441", "#ffd45c", "#140b08"
NEON_TXT = "#ffe0ef"

pix = instancer.instantiateVariableFont(TTFont(os.path.join(HERE, "PixelifySans[wght].ttf")), {"wght": 700})
silk = TTFont(os.path.join(HERE, "Silkscreen-Regular.ttf"))


def text(font, s, size, x, y, anchor="start", ls=0.0):
    """Returns (path_d, width) for string s with baseline at y."""
    upm = font["head"].unitsPerEm
    k = size / upm
    cmap, gs, hmtx = font.getBestCmap(), font.getGlyphSet(), font["hmtx"]
    names = [cmap[ord(c)] for c in s]
    width = sum(hmtx[n][0] * k for n in names) + ls * (len(s) - 1)
    cx = {"start": x, "middle": x - width / 2, "end": x - width}[anchor]
    pen = SVGPathPen(gs)
    for n in names:
        gs[n].draw(TransformPen(pen, (k, 0, 0, -k, cx, y)))
        cx += hmtx[n][0] * k + ls
    return pen.getCommands(), width


def tpath(font, s, size, x, y, fill, anchor="start", ls=0.0, extra=""):
    d, _ = text(font, s, size, x, y, anchor, ls)
    return f'<path d="{d}" fill="{fill}" {extra}/>'


class Sprite:
    def __init__(self, w=16, h=16):
        self.w, self.h, self.c = w, h, {}

    def R(self, x, y, w, h, col):
        for j in range(y, y + h):
            for i in range(x, x + w):
                if 0 <= i < self.w and 0 <= j < self.h:
                    self.c[(i, j)] = col

    def clear(self, x, y):
        self.c.pop((x, y), None)

    def outline(self, col=TINTA):
        filled = set(self.c)
        for j in range(self.h):
            for i in range(self.w):
                if (i, j) in filled:
                    continue
                if any((i + dx, j + dy) in filled for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    self.c[(i, j)] = col
        return self

    def svg(self, s, ox=0, oy=0):
        out = []
        for j in range(self.h):
            i = 0
            while i < self.w:
                col = self.c.get((i, j))
                if col is None:
                    i += 1
                    continue
                run = i
                while run + 1 < self.w and self.c.get((run + 1, j)) == col:
                    run += 1
                out.append(f'<rect x="{ox + i * s:g}" y="{oy + j * s:g}" width="{(run - i + 1) * s:g}" height="{s:g}" fill="{col}"/>')
                i = run + 1
        return "".join(out)


def lantern():
    sp = Sprite()
    R = sp.R
    R(7, 0, 2, 2, "#5a3320"); R(5, 2, 6, 1, "#e0a83a")
    R(4, 3, 8, 1, "#c8281e")
    for y in range(4, 11):
        R(3, y, 10, 1, "#c8281e")
    R(4, 11, 8, 1, "#c8281e")
    for y in range(4, 11):
        R(3, y, 1, 1, "#e8483a"); R(12, y, 1, 1, "#9a1c14")
    R(3, 6, 10, 1, "#9a1c14"); R(3, 9, 10, 1, "#9a1c14")
    R(7, 4, 2, 7, "#ffb060"); R(7, 5, 1, 5, "#ffe0a0")
    R(5, 12, 6, 1, "#e0a83a"); R(7, 13, 2, 1, "#e0a83a"); R(7, 14, 2, 2, "#c8281e")
    return sp.outline()


def mascot():
    sp = Sprite()
    R = sp.R
    R(2, 12, 12, 4, "#24242e"); R(6, 12, 4, 3, "#efeadf"); R(5, 12, 2, 2, "#c0262a"); R(9, 12, 2, 2, "#c0262a"); R(7, 12, 2, 1, "#8a1a1a")
    R(7, 11, 2, 1, "#dca97a")
    R(4, 4, 8, 7, "#f6cfa0"); R(11, 5, 1, 5, "#dca97a"); R(5, 10, 6, 1, "#dca97a"); R(3, 7, 1, 2, "#f6cfa0"); R(12, 7, 1, 2, "#dca97a")
    R(4, 2, 8, 2, "#c8c8d0"); R(3, 3, 1, 3, "#c8c8d0"); R(12, 3, 1, 3, "#8a8a94"); R(5, 4, 6, 1, "#c8c8d0"); R(9, 2, 3, 2, "#8a8a94"); R(6, 2, 1, 1, "#ffffff")
    R(5, 6, 2, 1, "#8a8a94"); R(9, 6, 2, 1, "#8a8a94"); R(5, 7, 1, 1, TINTA); R(10, 7, 1, 1, TINTA)
    R(5, 9, 6, 1, "#5a5a64"); R(4, 10, 1, 1, "#5a5a64"); R(11, 10, 1, 1, "#5a5a64")
    return sp.outline()


def bell():
    sp = Sprite()
    R = sp.R
    R(7, 3, 2, 1, "#e8b84a"); R(7, 4, 2, 1, "#a87a20")
    for i, w in enumerate([2, 3, 4, 5, 5, 6]):
        y = 5 + i
        R(8 - w, y, 2 * w, 1, "#e8b84a"); R(8 + w - 1, y, 1, 1, "#a87a20")
        if 0 < i < 4:
            R(8 - w + 1, y, 1, 1, "#fff3c0")
    R(1, 11, 14, 1, "#a87a20"); R(1, 12, 14, 2, "#8a5130"); R(1, 13, 14, 1, "#5a3320")
    return sp.outline()


# ---------- item icons (16x16) ----------
def ic_ticket():
    sp = Sprite(); R = sp.R
    R(1, 4, 14, 8, "#e8b84a"); R(1, 4, 14, 1, "#fff3c0"); R(1, 11, 14, 1, "#a87a20")
    for p in ((1, 7), (1, 8), (14, 7), (14, 8)):
        sp.clear(*p)
    for y in range(5, 11, 2):
        R(10, y, 1, 1, "#a87a20")
    R(3, 6, 5, 1, "#8a5130"); R(3, 8, 4, 1, "#8a5130"); R(12, 7, 1, 2, "#c8281e")
    return sp.outline()


def ic_console():
    sp = Sprite(); R = sp.R
    R(1, 2, 14, 10, "#5a5a64"); R(2, 3, 12, 8, "#1d1d26")
    R(6, 4, 1, 7, "#5fd39a"); R(7, 5, 1, 5, "#5fd39a"); R(8, 6, 1, 3, "#5fd39a"); R(9, 7, 1, 1, "#5fd39a")
    R(6, 12, 4, 1, "#5a5a64"); R(4, 13, 8, 1, "#8a8a94")
    return sp.outline()


def ic_moon():
    sp = Sprite(); R = sp.R
    for j in range(16):
        for i in range(16):
            if math.hypot(i - 7, j - 8) <= 5.6 and math.hypot(i - 9.6, j - 6.2) > 4.6:
                R(i, j, 1, 1, "#ffd45c")
    R(13, 2, 1, 3, "#fff3c0"); R(12, 3, 3, 1, "#fff3c0")
    R(12, 11, 1, 1, "#fff3c0")
    return sp.outline()


def ic_clipboard():
    sp = Sprite(); R = sp.R
    R(3, 2, 10, 13, "#8a5130"); R(4, 4, 8, 10, "#f3e6d3"); R(6, 1, 4, 2, "#c8c8d0")
    for y in (6, 9, 12):
        R(5, y, 1, 1, "#3fa874"); R(7, y, 4, 1, "#8a8a94")
    return sp.outline()


def ic_broom():
    sp = Sprite(); R = sp.R
    for i in range(8):
        R(13 - i, 1 + i, 1, 1, "#8a5130")
        if i < 7:
            R(14 - i, 1 + i, 1, 1, "#5a3320")
    R(3, 9, 5, 1, "#c8281e")
    R(2, 10, 6, 1, "#e8b84a"); R(1, 11, 7, 1, "#e8b84a"); R(1, 12, 6, 1, "#e8b84a"); R(0, 13, 6, 1, "#e8b84a")
    for x in (3, 5):
        R(x, 11, 1, 2, "#a87a20")
    R(10, 13, 1, 1, "#fff3c0"); R(12, 11, 1, 1, "#fff3c0"); R(13, 14, 1, 1, "#fff3c0")
    return sp.outline()


def ic_book():
    sp = Sprite(); R = sp.R
    R(1, 4, 6, 9, "#f3e6d3"); R(9, 4, 6, 9, "#f3e6d3"); R(7, 3, 2, 11, "#c8281e"); R(1, 13, 14, 1, "#9a1c14")
    for y in (6, 8, 10):
        R(2, y, 4, 1, "#8a8a94"); R(10, y, 4, 1, "#8a8a94")
    return sp.outline()


def ic_shield():
    sp = Sprite(); R = sp.R
    rows = {1: (2, 13), 2: (2, 13), 3: (2, 13), 4: (2, 13), 5: (2, 13), 6: (2, 13), 7: (2, 13), 8: (3, 12), 9: (3, 12), 10: (4, 11), 11: (5, 10), 12: (6, 9), 13: (7, 8)}
    for y, (a, b) in rows.items():
        R(a, y, b - a + 1, 1, "#e8b84a")
    for y, (a, b) in rows.items():
        if 2 <= y <= 12 and b - a >= 3:
            R(a + 1, y, b - a - 1, 1, "#c8281e")
    R(5, 7, 1, 1, "#fff3c0"); R(6, 8, 1, 1, "#fff3c0"); R(7, 9, 1, 1, "#fff3c0"); R(8, 8, 1, 1, "#fff3c0"); R(9, 7, 1, 1, "#fff3c0"); R(10, 6, 1, 1, "#fff3c0")
    return sp.outline()


def ic_cap():
    sp = Sprite(); R = sp.R
    for i, (a, b) in enumerate([(7, 8), (5, 10), (3, 12), (1, 14), (3, 12), (5, 10), (7, 8)]):
        R(a, 3 + i, b - a + 1, 1, "#2a2a36")
    R(7, 3, 2, 1, "#5a5a64"); R(4, 7, 8, 1, "#5a5a64")
    R(4, 8, 8, 4, "#24242e"); R(4, 8, 8, 1, "#3a3a46")
    R(8, 5, 5, 1, OURO); R(12, 5, 1, 6, OURO); R(11, 11, 3, 2, "#e8b84a")
    return sp.outline()


def ic_case():
    sp = Sprite(); R = sp.R
    R(6, 2, 4, 1, "#5a3320"); R(5, 3, 1, 2, "#5a3320"); R(10, 3, 1, 2, "#5a3320")
    R(1, 5, 14, 9, "#8a5130"); R(1, 5, 14, 1, "#a86a40"); R(1, 9, 14, 1, "#5a3320")
    R(7, 8, 2, 3, OURO)
    return sp.outline()


def ic_mask():
    sp = Sprite(); R = sp.R
    R(3, 3, 10, 9, "#a77bf0"); R(4, 12, 8, 1, "#a77bf0"); R(5, 13, 6, 1, "#a77bf0")
    R(5, 6, 2, 2, TINTA); R(9, 6, 2, 2, TINTA); R(6, 10, 4, 1, "#5a3a8a"); R(4, 3, 8, 1, "#c8a8ff")
    return sp.outline()


NEON_FILTER = """
<filter id="neon" x="-15%" y="-60%" width="130%" height="220%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="{a}" result="b1"/>
  <feGaussianBlur in="SourceAlpha" stdDeviation="{b}" result="b2"/>
  <feGaussianBlur in="SourceAlpha" stdDeviation="{c}" result="b3"/>
  <feMerge result="bm"><feMergeNode in="b1"/><feMergeNode in="b2"/><feMergeNode in="b3"/></feMerge>
  <feFlood flood-color="#ff2d8a"/><feComposite in2="bm" operator="in" result="glow"/>
  <feMerge><feMergeNode in="glow"/><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>"""

STYLE = """
<style>
  .flicker { animation: flicker 7s infinite steps(1); }
  @keyframes flicker { 0%,61%,63%,66%,100% { opacity: 1 } 62%,65% { opacity: .55 } 64% { opacity: .9 } }
  .sway { transform-box: view-box; animation: sway 5s ease-in-out infinite alternate; }
  .sway.b { animation-delay: -2.5s; }
  @keyframes sway { from { transform: rotate(-2.5deg) } to { transform: rotate(2.5deg) } }
  .pulse { animation: pulse 3.2s ease-in-out infinite alternate; }
  @keyframes pulse { from { opacity: .45 } to { opacity: .8 } }
  .tw { animation: tw 2.4s steps(2) infinite; }
  @keyframes tw { 0% { opacity: 0 } 50% { opacity: 1 } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important } }
</style>"""


def svg(w, h, body, title, defs=""):
    title = escape(title, {'"': "&quot;"})
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f"<title>{title}</title><defs>{defs}</defs>{body}</svg>\n")


def frieze(x0, x1, y, h=30):
    """Gold key-pattern band."""
    out = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" fill="{TINTA}"/>',
           f'<rect x="{x0}" y="{y + 3}" width="{x1 - x0}" height="3" fill="{OURO}"/>',
           f'<rect x="{x0}" y="{y + h - 6}" width="{x1 - x0}" height="3" fill="{OURO}"/>']
    step = 24
    for x in range(x0 + 6, x1 - 18, step):
        yy = y + 9
        out.append(f'<rect x="{x}" y="{yy}" width="12" height="12" fill="none" stroke="{OURO}" stroke-width="3"/>')
        out.append(f'<rect x="{x + 4.5}" y="{yy + 4.5}" width="3" height="3" fill="{LUZ}"/>')
        out.append(f'<rect x="{x + 14}" y="{yy + 4.5}" width="6" height="3" fill="{OURO}"/>')
    return "".join(out)


def lattice(x, y, w, h, cell=24):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{LUZ}" opacity=".16"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#warm)" class="pulse"/>']
    for gx in range(x + cell, x + w, cell):
        out.append(f'<rect x="{gx - 1.5}" y="{y}" width="3" height="{h}" fill="#8a5a1c"/>')
    for gy in range(y + cell, y + h, cell):
        out.append(f'<rect x="{x}" y="{gy - 1.5}" width="{w}" height="3" fill="#8a5a1c"/>')
    for gx in range(x + cell // 2, x + w, cell * 2):
        for gy in range(y + cell // 2, y + h, cell * 2):
            out.append(f'<rect x="{gx - 4}" y="{gy - 4}" width="8" height="8" fill="none" stroke="{OURO}" stroke-width="2"/>')
    out.append(f'<rect x="{x - 3}" y="{y - 3}" width="{w + 6}" height="{h + 6}" fill="none" stroke="{OURO}" stroke-width="6"/>')
    return "".join(out)


def hanging_lantern(cx, top, s, cls):
    sp = lantern().svg(s, cx - 8 * s, top + 40)
    glow = f'<ellipse cx="{cx}" cy="{top + 40 + 7 * s}" rx="{9 * s}" ry="{9 * s}" fill="url(#lglow)" class="pulse"/>'
    cord = f'<rect x="{cx - 1.5}" y="{top}" width="3" height="40" fill="#5a3320"/>'
    return f'{glow}<g class="sway {cls}" style="transform-origin:{cx}px {top}px" shape-rendering="crispEdges">{cord}{sp}</g>'


def banner():
    W, H = 1200, 400
    d = [f'<rect width="{W}" height="{H}" fill="url(#wall)"/>',
         f'<ellipse cx="600" cy="190" rx="520" ry="210" fill="url(#warm)" opacity=".55"/>',
         '<g shape-rendering="crispEdges">',
         frieze(0, W, 0, 30),
         lattice(36, 78, 120, 240),
         lattice(W - 156, 78, 120, 240),
         # bar counter
         f'<rect x="0" y="344" width="{W}" height="56" fill="#2a110b"/>',
         f'<rect x="0" y="338" width="{W}" height="8" fill="#5a3320"/>',
         f'<rect x="0" y="338" width="{W}" height="3" fill="{OURO}"/>',
         ''.join(f'<rect x="{x}" y="352" width="3" height="48" fill="#8a5a1c"/>' for x in range(30, W, 60)),
         bell().svg(3, 960, 290),
         '</g>']
    # neon sign
    name_d, name_w = text(pix, "daniel rodrigues", 66, 600, 190, "middle", 2)
    fx0, fx1 = 600 - name_w / 2 - 30, 600 + name_w / 2 + 30
    lx = round((156 + fx0) / 2)
    d += [hanging_lantern(lx, 30, 5, "a"), hanging_lantern(W - lx, 30, 5, "b")]
    d.append(f'<g class="flicker" filter="url(#neon)">'
             f'<rect x="{fx0:.0f}" y="108" width="{fx1 - fx0:.0f}" height="112" rx="14" fill="none" stroke="{NEON_TXT}" stroke-width="4"/>'
             f'<path d="{name_d}" fill="{NEON_TXT}"/></g>')
    d.append(tpath(silk, "FULL-STACK ENGINEER  /  MULTI-AGENT ORCHESTRATION", 20, 600, 274, OURO, "middle", 1))
    d.append(tpath(silk, "PORTO ALEGRE, BRAZIL", 14, 600, 304, "#cbb9a6", "middle", 2))
    # dust in the light
    for i, (x, y) in enumerate([(330, 80), (880, 70), (420, 300), (790, 290), (980, 150), (220, 300), (520, 60), (690, 320)]):
        d.append(f'<rect x="{x}" y="{y}" width="3" height="3" fill="{LUZ}" class="tw" style="animation-delay:{-i * 0.37:.2f}s"/>')
    defs = (STYLE + NEON_FILTER.format(a=2, b=6, c=14) +
            '<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a1912"/><stop offset=".6" stop-color="#3a130f"/><stop offset="1" stop-color="#1d0906"/></linearGradient>'
            '<radialGradient id="warm"><stop offset="0" stop-color="#ffd45c" stop-opacity=".35"/><stop offset="1" stop-color="#ffd45c" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="lglow"><stop offset="0" stop-color="#ffb060" stop-opacity=".55"/><stop offset="1" stop-color="#ff7a3a" stop-opacity="0"/></radialGradient>')
    return svg(W, H, "".join(d), "Daniel Rodrigues: full-stack engineer, multi-agent orchestration, Porto Alegre, Brazil", defs)


def sign(label, icon_sprite, fname):
    """Section header: a small neon sign on a lacquer plaque."""
    size = 34
    _, tw = text(pix, label, size, 0, 0, "start", 1)
    W = int(tw + 32 + 48 + 34)
    H = 64
    body = [f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="6" fill="{TINTA}" stroke="{OURO}" stroke-width="3"/>',
            f'<g shape-rendering="crispEdges">{icon_sprite.svg(3, 16, 8)}</g>',
            f'<g class="flicker" filter="url(#neon)">{tpath(pix, label, size, 76, 44, NEON_TXT, "start", 1)}</g>']
    write(fname, svg(W, H, "".join(body), label, STYLE + NEON_FILTER.format(a=1.2, b=3.5, c=8)))


def featured():
    W, H = 1200, 260
    m = mascot()
    body = [f'<rect width="{W}" height="{H}" fill="url(#wall)"/>',
            f'<rect x="3" y="3" width="{W - 6}" height="{H - 6}" fill="none" stroke="{OURO}" stroke-width="6"/>',
            f'<ellipse cx="170" cy="130" rx="150" ry="120" fill="url(#warm)" class="pulse"/>',
            f'<g shape-rendering="crispEdges">{m.svg(11, 170 - 88, 130 - 88)}</g>',
            f'<g class="flicker" filter="url(#neon)">{tpath(pix, "maître", 96, 330, 128, NEON_TXT, "start", 2)}</g>',
            tpath(pix, "Your agents' lounge.", 34, 334, 182, LUZ),
            tpath(silk, "TERMINAL ORCHESTRATOR FOR CLAUDE CODE AGENTS  /  EARLY", 15, 334, 220, OURO, "start", 1)]
    # small lanterns at the right
    for cx, cls in ((1060, "a"), (1130, "b")):
        body.append(f'<g class="sway {cls}" style="transform-origin:{cx}px 6px" shape-rendering="crispEdges">'
                    f'<rect x="{cx - 1}" y="6" width="2" height="24" fill="#5a3320"/>{lantern().svg(4, cx - 32, 30)}</g>')
    defs = (STYLE + NEON_FILTER.format(a=2, b=6, c=14) +
            '<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a0e0a"/><stop offset="1" stop-color="#140b08"/></linearGradient>'
            '<radialGradient id="warm"><stop offset="0" stop-color="#ffd45c" stop-opacity=".35"/><stop offset="1" stop-color="#ffd45c" stop-opacity="0"/></radialGradient>')
    write("maitre.svg", svg(W, H, "".join(body), "maître: your agents' lounge", defs))


def footer():
    W, H = 1200, 70
    body = [f'<g shape-rendering="crispEdges">{frieze(0, W, 0, 30)}</g>',
            tpath(silk, "SEATING AGENTS SINCE 2026", 14, 600, 58, "#a8957f", "middle", 3)]
    write("footer.svg", svg(W, H, "".join(body), "Seating agents since 2026"))


def write(fname, content):
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(content)


def icon(sp, fname, title, s=3):
    write(fname,
        svg(16 * s, 16 * s, f'<g shape-rendering="crispEdges">{sp.svg(s)}</g>', title))


os.makedirs(OUT, exist_ok=True)
write("banner.svg", banner())
featured()
footer()
sign("about", mascot(), "h-about.svg")
sign("now building", bell(), "h-building.svg")
sign("selected work", lantern(), "h-work.svg")
sign("experience", ic_case(), "h-experience.svg")
sign("education", ic_cap(), "h-education.svg")
sign("stack", ic_clipboard(), "h-stack.svg")
for fn, sp, t in [("i-ticket.svg", ic_ticket(), "ticket"), ("i-console.svg", ic_console(), "console"),
                  ("i-moon.svg", ic_moon(), "moon"), ("i-spec.svg", ic_clipboard(), "clipboard"),
                  ("i-broom.svg", ic_broom(), "broom"), ("i-book.svg", ic_book(), "book"),
                  ("i-shield.svg", ic_shield(), "shield"), ("i-mask.svg", ic_mask(), "mask")]:
    icon(sp, fn, t)
print("ok")

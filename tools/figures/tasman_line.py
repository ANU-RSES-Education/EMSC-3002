"""The Tasman "Line" — and why the figure deliberately does not draw one.

The classic definition is the boundary between Precambrian outcrop to
the west and Phanerozoic to the east, so the obvious figure is that
contact drawn as a line. Two attempts at tracing it convinced me not to
ship one. Taking the easternmost Precambrian pixel per row produces a
spike straight across the continent wherever the eastern Precambrian is
absent and the trace jumps back to the Yilgarn — the construction fails
exactly where the concept does, which is cute but is an artefact, not a
result. Any smoothed version is then my invention rather than anyone's
published trace.

So this shades the two domains the base map already distinguishes,
Precambrian against Phanerozoic, and marks the north Queensland inliers
— Coen, Yambo, Georgetown — which carry the easternmost Precambrian
outcrop and are separated from the Tasmanides by the faults that define
the line in the north. (An earlier draft marked Mount Isa and Curnamona
as sitting "east of the line"; they do not, they are interior to the
Precambrian, and the claim was wrong.) No new geometry is asserted.
Direen & Crawford (2003) found the published definitions mutually
inconsistent and proposed abandoning the concept.

Base map: Woudloper, Wikimedia Commons, CC BY 4.0.
Run:  pixi run python tools/figures/tasman_line.py
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
IMG = os.path.join(ROOT, "Lectures", "images", "Australia")
BASE = os.path.join(IMG, "australia-cratons-base.png")

ARCHAEAN = (142, 124, 83)
PROTEROZOIC = (187, 165, 119)
PHANEROZOIC = (215, 195, 160)

X_W, LON_W = 370, 113.16
X_E, LON_E = 3493, 153.63
Y_S, LAT_S = 2495, -39.14
SX = (X_E - X_W) / (LON_E - LON_W)
X = lambda lon: X_W + (lon - LON_W) * SX
Y = lambda lat: Y_S - (lat - LAT_S) * SX

im = Image.open(BASE).convert("RGB")
a = np.array(im).astype(int)


def mask(rgb, tol=18):
    return (np.abs(a - np.array(rgb)).sum(axis=2) < tol)


precam = mask(ARCHAEAN) | mask(PROTEROZOIC)
phan = mask(PHANEROZOIC)
H, W = precam.shape

fig, ax = plt.subplots(figsize=(11.6, 9.6))
OCEAN = tuple(c / 255 for c in im.getpixel((5, 5)))
fig.patch.set_facecolor(OCEAN)
ax.set_facecolor(OCEAN)
ax.imshow(im)

# Wash the two domains the base map already distinguishes, so the
# contact reads at a glance without a line being drawn over it.
for m, rgb in ((precam, (0.42, 0.13, 0.13)), (phan, (0.05, 0.30, 0.45))):
    ov = np.zeros((H, W, 4))
    ov[..., 0], ov[..., 1], ov[..., 2] = rgb
    ov[..., 3] = m * 0.30
    ax.imshow(ov, zorder=3)

ax.text(X(126.5), Y(-21.0), "PRECAMBRIAN", fontsize=17, color="#6b1414",
        ha="center", va="center", zorder=6, weight="bold", alpha=0.85)
ax.text(X(149.5), Y(-28.5), "TASMANIDES\n(Phanerozoic)", fontsize=15,
        color="#0d3a55", ha="center", va="center", zorder=6, weight="bold",
        alpha=0.9, linespacing=1.3)

for nm, lat, lon, dx, dy in [("Coen", -13.90, 143.20, 300, -150),
                             ("Yambo", -16.50, 144.50, 330, -30),
                             ("Georgetown", -18.30, 143.55, 300, 170)]:
    ax.plot(X(lon), Y(lat), "o", ms=13, mfc="none", mec="white", mew=4.5,
            zorder=5)
    ax.plot(X(lon), Y(lat), "o", ms=13, mfc="none", mec="#1a237e", mew=2.6,
            zorder=6)
    ax.annotate(nm, xy=(X(lon), Y(lat)),
                xytext=(X(lon) + dx, Y(lat) + dy), fontsize=11,
                color="#1a237e", ha="center", va="center", zorder=7,
                bbox=dict(fc="white", ec="#1a237e", lw=1.0, alpha=0.93,
                          pad=3),
                arrowprops=dict(arrowstyle="-", lw=1.4, color="#1a237e",
                                shrinkA=2, shrinkB=11))
ax.text(0.5, 0.968,
        "The contact as mapped from OUTCROP — gravity, magnetic, seismic\n"
        "and isotopic definitions put the boundary in different places",
        transform=ax.transAxes, fontsize=12.5, color="#1a237e",
        ha="center", va="top", linespacing=1.45,
        bbox=dict(fc="white", ec="#1a237e", lw=1.2, alpha=0.94, pad=5))
ax.text(X(152.0), Y(-24.5),
        "north Queensland inliers:\nthe easternmost Precambrian,\n"
        "faulted against the Tasmanides",
        fontsize=10.5, color="#1a237e", ha="center", va="center", zorder=7,
        linespacing=1.35,
        bbox=dict(fc="white", ec="#1a237e", lw=1.0, alpha=0.9, pad=4))
ax.text(0.985, 0.012, "Base map: Woudloper, Wikimedia Commons, CC BY 4.0",
        transform=ax.transAxes, fontsize=8.5, color="0.85", ha="right")

ax.set_xlim(120, 3760)
ax.set_ylim(Y(-45.5), 20)
ax.axis("off")
fig.tight_layout(pad=0.2)
out = os.path.join(IMG, "tasman-line.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=OCEAN)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")
print(f"precambrian {precam.sum() / 1e6:.2f} Mpx, "
      f"phanerozoic {phan.sum() / 1e6:.2f} Mpx")

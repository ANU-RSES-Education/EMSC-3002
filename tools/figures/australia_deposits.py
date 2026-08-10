"""Major Australian ore deposits, on the craton/age base map.

Puts a handful of world-class deposits onto the Archaean / Proterozoic /
Phanerozoic map used in Module 1.1a, so students can see the point that
matters: *which deposits you get depends on which piece of crust you are
standing on, and when that piece formed.*

Base map: "Australia cratons EN.svg" by Woudloper, Wikimedia Commons,
CC BY 4.0 — https://commons.wikimedia.org/wiki/File:Australia_cratons_EN.svg
The rendered PNG is committed beside this script's output so the figure
can be rebuilt without re-fetching.

Georeferencing: the base map is EQUIRECTANGULAR (verified — a Mercator
fit puts every deposit about two degrees too far north, and lands
Kalgoorlie outside the Yilgarn). Longitude is calibrated on the
mainland's east-west extremes, which give the longest and therefore most
robust baseline; latitude uses the same degrees-per-pixel anchored on the
southernmost mainland point. Every marker was then checked against the
province it is known to sit in.

Run:  pixi run python tools/figures/australia_deposits.py
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

# --- georeference (equirectangular) -----------------------------------------
X_W, LON_W = 370, 113.16      # Steep Point, mainland westernmost
X_E, LON_E = 3493, 153.63     # Cape Byron, mainland easternmost
Y_S, LAT_S = 2495, -39.14     # Wilsons Promontory, mainland southernmost
SX = (X_E - X_W) / (LON_E - LON_W)


def X(lon):
    return X_W + (lon - LON_W) * SX


def Y(lat):
    return Y_S - (lat - LAT_S) * SX


# --- what to show -----------------------------------------------------------
# (name, lat, lon, commodity, why it is here, label offset in px, colour)
IRON, GOLD, POLY, IOCG, LIFE = ("#b03a2e", "#b8860b", "#5b2c8d",
                                "#0b6e4f", "#1565c0")
SITES = [
    ("Hamersley\n(Mt Whaleback)", -23.36, 119.75, "iron ore — BIF",
     (-620, 210), IRON),
    ("Strelley Pool", -21.15, 119.40, "3.4 Ga stromatolites",
     (-560, -230), LIFE),
    ("Kalgoorlie", -30.75, 121.47, "gold — greenstone belts",
     (-140, 330), GOLD),
    ("Olympic Dam", -30.44, 136.89, "Cu–U–Au (IOCG)", (330, 190), IOCG),
    ("Mount Isa", -20.72, 139.49, "Pb–Zn–Ag", (330, -170), POLY),
    ("Broken Hill", -31.96, 141.47, "Pb–Zn–Ag", (400, 210), POLY),
]

im = Image.open(BASE).convert("RGB")
W, H = im.size
# Callout boxes sit outside the map edge; painting the figure in the
# map's own ocean colour makes that margin continuous with the sea
# instead of a white notch on one side.
OCEAN = tuple(c / 255 for c in im.getpixel((5, 5)))
fig, ax = plt.subplots(figsize=(13.2, 10.4), facecolor=OCEAN)
ax.set_facecolor(OCEAN)
ax.imshow(im)

for name, lat, lon, what, (dx, dy), col in SITES:
    x, y = X(lon), Y(lat)
    ax.plot(x, y, "o", ms=17, mfc="none", mec="white", mew=5.0, zorder=4)
    ax.plot(x, y, "o", ms=17, mfc="none", mec=col, mew=3.0, zorder=5)
    ax.plot(x, y, "o", ms=4, color=col, zorder=5)
    ax.annotate(f"{name}\n{what}", xy=(x, y), xytext=(x + dx, y + dy),
                fontsize=12.5, color=col, ha="center", va="center",
                zorder=6, linespacing=1.35,
                bbox=dict(fc="white", ec=col, lw=1.2, alpha=0.93, pad=4.0),
                arrowprops=dict(arrowstyle="-", lw=1.6, color=col,
                                shrinkA=2, shrinkB=13))

ax.text(0.985, 0.018,
        "Base map: Woudloper, Wikimedia Commons, CC BY 4.0",
        transform=ax.transAxes, fontsize=8.5, color="0.85",
        ha="right", va="bottom")
ax.set_xlim(120, 3720)
ax.set_ylim(H - 40, 20)
ax.axis("off")
fig.tight_layout(pad=0.2)
out = os.path.join(IMG, "australia-deposits.png")
fig.savefig(out, dpi=155, bbox_inches="tight", facecolor=OCEAN)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")

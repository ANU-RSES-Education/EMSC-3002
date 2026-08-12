"""Lithospheric thickness beneath Australia — and why ore deposits care.

Depth to the lithosphere–asthenosphere boundary from LithoRef18, on the
same base map as the Moho, stress, seismicity and deposit figures.

The 170 km contour is picked out deliberately. Hoggard et al. (2020)
showed that sediment-hosted base metal deposits sit preferentially at
the STEP between thick and thin lithosphere: 85% of them, and every
giant deposit, fall within 200 km of that transition. Australia supplies
two of the textbook examples — Mount Isa and Broken Hill — and they are
plotted here so students can check the claim against the map themselves
rather than take it on trust.

Data: LithoRef18, Afonso, Salajegheh, Szwillus, Ebbing & Gaina (2019),
Geophys. J. Int. 217, 1602-1628, doi:10.1093/gji/ggz094; grid hosted by
EarthByte. Preferred over LITHO1.0 as the more modern reference model.
The native model is 2 degrees — this is EarthByte's GMT-surfaced 0.25
degree rendering, so it is SMOOTHER THAN THE UNDERLYING DATA. Do not
read detail from it at province scale; the first-order thick/thin
contrast is the point.

Run:  pixi run python tools/figures/australia_lab.py
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import ausmap as am

DATA = os.path.join(am.DIR, "data", "au_lab.csv")
CRATON_EDGE = 170.0        # km — Hoggard et al. (2020) craton-edge proxy

lon, lat, lab = [], [], []
for r in csv.DictReader(open(DATA)):
    lon.append(float(r["lon"]))
    lat.append(float(r["lat"]))
    lab.append(float(r["lab_km"]))
lon, lat, lab = np.array(lon), np.array(lat), np.array(lab)

ulon, ulat = np.unique(lon), np.unique(lat)
grid = np.full((len(ulat), len(ulon)), np.nan)
grid[np.searchsorted(ulat, lat), np.searchsorted(ulon, lon)] = lab

im, arr, ocean = am.load()
LON, LAT = np.meshgrid(ulon, ulat)
onland = am.on_land(arr, LAT.ravel(), LON.ravel()).reshape(LAT.shape)
land = np.where(onland, grid, np.nan)
v = land[np.isfinite(land)]
lo, hi = np.percentile(v, [2, 98])
print(f"{onland.sum()} nodes on land; LAB {v.min():.0f}–{v.max():.0f} km "
      f"raw, {lo:.0f}–{hi:.0f} km at the 2nd–98th percentile")

fig, ax = plt.subplots(figsize=(11.8, 9.6))
am.setup(ax, fig, ocean, im)

extent = [float(am.X(ulon.min())), float(am.X(ulon.max())),
          float(am.Y(ulat.min())), float(am.Y(ulat.max()))]
pc = ax.imshow(land, origin="lower", extent=extent, cmap="magma_r",
               vmin=60, vmax=220, alpha=0.88, zorder=4,
               interpolation="bilinear")
edge = ax.contour(am.X(LON), am.Y(LAT), land, levels=[CRATON_EDGE],
                  colors="#00e5ff", linewidths=3.2, zorder=6)
ax.clabel(edge, fmt=f"{CRATON_EDGE:.0f} km", fontsize=10, colors="#00e5ff")
am.province_outlines(ax, arr, color="white", lw=1.2, alpha=0.5)

# the two Australian sediment-hosted giants
for nm, la, lo_, dx, dy in [("Mount Isa", -20.72, 139.49, 330, -230),
                            ("Broken Hill", -31.96, 141.47, 430, 180)]:
    x, y = float(am.X(lo_)), float(am.Y(la))
    ax.plot(x, y, "o", ms=15, mfc="none", mec="white", mew=4.5, zorder=7)
    ax.plot(x, y, "o", ms=15, mfc="none", mec="#00e5ff", mew=2.4, zorder=8)
    ax.annotate(nm, xy=(x, y), xytext=(x + dx, y + dy), fontsize=12.5,
                color="#065a66", ha="center", va="center", zorder=9,
                bbox=dict(fc="white", ec="#00e5ff", lw=1.4, alpha=0.95,
                          pad=4),
                arrowprops=dict(arrowstyle="-", lw=1.6, color="#00e5ff",
                                shrinkA=2, shrinkB=13))

cb = fig.colorbar(pc, ax=ax, fraction=0.030, pad=0.01)
cb.set_label("depth to the lithosphere–asthenosphere boundary (km)",
             fontsize=10.5)
cb.ax.tick_params(labelsize=9)
ax.text(0.5, 0.972,
        "Thick lithosphere west and centre, thin in the east — and the "
        f"deposits sit on the {CRATON_EDGE:.0f} km step",
        transform=ax.transAxes, fontsize=12.5, color="#111", ha="center",
        va="top",
        bbox=dict(fc="white", ec="0.4", lw=1.2, alpha=0.94, pad=5))
am.credit(ax, "LAB: LithoRef18 (Afonso et al. 2019), via EarthByte")

fig.tight_layout(pad=0.2)
out = os.path.join(am.IMG, "australia-lab.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=ocean)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")

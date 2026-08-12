"""Bouguer gravity: the density structure under the cover.

The complete spherical cap Bouguer anomaly, masked to land and shown on
the shared base map. With the sediment figure it makes the pair the deck
needs: most of Australia's geology is buried, and gravity plus magnetics
are how it is mapped anyway. Craton edges and deep basins are the
features to look for.

Units: Geoscience Australia distributes these grids in micrometres per
second squared; 10 um/s^2 = 1 mGal. The file carries no units attribute,
so this is checked against the onshore range printed below — a few
hundred um/s^2 either side of zero is right for continental Bouguer,
whereas mGal would put it in the thousands.

Data: National Gravity Compilation 2019 (CSCBA), Geoscience Australia,
eCat 144786; the file's metadata states CC BY 4.0.

Run:  pixi run python tools/figures/australia_gravity.py
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import ausmap as am

d = np.load(os.path.join(am.DIR, "data", "au_gravity.npz"))
z, glat, glon = d["z"], d["lat"], d["lon"]
# This grid is GDAL-derived and its latitudes run NORTH to SOUTH, unlike
# the Moho and LAB grids. Left unhandled it renders upside down AND
# mis-associates the land mask, so sort into ascending order here.
if glat[0] > glat[-1]:
    glat = glat[::-1]
    z = z[::-1, :]
assert glat[0] < glat[-1] and glon[0] < glon[-1]

im, arr, ocean = am.load()
LON, LAT = np.meshgrid(glon, glat)
onland = am.on_land(arr, LAT.ravel(), LON.ravel()).reshape(LAT.shape)
land = np.where(onland & np.isfinite(z), z, np.nan)
v = land[np.isfinite(land)]
lo, hi = np.percentile(v, [1, 99])
print(f"{onland.sum()} cells on land; onshore Bouguer {v.min():.0f} to "
      f"{v.max():.0f}, 1st–99th percentile {lo:.0f} to {hi:.0f}, "
      f"median {np.median(v):.0f} um/s^2  "
      f"({lo / 10:.0f} to {hi / 10:.0f} mGal)")

fig, ax = plt.subplots(figsize=(11.8, 9.6))
am.setup(ax, fig, ocean, im)

lim = float(max(abs(lo), abs(hi)))
extent = [float(am.X(glon.min())), float(am.X(glon.max())),
          float(am.Y(glat.min())), float(am.Y(glat.max()))]
pc = ax.imshow(land, origin="lower", extent=extent, cmap="RdYlBu_r",
               vmin=-lim, vmax=lim, alpha=0.9, zorder=4,
               interpolation="bilinear")
am.province_outlines(ax, arr, color="black", lw=1.2, alpha=0.5)

cb = fig.colorbar(pc, ax=ax, fraction=0.030, pad=0.01)
cb.set_label(r"Bouguer anomaly ($\mu$m s$^{-2}$;  10 = 1 mGal)",
             fontsize=10.5)
cb.ax.tick_params(labelsize=9)
ax.text(0.5, 0.972,
        "Density structure, straight through the cover",
        transform=ax.transAxes, fontsize=13, color="#111", ha="center",
        va="top",
        bbox=dict(fc="white", ec="0.4", lw=1.2, alpha=0.94, pad=5))
am.credit(ax, "Gravity: National Gravity Compilation 2019, GA, CC BY 4.0")

fig.tight_layout(pad=0.2)
out = os.path.join(am.IMG, "australia-gravity.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=ocean)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")

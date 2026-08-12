"""Depth to basement: how much sediment sits on top of the story.

Every other figure in this set shows the basement — provinces, Moho,
lithospheric thickness. This one shows what is in the way. Most of
Australia's geology is not exposed; it is under kilometres of basin fill,
which is why the magnetic and gravity "X-rays" matter so much here.

Data: OZ SEEBASE 2021, Geognostics Australia Pty Ltd, served by
Geoscience Australia's Estimates of Geological and Geophysical Surfaces
WCS. CC BY 4.0 per the GA eCat record — worth saying out loud, because
OZ SEEBASE is a commercial product and the natural assumption is that it
is off limits. It is not, with attribution.

Run:  pixi run python tools/figures/australia_sediment.py
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

import ausmap as am

d = np.load(os.path.join(am.DIR, "data", "au_sediment.npz"))
z = d["z"] / 1000.0                       # metres -> km
lon0, lat0, lon1, lat1 = d["bbox"]

im, arr, ocean = am.load()
h, w = z.shape
lons = np.linspace(lon0, lon1, w)
lats = np.linspace(lat1, lat0, h)         # GeoTIFF rows run north -> south
LON, LAT = np.meshgrid(lons, lats)
onland = am.on_land(arr, LAT.ravel(), LON.ravel()).reshape(LAT.shape)
land = np.where(onland & np.isfinite(z), z, np.nan)
v = land[np.isfinite(land)]
print(f"{onland.sum()} cells on land; sediment 0–{v.max():.1f} km, "
      f"median {np.median(v):.2f} km, "
      f"{100 * (v > 1).mean():.0f}% of the continent under >1 km")

fig, ax = plt.subplots(figsize=(11.8, 9.6))
am.setup(ax, fig, ocean, im)

extent = [float(am.X(lon0)), float(am.X(lon1)),
          float(am.Y(lat0)), float(am.Y(lat1))]
# thickness spans four orders of magnitude, so a log scale is the only
# way to see both the shallow shields and the deep basins at once
pc = ax.imshow(np.flipud(land), origin="lower", extent=extent,
               cmap="YlGnBu", norm=LogNorm(vmin=0.1, vmax=15),
               alpha=0.9, zorder=4, interpolation="bilinear")
am.province_outlines(ax, arr, color="black", lw=1.2, alpha=0.45)

for nm, la, lo in [("Canning", -19.5, 124.0), ("Amadeus", -24.5, 132.0),
                   ("Officer", -27.5, 129.0), ("Eromanga", -26.0, 142.5),
                   ("Otway", -38.3, 142.5), ("NW Shelf", -18.5, 117.5)]:
    ax.text(float(am.X(lo)), float(am.Y(la)), nm, fontsize=11.5,
            color="#0d2f4f", ha="center", va="center", zorder=8,
            bbox=dict(fc="white", ec="none", alpha=0.8, pad=2))

cb = fig.colorbar(pc, ax=ax, fraction=0.030, pad=0.01)
cb.set_label("sediment thickness (km)", fontsize=11)
cb.ax.tick_params(labelsize=9)
ax.text(0.5, 0.972,
        "Most of the continent's geology is buried — this is how deep",
        transform=ax.transAxes, fontsize=13, color="#111", ha="center",
        va="top",
        bbox=dict(fc="white", ec="0.4", lw=1.2, alpha=0.94, pad=5))
am.credit(ax, "Sediment: OZ SEEBASE 2021 (Geognostics) via GA, CC BY 4.0")

fig.tight_layout(pad=0.2)
out = os.path.join(am.IMG, "australia-sediment.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=ocean)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")

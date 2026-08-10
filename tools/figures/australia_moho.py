"""Moho depth beneath Australia, on the craton base map.

AusMoho gives the depth to the crust–mantle boundary on a 0.25 degree
grid, built from decades of refraction, reflection and receiver-function
work. Plotted here on the same base map as the province, deposit,
seismicity and stress figures, so the crustal-thickness pattern can be
read directly against the geology.

The grid extends well offshore; it is masked to mapped land, because the
teaching point is the contrast between provinces and the offshore values
would otherwise dominate the colour range.

Data: Kennett, B. (2019), AusMoho, AusPass / ANU Data Commons,
doi:10.25911/5cf751c17b3d4 — AuSREM 2023 Moho surface, CC BY 4.0.
Fetched by tools/figures/fetch_data.py.

Run:  pixi run python tools/figures/australia_moho.py
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import ausmap as am

DATA = os.path.join(am.DIR, "data", "au_moho.csv")

lon, lat, moho = [], [], []
for r in csv.DictReader(open(DATA)):
    lon.append(float(r["lon"]))
    lat.append(float(r["lat"]))
    moho.append(float(r["moho_km"]))
lon, lat, moho = np.array(lon), np.array(lat), np.array(moho)

ulon, ulat = np.unique(lon), np.unique(lat)
grid = np.full((len(ulat), len(ulon)), np.nan)
ix = np.searchsorted(ulon, lon)
iy = np.searchsorted(ulat, lat)
grid[iy, ix] = moho
print(f"grid {grid.shape}, lon {ulon.min()}–{ulon.max()}, "
      f"lat {ulat.min()}–{ulat.max()}")

im, arr, ocean = am.load()

# mask to mapped land, sampling the land mask at each grid node
LON, LAT = np.meshgrid(ulon, ulat)
onland = am.on_land(arr, LAT.ravel(), LON.ravel()).reshape(LAT.shape)
grid = np.where(onland, grid, np.nan)
vals = grid[np.isfinite(grid)]
# Nodes right on the coast pick up thinned/marginal crust and drag the
# extremes down to values no continent has (13 km). Quote a robust range.
lo, hi = np.percentile(vals, [2, 98])
print(f"{onland.sum()} nodes on land; Moho {vals.min():.1f}–"
      f"{vals.max():.1f} km raw, {lo:.0f}–{hi:.0f} km at the 2nd–98th "
      f"percentile, median {np.median(vals):.1f} km")

fig, ax = plt.subplots(figsize=(11.8, 9.6))
am.setup(ax, fig, ocean, im)

# equirectangular, so a single extent is exact
extent = [float(am.X(ulon.min())), float(am.X(ulon.max())),
          float(am.Y(ulat.min())), float(am.Y(ulat.max()))]
pc = ax.imshow(grid, origin="lower", extent=extent, cmap="viridis",
               vmin=25, vmax=52, alpha=0.85, zorder=4,
               interpolation="bilinear")
cs = ax.contour(am.X(LON), am.Y(LAT), grid, levels=[30, 35, 40, 45, 50],
                colors="white", linewidths=0.8, alpha=0.5, zorder=5)
ax.clabel(cs, fmt="%d", fontsize=8, colors="white")
# the filled field hides the base map's colours, so outline the provinces
am.province_outlines(ax, arr, color="black", lw=1.4, alpha=0.55)

cb = fig.colorbar(pc, ax=ax, fraction=0.030, pad=0.01)
cb.set_label("Moho depth (km)", fontsize=11)
cb.ax.tick_params(labelsize=9)
ax.text(0.5, 0.972,
        f"Depth to the crust–mantle boundary: most of the continent "
        f"lies between {lo:.0f} and {hi:.0f} km",
        transform=ax.transAxes, fontsize=13, color="#111", ha="center",
        va="top",
        bbox=dict(fc="white", ec="0.4", lw=1.2, alpha=0.94, pad=5))
am.credit(ax, "Moho: AusMoho / AuSREM 2023 (Kennett), CC BY 4.0")

fig.tight_layout(pad=0.2)
out = os.path.join(am.IMG, "australia-moho.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=ocean)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")

"""Australian seismicity: where stress meets inherited structure.

Intraplate earthquakes are not spread evenly across the continent — they
cluster, and the clusters sit on old structure. This plots the recorded
epicentres on the same craton base map as the other 1.1a figures so the
clusters can be read against the provinces directly.

Events are filtered to MAPPED LAND using the base map's own land mask.
Without that the query is dominated by the Banda Arc and New Guinea
plate boundaries a few hundred kilometres north, which are a different
phenomenon entirely and would bury the intraplate signal.

Data: USGS ComCat (which folds in the ISC-GEM catalogue), M >= 4.
Fetched by tools/figures/fetch_data.py; the extract is committed.

Run:  pixi run python tools/figures/australia_seismicity.py
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import ausmap as am

DATA = os.path.join(am.DIR, "data", "au_earthquakes.csv")

lat, lon, mag = [], [], []
for r in csv.DictReader(open(DATA)):
    lat.append(float(r["latitude"]))
    lon.append(float(r["longitude"]))
    mag.append(float(r["mag"]))
lat, lon, mag = np.array(lat), np.array(lon), np.array(mag)

im, arr, ocean = am.load()
keep = am.on_land(arr, lat, lon)
lat, lon, mag = lat[keep], lon[keep], mag[keep]
print(f"{keep.sum()} of {len(keep)} events fall on mapped land; "
      f"M {mag.min():.1f}–{mag.max():.1f}")

fig, ax = plt.subplots(figsize=(11.8, 9.6))
am.setup(ax, fig, ocean, im)

order = np.argsort(mag)                     # big events drawn on top
sz = 9 * (mag[order] - 3.2) ** 2.6
sc = ax.scatter(am.X(lon[order]), am.Y(lat[order]), s=sz, c=mag[order],
                cmap="YlOrRd", vmin=4, vmax=6.5, alpha=0.82,
                edgecolors="0.15", linewidths=0.5, zorder=5)

# the three zones the deck names
for nm, lat0, lon0, dx, dy in [
        ("South West\nSeismic Zone", -32.0, 117.2, -560, 120),
        ("Flinders\nRanges", -31.5, 138.6, -430, 330),
        ("SE Highlands", -36.0, 148.5, 430, 260)]:
    ax.annotate(nm, xy=(am.X(lon0), am.Y(lat0)),
                xytext=(am.X(lon0) + dx, am.Y(lat0) + dy),
                fontsize=13, color="#7f1010", ha="center", va="center",
                zorder=7, linespacing=1.3,
                bbox=dict(fc="white", ec="#7f1010", lw=1.3, alpha=0.94,
                          pad=4),
                arrowprops=dict(arrowstyle="-|>", lw=1.8, color="#7f1010"))

cb = fig.colorbar(sc, ax=ax, fraction=0.030, pad=0.01)
cb.set_label("magnitude", fontsize=11)
cb.ax.tick_params(labelsize=9)
ax.text(0.5, 0.972,
        f"{len(mag)} earthquakes, M $\\geq$ 4 — and they are not "
        "spread evenly",
        transform=ax.transAxes, fontsize=13.5, color="#7f1010",
        ha="center", va="top",
        bbox=dict(fc="white", ec="#7f1010", lw=1.2, alpha=0.94, pad=5))
am.credit(ax, "Earthquakes: USGS ComCat / ISC-GEM")

fig.tight_layout(pad=0.2)
out = os.path.join(am.IMG, "australia-seismicity.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=ocean)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")

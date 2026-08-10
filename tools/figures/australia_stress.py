"""The Australian stress field, from the World Stress Map.

Each tick is one measurement, drawn along the maximum horizontal
compression direction SHmax and coloured by the stress regime it
implies. Plotted on the same craton base map as the other 1.1a figures,
so the stress pattern can be read against the provinces and against the
seismicity.

Only quality A–C records are shown, which is the World Stress Map's own
convention for "reliable enough to interpret"; D and E are dropped.

The point of the slide it serves: Australia is in COMPRESSION almost
everywhere, and SHmax swings systematically across the continent rather
than pointing one way. Both facts are consequences of plate-boundary
forces, not of anything local — which is why Module 1.3 can treat the
whole continent as one loaded plate.

Data: World Stress Map Database Release 2016 (Heidbach et al., GFZ Data
Services, doi:10.5880/WSM.2016.001), CC BY 4.0. Fetched by
tools/figures/fetch_data.py; the Australian extract is committed.

Run:  pixi run python tools/figures/australia_stress.py
"""
import csv
import os
from collections import Counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

import ausmap as am

DATA = os.path.join(am.DIR, "data", "au_stress.csv")

# World Stress Map regime colours
REGIME = {"NF": ("#d32f2f", "normal — extension"),
          "NS": ("#d32f2f", None),
          "SS": ("#2e7d32", "strike-slip"),
          "TS": ("#1565c0", None),
          "TF": ("#1565c0", "thrust — compression"),
          "U": ("0.35", "undetermined")}

lat, lon, azi, reg = [], [], [], []
for r in csv.DictReader(open(DATA)):
    if r["QUALITY"] not in ("A", "B", "C"):
        continue
    try:
        a = float(r["AZI"])
    except (TypeError, ValueError):
        continue
    lat.append(float(r["LAT"]))
    lon.append(float(r["LON"]))
    azi.append(a)
    reg.append(r["REGIME"] if r["REGIME"] in REGIME else "U")
lat, lon, azi = np.array(lat), np.array(lon), np.array(azi)
reg = np.array(reg)

im, arr, ocean = am.load()
keep = am.on_land(arr, lat, lon)
lat, lon, azi, reg = lat[keep], lon[keep], azi[keep], reg[keep]
counts = Counter(reg)
print(f"{len(lat)} quality A–C records on mapped land")
print("  regimes:", dict(counts))
# Most records carry no regime, so the meaningful statistic is the share
# of those where it WAS determined — not the share of all records.
determined = sum(counts[k] for k in ("TF", "TS", "SS", "NF", "NS"))
compressive = sum(counts[k] for k in ("TF", "TS", "SS"))
print(f"  regime determined for {determined} records; of those, "
      f"{compressive} are compressional (TF/TS/SS) = "
      f"{100 * compressive / max(determined, 1):.0f}%, and "
      f"{counts['NF'] + counts['NS']} are extensional")

fig, ax = plt.subplots(figsize=(11.8, 9.6))
am.setup(ax, fig, ocean, im)

L = 52.0                       # half-length of each tick, in pixels
x, y = am.X(lon), am.Y(lat)
# WSM azimuths are degrees clockwise from north; image y increases south
dx = L * np.sin(np.radians(azi))
dy = -L * np.cos(np.radians(azi))
for r in ("U", "SS", "NF", "NS", "TS", "TF"):
    m = reg == r
    if not m.any():
        continue
    col = REGIME[r][0]
    segs = np.empty((2 * m.sum(), 2))
    segs[0::2, 0], segs[0::2, 1] = x[m] - dx[m], y[m] - dy[m]
    segs[1::2, 0], segs[1::2, 1] = x[m] + dx[m], y[m] + dy[m]
    for i in range(m.sum()):
        ax.plot(segs[2 * i:2 * i + 2, 0], segs[2 * i:2 * i + 2, 1], "-",
                color=col, lw=2.0, alpha=0.85, zorder=5,
                solid_capstyle="round")

ax.text(0.5, 0.972,
        f"{len(lat)} stress measurements — ticks show $S_{{Hmax}}$, "
        "the direction of greatest horizontal compression",
        transform=ax.transAxes, fontsize=12.5, color="#111", ha="center",
        va="top",
        bbox=dict(fc="white", ec="0.4", lw=1.2, alpha=0.94, pad=5))
ax.legend(handles=[Line2D([], [], color=c, lw=3, label=lab)
                   for c, lab in
                   [REGIME[k] for k in ("TF", "SS", "NF", "U")]],
          loc="upper right", fontsize=11, framealpha=0.94,
          title="stress regime", title_fontsize=11)
am.credit(ax, "Stress: World Stress Map 2016 (Heidbach et al.), CC BY 4.0")

fig.tight_layout(pad=0.2)
out = os.path.join(am.IMG, "australia-stress.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=ocean)
print(f"wrote {out} ({os.path.getsize(out) / 1024:.0f} KB)")

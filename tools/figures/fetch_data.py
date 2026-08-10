"""Fetch the public datasets the 1.1a figures are built from.

Run once; the extracts are small and are committed, so the figure
scripts rebuild offline. Re-run only to refresh.

    pixi run python tools/figures/fetch_data.py

Sources and licences:
  * Earthquakes — USGS ComCat FDSN event service, which folds in
    ISC-GEM. US Government work / ISC-GEM is CC BY.
  * Stress — World Stress Map Database Release 2016, Heidbach, O.,
    Rajabi, M., Reiter, K., Ziegler, M. & WSM Team, GFZ Data Services,
    doi:10.5880/WSM.2016.001, CC BY 4.0. The full release is ~9.5 MB
    and global; only the Australian window is kept.
  * Moho — AusMoho / AuSREM 2023 Moho surface at 0.25 degrees. Kennett,
    B. (2019), AusMoho, AusPass and the ANU Data Commons,
    doi:10.25911/5cf751c17b3d4, CC BY 4.0.
"""
import csv
import io
import os
import urllib.request

DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(DIR, "data")
os.makedirs(OUT, exist_ok=True)

BOX = dict(latmin=-45, latmax=-9, lonmin=110, lonmax=156)
UA = {"User-Agent": "EMSC3002-course-materials/1.0 "
                    "(louis.moresi@anu.edu.au)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


# --- earthquakes ------------------------------------------------------------
q = ("https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv"
     f"&minlatitude={BOX['latmin']}&maxlatitude={BOX['latmax']}"
     f"&minlongitude={BOX['lonmin']}&maxlongitude={BOX['lonmax']}"
     "&minmagnitude=4.0&starttime=1900-01-01")
rows = list(csv.DictReader(io.StringIO(get(q).decode())))
keep = ("time", "latitude", "longitude", "depth", "mag", "place")
dst = os.path.join(OUT, "au_earthquakes.csv")
with open(dst, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=keep)
    w.writeheader()
    for r in rows:
        if r.get("type") != "earthquake":
            continue
        w.writerow({k: r[k] for k in keep})
print(f"wrote {dst}: {sum(1 for _ in open(dst)) - 1} events")

# --- stress -----------------------------------------------------------------
wsm = get("https://datapub.gfz-potsdam.de/download/"
          "10.5880.WSM.2016.001/wsm2016.csv").decode("latin-1")
rows = list(csv.DictReader(io.StringIO(wsm)))
keep = ("ID", "LAT", "LON", "AZI", "TYPE", "DEPTH", "QUALITY", "REGIME")
dst = os.path.join(OUT, "au_stress.csv")
n = 0
with open(dst, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=keep)
    w.writeheader()
    for r in rows:
        try:
            la, lo = float(r["LAT"]), float(r["LON"])
        except (TypeError, ValueError):
            continue
        if not (BOX["latmin"] < la < BOX["latmax"]
                and BOX["lonmin"] < lo < BOX["lonmax"]):
            continue
        w.writerow({k: r[k] for k in keep})
        n += 1
print(f"wrote {dst}: {n} stress records")

# --- Moho -------------------------------------------------------------------
# 11 header lines, then "longitude latitude moho_km" on a regular grid.
raw = get("https://auspass.edu.au/research/AR23-moho-hm.txt").decode()
dst = os.path.join(OUT, "au_moho.csv")
n = 0
with open(dst, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["lon", "lat", "moho_km"])
    for line in raw.splitlines()[11:]:
        p = line.split()
        if len(p) != 3:
            continue
        lo, la = float(p[0]), float(p[1])
        if not (BOX["latmin"] < la < BOX["latmax"]
                and BOX["lonmin"] < lo < BOX["lonmax"]):
            continue
        w.writerow(p)
        n += 1
print(f"wrote {dst}: {n} Moho grid nodes")

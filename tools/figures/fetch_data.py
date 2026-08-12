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
  * LAB — LithoRef18, Afonso et al. (2019), Geophys. J. Int. 217,
    1602-1628, doi:10.1093/gji/ggz094, hosted by EarthByte for the
    GPlates portal. Chosen over LITHO1.0 as the more modern global
    reference model. NOTE the native model is 2 degrees; the file taken
    here is EarthByte's GMT-surfaced 0.25 degree rendering of it, so it
    is smoother than the underlying resolution.
  * Sediment thickness — OZ SEEBASE 2021 (Geognostics Australia),
    served by Geoscience Australia's "Estimates of Geological and
    Geophysical Surfaces" WCS. CC BY 4.0 per the GA eCat record — worth
    stating plainly, because OZ SEEBASE is a commercial product and the
    obvious assumption is that it cannot be reused. It can, with
    attribution.
  * Gravity — National Gravity Compilation 2019 (complete spherical cap
    Bouguer anomaly), Geoscience Australia, eCat 144786. The file's own
    metadata states "CC BY 4.0 (C) Commonwealth of Australia". The full
    grid is 13441 x 9601 at 15 arc-seconds, so it is read over OPeNDAP
    from NCI with a stride rather than downloaded.
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

# --- LAB --------------------------------------------------------------------
# Global NetCDF; keep only the Australian window as a small CSV so the
# figure scripts need no netCDF dependency and the extract stays committable.
import tempfile

import netCDF4
import numpy as np

blob = get("https://www.earthbyte.org/webdav/ftp/earthbyte/gplates_portal/"
           "Afonso_etal_lithospheric_thickness_GJI2019/"
           "lithospheric-thickness-gmt-surface.nc")
with tempfile.NamedTemporaryFile(suffix=".nc", delete=False) as tf:
    tf.write(blob)
    tmp = tf.name
ds = netCDF4.Dataset(tmp)
lon = np.asarray(ds.variables["lon"][:])
lat = np.asarray(ds.variables["lat"][:])
z = np.asarray(ds.variables["z"][:])            # LAB depth, metres
ds.close()
os.unlink(tmp)
ix = np.nonzero((lon > BOX["lonmin"]) & (lon < BOX["lonmax"]))[0]
iy = np.nonzero((lat > BOX["latmin"]) & (lat < BOX["latmax"]))[0]
dst = os.path.join(OUT, "au_lab.csv")
with open(dst, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["lon", "lat", "lab_km"])
    for j in iy:
        for i in ix:
            v = z[j, i]
            if np.isfinite(v):
                w.writerow([f"{lon[i]:.4f}", f"{lat[j]:.4f}",
                            f"{v / 1000.0:.2f}"])
print(f"wrote {dst}: {len(ix) * len(iy)} LAB grid nodes")

# --- sediment thickness -----------------------------------------------------
# WCS returns a float32 GeoTIFF on the requested bbox, so the geographic
# corners are exactly the bbox and no world file is needed.
SED_BBOX = (110.0, -45.0, 156.0, -9.0)          # lon0, lat0, lon1, lat1
SED_W, SED_H = 920, 720
u = ("https://services.ga.gov.au/gis/eggs/wcs?service=WCS&version=1.0.0"
     "&request=GetCoverage&coverage=eggs:OZSEEBASE_2021_Sediment_"
     "Thickness_Grid_Geognostics&crs=EPSG:4326"
     f"&bbox={SED_BBOX[0]},{SED_BBOX[1]},{SED_BBOX[2]},{SED_BBOX[3]}"
     f"&width={SED_W}&height={SED_H}&format=GeoTIFF")
dst = os.path.join(OUT, "au_sediment.npz")
tif = os.path.join(OUT, "_sed.tif")
with open(tif, "wb") as fh:
    fh.write(get(u))
from PIL import Image                                       # noqa: E402
a = np.array(Image.open(tif), dtype=np.float32)
os.unlink(tif)
a[a < -1e30] = np.nan                                       # WCS nodata
np.savez_compressed(dst, z=a, bbox=np.array(SED_BBOX))
print(f"wrote {dst}: {a.shape} sediment grid, "
      f"{np.isfinite(a).sum()} valid cells")

# --- gravity ----------------------------------------------------------------
import netCDF4                                              # noqa: E402

STRIDE = 10
ds = netCDF4.Dataset(
    "https://thredds.nci.org.au/thredds/dodsC/iv65/"
    "Geoscience_Australia_Geophysics_Reference_Data_Collection/"
    "national_geophysical_compilations/Gravmap2019/"
    "Gravmap2019-grid-grv_cscba.nc")
glat = np.asarray(ds.variables["lat"][::STRIDE])
glon = np.asarray(ds.variables["lon"][::STRIDE])
gz = np.asarray(ds.variables["Band1"][::STRIDE, ::STRIDE], dtype=np.float32)
ds.close()
gz[gz < -9e5] = np.nan                                      # _FillValue
dst = os.path.join(OUT, "au_gravity.npz")
np.savez_compressed(dst, z=gz, lat=glat, lon=glon)
print(f"wrote {dst}: {gz.shape} gravity grid (stride {STRIDE})")

"""Shared base map and georeferencing for the Module 1.1a figures.

Every figure in this directory is drawn on the same Archaean /
Proterozoic / Phanerozoic map of Australia, so they read as one set and
a student can carry a location from one slide to the next.

Base map: "Australia cratons EN.svg" by Woudloper, Wikimedia Commons,
CC BY 4.0 — https://commons.wikimedia.org/wiki/File:Australia_cratons_EN.svg
The rendered PNG is committed, so the figures rebuild with no network.

GEOREFERENCING. The base map is EQUIRECTANGULAR. That was established,
not assumed: a Mercator fit puts every ore deposit about two degrees too
far north and lands Kalgoorlie outside the Yilgarn, while the
equirectangular fit puts each one in the province it is known to occupy.
Longitude is calibrated on the mainland's east-west extremes, the
longest available baseline; latitude uses the same degrees-per-pixel,
anchored on the southernmost mainland point.

Anyone adding a figure here: plot a couple of places whose province you
already know before trusting the transform.
"""
import os

import numpy as np
from PIL import Image

DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(DIR))
IMG = os.path.join(ROOT, "Lectures", "images", "Australia")
BASE = os.path.join(IMG, "australia-cratons-base.png")

# calibration points (mainland extremes)
X_W, LON_W = 370, 113.16      # Steep Point
X_E, LON_E = 3493, 153.63     # Cape Byron
Y_S, LAT_S = 2495, -39.14     # Wilsons Promontory
SX = (X_E - X_W) / (LON_E - LON_W)          # pixels per degree

# the base map's three land classes, sampled from the image
ARCHAEAN = (142, 124, 83)
PROTEROZOIC = (187, 165, 119)
PHANEROZOIC = (215, 195, 160)


def X(lon):
    return X_W + (np.asarray(lon) - LON_W) * SX


def Y(lat):
    return Y_S - (np.asarray(lat) - LAT_S) * SX


def load():
    """(PIL image, RGB array, ocean colour as a 0-1 triple)."""
    im = Image.open(BASE).convert("RGB")
    return im, np.array(im).astype(int), tuple(c / 255
                                               for c in im.getpixel((5, 5)))


def class_mask(arr, rgb, tol=18):
    return np.abs(arr - np.array(rgb)).sum(axis=2) < tol


# The base map's legend sits bottom-left and draws its key using the
# SAME three land colours, so a naive colour test counts the swatches as
# continent. Everything here excludes this rectangle.
LEGEND_BOX = (0, 1100, 2250, 3032)          # x0, x1, y0, y1


def land_mask(arr):
    """Anything the base map draws as continental crust."""
    m = (class_mask(arr, ARCHAEAN) | class_mask(arr, PROTEROZOIC)
         | class_mask(arr, PHANEROZOIC))
    x0, x1, y0, y1 = LEGEND_BOX
    m[y0:y1, x0:x1] = False
    return m


def province_outlines(ax, arr, color="white", lw=1.0, alpha=0.55):
    """Draw the province boundaries as lines.

    A filled field (Moho, and anything else added later) hides the base
    map's colours completely, which defeats the point of using a common
    base. Outlining the Archaean cores and the Precambrian/Phanerozoic
    contact keeps the comparison readable.
    """
    x0, x1, y0, y1 = LEGEND_BOX
    for m in (class_mask(arr, ARCHAEAN),
              class_mask(arr, ARCHAEAN) | class_mask(arr, PROTEROZOIC)):
        f = m.astype(float)
        f[y0:y1, x0:x1] = 0.0
        ax.contour(f, levels=[0.5], colors=color, linewidths=lw,
                   alpha=alpha, zorder=6)


def on_land(arr, lat, lon):
    """Boolean array: does each (lat, lon) fall on mapped land?

    Used to drop the Banda Arc and other off-continent seismicity, which
    would otherwise dominate any Australian catalogue query.
    """
    m = land_mask(arr)
    h, w = m.shape
    xs = np.rint(X(lon)).astype(int)
    ys = np.rint(Y(lat)).astype(int)
    ok = (xs >= 0) & (xs < w) & (ys >= 0) & (ys < h)
    out = np.zeros(len(xs), dtype=bool)
    out[ok] = m[ys[ok], xs[ok]]
    return out


def setup(ax, fig, ocean, im, xlim=(120, 3760), lat_bottom=-45.5):
    ax.set_facecolor(ocean)
    fig.patch.set_facecolor(ocean)
    ax.imshow(im)
    ax.set_xlim(*xlim)
    ax.set_ylim(float(Y(lat_bottom)), 20)
    ax.axis("off")


def credit(ax, extra=""):
    txt = "Base map: Woudloper, Wikimedia Commons, CC BY 4.0"
    if extra:
        txt = extra + "   ·   " + txt
    ax.text(0.985, 0.012, txt, transform=ax.transAxes, fontsize=8.5,
            color="0.85", ha="right")

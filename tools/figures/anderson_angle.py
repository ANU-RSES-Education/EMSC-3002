"""Where Anderson's 60 and 30 degrees come from.

Module 3.1 tells students that normal faults dip at "roughly" 60 deg and
thrusts at "roughly" 30 deg, and leaves it there. The number is not
arbitrary and it is not empirical: it falls out of the Coulomb-Mohr
criterion the lecture has just built, and the thing that sets it is the
angle of internal friction.

Left panel: the construction. A Mohr circle grown until it just touches
the failure envelope. Failure happens at the point of tangency, and the
radius drawn to a tangent point is perpendicular to the envelope -- so
that radius sits at 90 + phi from the sigma-1 direction. Mohr angles are
doubled, so

    2 theta = 90 + phi        theta = 45 + phi/2

with theta the angle from sigma-1 to the fault's NORMAL, which is the
convention this deck uses throughout ("Mohr Circle & the Angle theta").
The fault PLANE therefore sits at 45 - phi/2 from sigma-1. There are two
tangent points, so faults come in conjugate pairs straddling sigma-1
with 90 - phi between them.

Right panels: the same angle in the ground, in Anderson's three regimes.
With phi = 30 deg (mu = tan phi = 0.58, mid-range for rock) the plane is
at 30 deg to sigma-1, and the dips follow from where sigma-1 points.

The point of the slide it serves: the "roughly" in "roughly 60 degrees"
is the spread in mu, not vagueness in the theory.

Everything here is geometry, not measurement -- the construction is the
content. The measured counterpart, an envelope found by rotating a real
Coulomb fault through every orientation, is the "Envelope, Measured"
slide earlier in the same deck.

Run:  pixi run python tools/figures/anderson_angle.py
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "Lectures", "Module-iii-Theory",
                   "anderson-fault-angle.png")

PHI = 30.0                 # angle of internal friction, degrees
COH = 0.30                 # cohesion, in the same arbitrary stress units
SM = 2.00                  # centre of the circle that just fails

ENV_C = "#37474f"          # the failure envelope
CIRC_C = "#1565c0"         # the Mohr circle
FAULT_C = "#c62828"        # the fault planes it predicts
ANG_C = "#1b5e20"          # angles
S1_C = "#4527a0"           # sigma 1

phi = np.radians(PHI)
R = SM * np.sin(phi) + COH * np.cos(phi)      # tangency condition
S1, S3 = SM + R, SM - R
THETA = 45.0 + PHI / 2.0                      # sigma-1 to the fault NORMAL
PLANE = 90.0 - THETA                          # sigma-1 to the fault PLANE
print(f"phi = {PHI}  mu = {np.tan(phi):.3f}   R = {R:.3f}   "
      f"sigma1 = {S1:.3f}  sigma3 = {S3:.3f}")
print(f"theta (to the normal) = {THETA}    plane at {PLANE} deg to sigma 1")
print(f"conjugate planes {2 * PLANE} deg apart, i.e. 90 - phi = {90 - PHI}")


def arc(ax, c, r, a0, a1, **kw):
    t = np.radians(np.linspace(a0, a1, 80))
    ax.plot(c[0] + r * np.cos(t), c[1] + r * np.sin(t), **kw)


# ---------------------------------------------------------------- Mohr
fig = plt.figure(figsize=(13.0, 3.9))
gs = fig.add_gridspec(1, 4, width_ratios=[1.5, 1, 1, 1], wspace=0.22)
ax = fig.add_subplot(gs[0, 0])

x = np.linspace(-0.45, 3.95, 200)
ax.fill_between(x, COH + x * np.tan(phi), 3.2, color="#fdecea", zorder=0)
for sgn in (+1, -1):
    ax.plot(x, sgn * (COH + x * np.tan(phi)), "-", color=ENV_C, lw=2.0,
            zorder=3)
ax.text(0.035, 0.945, r"envelope  $\tau = C + \sigma\tan\phi$",
        fontsize=9.5, color=ENV_C, transform=ax.transAxes)

t = np.linspace(0, 2 * np.pi, 400)
ax.plot(SM + R * np.cos(t), R * np.sin(t), "-", color=CIRC_C, lw=1.8,
        zorder=2)
ax.text(0.035, 0.875, "the circle that just fails", fontsize=9.5,
        color=CIRC_C, transform=ax.transAxes)
ax.axhline(0, color="0.75", lw=0.8, zorder=1)

# the angle of internal friction, where the envelope leaves the axis
xi = -COH / np.tan(phi)
arc(ax, (xi, 0), 0.60, 0, PHI, color=ANG_C, lw=1.4)
ax.text(xi + 0.72, 0.17, r"$\phi$", fontsize=13, color=ANG_C)

# the tangency: the radius to it is perpendicular to the envelope, so it
# lies at 90 + phi from the sigma-1 direction. THIS is the whole slide.
a_t = np.radians(90.0 + PHI)
P = np.array([SM + R * np.cos(a_t), R * np.sin(a_t)])
ax.plot([SM, P[0]], [0, P[1]], "-", color=FAULT_C, lw=1.9, zorder=4)
ax.plot([SM, S1], [0, 0], "-", color=FAULT_C, lw=1.9, zorder=4)
ax.plot([P[0]], [P[1]], "o", ms=10, color=FAULT_C, zorder=5)
arc(ax, (SM, 0), 0.42, 0, 90 + PHI, color=ANG_C, lw=1.7)
ax.text(SM + 0.05, 0.86, r"$2\theta = 90° + \phi$", fontsize=12.5,
        color=ANG_C, ha="left", va="bottom",
        bbox=dict(fc="white", ec="none", alpha=0.9, pad=1.4))

# right angle between the radius and the envelope
u = (P - np.array([SM, 0])) / R
w = np.array([np.cos(phi), np.sin(phi)])
ax.plot(*np.array([P - 0.17 * u, P - 0.17 * u + 0.17 * w,
                   P + 0.17 * w]).T, "-", color="0.35", lw=1.1, zorder=5)

# the second contact, below the axis: this is why faults are conjugate
Q = np.array([SM + R * np.cos(-a_t), R * np.sin(-a_t)])
ax.plot([SM, Q[0]], [0, Q[1]], "-", color=FAULT_C, lw=1.9, zorder=4)
ax.plot([Q[0]], [Q[1]], "o", ms=10, color=FAULT_C, zorder=5)
ax.text(1.24, Q[1] - 0.06, "two contacts:\nconjugate faults",
        fontsize=8.5, color=FAULT_C, ha="right", va="center")

for v, lab in ((S3, r"$\sigma_3$"), (S1, r"$\sigma_1$")):
    ax.plot([v], [0], "|", ms=12, color="0.3", zorder=5)
    ax.text(v, 0.13, lab, fontsize=12, ha="center", color="0.3", zorder=6,
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.6))
ax.set_xlim(-0.55, 4.05)
ax.set_ylim(-1.45, 1.95)
ax.set_xlabel(r"normal stress $\sigma$ (compression positive)", fontsize=9.5)
ax.set_ylabel(r"shear stress $\tau$", fontsize=9.5)
ax.tick_params(labelsize=8.5)
ax.set_title("Failure where the circle touches the envelope", fontsize=10.5)
ax.set_aspect("equal")


# ------------------------------------------------- the three regimes
def regime(ax, s1_vertical, dip, title, sub, mapview=False):
    ax.add_patch(plt.Rectangle((-1, -1), 2, 2, fc="#f5f2ec", ec="none"))
    for sgn in (+1, -1):                       # the conjugate pair, equals
        d = np.array([np.cos(np.radians(sgn * dip)),
                      np.sin(np.radians(sgn * dip))])
        ax.plot([-1.05 * d[0], 1.05 * d[0]], [-1.05 * d[1], 1.05 * d[1]],
                "-", color=FAULT_C, lw=2.4, zorder=2)
    if not mapview:                            # faults stop at the ground
        ax.add_patch(plt.Rectangle((-1.06, 0.72), 2.12, 0.45, fc="white",
                                   ec="none", zorder=3))
        ax.plot([-1, 1], [0.72, 0.72], "-", color="#6d4c41", lw=2.2,
                zorder=4)
        ax.text(0.97, 0.79, "surface", fontsize=7.5, color="#6d4c41",
                ha="right", zorder=4)

    v = np.array([0.0, 1.0]) if s1_vertical else np.array([1.0, 0.0])
    h = np.array([1.0, 0.0]) if s1_vertical else np.array([0.0, 1.0])
    for d, col, lw, lab in ((v, S1_C, 2.6, r"$\sigma_1$"),
                            (h, "0.5", 1.6, r"$\sigma_3$")):
        for sgn in (+1, -1):
            ax.annotate("", xytext=sgn * 0.98 * d, xy=sgn * 0.58 * d,
                        arrowprops=dict(arrowstyle="-|>", lw=lw, color=col),
                        zorder=5)
        p = 0.44 * d + 0.34 * np.array([-d[1], d[0]])
        ax.text(p[0], p[1], lab, fontsize=11, color=col, ha="center",
                va="center", zorder=6,
                bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.8))

    ax.text(0, -0.90, sub, fontsize=9.5, color=FAULT_C, ha="center",
            va="center", zorder=6,
            bbox=dict(fc="white", ec="none", alpha=0.92, pad=1.8))
    ax.set_xlim(-1.06, 1.06)
    ax.set_ylim(-1.06, 1.06)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=10.5)


DIP_N = 90.0 - PLANE          # sigma 1 vertical -> plane 30 deg off it
DIP_T = PLANE                 # sigma 1 horizontal -> plane 30 deg off it
regime(fig.add_subplot(gs[0, 1]), True, DIP_N, "Normal", f"dip {DIP_N:.0f}°")
regime(fig.add_subplot(gs[0, 2]), False, DIP_T, "Thrust / reverse",
       f"dip {DIP_T:.0f}°")
regime(fig.add_subplot(gs[0, 3]), False, DIP_T, "Strike-slip  (map view)",
       f"vertical, striking {DIP_T:.0f}°" + "\n" + r"($\sigma_2$ is vertical)",
       mapview=True)

fig.suptitle(r"The fault plane forms at $45° - \phi/2$ from $\sigma_1$, "
             r"which is $30°$ when $\phi = 30°$  ($\mu = \tan\phi = 0.58$)",
             fontsize=12.5)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig(os.path.normpath(OUT), dpi=190, bbox_inches="tight")
print("wrote", os.path.normpath(OUT))

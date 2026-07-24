# Slides moved out of Module 1.3 → to merge into Module 3

Removed from `Lectures/Module-i-GlobalTectonics-3.reveal.md` in the 2026 trim
(1.3 = concepts + geometry + simple numbers; Module 3 = derivations).
Each block below is verbatim deck markdown with its **destination anchor** in the
Module 3 draft decks. Louis's figures/voice should be *merged into* the existing
Module 3 treatment, not appended as duplicates.

---

## → iii-1 (Stress), anchor: "Stress on a Plane via Stress Tensor"

### The Stress Tensor (traction vector)

If we cut out a plane through a material that is under stress, then there is a **traction vector** (a force) on this plane that results from the unbalanced stresses and *the vector changes with the orientation of the plane*. 

![](images/GlobalTectonics/TractionsOnAPlane.png)  <!-- .element style="float:right;width:49%%" -->

In fact, this is enough to define the stress tensor.

$$ T_i = \sum_{j} \sigma_{ij} \times n_j = \boldsymbol{\sigma} \cdot \mathbf{n} $$

where $\left\\{ n \right\\}$ is the vector normal to the plane.

Here is a way to think about it: *In general, the force that we need to balance in a void in the ground will be in a different direction for the roof from the walls*

Pressures are stresses (forces acting per area of a surface) and so stresses have the same units: $\textrm{Pa} \equiv N / m^2 $

---

## → iii-1 (Stress), anchor: "Stress State in 3D" / "Deviatoric Stress and Mean Stress"

### The Stress Tensor (matrix, symmetry, deviatoric/volumetric)

The complexity we have seen reflects the fact that **stress is a tensor quantity**. 

$$ \mathbf{\sigma} = 
\begin{bmatrix}
\sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\\\
\sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\\\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz} 
\end{bmatrix} $$

The stress tensor is **symmetric**. i.e. $\sigma_{xy} = \sigma_{yx}$ 

It has a **volumetric** component (pressure) that is independent of the orientation and a **deviatoric** component (the shear stresses) that is not.

We can rotate the coordinates (equivalent to adjusting our point of view) and in one specific orientation, the shear stresses all vanish. This coordinate system defines the principal stresses.

---

## → iii-2 (Strain), anchor: "Strain Tensor"

### Strain tensor components (from "What is Strain?" + "Strain Tensor")

In three dimensions, like stress, strain is a tensor:

$$ 
\mathbf{\varepsilon} = 
\begin{bmatrix}
\varepsilon_{xx} & \varepsilon_{xy} & \varepsilon_{xz} \\\\
\varepsilon_{yx} & \varepsilon_{yy} & \varepsilon_{yz} \\\\
\varepsilon_{zx} & \varepsilon_{zy} & \varepsilon_{zz} 
\end{bmatrix} 
$$

The strain tensor contains volumetric strains, shear strains and normal strains. The shear and normal strains are the the **deviatoric** parts of the tensor. These are analogous to the shear stresses and normal stresses of the deviatoric stress tensor.

The components of the strain tensor are usually expressed this way:

$$
\varepsilon_{ij}  = \frac{1}{2} \left[ \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}  \right]
$$

Where $u_i$ is the displacement in the direction $i$. $i,j$ can be any of $\{1,2,3\}$ and the coordinates $\{x,y,z\}$ are then referred to as $\{x_1, x_2, x_3\}$ (etc).

A typical component might be written

$$
\varepsilon_{xy}  \equiv \varepsilon_{12} = \frac{1}{2} \left[ \frac{\partial u_1}{\partial x_2} + \frac{\partial u_2}{\partial x_1}  \right]  
$$

### Symmetry of the Strain Tensor

From the definition given, it is clear that $\varepsilon_{xy} \equiv \varepsilon_{yx}$.

The strain tensor is the **symmetric part** of the more general deformation tensor and this 
removes all components of the deformation that are associated with pure **rotation**.

Rotations are equivalent to changes in the point of view of the observer and we know that the forces and responses cannot depend on the coordinate system itself. 

This principle is known as **objectivity** - our systems of equations cannot include translations and rotation of the coordinate system.

*It is possible to have equations that are sensitive to rotation but these also need additional conservation equations, physical moduli and forces*

### Volumetric Strain and Incompressibility

The volumetric strain (or dilatation) on a material is given by

$$
\delta = \frac{\Delta V}{V_0} = \sum_{i} \varepsilon_{ii}
$$

In an incompressible material (an idealised situation, not unlike the notion of a rigid plate), the volumetric strain is always zero (identically zero).

Engineers often have a sign convention that differs from the everyday one. Here, increasing volume is 
considered positive (so an increasing pressure should produce a negative volumetric strain)

### Invariants of the (Strain) Tensor

Tensors have a number of *invariants*, properties that do not change with the coordinate system.

We have met one example already:

$$
\delta = \frac{\Delta V}{V_0} = \sum_{i} \varepsilon_{ii} = \sum_{k} \epsilon_k
$$

where $\epsilon_k$ represents the principal strains which are unique for the tensor no matter what coordinate system it is expressed in. This is known as the **first invariant** of the tensor, often $I_{\varepsilon}$

The **second invariant**, $II_{\varepsilon}$ is defined as

$$
II_{\varepsilon} = \frac{1}{2} \left( \epsilon_1 \epsilon_2 + \epsilon_2 \epsilon_3 + \epsilon_1 \epsilon_3 \right)
$$

This plays the role of the magnitude of the deviatoric part of the tensor and that is why it is used
when we plot the world strain rate map. 

---

## → iii-2 (Strain), anchor: "Strain Rate Tensor"

### Strain-rate tensor (formal part of "What is Strain-Rate?")

The strain rate tensor is sometimes written as $\dot\varepsilon$, but we will refer to $\mathbf{D}$  

$$ 
\mathbf{D} = 
\begin{bmatrix}
D_{xx} & D_{xy} & D_{xz} \\\\
D_{yx} & D_{yy} & D_{yz} \\\\
D_{zx} & D_{zy} & D_{zz} 
\end{bmatrix} \quad \textrm{or} \quad D_{ij} = \frac{1}{2} \left[ \frac{\partial v_i}{\partial x_j} + \frac{\partial v_j}{\partial x_i}  \right]
$$

Here we have replaced the displacement vector in the strain, $\mathbf{u}$ with the velocity vector, $\mathbf{v}$ and all other remarks we made about the strain still hold.

The strain rate is a symmetric tensor and there are principal strain rates all shear values vanish. The diagonal sums to zero if the material is incompressible (a.k.a zero trace, first invariant is zero). The second invariant is defined from the principal values and represents the magnitude. 

**NB:** the definition of $\partial \boldsymbol{\varepsilon} / \partial t$ is ambiguous because, in some derivations, we don't just differentiate the displacement to get a velocity, we also account for the distortion of the original coordinate system during deformation. That's why we start with velocity gradients etc. 

### Advanced: Velocity Gradient, Vorticity

The strain rate is the symmetric part of a more general **velocity gradient tensor** which can be written $\nabla \mathbf{v}$ (the *gradient of a vector* and not to be confused with $\nabla \cdot \mathbf{v}$, the divergence).

$$
L_{ij} \equiv \left( \nabla\mathbf{v}\right)^T = \partial v_i / \partial x_j  \quad \\{i,j\\}:\\{1,2,3\\}
$$

Which means you may see the strain rate written like this:

$$
\mathbf{D} = 
\frac{1}{2}\left(\nabla \mathbf{v} + \left( \nabla \mathbf{v} \right)^T \right) \equiv
\frac{1}{2}\left(\mathbf{L} + \mathbf{L}^T \right) \quad \textrm{and} \quad \mathbf{W} 
= \frac{1}{2} \left(\mathbf{L} - \mathbf{L}^T\right)
$$ 

Here $\mathbf{W}$ is the spin tensor. It is related to the better known **vorticity** vector, $\omega$ through 

$$
 \omega_i = -\epsilon_{ijk} W_{kj} = 2\Omega
$$

$\Omega$ is the angular velocity at each point in the fluid. Hence the names "spin" and "vorticity".

<small>

The wikipedia article is quite good: https://en.wikipedia.org/wiki/Strain-rate_tensor

Smith, A. C., & Kaloni, P. N. (1996). A note on spin, vorticity and the deformation-rate tensor. Journal of Non-Newtonian Fluid Mechanics, 62(1), 95–98. https://doi.org/10/dfxhjj

</small>

---

## → iii-2 (Strain), anchor: "Strain Rates at Plate Boundaries"

### Kostrov Summation links seismicity / strain

There is a connection between the seismic moment tensor and the strain rate tensor which is attributed to Kostrov (1974).

![](images/GlobalTectonics/Jackson_McKenzie_Kostrov_Fig.png) <!-- .element style="width:30%;float:right; margin-left:30px;" -->

The moment tensor can be interpreted as:

$$ M^n_{ij} = M^n_0 \left(u_i n_j + u_j n_i \right) $$

where $\mathbf{\hat{u}}$ and $\mathbf{\hat{n}}$ are unit vectors describing the slip direction and the normal to the slip plane respectively (see diagram)

$$
\left< \varepsilon \right>_{ij} = \frac{1}{2 \mu V} \sum_n M^n _{ij} \quad \textrm{or} \quad 
\left< D \right> _{ij} = \frac{1}{2 \mu V \tau} \sum_n M^n _{ij}
$$

Here, $\tau$ is a time over which we are summing the moment tensor to create a time-average. $\left< . \right>$ denotes an average over the volume, $V$.

<small>

Jackson, J., & McKenzie, D. (1988). The relationship between plate motions and seismic moment tensors, and the rates of active deformation in the Mediterranean and Middle East. Geophysical Journal International, 93(1), 45–73. https://doi.org/10/fp7rkq

Kostrov, V.V., 1974. Seismic moment and energy of earthquakes, and seismic flow of rock. Izv. Acad. Sci. USSR Phys. Solid Earth, 1, 23–44.

</small>

---

## → iii-3 (Rheology), anchor: "Elastic Tensor" / "Elastic Deformation in 3D"

### Constitutive tensor (from "Rheology" overview)

$$
    \sigma_{ij} = C_{ijkl} \varepsilon_{kl}
$$

The coefficients should be (rank 4) tensors 
because there is no particular reason to expect all the stress and strain directions to respond the same way. But symmetry is helpful and usually we work with simplifications. 

### Rheology: Elasticity (3D response)

![](images/GlobalTectonics/ElasticStretching.svg) <!-- .element style="width:40%;float:right" -->

$$
\sigma_{ij} = \color{Black}{2\mu D_{ij}} + \color{Black}{\lambda \delta_{ij} D_{kk}}
$$

If we apply a single normal stress component, it is clear that there must still be a response in all three dimensions (two in the sketch), especially if the material is incompressible, or very nearly so.

(Also the general form from the first elasticity slide:
$\sigma_{ij} = \color{Blue}{2\mu \varepsilon_{ij}} + \color{Red}{\lambda \delta_{ij} \varepsilon_{kk}}$
where the Red term is volumetric.)

---

## → iii-3 (Rheology), anchor: "Viscous Deformation" (Newtonian vs power-law)

### Rheology: Viscosity (power-law / thixotropy)

![](images/GlobalTectonics/Rheology-ViscousBehaviour.svg) <!-- .element style="width:35%;float:right;margin-left:40px;" -->

The idealised, linear relationship between the shear stress ($\tau$) and the deviatoric strain rate, is attributed to Newton but many fluids start to lose their ability to resist at high stress. These are known
as thixotropic materials. 

Rocks can be viscous without being liquid: they deform by migration of defects (dislocations, point defects, grain boundaries) which is often known as crystal plasticity. The changes are permanent and dissipate rather than store energy. 

Many forms of crystal plasticity weaken at high stresses and this can typically be expressed as a power law. 

$$
  \eta = K \left( II_D \right) ^{n-1}
$$

### Plasticity as an effective viscosity (from "Rheology: Plasticity")

$$ 
\eta = \frac{\tau_Y}{II_D}
$$

---

## → iii-3 (Rheology), anchor: "Rheology of the Lithosphere"

### Rock Deformation Map (standalone version)

![DefMap](images/GlobalTectonics/Gomez-Rivas-DeformationMap.jpg) <!-- .element style="display:block; margin-left:auto; margin-right:auto; width:50%" -->

Rock deformation map that shows how temperature and the magnitude of the differential stress (shear stress compared to confining pressure) influence how rocks deform.

<small>

Gomez-Rivas, E., Butler, R. W. H., Healy, D., & Alsop, I. (2020). From hot to cold - The temperature dependence on rock deformation processes: An introduction. Journal of Structural Geology, 132, 103977. https://doi.org/10/gk6kn4

</small>

### The Brittle-Ductile Transition (Byerlee 1968)

The classic work on the deformation of crustal rocks is Byerlee's paper of 1968. *"... at low confining pressure, many rocks are brittle. That is, when differential stress is sufficiently high, a fault is formed and, after faulting, the compressive stress is decreased. At high confining pressure, the same rocks may be ductile."* 

![Byerlee1968](images/GlobalTectonics/Byerlee1968.svg) <!-- .element style="width:66%" -->

<small>

Byerlee, J. D. (1968). Brittle-ductile transition in rocks. Journal of Geophysical Research, 73(14), 4741–4750. https://doi.org/10/dtqwmx

</small>

---

**NB on figures:** the referenced images live in `Lectures/images/GlobalTectonics/`.
When merging into Module 3, either copy the figures into the Module 3 image dirs or
reference them in place (the slide build serves `images/` at the same level).

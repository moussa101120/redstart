import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4], 
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )    
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    Un équilibre correspond à une situation où le booster ne bouge pas et où son état ne change plus avec le temps.
    L'état du booster est
    \[
    s = (x, v_x, y, v_y, \theta, \omega)
    \]
    avec
    \[
    v_x = \dot{x}, \qquad v_y = \dot{y}, \qquad \omega = \dot{\theta}.
    \]
    À l'équilibre, toutes les dérivées sont nulles. Donc :
    \[
    v_x = 0, \qquad v_y = 0, \qquad \omega = 0,
    \]
    mais aussi
    \[
    \ddot{x} = 0, \qquad \ddot{y} = 0, \qquad \ddot{\theta} = 0.
    \]

    D'après les équations du modèle,
    \[
    \ddot{x} = -\frac{f}{M}\sin(\theta+\phi),
    \]
    \[
    \ddot{y} = \frac{f}{M}\cos(\theta+\phi)-g,
    \]

    et
    \[
    \ddot{\theta} = -\frac{f}{J}\frac{\ell}{2}\sin(\phi).
    \]
    Comme on suppose que \(f>0\), la condition \(\ddot{\theta}=0\) impose
    \[
    \sin(\phi)=0.
    \]
    Or on suppose aussi que
    \[
    |\phi| < \frac{\pi}{2}.
    \]
    Donc :
    \[
    \phi = 0.
    \]
    Ensuite, la condition \(\ddot{x}=0\) donne
    \[
    \sin(\theta+\phi)=0.
    \]
    Comme \(\phi=0\), on obtient
    \[
    \sin(\theta)=0.
    \]
    Et comme
    \[
    |\theta| < \frac{\pi}{2},
    \]
    on obtient
    \[
    \theta = 0.
    \]
    Enfin, la condition \(\ddot{y}=0\) donne
    \[
    \frac{f}{M}\cos(0)-g = 0.
    \]
    Donc
    \[
    \frac{f}{M}=g,
    \]
    c-à-d
    \[
    f = Mg.
    \]
    Ainsi, les équilibres possibles sont les états de la forme
    \[
    s_{\text{eq}} = (x_{\text{eq}}, 0, y_{\text{eq}}, 0, 0, 0),
    \]
    avec les entrées constantes
    \[
    f_{\text{eq}} = Mg,
    \qquad
    \phi_{\text{eq}} = 0.
    \]

    Conclusion : le booster est vertical, immobile, sans rotation, et la poussée du moteur compense exactement son poids. Les positions \(x_{\text{eq}}\) et \(y_{\text{eq}}\) peuvent être quelconques dans ce modèle, car on cherche seulement un équilibre dynamique.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    On se place autour de l'équilibre trouvé juste avant. À l'équilibre, le booster est vertical, immobile, et la poussée compense exactement le poids :

    \[
    \theta_{\text{eq}} = 0,
    \qquad
    \phi_{\text{eq}} = 0,
    \qquad
    f_{\text{eq}} = Mg.
    \]
    Comme on vient d'indiquer , les positions \(x_{\text{eq}}\) et \(y_{\text{eq}}\) peuvent être quelconques, car ce qui compte ici est surtout le mouvement autour de cette position.
    On introduit donc les variables d'erreur :
    \[
    \Delta x = x - x_{\text{eq}},
    \qquad
    \Delta y = y - y_{\text{eq}},
    \qquad
    \Delta \theta = \theta - 0 = \theta,
    \]
    et aussi pour les vitesses :
    \[
    \Delta v_x = v_x,
    \qquad
    \Delta v_y = v_y,
    \qquad
    \Delta \omega = \omega.
    \]
    Pour les commandes, on écrit :\[
    \Delta f = f - Mg,
    \qquad
    \Delta \phi = \phi.
    \]
    L'idée de la linéarisation est de dire que près de l'équilibre, les angles sont petits. On peut donc utiliser les approximations :
    \[
    \sin(\Delta \theta + \Delta \phi) \approx \Delta \theta + \Delta \phi,
    \]
    \[
    \cos(\Delta \theta + \Delta \phi) \approx 1,
    \]
    \[
    \sin(\Delta \phi) \approx \Delta \phi.
    \]
    On part des équations non linéaires :
    \[
    \ddot{x} = -\frac{f}{M}\sin(\theta+\phi),
    \]
    \[
    \ddot{y} = \frac{f}{M}\cos(\theta+\phi)-g,
    \]
    \[
    \ddot{\theta} =
    -\frac{f}{J}\frac{\ell}{2}\sin(\phi).
    \]
    Comme \(f = Mg + \Delta f\), on obtient au premier ordre :
    \[
    \Delta \ddot{x}
    \approx
    -g\Delta \theta - g\Delta \phi.
    \]
    Pour la verticale :
    \[
    \Delta \ddot{y}
    \approx
    \frac{\Delta f}{M}.
    \]
    Pour la rotation :
    \[
    \Delta \ddot{\theta}
    \approx
    -\frac{Mg}{J}\frac{\ell}{2}\Delta \phi.
    \]
    Donc le modèle linéarisé est :
    \[
    \Delta \dot{x} = \Delta v_x,
    \]
    \[
    \Delta \dot{v}_x = -g\Delta \theta - g\Delta \phi,
    \]
    \[
    \Delta \dot{y} = \Delta v_y,
    \]
    \[
    \Delta \dot{v}_y = \frac{\Delta f}{M},
    \]
    \[
    \Delta \dot{\theta} = \Delta \omega,
    \]
    \[
    \Delta \dot{\omega}
    =
    -\frac{Mg\ell}{2J}\Delta \phi.
    \]
    Avec les valeurs : \(M=1\), \(g=1\), \(\ell=2\), et \(J=1/3\), on a :
    \[
    \frac{Mg\ell}{2J} = 3.
    \]
    Donc ici :
    \[
    \Delta \dot{\omega} = -3\Delta \phi.
    \]
    Physiquement, ça veut dire que \(\Delta f\) sert surtout à contrôler le mouvement vertical, alors que \(\Delta \phi\) agit sur la rotation du booster, et donc indirectement sur le mouvement horizontal.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    rotation_gain = M * g * l / (2 * J)

    def linearized_model(delta_state, delta_input):
        """
        delta_state = [Delta x, Delta vx, Delta y, Delta vy, Delta theta, Delta omega]
        delta_input = [Delta f, Delta phi]
        """
        delta_x, delta_vx, delta_y, delta_vy, delta_theta, delta_omega = delta_state
        delta_f, delta_phi = delta_input

        d_delta_x = delta_vx
        d_delta_vx = -g * delta_theta - g * delta_phi

        d_delta_y = delta_vy
        d_delta_vy = delta_f / M

        d_delta_theta = delta_omega
        d_delta_omega = -rotation_gain * delta_phi

        return np.array([
            d_delta_x,
            d_delta_vx,
            d_delta_y,
            d_delta_vy,
            d_delta_theta,
            d_delta_omega,
        ])

    print(rotation_gain)
    return (rotation_gain,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse 1.
    On écrit le modèle linéarisé sous la forme standard :
    \[
    \Delta \dot{s} = A\Delta s + B\Delta u.
    \]
    On prend comme état :
    \[
    \Delta s =
    (\Delta x,\Delta v_x,\Delta y,\Delta v_y,\Delta \theta,\Delta \omega)
    \]
    et comme commande :
    \[
    \Delta u = (\Delta f,\Delta \phi).
    \]
    D'après le modèle linéarisé :
    \[
    \Delta \dot{x} = \Delta v_x,
    \qquad
    \Delta \dot{v}_x = -g\Delta\theta - g\Delta\phi,
    \]
    \[
    \Delta \dot{y} = \Delta v_y,
    \qquad
    \Delta \dot{v}_y = \frac{\Delta f}{M},
    \]
    \[
    \Delta \dot{\theta} = \Delta\omega,
    \qquad
    \Delta \dot{\omega} = -\frac{Mg\ell}{2J}\Delta\phi.
    \]
    Donc la matrice \(A\) regroupe les termes qui dépendent de l'état, et la matrice \(B\) regroupe les termes qui dépendent des commandes.
    Avec \(g=1\), \(M=1\), \(\ell=2\), et \(J=1/3\), on a :
    \[
    \frac{Mg\ell}{2J}=3.
    \]
    """)
    return


@app.cell
def _(M, g, np, rotation_gain):
    A = np.array([
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, -g, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
    ], dtype=float)

    B = np.array([
        [0, 0],
        [0, -g],
        [0, 0],
        [1 / M, 0],
        [0, 0],
        [0, -rotation_gain],
    ], dtype=float)
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell
def _(A, np):
    eigenvalues_A = np.linalg.eigvals(A)

    is_asymptotically_stable = np.all(np.real(eigenvalues_A) < 0)

    print("Eigenvalues of A:")
    print(eigenvalues_A)

    print("Asymptotiquement stable ??", is_asymptotically_stable)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Conclusion

    Les valeurs propres de \(A\) sont nulles. Elles ne sont donc pas strictement négatives.
    L'équilibre n'est donc pas asymptotiquement stable : si le booster est perturbé, le modèle ne le ramène pas naturellement vers l'équilibre. Il faut ajouter un contrôleur.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour vérifier si le système linéarisé est contrôlable, on utilise la matrice de contrôlabilité :

    \[
    \mathcal{C} =
    \begin{bmatrix}
    B & AB & A^2B & \cdots & A^{n-1}B
    \end{bmatrix}.
    \]

    Ici, l'état est de dimension \(n=6\).
    Le système est contrôlable si le rang de \(\mathcal{C}\) vaut 6.

    Physiquement, \(\Delta f\) agit sur le mouvement vertical \(y\), tandis que \(\Delta \phi\) agit sur la rotation \(\theta\) et donc aussi sur le déplacement horizontal \(x\).
    c/c : Donc on s'attend à ce que le système complet soit contrôlable.
    """)
    return


@app.cell
def _(A, B, np):
    n = A.shape[0]

    controllability_matrix = B
    for k in range(1, n):
        controllability_matrix = np.hstack(
            [controllability_matrix, np.linalg.matrix_power(A, k) @ B]
        )

    controllability_rank = np.linalg.matrix_rank(controllability_matrix)
    is_controllable = controllability_rank == n

    print("Rang de la Matrice controllability : ", controllability_rank)
    print("dimension d'état:", n)
    print("Controllable?", is_controllable)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Conclusion:
    Le rang de la matrice de contrôlabilité est égal à la dimension de l'état, donc le modèle linéarisé complet est contrôlable.

    Cela signifie qu'avec les deux commandes \(\Delta f\) et \(\Delta \phi\), on peut agir sur toutes les variables du modèle linéarisé.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse
    On garde seulement les variables liées au mouvement latéral :
    \[
    z =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}\]
    On fixe la poussée à sa valeur d'équilibre :
    \[
    f = Mg\]
    et on contrôle seulement avec l'angle du moteur :
    \[
    u = \Delta \phi.\]
    Le modèle réduit devient :
    \[
    \Delta \dot{x} = \Delta \dot{x},
    \]
    \[
    \Delta \ddot{x} = -g\Delta\theta - g\Delta\phi,
    \]
    \[
    \Delta \dot{\theta} = \Delta \dot{\theta},\]
    \[
    \Delta \ddot{\theta}
    =
    -\frac{Mg\ell}{2J}\Delta\phi.
    \]
    Avec \(g=1\), \(M=1\), \(\ell=2\), et \(J=1/3\), on a :
    \[
    \frac{Mg\ell}{2J}=3.\]
    Donc \(\Delta \phi\) permet d'agir sur la rotation du booster, et aussi sur son déplacement horizontal. On vérifie ensuite la contrôlabilité avec la matrice de contrôlabilité.
    """)
    return


@app.cell
def _(g, np, rotation_gain):
    A_lat = np.array([
        [0, 1, 0, 0],
        [0, 0, -g, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ], dtype=float)

    B_lat = np.array([
        [0],
        [-g],
        [0],
        [-rotation_gain],
    ], dtype=float)

    n_lat = A_lat.shape[0]

    controllability_matrix_lat = B_lat
    for i in range(1, n_lat):
        controllability_matrix_lat = np.hstack(
            [controllability_matrix_lat, np.linalg.matrix_power(A_lat, i) @ B_lat]
        )

    rank_lat = np.linalg.matrix_rank(controllability_matrix_lat)
    is_controllable_lat = rank_lat == n_lat

    print("A_lat =")
    print(A_lat)

    print("B_lat =")
    print(B_lat)

    print("Rank of controllability matrix:", rank_lat)
    print("State dimension:", n_lat)
    print("Controllable?", is_controllable_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On utilise le modèle linéarisé latéral :

    \[
    z =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \]

    avec la condition initiale :

    \[
    \Delta x(0)=0,\quad
    \Delta \dot{x}(0)=0,\quad
    \Delta \theta(0)=\frac{\pi}{4},\quad
    \Delta \dot{\theta}(0)=0.
    \]

    On impose aussi :

    \[
    \Delta \phi(t)=0.
    \]

    Donc il n'y a pas de correction avec le moteur.

    Comme \(\Delta \phi=0\), l'équation de rotation donne :

    \[
    \Delta \ddot{\theta}=0.
    \]

    Donc l'angle reste constant :

    \[
    \Delta \theta(t)=\frac{\pi}{4}.
    \]

    Mais comme le booster reste incliné, il crée une accélération horizontale :

    \[
    \Delta \ddot{x} = -g\Delta \theta.
    \]

    Donc \(x(t)\) dérive de plus en plus vers un côté.
    On doit donc voir que \(\theta(t)\) reste constant, tandis que \(x(t)\) part de façon parabolique.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy):
    def linear_free_fall_example():
        t_span = [0.0, 5.0]

        # z = [Delta x, Delta vx, Delta theta, Delta omega]
        z0 = np.array([0.0, 0.0, np.pi / 4, 0.0])

        def phi(t):
            return 0.0

        def rhs(t, z):
            u = np.array([phi(t)])
            return A_lat @ z + B_lat @ u

        sol = scipy.integrate.solve_ivp(
         rhs,t_span,z0, dense_output=True,
        )

        t = np.linspace(t_span[0], t_span[1], 1000)
        z_t = sol.sol(t)

        x_t = z_t[0]
        theta_t = z_t[2]

        plt.figure()
        plt.plot(t, x_t, label=r"$\Delta x(t)$")
        plt.title("Linear model: lateral position")
        plt.xlabel("time $t$")
        plt.ylabel(r"$\Delta x(t)$")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(t, theta_t, label=r"$\Delta \theta(t)$")
        plt.axhline(np.pi / 4, color="grey", linestyle="--", label=r"$\pi/4$")
        plt.title("Linear model: tilt angle")
        plt.xlabel("time $t$")
        plt.ylabel(r"$\Delta \theta(t)$")
        plt.grid(True)
        plt.legend()
        plt.show()

    linear_free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Observation

    Sur le graphe de \(\Delta \theta(t)\), on voit que l'angle reste constant à sa valeur initiale :

    \[
    \Delta \theta(t) = \frac{\pi}{4}.
    \]

    C'est logique, car on impose \(\Delta \phi(t)=0\). Donc le moteur ne crée pas de couple pour corriger l'inclinaison, et on a \[\Delta \ddot{\theta}=0.\]

    Comme la vitesse angulaire initiale est aussi nulle, l'angle ne change pas.
    Par contre, sur le graphe de \(\Delta x(t)\), on voit que la position horizontale dérive de plus en plus. Cela vient du fait que le booster reste incliné. Dans le modèle linéarisé :
    \[
    \Delta \ddot{x} = -g\Delta \theta.
    \]
    Comme \(\Delta \theta = \pi/4\), l'accélération horizontale est constante et non nulle. Donc \(\Delta x(t)\) évolue comme une parabole.
    Conclusion : sans correction avec \(\phi\), le booster ne se redresse pas et il part horizontalement.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###réponse
    On utilise le modèle latéral :
    \[
    z =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \]
    et la commande :\[
    \Delta \phi(t) = -Kz(t).
    \]
    Dans cette question, on impose :\[
    K = [0,\ 0,\ k_\theta,\ k_\omega].
    \]
    Donc on ne contrôle pas directement la position horizontale \(x\). On essaie seulement de corriger l'angle du booster.
    L'idée est simple : si le booster est incliné, on choisit \(\phi\) pour créer un moment qui le ramène vers la verticale. On ajoute aussi un terme avec \(\dot{\theta}\) pour freiner la rotation.

    Comme l'équation linéarisée de rotation est :\[
    \Delta \ddot{\theta} = -3 \Delta \phi,
    \]
    et que\[
    \Delta \phi = -k_\theta \Delta \theta - k_\omega \Delta \dot{\theta},
    \]
    on obtient :
    \[
    \Delta \ddot{\theta}
    =
    3 k_\theta \Delta \theta + 3 k_\omega \Delta \dot{\theta}.
    \]
    Pour stabiliser l'angle, il faut donc choisir \(k_\theta < 0\) et \(k_\omega < 0\).
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy):
    def simulate_manual_controller(K, T=20.0):
        K = np.array(K, dtype=float).reshape(1, 4)
        z0 = np.array([0.0, 0.0, np.pi / 4, 0.0])

        def rhs(t, z):
            phi = float(-(K @ z)[0])
            return A_lat @ z + B_lat[:, 0] * phi

        sol = scipy.integrate.solve_ivp(
            rhs,
            [0.0, T],
            z0,
            dense_output=True,
        )

        t = np.linspace(0.0, T, 1000)
        z_t = sol.sol(t)

        phi_t = np.array([
            float(-(K @ z_t[:, i])[0])
            for i in range(z_t.shape[1])
        ])

        eigenvalues = np.linalg.eigvals(A_lat - B_lat @ K)

        return t, z_t, phi_t, eigenvalues


    # Essais 
    guesses = {
        "essai 1: doux": [0.0, 0.0, -0.020, -0.120],
        "essai 2: retenu": [0.0, 0.0, -0.060, -0.300],
        "essai 3: plus nerveux": [0.0, 0.0, -0.150, -0.700],
    }

    plt.figure()
    for label, K in guesses.items():
        t, z_t, phi_t, eigs = simulate_manual_controller(K)
        theta_t = z_t[2]
        plt.plot(t, theta_t, label=label)

    plt.axhline(np.pi / 2, color="grey", linestyle="--", label=r"$\pi/2$")
    plt.axhline(-np.pi / 2, color="grey", linestyle="--", label=r"$-\pi/2$")
    plt.xlabel("time t")
    plt.ylabel(r"$\Delta \theta(t)$")
    plt.title("Manual tuning: angle response")
    plt.grid(True)
    plt.legend()
    plt.show()


    # Choix final
    K_manual = np.array([[0.0, 0.0, -0.060, -0.300]])

    t, z_t, phi_t, eigs_manual = simulate_manual_controller(K_manual)


    plt.figure()
    plt.plot(t, phi_t, label=r"$\Delta \phi(t)$")
    plt.axhline(np.pi / 2, color="grey", linestyle="--", label=r"$\pi/2$")
    plt.axhline(-np.pi / 2, color="grey", linestyle="--", label=r"$-\pi/2$")
    plt.xlabel("time t")
    plt.ylabel(r"$\Delta \phi(t)$")
    plt.title("Manual controller: command")
    plt.grid(True)
    plt.legend()
    plt.show()


    plt.figure()
    plt.plot(t, z_t[0], label=r"$\Delta x(t)$")
    plt.xlabel("time t")
    plt.ylabel(r"$\Delta x(t)$")
    plt.title("Manual controller: horizontal drift")
    plt.grid(True)
    plt.legend()
    plt.show()

    print("Final K_manual =", K_manual)
    print("Max |theta| =", np.max(np.abs(z_t[2])))
    print("Max |phi| =", np.max(np.abs(phi_t)))
    print("Closed-loop eigenvalues =", eigs_manual)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Observation

    Avec le premier essai, l'angle revient vers 0 mais assez lentement.
    Avec le troisième essai, la correction est plus forte.
    J'ai gardé l'essai intermédiaire :
    \[
    K = [0, 0, -0.060, -0.300].
    \]
    Avec ce choix, \(\Delta \theta(t)\) revient vers 0 en moins de 20 secondes, et la commande \(\Delta \phi(t)\) reste largement dans l'intervalle autorisé :
    \[
    |\Delta \phi(t)| < \frac{\pi}{2}.
    \]
    Par contre, comme les deux premiers coefficients de \(K\) sont nuls, le contrôleur ne corrige pas directement la position horizontale. Donc \(x(t)\) peut dériver.
    La dynamique en boucle fermée n'est donc pas asymptotiquement stable pour tout l'état latéral, car la partie \(x\) n'est pas stabilisée. Mais pour l'objectif demandé ici, c'est acceptable, car on voulait surtout ramener l'angle \(\theta\) vers 0.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Solution
    On utilise le modèle latéral :
    \[
    \dot{z} = A_{\text{lat}}z + B_{\text{lat}}\Delta\phi
    \]
    avec
    \[
    z =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}.
    \]

    On cherche une commande de la forme :

    \[
    \Delta \phi(t) = -K_{pp}z(t).
    \]
    Donc le système en boucle fermée devient :

    \[
    \dot{z} = (A_{\text{lat}} - B_{\text{lat}}K_{pp})z.
    \]

    L'idée du pole placement est de choisir directement les valeurs propres de la matrice fermée
    \(A_{\text{lat}} - B_{\text{lat}}K_{pp}\).

    Pour que le système soit asymptotiquement stable, il faut choisir des pôles avec une partie réelle négative.
    J'ai choisi les pôles :
    \[
    -0.5,\quad -0.7,\quad -9.0,\quad -1.1.
    \]
    Ils ne sont pas trop lents, donc le retour vers zéro se fait avant environ 20 secondes, mais ils ne sont pas trop rapides non plus pour éviter une commande \(\Delta \phi\) trop grande.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt):
    from scipy.signal import place_poles
    from scipy.integrate import solve_ivp


    desired_poles = np.array([-0.5, -0.7, -0.9, -1.1])

    K_pp = place_poles(A_lat, B_lat, desired_poles).gain_matrix

    A_cl_pp = A_lat - B_lat @ K_pp
    eigs_pp = np.linalg.eigvals(A_cl_pp)

    print("Pôles demandés =", desired_poles)
    print("K_pp =", K_pp)
    print("Valeurs propres obtenues =", eigs_pp)

    # Simul
    T = 20.0
    z0 = np.array([0.0, 0.0, np.pi / 4, 0.0])

    def rhs_pp(t, z):
        return A_cl_pp @ z

    sol_pp = solve_ivp(
        rhs_pp,
        [0.0, T],
        z0,
        dense_output=True,
    )

    tt = np.linspace(0.0, T, 1000)
    z_tt = sol_pp.sol(tt)

    x_tt = z_tt[0]
    vx_tt = z_tt[1]
    theta_tt = z_tt[2]
    omega_tt = z_tt[3]

    phi_tt = -(K_pp @ z_tt).ravel()

    print("Max |theta| =", np.max(np.abs(theta_tt)))
    print("Max |phi| =", np.max(np.abs(phi_tt)))
    print("pi/2 =", np.pi / 2)
    print("x(20) =", x_tt[-1])
    print("theta(20) =", theta_tt[-1])

    # Graphe 1 : position latérale
    plt.figure(figsize=(7, 4))
    plt.plot(tt, x_tt, color="darkgreen", linewidth=2.0, label=r"$\Delta x(t)$")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.title("Pole placement — position laterale")
    plt.xlabel("time t")
    plt.ylabel(r"$\Delta x(t)$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    # Graphe 2 : angle
    plt.figure(figsize=(7, 4))
    plt.plot(tt, theta_tt, color="darkorange", linewidth=2.0, label=r"$\Delta \theta(t)$")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.axhline(np.pi / 2, color="red", linestyle=":", linewidth=1, label=r"$\pm \pi/2$")
    plt.axhline(-np.pi / 2, color="red", linestyle=":", linewidth=1)
    plt.title("Pole placement — angle du booster")
    plt.xlabel("time t")
    plt.ylabel(r"$\Delta \theta(t)$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    # Graphe 3 : commande
    plt.figure(figsize=(7, 4))
    plt.plot(tt, phi_tt, color="purple", linewidth=2.0, label=r"$\Delta \phi(t)$")
    plt.axhline(np.pi / 2, color="red", linestyle="--", linewidth=1, label=r"$\pm \pi/2$")
    plt.axhline(-np.pi / 2, color="red", linestyle="--", linewidth=1)
    plt.title("Pole placement — commande moteur")
    plt.xlabel("time t")
    plt.ylabel(r"$\Delta \phi(t)$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    # Graphe 4 : comparaison theta et phi
    plt.figure(figsize=(7, 4))
    plt.plot(tt, theta_tt, color="darkorange", linewidth=2.0, label=r"$\Delta \theta(t)$")
    plt.plot(tt, phi_tt, color="purple", linewidth=2.0, linestyle="--", label=r"$\Delta \phi(t)$")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.title("Comparaison angle / commande")
    plt.xlabel("time t")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    return (K_pp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Observation
    Avec les pôles choisis \(-0.5\), \(-0.7\), \(-0.9\) et \(-1.1\), les valeurs propres de la boucle fermée sont toutes négatives. Le modèle linéaire est donc asymptotiquement stable.
    Sur les graphes, on voit que \(\Delta \theta(t)\) revient vers 0 et que \(\Delta x(t)\) revient aussi vers 0.
    Ce contrôleur est plus complet que le réglage manuel, car il corrige à la fois l'inclinaison et la position horizontale.
    La commande \(\Delta \phi(t)\) reste inférieure à \(\pi/2\), donc la contrainte est respectée.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Solution
    Ici, on utilise un contrôleur optimal de type LQR sur le modèle latéral :
    \[
    \dot{z} = A_{\text{lat}}z + B_{\text{lat}}\Delta\phi.
    \]
    La commande est :
    \[
    \Delta\phi(t) = -K_{oc}z(t).
    \]
    Le principe est de choisir deux matrices \(Q\) et \(R\).
    \(Q\) pénalise les erreurs d'état, donc par exemple l'erreur de position ou d'angle.
    \(R\) pénalise l'utilisation de la commande \(\Delta\phi\).
    J'ai choisi de donner plus d'importance à l'angle \(\Delta\theta\), car le but principal est de redresser le booster, tout en gardant une commande raisonnable.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy):
    # z = [Delta x, Delta vx, Delta theta, Delta omega]
    # LQR
    oc_Q = np.diag([3.0, 0.5, 70.0, 8.0])
    oc_R = np.array([[300.0]])

    # Résolution de l'équation de Riccati
    oc_P = scipy.linalg.solve_continuous_are(A_lat, B_lat, oc_Q, oc_R)

    # Gain LQR
    K_lqr_custom = np.linalg.inv(oc_R) @ B_lat.T @ oc_P

    # Boucle 
    oc_A_cl = A_lat - B_lat @ K_lqr_custom
    oc_eigs = np.linalg.eigvals(oc_A_cl)

    print("Q =", oc_Q)
    print("R =", oc_R)
    print("K_lqr_custom =", K_lqr_custom)
    print("Closed-loop eigenvalues =", oc_eigs)

    # Simulation
    oc_T = 20.0
    oc_z_initial = np.array([0.0, 0.0, np.pi / 4, 0.0])

    def oc_rhs(t, z):
        return oc_A_cl @ z

    oc_sol = scipy.integrate.solve_ivp(
        oc_rhs,
        [0.0, oc_T],
        oc_z_initial,
        dense_output=True,
    )

    oc_time = np.linspace(0.0, oc_T, 1000)
    oc_traj = oc_sol.sol(oc_time)

    oc_x = oc_traj[0]
    oc_vx = oc_traj[1]
    oc_theta = oc_traj[2]
    oc_omega = oc_traj[3]

    oc_phi = -(K_lqr_custom @ oc_traj).ravel()

    print("Max |theta| =", np.max(np.abs(oc_theta)))
    print("Max |phi| =", np.max(np.abs(oc_phi)))
    print("pi/2 =", np.pi / 2)
    print("x(20) =", oc_x[-1])
    print("theta(20) =", oc_theta[-1])

    # Graphe 1 : position et angle
    plt.figure(figsize=(8, 4))
    plt.plot(oc_time, oc_x, color="seagreen", linewidth=2, label=r"$\Delta x(t)$")
    plt.plot(oc_time, oc_theta, color="darkorange", linewidth=2, label=r"$\Delta \theta(t)$")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.title("LQR — position et angle")
    plt.xlabel("time t")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    # Graphe 2 : commande phi
    plt.figure(figsize=(8, 4))
    plt.plot(oc_time, oc_phi, color="indigo", linewidth=2, label=r"$\Delta \phi(t)$")
    plt.axhline(np.pi / 2, color="red", linestyle="--", linewidth=1, label=r"$\pm \pi/2$")
    plt.axhline(-np.pi / 2, color="red", linestyle="--", linewidth=1)
    plt.title("LQR — commande")
    plt.xlabel("time t")
    plt.ylabel(r"$\Delta \phi(t)$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    # Graphe 3 : vitesses
    plt.figure(figsize=(8, 4))
    plt.plot(oc_time, oc_vx, color="steelblue", linewidth=2, label=r"$\Delta \dot{x}(t)$")
    plt.plot(oc_time, oc_omega, color="crimson", linewidth=2, label=r"$\Delta \dot{\theta}(t)$")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.title("LQR — vitesses")
    plt.xlabel("time t")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    return (K_lqr_custom,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Observation

    Avec ce choix de \(Q\) et \(R\), les valeurs propres de la boucle fermée ont une partie réelle négative. Donc le modèle linéaire est asymptotiquement stable.

    On voit sur les graphes que l'angle \(\Delta\theta(t)\) revient vers 0, et que la position \(\Delta x(t)\) revient aussi vers 0.

    La commande \(\Delta\phi(t)\) reste inférieure à \(\pi/2\), donc elle respecte la contrainte demandée.

    Ce réglage est différent du placement de pôles : ici, je ne choisis pas directement les valeurs propres. Je choisis plutôt les poids \(Q\) et \(R\), puis le gain \(K_{oc}\) est calculé automatiquement.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  Solution

    Ici, je teste les deux contrôleurs trouvés avant sur le modèle non linéaire complet.

    Les contrôleurs ont été calculés avec le modèle linéarisé, donc il faut vérifier qu'ils marchent aussi avec les vraies équations :

    \[
    \ddot{x} = -\frac{f}{M}\sin(\theta+\phi),
    \]

    \[
    \ddot{y} = \frac{f}{M}\cos(\theta+\phi)-g,
    \]

    \[
    \ddot{\theta} =
    -\frac{f}{J}\frac{\ell}{2}\sin(\phi).
    \]

    Je garde \(f = Mg\), et je contrôle seulement l'angle du moteur :

    \[
    \phi(t) = -Kz(t),
    \]

    avec

    \[
    z =
    \begin{bmatrix}
    x \\
    \dot{x} \\
    \theta \\
    \dot{\theta}
    \end{bmatrix}.
    \]

    Le but est de vérifier que \(x(t)\) et \(\theta(t)\) reviennent vers 0, et que la commande reste raisonnable.
    """)
    return


@app.cell
def _(
    K_lqr_custom,
    K_pp,
    M,
    booster_anim,
    g,
    mo,
    np,
    plt,
    redstart_solve,
    world,
):
    def validate_nonlinear_controller(K, name, T=20.0, y_start=80.0):
        K = np.array(K, dtype=float).reshape(1, 4)

    
        # [x, vx, y, vy, theta, omega]
        # Etat  non linéaire :
        y0 = np.array([0.0, 0.0, y_start, 0.0, np.pi / 4, 0.0])

        def controller_phi(state):
            x, vx, y, vy, theta, omega = state
            z_lat = np.array([x, vx, theta, omega])
            return float(-(K @ z_lat)[0])

        def f_phi(t, state):
            phi = controller_phi(state)
            f = M * g
            return np.array([f, phi])

        sol = redstart_solve([0.0, T], y0, f_phi)

        tt = np.linspace(0.0, T, 1000)
        states = sol(tt)
        x_tt = states[0]
        y_tt = states[2]
        theta_tt = states[4]

        phi_tt = np.array([
            controller_phi(states[:, i])
            for i in range(states.shape[1])
        ])

        print("-----", name, "----")
        print("x(T) =", x_tt[-1])
        print("theta(T) =", theta_tt[-1])
        print("Max |theta| =", np.max(np.abs(theta_tt)))
  
        print("Max |phi| =", np.max(np.abs(phi_tt)))
        print("pi/2 =", np.pi / 2)
        if np.max(np.abs(phi_tt)) > np.pi / 2:
            print("Attention : phi dépasse pi/2. Il faudrait retoucher le contrôleur.")
        else:
            print("Contrainte sur phi respectée.")
        return {
            "name": name,
            "K": K,
            "sol": sol,
            "tt": tt,
            "x": x_tt,
            "y": y_tt,
            "theta": theta_tt,
            "phi": phi_tt,
            "T": T,
        }


    pp_result = validate_nonlinear_controller(K_pp, "Pole placement")
    oc_result = validate_nonlinear_controller(K_lqr_custom, "Optimal control / LQR")


    # Comparaison de x(t)
    plt.figure(figsize=(8, 4))
    plt.plot(pp_result["tt"], pp_result["x"], color="darkslateblue", linewidth=2, label="Pole placement")
    plt.plot(oc_result["tt"], oc_result["x"], color="mediumseagreen", linewidth=2, linestyle="--", label="Optimal control")
    plt.axhline(0, color="black", linestyle=":", linewidth=1)
    plt.title("Nonlinear validation — lateral position")
    plt.xlabel("time t")
    plt.ylabel("x(t)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    # Comparaison de theta(t
    plt.figure(figsize=(8, 4))
    plt.plot(pp_result["tt"], pp_result["theta"], color="darkorange", linewidth=2, label="Pole placement")
    plt.plot(oc_result["tt"], oc_result["theta"], color="crimson", linewidth=2, linestyle="--", label="Optimal control")
    plt.axhline(0, color="black", linestyle=":", linewidth=1)
    plt.axhline(np.pi / 2, color="grey", linestyle="--", linewidth=1)
    plt.axhline(-np.pi / 2, color="grey", linestyle="--", linewidth=1)
    plt.title("Nonlinear validation — tilt angle")
    plt.xlabel("time t")
    plt.ylabel(r"$\theta(t)$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    # Comparaison de phi
    plt.figure(figsize=(8, 4))
    plt.plot(pp_result["tt"], pp_result["phi"], color="purple", linewidth=2, label="Pole placement")
    plt.plot(oc_result["tt"], oc_result["phi"], color="teal", linewidth=2, linestyle="--", label="Optimal control")
    plt.axhline(np.pi / 2, color="red", linestyle="--", linewidth=1, label=r"$\pm \pi/2$")
    plt.axhline(-np.pi / 2, color="red", linestyle="--", linewidth=1)
    plt.title("Nonlinear validation — command")
    plt.xlabel("time t")
    plt.ylabel(r"$\phi(t)$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    def nonlinear_animation(result):
        sol = result["sol"]
        K = result["K"]
        T = result["T"]

        def x(t):
            return sol(t)[0]

        def y(t):
            return sol(t)[2]

        def theta(t):
            return sol(t)[4]

        def f(t):
            return M * g

        def phi(t):
            state = sol(t)
            z_lat = np.array([state[0], state[1], state[4], state[5]])
            return float(-(K @ z_lat)[0])

        return mo.Html(
            f"<h3>{result['name']}</h3>"
            + world(
                [-15, 15, -5, 90],
                booster_anim(x, y, theta, f, phi, T=T),
            )
        )


    mo.vstack(
        [
            nonlinear_animation(pp_result),
            nonlinear_animation(oc_result),
        ]
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Observations

    Les deux contrôleurs sont ensuite testés sur le vrai modèle non linéaire.

    On vérifie sur les graphes que \(x(t)\) revient vers 0 et que \(\theta(t)\) revient aussi vers 0.
    Cela montre que les contrôleurs calculés sur le modèle linéaire restent valables sur le modèle complet.

    On vérifie aussi la commande \(\phi(t)\). Si elle reste dans l'intervalle

    \[
    |\phi(t)| < \frac{\pi}{2},
    \]

    alors la contrainte demandée est respectée.

    Sur l'animation, le booster se redresse progressivement.
    La hauteur \(y(t)\) n'est très importante ici, car dans cette partie on contrôle seulement la dynamique latérale.
    """)
    return


if __name__ == "__main__":
    app.run()

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

    return la, np, plt, sci, scipy


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


@app.cell
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


@app.cell
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
    """)
    return


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
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(g, np):
    A = np.zeros((6, 6))
    A[0, 1] = 1.0
    A[1, 4] = -g
    A[2, 3] = 1.0
    A[4, -1] = 1.0
    A
    return (A,)


@app.cell(hide_code=True)
def _(M, g, l, np):
    B = np.zeros((6, 2))
    B[ 1, 1]  = -g 
    B[ 3, 0]  = 1/M
    B[-1, 1] = -6 * g / l
    B
    return (B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell(hide_code=True)
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)
    print(f"Eigenvalues of A: {eigenvalues}")
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
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell(hide_code=True)
def _(A, B, np):
    # Controllability
    cs = np.column_stack
    mp = np.linalg.matrix_power
    KC = cs([mp(A, k) @ B for k in range(6)])
    KC
    return (KC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell(hide_code=True)
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
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
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0], 
        [0, 0, -g, 0], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0]], dtype=np.float64)
    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T

    print("A_lat:")
    print(A_lat)
    print("B_lat:")
    print(B_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(A_lat, B_lat, np):
    # Controllability
    _cs = np.column_stack
    _mp = np.linalg.matrix_power
    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])
    KC_lat
    return (KC_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell(hide_code=True)
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
    return


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
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(g, l, np):
    def make_fun_lat(phi):
        def fun_lat(t, state):
            x, dx, theta, dtheta = state
            phi_ = phi(t, state)
            d2x = -g * (theta + phi_)
            d2theta = - 6 * g / l * phi_
            return np.array([dx, d2x, dtheta, d2theta])

        return fun_lat

    return (make_fun_lat,)


@app.cell(hide_code=True)
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():
        def phi(t, state):
            return 0.0

        f_lat = make_fun_lat(phi)
        t_span = [0, 10]
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]
        r = sci.solve_ivp(
            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True
        )
        t = np.linspace(t_span[0], t_span[1], 1000)
        sol_t = r.sol(t)
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t, sol_t[0], label=r"$x(t)$")
        ax1.grid(True)
        ax1.legend()
        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")
        ax2.grid(True)
        ax2.set_xlabel(r"time $t$")
        ax2.legend()
        return mo.center(fig)


    lin_sim_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():

        K = np.array([0.0, 0.0, -1.0, 0.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():

        K = np.array([0.0, 0.0, -1.0, -0.1])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():

        K = np.array([0.0, 0.0, -1.0, -5.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k3()
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(
        A=A_lat,
        B=B_lat,
        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),
    ).gain_matrix.squeeze()


    def lin_sim_32():
        K = Kpp
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
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
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():
        Q = np.eye(4,4)
        print("Q:", Q)
        R = np.eye(1) #10*l**2 * np.eye(1)
        print("R:", R)
        Pi = scipy.linalg.solve_continuous_are(
            a=A_lat, 
            b=B_lat, 
            q=Q, 
            r=R
        )
        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_4()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4,4)
    print("Q:", Q)
    R = 100 * np.eye(1)
    print("R:", R)
    Pi = scipy.linalg.solve_continuous_are(
        a=A_lat, 
        b=B_lat, 
        q=Q, 
        r=R
    )
    Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

    def lin_sim_42():
        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_42()
    return (Koc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Kpp.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Koc.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & +\cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse
    Le point \(h\) est défini par
    \[
    h =
    \begin{bmatrix}
    x - \frac{\ell}{6}\sin\theta \\
    y + \frac{\ell}{6}\cos\theta
    \end{bmatrix}.
    \]
    Alors
    \[
    h =
    \begin{bmatrix}
    x \\
    y
    \end{bmatrix}
    +
    \frac{\ell}{6}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}.
    \]
    Le vecteur
    \[
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \]
    est le vecteur directeur de l'axe du booster, orienté vers le haut du booster.
    Donc \(h\) représente un point situé sur le booster, à une distance \(\ell/6\) du centre de masse, dans la direction du haut du booster.
    Comme le booster a une longueur totale \(\ell\), son centre de masse est au milieu. Le point \(h\) est donc un point placé un peu au-dessus du centre du booster, sur son axe.
    En résumé, \(h\) n'est pas le centre de masse : c'est un autre point du booster qu'on choisit comme sortie à contrôler. L'intérêt est que cette sortie va permettre ensuite d'obtenir une dynamique plus simple pour faire l'exact linearization.
    """)
    return


@app.cell
def _(l, np, plt):
    ## Schéma du point h
    def point_h_drawing():
        x0 = 0.0
        y0 = 0.0
        theta0 = np.pi / 6
        axis = np.array([-np.sin(theta0), np.cos(theta0)])
        center = np.array([x0, y0])
        bottom = center - (l / 2) * axis
        top = center + (l / 2) * axis
        h_point = center + (l / 6) * axis

        plt.figure(figsize=(4,4))
        plt.plot([bottom[0], top[0]], [bottom[1], top[1]], linewidth=4, label="booster")
        plt.scatter(center[0], center[1], s=80, label="Centre de masse")
        plt.scatter(h_point[0], h_point[1], s=80, label="point h")

        plt.text(center[0] + 0.05, center[1], "(x,y)")
        plt.text(h_point[0] + 0.05, h_point[1], "h")

        plt.axis("equal")
        plt.grid(True)
        plt.legend()
        plt.title("Interprétation géométrique du point h")
        plt.show()

    point_h_drawing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    On part de la sortie

    \[
    h =
    \begin{bmatrix}
    x - \frac{\ell}{6}\sin\theta \\
    y + \frac{\ell}{6}\cos\theta
    \end{bmatrix}.
    \]

    Donc, en dérivant une première fois :

    \[
    \dot h =
    \begin{bmatrix}
    \dot{x} - \frac{\ell}{6}\cos\theta \dot{\theta} \\
    \dot{y} - \frac{\ell}{6}\sin\theta \dot{\theta}
    \end{bmatrix}.
    \]

    Pour calculer \(\ddot h\), on dérive encore une fois chaque composante.

    Pour la première composante :

    \[
    \dot h_x = \dot{x} - \frac{\ell}{6}\cos\theta \dot{\theta}.
    \]

    Donc :

    \[
    \ddot h_x
    =
    \ddot{x}
    -
    \frac{\ell}{6}
    \left(
    -\sin\theta \dot{\theta}^2
    +
    \cos\theta \ddot{\theta}
    \right).
    \]

    Ainsi :

    \[
    \ddot h_x
    =
    \ddot{x}
    +
    \frac{\ell}{6}\sin\theta \dot{\theta}^2
    -
    \frac{\ell}{6}\cos\theta \ddot{\theta}.
    \]

    Pour la deuxième composante :

    \[
    \dot h_y = \dot{y} - \frac{\ell}{6}\sin\theta \dot{\theta}.
    \]

    Donc :

    \[
    \ddot h_y
    =
    \ddot{y}
    -
    \frac{\ell}{6}
    \left(
    \cos\theta \dot{\theta}^2
    +
    \sin\theta \ddot{\theta}
    \right).
    \]

    Ainsi :

    \[
    \ddot h_y
    =
    \ddot{y}
    -
    \frac{\ell}{6}\cos\theta \dot{\theta}^2
    -
    \frac{\ell}{6}\sin\theta \ddot{\theta}.
    \]

    Maintenant, on remplace \(\ddot{x}\), \(\ddot{y}\) et \(\ddot{\theta}\) par les équations du mouvement.

    Pour le centre de masse :

    \[
    M\ddot{x}=f_x,
    \qquad
    M\ddot{y}=f_y-Mg.
    \]

    Donc :

    \[
    \ddot{x}=\frac{f_x}{M},
    \qquad
    \ddot{y}=\frac{f_y}{M}-g.
    \]

    Pour la rotation, avec le système auxiliaire on obtient :

    \[
    \ddot{\theta} = \frac{v_2}{z}.
    \]

    La force auxiliaire est choisie sous la forme :

    \[
    \begin{bmatrix}
    f_x\\
    f_y
    \end{bmatrix}
    =
    R\left(\theta-\frac{\pi}{2}\right)
    \begin{bmatrix}
    z-\frac{M\ell \dot{\theta}^2}{6}\\
    \frac{M\ell v_2}{6z}
    \end{bmatrix}.
    \]

    En utilisant la matrice \(R\left(\theta-\frac{\pi}{2}\right)\), on obtient :

    \[
    f_x
    =
    \left(z-\frac{M\ell\dot{\theta}^2}{6}\right)\sin\theta
    +
    \frac{M\ell v_2}{6z}\cos\theta,
    \]

    \[
    f_y
    =
    -\left(z-\frac{M\ell\dot{\theta}^2}{6}\right)\cos\theta
    +
    \frac{M\ell v_2}{6z}\sin\theta.
    \]

    On remplace alors ces expressions dans \(\ddot h_x\) et \(\ddot h_y\).

    Pour \(\ddot h_x\) :

    \[
    \ddot h_x
    =
    \frac{f_x}{M}
    +
    \frac{\ell}{6}\sin\theta \dot{\theta}^2
    -
    \frac{\ell}{6}\cos\theta \frac{v_2}{z}.
    \]

    Après remplacement de \(f_x\), les termes en \(\dot{\theta}^2\) et en \(v_2\) se compensent, et il reste :

    \[
    \ddot h_x = \frac{z}{M}\sin\theta.
    \]

    Pour \(\ddot h_y\) :

    \[
    \ddot h_y
    =
    \frac{f_y}{M}
    -
    g
    -
    \frac{\ell}{6}\cos\theta \dot{\theta}^2
    -
    \frac{\ell}{6}\sin\theta \frac{v_2}{z}.
    \]

    Après remplacement de \(f_y\), les termes en \(\dot{\theta}^2\) et en \(v_2\) se compensent aussi, et il reste :

    \[
    \ddot h_y = -\frac{z}{M}\cos\theta - g.
    \]

    Finalement :

    \[
    \ddot h =
    \begin{bmatrix}
    \frac{z}{M}\sin\theta \\
    -\frac{z}{M}\cos\theta - g
    \end{bmatrix}.
    \]

    Donc \(\ddot h\) dépend seulement de \(\theta\), de \(z\), et des constantes \(M\) et \(g\).
    Je garde \(M\) dans les formules pour rester cohérent avec la suite, même si numériquement \(M=1\).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    On part du résultat obtenu juste avant :

    \[
    \ddot h =
    \begin{bmatrix}
    \frac{z}{M}\sin\theta \\
    -\frac{z}{M}\cos\theta - g
    \end{bmatrix}.
    \]

    Pour calculer \(h^{(3)}\), on dérive chaque composante.

    Pour la première composante :

    \[
    \ddot h_x = \frac{z}{M}\sin\theta.
    \]

    Donc :

    \[
    h_x^{(3)}
    =
    \frac{1}{M}
    \left(
    \dot z \sin\theta + z\dot\theta\cos\theta
    \right).
    \]

    Pour la deuxième composante :

    \[
    \ddot h_y = -\frac{z}{M}\cos\theta - g.
    \]

    Comme \(g\) est constant, sa dérivée est nulle. Donc :

    \[
    h_y^{(3)}
    =
    \frac{1}{M}
    \left(
    -\dot z \cos\theta + z\dot\theta\sin\theta
    \right).
    \]

    Ainsi :

    \[
    h^{(3)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    \dot z \sin\theta + z\dot\theta\cos\theta \\
    -\dot z \cos\theta + z\dot\theta\sin\theta
    \end{bmatrix}.
    \]

    Ensuite, on dérive encore une fois pour obtenir \(h^{(4)}\).
    On utilise :

    \[
    \ddot z = v_1
    \]

    et, avec le système auxiliaire :

    \[
    \ddot\theta = \frac{v_2}{z}.
    \]

    Après simplification, on obtient :

    \[
    h^{(4)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    (v_1 - z\dot\theta^2)\sin\theta
    +
    (v_2 + 2\dot z\dot\theta)\cos\theta
    \\
    -(v_1 - z\dot\theta^2)\cos\theta
    +
    (v_2 + 2\dot z\dot\theta)\sin\theta
    \end{bmatrix}.
    \]

    On peut aussi écrire cette expression sous forme matricielle :

    \[
    h^{(4)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    \sin\theta & \cos\theta \\
    -\cos\theta & \sin\theta
    \end{bmatrix}
    \begin{bmatrix}
    v_1 - z\dot\theta^2 \\
    v_2 + 2\dot z\dot\theta
    \end{bmatrix}.
    \]

    Cette écriture est utile parce qu'on voit clairement que les commandes \(v_1\) et \(v_2\) apparaissent dans la quatrième dérivée de \(h\).
    Donc, à l'étape suivante, on pourra choisir \(v_1\) et \(v_2\) pour imposer directement \(h^{(4)} = u\).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    À l'étape précédente, on a obtenu :

    \[
    h^{(4)}
    =
    \frac{1}{M}
    R\left(\theta-\frac{\pi}{2}\right)
    \begin{bmatrix}
    v_1 - z\dot\theta^2 \\
    v_2 + 2\dot z\dot\theta
    \end{bmatrix}.
    \]

    On veut choisir \(v_1\) et \(v_2\) pour imposer directement :

    \[
    h^{(4)} = u
    \]

    avec

    \[
    u =
    \begin{bmatrix}
    u_1\\
    u_2
    \end{bmatrix}.
    \]

    Donc il faut que :

    \[
    \frac{1}{M}
    R\left(\theta-\frac{\pi}{2}\right)
    \begin{bmatrix}
    v_1 - z\dot\theta^2 \\
    v_2 + 2\dot z\dot\theta
    \end{bmatrix}
    =
    u.
    \]

    On multiplie alors par \(M\), puis par l'inverse de la matrice de rotation :

    \[
    \begin{bmatrix}
    v_1 - z\dot\theta^2 \\
    v_2 + 2\dot z\dot\theta
    \end{bmatrix}
    =
    M
    R\left(\theta-\frac{\pi}{2}\right)^{-1}
    u.
    \]

    Comme \(R\) est une matrice de rotation, son inverse est simplement :

    \[
    R\left(\theta-\frac{\pi}{2}\right)^{-1}
    =
    R\left(-\theta+\frac{\pi}{2}\right).
    \]

    En développant cette matrice, on obtient :

    \[
    R\left(\theta-\frac{\pi}{2}\right)^{-1}
    =
    \begin{bmatrix}
    \sin\theta & -\cos\theta \\
    \cos\theta & \sin\theta
    \end{bmatrix}.
    \]

    Donc :

    \[
    \begin{bmatrix}
    v_1 - z\dot\theta^2 \\
    v_2 + 2\dot z\dot\theta
    \end{bmatrix}
    =
    M
    \begin{bmatrix}
    \sin\theta & -\cos\theta \\
    \cos\theta & \sin\theta
    \end{bmatrix}
    \begin{bmatrix}
    u_1\\
    u_2
    \end{bmatrix}.
    \]

    On obtient alors :

    \[
    v_1
    =
    z\dot\theta^2
    +
    M(\sin\theta\,u_1-\cos\theta\,u_2),
    \]

    \[
    v_2
    =
    -2\dot z\dot\theta
    +
    M(\cos\theta\,u_1+\sin\theta\,u_2).
    \]

    Avec ce choix de \(v_1\) et \(v_2\), les termes compliqués se compensent et il reste bien :

    \[
    h^{(4)} = u.
    \]

    C'est donc à ce moment-là que la dynamique de la sortie \(h\) devient linéaire.
    """)
    return


@app.cell
def _(M, np):
    def exact_linearizing_v(theta, dtheta, z, dz, u):
        u1, u2 = u

        v1 = z * dtheta**2 + M * (np.sin(theta) * u1 - np.cos(theta) * u2)
        v2 = -2 * dz * dtheta + M * (np.cos(theta) * u1 + np.sin(theta) * u2)

        return np.array([v1, v2])

    return (exact_linearizing_v,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell
def _(M, g, l, np):
    def Tr(x, dx, y, dy, theta, dtheta, z, dz):
        # h
        hx = x - (l / 6) * np.sin(theta)
        hy = y + (l / 6) * np.cos(theta)

        # h'
        dhx = dx - (l / 6) * np.cos(theta) * dtheta
        dhy = dy - (l / 6) * np.sin(theta) * dtheta

        # h''
        d2hx = (z / M) * np.sin(theta)
        d2hy = -(z / M) * np.cos(theta) - g

        # h'''
        d3hx = (dz * np.sin(theta) + z * dtheta * np.cos(theta)) / M
        d3hy = (-dz * np.cos(theta) + z * dtheta * np.sin(theta)) / M

        return np.array([
            hx, hy,
            dhx, dhy,
            d2hx, d2hy,
            d3hx, d3hy,
        ])

    return (Tr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    On veut faire l'opération inverse de `Tr`.

    La fonction `Tr` part de l'état physique et auxiliaire :
    \[
    x,\dot{x},y,\dot{y},\theta,\dot{\theta},z,\dot z
    \]
    et calcule :
    \[
    h,\dot h,\ddot h,h^{(3)}.
    \]
    Ici, on veut faire l'inverse : à partir de
    \[
    h,\dot h,\ddot h,h^{(3)},
    \]
    on veut retrouver :
    \[
    x,\dot{x},y,\dot{y},\theta,\dot{\theta},z,\dot z.
    \]

    On commence avec la formule de \(\ddot h\) :
    \[
    \ddot h =
    \begin{bmatrix}
    \frac{z}{M}\sin\theta \\
    -\frac{z}{M}\cos\theta - g
    \end{bmatrix}.
    \]
    On isole la partie qui ne contient pas la gravité en posant :
    \[
    a =
    \begin{bmatrix}
    \ddot h_x \\
    \ddot h_y + g
    \end{bmatrix}.
    \]

    Alors :

    \[
    a =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}.
    \]

    Le vecteur
    \[
    b_1 =
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    \]
    est un vecteur unitaire, car :
    \[
    \|b_1\| =
    \sqrt{\sin^2\theta+\cos^2\theta}
    =1.
    \]
    Donc :
    \[
    \|a\| =
    \left|\frac{z}{M}\right|.
    \]

    Comme on suppose dans l'énoncé que \(z<0\), on choisit le signe négatif :
    \[
    z = -M\|a\|.
    \]
    C'est pour cela que l'hypothèse \(z<0\) est importante : sans elle, on ne saurait pas choisir entre \(z\) et \(-z\).


    Ensuite, on retrouve \(\theta\).

    On sait que :
    \[
    a =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}.
    \]
    Comme \(z<0\), le vecteur \(a\) est dans la direction opposée à
    \[
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}.
    \]
    Dans le code, on utilise directement la relation :
    \[
    \theta = \operatorname{atan2}(-a_x,a_y).
    \]
    Cela permet de retrouver l'angle avec le bon quadrant.


    Une fois \(z\) et \(\theta\) connus, il reste à retrouver \(\dot z\) et \(\dot\theta\).

    On utilise la formule de \(h^{(3)}\) :

    \[
    h^{(3)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    \dot z \sin\theta + z\dot\theta\cos\theta \\
    -\dot z \cos\theta + z\dot\theta\sin\theta
    \end{bmatrix}.
    \]

    On la réécrit sous la forme :

    \[
    M h^{(3)}
    =
    \dot z
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    +
    z\dot\theta
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}.
    \]

    On pose :

    \[
    b_1 =
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix},
    \qquad
    b_2 =
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}.
    \]

    Ces deux vecteurs sont orthogonaux, car :

    \[
    b_1 \cdot b_2
    =
    \sin\theta\cos\theta
    -
    \cos\theta\sin\theta
    =0.
    \]

    Ils sont aussi unitaires. Donc ils forment une base orthonormée.

    Ainsi, pour retrouver \(\dot z\), on projette \(M h^{(3)}\) sur \(b_1\) :

    \[
    \dot z = M h^{(3)} \cdot b_1.
    \]

    Et pour retrouver \(z\dot\theta\), on projette \(M h^{(3)}\) sur \(b_2\) :

    \[
    z\dot\theta = M h^{(3)} \cdot b_2.
    \]

    Comme on connaît déjà \(z\), on obtient :

    \[
    \dot\theta =
    \frac{M h^{(3)} \cdot b_2}{z}.
    \]


    Il reste maintenant à retrouver \(x,y,\dot x,\dot y\).

    On repart de la définition de \(h\) :

    \[
    h_x = x - \frac{\ell}{6}\sin\theta,
    \qquad
    h_y = y + \frac{\ell}{6}\cos\theta.
    \]

    Donc :

    \[
    x = h_x + \frac{\ell}{6}\sin\theta,
    \]

    \[
    y = h_y - \frac{\ell}{6}\cos\theta.
    \]

    Puis on utilise la formule de \(\dot h\) :

    \[
    \dot h_x =
    \dot x - \frac{\ell}{6}\cos\theta\dot\theta,
    \]

    \[
    \dot h_y =
    \dot y - \frac{\ell}{6}\sin\theta\dot\theta.
    \]

    Donc :

    \[
    \dot x =
    \dot h_x + \frac{\ell}{6}\cos\theta\dot\theta,
    \]

    \[
    \dot y =
    \dot h_y + \frac{\ell}{6}\sin\theta\dot\theta.
    \]

    Finalement, on a bien retrouvé toutes les variables :

    \[
    x,\dot{x},y,\dot{y},\theta,\dot{\theta},z,\dot z.
    \]

    C'est exactement ce que fait la fonction `T_inv`.
    """)
    return


@app.cell
def _(M, g, l, np):
    def T_inv(hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy):


        # On reconstruit a à partir de h''
        a = np.array([d2hx, d2hy + g])
        a_norm = np.linalg.norm(a)

        if a_norm < 1e-12:
            raise ValueError("Impossible d'inverser : a est trop proche de zéro.")

        # Comme on suppose z < 0
        z = -M * a_norm

        # Direction de l'axe du booster
        theta = np.arctan2(-a[0], a[1])

        sin_theta = np.sin(theta)
        cos_theta = np.cos(theta)  

        #  dz et dtheta à partir de h'''
        h3 = M * np.array([d3hx, d3hy])

        b1 = np.array([sin_theta, -cos_theta])
        b2 = np.array([cos_theta, sin_theta])

        dz = h3 @ b1
        dtheta = (h3 @ b2) / z

        #  x et y à partir de h
        x = hx + (l / 6) * sin_theta
        y = hy - (l / 6) * cos_theta

        #  dx et dy à partir de dh
        dx = dhx + (l / 6) * cos_theta * dtheta
        dy = dhy + (l / 6) * sin_theta * dtheta

        return np.array([
            x, dx,
            y, dy,
            theta, dtheta,
            z, dz,
        ])

    return (T_inv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    On veut construire une trajectoire admissible entre un état initial et un état final.

    Grâce à la linéarisation exacte, on ne travaille pas directement avec les variables physiques

    \[
    x,\dot{x},y,\dot{y},\theta,\dot{\theta},z,\dot z.
    \]

    On les transforme d'abord avec `Tr` pour obtenir :

    \[
    h,\quad \dot h,\quad \ddot h,\quad h^{(3)}.
    \]

    Comme la dynamique obtenue est :

    \[
    h^{(4)} = u,
    \]

    on peut choisir séparément une trajectoire polynomiale pour \(h_x(t)\) et \(h_y(t)\).

    Pour respecter les conditions initiales et finales sur :

    \[
    h,\quad \dot h,\quad \ddot h,\quad h^{(3)},
    \]

    on utilise un polynôme de degré 7.
    C'est logique, car on a 8 contraintes : 4 au début et 4 à la fin.

    Ensuite, pour chaque instant \(t\), on calcule :

    \[
    h(t),\dot h(t),\ddot h(t),h^{(3)}(t),h^{(4)}(t).
    \]

    Puis on utilise `T_inv` pour retrouver :

    \[
    x,\dot{x},y,\dot{y},\theta,\dot{\theta},z,\dot z.
    \]

    Enfin, avec \(h^{(4)}\), on calcule les commandes auxiliaires, puis la force réelle du booster, c'est-à-dire \(f\) et \(\phi\).
    Conclusion : la fonction "compute" construit une trajectoire complète qui respecte les états initial et final donnés.
    """)
    return


@app.cell
def _(M, T_inv, Tr, exact_linearizing_v, l, np):
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        # Transformation des états initial et final vers les dérivées de h
        tr_0 = Tr(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0)
        tr_f = Tr(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf)

        # Pour hx : [hx, dhx, d2hx, d3hx]
        hx_0 = tr_0[[0, 2, 4, 6]]
        hx_f = tr_f[[0, 2, 4, 6]]

        # Pour hy : [hy, dhy, d2hy, d3hy]
        hy_0 = tr_0[[1, 3, 5, 7]]
        hy_f = tr_f[[1, 3, 5, 7]]

        def polynomial_coeffs(jet_0, jet_f, tf):
     
            ##Calcule les coefficients d'un polynôme de degré 7.
            ##Le polynôme respecte p, p', p'', p''' au temps 0 et au temps tf.
    
            A_poly = np.zeros((8, 8))
            b_poly = np.zeros(8)

            # Contraintes en t = 0
            # p(0)
            A_poly[0, 0] = 1.0
            b_poly[0] = jet_0[0]

            # p'(0)
            A_poly[1, 1] = 1.0
            b_poly[1] = jet_0[1]

            # p''(0)
            A_poly[2, 2] = 2.0
            b_poly[2] = jet_0[2]

            # p'''(0)
            A_poly[3, 3] = 6.0
            b_poly[3] = jet_0[3]

            # Contraintes en t = tf
            for k in range(8):
                A_poly[4, k] = tf**k

                if k >= 1:
                    A_poly[5, k] = k * tf**(k - 1)

                if k >= 2:
                    A_poly[6, k] = k * (k - 1) * tf**(k - 2)

                if k >= 3:
                    A_poly[7, k] = k * (k - 1) * (k - 2) * tf**(k - 3)

            b_poly[4] = jet_f[0]
            b_poly[5] = jet_f[1]
            b_poly[6] = jet_f[2]
            b_poly[7] = jet_f[3]

            return np.linalg.solve(A_poly, b_poly)

        def eval_poly(coeffs, t, order):
    ##Évalue la dérivée d'ordre `order` du polynôme.
            value = 0.0

            for k, a_k in enumerate(coeffs):
                if k >= order:
                    factor = 1.0
                    for j in range(order):
                        factor *= k - j

                    value += a_k * factor * t**(k - order)

            return value

        coeffs_hx = polynomial_coeffs(hx_0, hx_f, tf)
        coeffs_hy = polynomial_coeffs(hy_0, hy_f, tf)

        def R_matrix(alpha):
            return np.array([
                [np.cos(alpha), -np.sin(alpha)],
                [np.sin(alpha), np.cos(alpha)],
            ])

        def one_time(t):
            # h et ses dérivées jusqu'à l'ordre 4
            hx = eval_poly(coeffs_hx, t, 0)
            dhx = eval_poly(coeffs_hx, t, 1)
            d2hx = eval_poly(coeffs_hx, t, 2)
            d3hx = eval_poly(coeffs_hx, t, 3)
            d4hx = eval_poly(coeffs_hx, t, 4)

            hy = eval_poly(coeffs_hy, t, 0)
            dhy = eval_poly(coeffs_hy, t, 1)
            d2hy = eval_poly(coeffs_hy, t, 2)
            d3hy = eval_poly(coeffs_hy, t, 3)
            d4hy = eval_poly(coeffs_hy, t, 4)

            # Retour vers les variables physiques
            state = T_inv(hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy)

            x, dx, y, dy, theta, dtheta, z, dz = state

            # Ici u = h^(4)
            u = np.array([d4hx, d4hy])

            # Calcul de v = [v1, v2]
            v1, v2 = exact_linearizing_v(theta, dtheta, z, dz, u)

            # Force cartésienne donnée par le système auxiliaire
            force_local = np.array([
                z - M * l * dtheta**2 / 6,
                M * l * v2 / (6 * z),
            ])

            fx, fy = R_matrix(theta - np.pi / 2) @ force_local

            # Conversion de (fx, fy) vers (f, phi)
            f = np.sqrt(fx**2 + fy**2)
            phi = np.arctan2(-fx, fy) - theta

            return np.array([
                x, dx, y, dy, theta, dtheta, z, dz, f, phi,
            ])

        def fun(t):
            t_array = np.asarray(t)

            if t_array.ndim == 0:
                return one_time(float(t_array))

            return np.column_stack([
                one_time(float(t_i))
                for t_i in t_array
            ])

        return fun

    return (compute,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Réponse

    On teste maintenant la trajectoire calculée par `compute`.

    D'après ces données , l'idée est de partir d'un état initial où le booster est incliné et décalé horizontalement :

    \[
    x_0 = 5,\qquad y_0 = 20,\qquad \theta_0 = -\frac{\pi}{8}.
    \]

    On veut arriver à un état final où le booster est proche de la cible, vertical et au repos :

    \[
    x_f = 0,\qquad y_f = \frac{2\ell}{3},\qquad \theta_f = 0.
    \]

    La fonction `compute` construit une trajectoire pour la sortie \(h\), puis utilise `T_inv` pour retrouver les vraies variables du booster :

    \[
    x,\dot{x},y,\dot{y},\theta,\dot{\theta},z,\dot z.
    \]

    On vérifie ensuite les graphes de \(x(t)\), \(y(t)\), \(\theta(t)\), \(f(t)\) et \(\phi(t)\), puis on affiche une animation du mouvement.
    """)
    return


@app.cell
def _(M, booster_anim, compute, g, l, mo, np, plt, world):
    gv_fun = compute(
        5.0, 0.0, 20.0, -1.0, -np.pi / 8, 0.0, -M * g, 0.0,
        0.0, 0.0, 2 * l / 3, 0.0, 0.0, 0.0, -M * g, 0.0,
        10.0,
    )

    gv_tf = 10.0
    gv_time = np.linspace(0.0, gv_tf, 1000)
    gv_values = gv_fun(gv_time)

    gv_x = gv_values[0]
    gv_dx = gv_values[1]
    gv_y = gv_values[2]
    gv_dy = gv_values[3]
    gv_theta = gv_values[4]
    gv_dtheta = gv_values[5]
    gv_z = gv_values[6]
    gv_dz = gv_values[7]
    gv_f = gv_values[8]
    gv_phi = gv_values[9]

    print("Initial value:")
    print(gv_fun(0.0))

    print("Final value:")
    print(gv_fun(gv_tf))

    print("Max |phi| =", np.max(np.abs(gv_phi)))
    print("Min f =", np.min(gv_f))
    print("Max f =", np.max(gv_f))
    print("Min z =", np.min(gv_z))


    # Graphe 1 : position
    plt.figure(figsize=(8, 4))
    plt.plot(gv_time, gv_x, label=r"$x(t)$")
    plt.plot(gv_time, gv_y, label=r"$y(t)$")
    plt.axhline(0, color="black", linestyle=":", linewidth=1)
    plt.axhline(2 * l / 3, color="grey", linestyle="--", linewidth=1, label=r"$y_f=2\ell/3$")
    plt.xlabel("time t")
    plt.title("Exact linearization — position")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    # Graphe 2 : vitesses
    plt.figure(figsize=(8, 4))
    plt.plot(gv_time, gv_dx, label=r"$\dot{x}(t)$")
    plt.plot(gv_time, gv_dy, label=r"$\dot{y}(t)$")
    plt.axhline(0, color="black", linestyle=":", linewidth=1)
    plt.xlabel("time t")
    plt.title("Exact linearization — velocities")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    # Graphe 3 : angle
    plt.figure(figsize=(8, 4))
    plt.plot(gv_time, gv_theta, label=r"$\theta(t)$")
    plt.plot(gv_time, gv_dtheta, label=r"$\dot{\theta}(t)$")
    plt.axhline(0, color="black", linestyle=":", linewidth=1)
    plt.axhline(np.pi / 2, color="red", linestyle="--", linewidth=1, label=r"$\pm\pi/2$")
    plt.axhline(-np.pi / 2, color="red", linestyle="--", linewidth=1)
    plt.xlabel("time t")
    plt.title("Exact linearization — angle")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    # Graphe 4 : z
    plt.figure(figsize=(8, 4))
    plt.plot(gv_time, gv_z, label=r"$z(t)$")
    plt.axhline(0, color="red", linestyle="--", linewidth=1, label=r"$z=0$")
    plt.xlabel("time t")
    plt.title("Auxiliary variable z")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    # Graphe 5 : commandes f et phi
    plt.figure(figsize=(8, 4))
    plt.plot(gv_time, gv_f, label=r"$f(t)$")
    plt.xlabel("time t")
    plt.title("Force amplitude")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.plot(gv_time, gv_phi, label=r"$\phi(t)$")
    plt.axhline(np.pi / 2, color="red", linestyle="--", linewidth=1, label=r"$\pm\pi/2$")
    plt.axhline(-np.pi / 2, color="red", linestyle="--", linewidth=1)
    plt.xlabel("time t")
    plt.title("Engine angle")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


    # Animation
    def gv_x_fun(t):
        return gv_fun(t)[0]

    def gv_y_fun(t):
        return gv_fun(t)[2]

    def gv_theta_fun(t):
        return gv_fun(t)[4]

    def gv_f_fun(t):
        return gv_fun(t)[8]

    def gv_phi_fun(t):
        return gv_fun(t)[9]

    mo.Html(
        world(
            [-2, 7, -2, 22],
            booster_anim(
                gv_x_fun,
                gv_y_fun,
                gv_theta_fun,
                gv_f_fun,
                gv_phi_fun,
                T=gv_tf,
            ),
        )
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Observation

    Les valeurs imprimées montrent que la trajectoire respecte bien les conditions imposées.

    Au temps initial, on obtient :

    \[
    x(0) \approx 5,\quad \dot{x}(0) \approx 0,
    \]

    \[
    y(0) = 20,\quad \dot{y}(0) = -1,
    \]

    \[
    \theta(0) \approx -0.3927 = -\frac{\pi}{8},\quad \dot{\theta}(0) \approx 0.
    \]

    Les très petites valeurs autour de \(10^{-16}\) sont simplement des erreurs numériques. On peut donc les considérer comme zéro.

    Au temps final, on obtient :

    \[
    x(t_f) \approx 0,\quad \dot{x}(t_f) \approx 0,
    \]

    \[
    y(t_f) = 1.3333 = \frac{2\ell}{3},
    \quad \dot{y}(t_f) \approx 0,
    \]

    \[
    \theta(t_f) \approx 0,\quad \dot{\theta}(t_f) \approx 0.
    \]

    Donc le booster arrive bien à la position demandée, vertical et pratiquement au repos.

    La variable auxiliaire vérifie aussi :

    \[
    z(0)=-Mg=-1,\qquad z(t_f)=-Mg=-1.
    \]

    Sur le graphe, il faut surtout vérifier que \(z(t)\) reste toujours négatif, car l'inversion `T_inv` suppose \(z<0\). Ici, cette condition est respectée.

    On remarque aussi que l'angle \(\theta(t)\) peut devenir assez grand pendant la trajectoire et se rapprocher de \(\pi/2\). Ce n'est pas forcément une erreur : la trajectoire polynomiale respecte les conditions initiales et finales, mais elle n'est pas optimisée pour minimiser l'inclinaison maximale. Comme le temps final est seulement \(10\) secondes, le booster doit revenir vers la cible assez rapidement, ce qui peut demander une inclinaison importante au milieu du mouvement.

    Les deux dernières valeurs affichées correspondent aux commandes \(f\) et \(\phi\).
    Au début et à la fin, elles restent raisonnables :

    \[
    f(0)\approx 1.011,\quad \phi(0)\approx -0.146,
    \]

    \[
    f(t_f)\approx 1.024,\quad \phi(t_f)\approx 0.217.
    \]

    Sur les graphes, \(x(t)\) revient vers la cible, \(y(t)\) descend vers la hauteur finale, et \(\theta(t)\) revient vers 0.
    L'animation doit donc montrer un booster qui part incliné et décalé à droite, puis descend vers la cible en se redressant progressivement.

    Conclusion : la trajectoire calculée par `compute` respecte bien les conditions initiales et finales. Les petites différences autour de \(10^{-14}\) ou \(10^{-16}\) viennent seulement de la précision numérique.
    """)
    return


if __name__ == "__main__":
    app.run()

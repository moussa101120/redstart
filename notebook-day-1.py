import marimo

__generated_with = "0.23.5"
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

    return np, plt, sci


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
    - the gravity constant $g$ is 10 m/s^2.

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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g = 10 ## pour simplifier g = 10
    M = 1
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Décomposition de la force du réacteur

    Le réacteur est fixé à la **base** du booster et peut pivoter d'un angle $\phi$ par rapport à l'axe du booster. La force qu'il génère, d'amplitude $f \geq 0$, pointe dans une direction faisant un angle $\theta + \phi$ avec la **verticale** (convention antihoraire).

    En projetant sur les axes cartésiens :

    $$f_x = -f\,\sin(\theta + \phi), \qquad f_y = f\,\cos(\theta + \phi)$$

    Le signe $-$ dans $f_x$ découle de la convention : un angle $\theta > 0$ (inclinaison vers la gauche) dévie la poussée vers la gauche ($-x$).
    """)
    return


@app.cell
def _(np):
    def force_components(f, theta, phi):
        fx = -np.sin(theta + phi) * f
        fy = np.cos(theta + phi) * f
        return fx, fy

    return (force_components,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Mouvement du centre de masse (2ème loi de Newton)

    Le booster est soumis à deux forces : la **gravité**  et la **poussée**. Le principe fondamental donne :

    $$M\ddot{x} = f_x = -f\sin(\theta+\phi)$$
    $$M\ddot{y} = f_y - Mg = f\cos(\theta+\phi) - Mg$$

    Ces équations du second ordre décrivent la trajectoire du centre de masse dans le plan vertical.
    """)
    return


@app.cell
def _(M, force_components, g):
    def acceleration_center(f, theta, phi):
        fx, fy = force_components(f, theta, phi)
        ax = fx / M
        ay = fy / M - g
        return ax, ay

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
    ### Moment d'inertie d'une tige homogène

    Le booster est modélisé comme une **tige rigide homogène** de masse $M$ et de longueur $\ell$. Son moment d'inertie par rapport à son centre de masse est :

    $$J = \frac{M\ell^2}{12}$$

    Ce résultat s'obtient en intégrant $J = \int r^2\,dm$ sur toute la tige. Avec $M=1$ kg et $\ell=2$ m, on obtient $J = \tfrac{1}{3}$ kg·m².
    """)
    return


@app.cell
def _(M, l):
    ## le moment d'une tige est ml2/12
    J = (M * (l**2)) / 12
    ## J = 1/3
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
    ### Rotation du booster — théorème du moment cinétique

    On applique le **théorème du moment cinétique** au centre de masse :

    $$J\ddot{\theta} = \sum \mathcal{M}$$

    La gravité agissant au centre de masse, son moment est nul. Seule la poussée du réacteur (situé à $\ell/2$ du centre) contribue. La composante perpendiculaire au bras de levier vaut $f\sin(\phi)$, ce qui donne :

    $$J\ddot{\theta} = -\frac{\ell}{2}\,f\sin(\phi)$$

    Le signe $-$ traduit que $\phi > 0$ (poussée déviée vers la droite) crée un moment **horaire**, réduisant $\theta$.
    """)
    return


@app.cell
def _(J, l, np):
    ## J θ'' = moment total
    ## moment = - (l / 2) f sin(phi)
    ## J θ'' = - (l / 2) f sin(phi)
    def angular_acceleration(f, phi):
        return -(l / 2) * f * np.sin(phi) / J

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
    ### Représentation d'état (state-space)

    Les équations de Newton sont du **second ordre** en $x$, $y$, $\theta$. Pour les résoudre numériquement, on les réécrit en système du **premier ordre** en introduisant les vitesses comme variables :

    | Variable | Signification |
    |---|---|
    | $x,\; v_x = \dot x$ | position et vitesse horizontales |
    | $y,\; v_y = \dot y$ | altitude et vitesse verticales |
    | $\theta,\; \omega = \dot\theta$ | inclinaison et vitesse angulaire |

    L'état complet est $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$ et le champ de vecteurs $F$ s'écrit :

    $$\dot{s} = F(s, f, \phi) = \begin{pmatrix} v_x \\ -f\sin(\theta+\phi)/M \\ v_y \\ f\cos(\theta+\phi)/M - g \\ \omega \\ -(\ell/2)f\sin(\phi)/J \end{pmatrix}$$
    """)
    return


@app.cell
def _(J, M, force_components, g, l, np):
    n = 6
    # On met les positions et les vitesses dans le même vecteur d'état.
    # f et phi ne sont pas dans l'état : ce sont deux commandes.
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s
        fx, fy = force_components(f, theta, phi)

        dx = vx
        dvx = fx / M
        dy = vy
        dvy = fy / M - g
        dtheta = omega
        domega = -(l / 2) * f * np.sin(phi) / J

        return np.array([dx, dvx, dy, dvy, dtheta, domega])


    return (F,)


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


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        def rhs(t, y):
            f,phi = f_phi(t, y)
            return F(y, f, phi)

        result = sci.solve_ivp(
            rhs,
            t_span,
            y0,
            dense_output=True,
        )

        return result.sol


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


@app.cell
def _(g, l, np, plt, redstart_solve):
    def free_fall_example():
        t_span =[0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

        def f_phi(t, y):
            return np.array([0.0, 0.0])  # [f, phi]

        sol = redstart_solve(t_span, y0, f_phi)

        # Vérification que sol accepte un temps seul et aussi un tableau de temps.
        assert sol(0.0).shape == (6,)
        assert sol(np.array([0.0, 1.0])).shape == (6, 2)

        # Théorie : y(t) = 10 - (1/2) g t^2.
        # On cherche y(t) = l.
        t_cross = np.sqrt(2 * (10 - l) / g)

        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.axvline(t_cross, color="grey", ls=":", label=fr"$t \approx {t_cross:.3f}$ s")
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
    mo.md(r"""
    ###Synthèse d'une loi de poussée

    Avec $\phi = 0$ et $\theta = 0$, le mouvement vertical est régi par $\ddot{y} = f(t)/M - g$. On cherche $f(t)$ tel que, partant de $(y_0, \dot y_0) = (10, -2)$, on atteigne $(y(5), \dot y(5)) = (\ell/2, 0)$.

    On choisit une **accélération affine** $\ddot{y}(t) = a_0 + a_1 t$, ce qui donne par intégration :

    $$y(t) = y_0 + \dot y_0\,t + \frac{a_0}{2}t^2 + \frac{a_1}{6}t^3$$

    Les deux conditions en $t = 5$ s forment un système $2 \times 2$ permettant de déterminer $a_0$ et $a_1$ de façon unique, et la poussée vaut alors :

    $$f(t) = M\bigl(g + a_0 + a_1 t\bigr)$$
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):
    # On cherche une accélération verticale a(t) = a0 + a1 t.
    # Conditions : y(0)=10, vy(0)=-2, y(5)=1, vy(5)=0.
    # Une solution est : a(t) = -0.56 + 0.384 t.
    # Comme y'' = f/M - g avec phi=0, on prend f(t)=M(g+a(t)).
    def controlled_force(t):
        a = -0.56 + 0.384 * t
        return M * (g + a)

    def controlled_landing():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([controlled_force(t), 0.0])

        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        values = sol(t)
        y_t = values[2]
        vy_t = values[3]
        f_t = np.array([controlled_force(tt) for tt in t])

        print("y(5)  =", sol(5.0)[2])
        print("vy(5) =", sol(5.0)[3])

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$")
        plt.axhline(l / 2, color="grey", linestyle="--", label=r"target $y=\ell/2$")
        plt.xlabel("time $t$")
        plt.ylabel("height $y(t)$")
        plt.title("Controlled landing: height")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(t, vy_t, label=r"$v_y(t)$")
        plt.axhline(0, color="grey", linestyle="--", label=r"target $v_y=0$")
        plt.xlabel("time $t$")
        plt.ylabel("vertical velocity $v_y(t)$")
        plt.title("Controlled landing: vertical velocity")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(t, f_t, label=r"$f(t)$")
        plt.xlabel("time $t$")
        plt.ylabel("force $f(t)$")
        plt.title("Controlled landing: thrust")
        plt.grid(True)
        plt.legend()
        plt.show()

    controlled_landing()
    return (controlled_force,)


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

    return (svg,)


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


@app.cell
def _():
    def _svg_join(objects):
        return "\n".join(str(obj) for obj in objects if obj is not None)

    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        width = x_max - x_min
        height = y_max - y_min

        sky_y = max(0, y_min)
        sky_h = max(0, y_max - sky_y)
        ground_y = y_min
        ground_h = max(0, min(0, y_max) - y_min)
        extra = _svg_join(objects)

        return f'''
    <svg width="300" height="300" viewBox="{x_min} {-y_max} {width} {height}" xmlns="http://www.w3.org/2000/svg">
      <g transform="scale(1,-1)">
        <rect x="{x_min}" y="{sky_y}" width="{width}" height="{sky_h}" fill="#dff3ff" />
        <rect x="{x_min}" y="{ground_y}" width="{width}" height="{ground_h}" fill="#d2b48c" />
        <rect x="-1" y="-0.05" width="2" height="0.10" fill="green" />
        {extra}
        <rect x="{x_min}" y="{y_min}" width="{width}" height="{height}" fill="none" stroke="black" stroke-width="0.02" />
      </g>
    </svg>
    '''


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
            ),
        ],
        justify="space-around",
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


@app.cell
def _(M, g, l, np):
    def _points_to_svg(points):
        return " ".join(f"{float(px):.6f},{float(py):.6f}" for px, py in points)
    def booster(x, y, theta, f, phi):
        body_width = 0.20
        e_axis =np.array([-np.sin(theta), np.cos(theta)])
        e_perp = np.array([np.cos(theta), np.sin(theta)])
        center =np.array([x, y])
        top = center + (l / 2) * e_axis
        base= center - (l / 2) * e_axis
        p1 = top+ (body_width / 2) * e_perp
        p2 = top - (body_width / 2) * e_perp
        p3 = base -(body_width / 2) * e_perp
        p4 = base + (body_width / 2) * e_perp
        body = f'<polygon points="{_points_to_svg([p1, p2, p3, p4])}" fill="white" stroke="black" stroke-width="0.03" />'



        flame = ""
        flame_length = (l / 2) * max(0.0, float(f)) / (M * g)
        if flame_length > 1e-12:
            force_dir = np.array([ -np.sin(theta + phi), np.cos(theta + phi)])
            flame_dir = -force_dir
            flame_perp = np.array([flame_dir[1], -flame_dir[0]])
            flame_width = 0.18
            q1 = base + (flame_width / 2) * flame_perp
            q2 = base - (flame_width / 2) * flame_perp
            q3 = base + flame_length * flame_dir
            flame = f'<polygon points="{_points_to_svg([q1, q2, q3])}" fill="orange" stroke="red" stroke-width="0.02" />'
        return f"<g>{flame}{body}</g>"

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l / 2, 0, 0, 0),
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
                    booster(-l / 2, l, np.pi / 4, 2 * M * g, np.pi / 2),
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
    mo.md(r"""
    Pour animer le booster, on calcule plusieurs positions successives.
    Chaque position est dessinée comme une image SVG différente.
    L’animation affiche ces images l’une après l’autre.
    """)
    return


@app.cell
def _(booster, np):
    def booster_anim(x, y, theta, f, phi, T=5.0, frames=80):
        times = np.linspace(0.0, T, frames, endpoint=False)
        key_times = ";".join(f"{i / frames:.6f}" for i in range(frames)) + ";1"
        groups = []

        for i, tt in enumerate(times):
            values = ["0"] * frames + ["0"]
            values[i] = "1"
            if i == 0:
                values[-1] = "1"

            values= ";".join(values)


            frame_svg = booster(
                float(x(tt)),
                float(y(tt)),
                float(theta(tt)),
                float(f(tt)),
                float(phi(tt)),
            )
            groups.append(f'''
    <g opacity="0">
      <animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{key_times}" values="{values}" />
      {frame_svg}
    </g>
    ''')
        return "\n".join(groups)

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np, world):
    def booster_anim_0():
        T = 5.0

        def x(t):
            return -l / 2 + l * (t / T)

        def y(t):
            return l / 2 + l / 2 * (t / T)

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


@app.cell
def _(M, booster_anim, controlled_force, g, mo, np, redstart_solve, world):
    def simulation_animation(f_phi, y0, title, T=5.0):
        sol = redstart_solve([0.0, T], y0, f_phi)

        def x(t):
            return sol(t)[0]
        def y(t):
            return sol(t)[2]
        def theta(t):
            return sol(t)[4]
        def f(t):
            return f_phi(float(t), sol(float(t)))[0]
        def phi(t):
            return f_phi(float(t), sol(float(t)))[1]
        return mo.Html(
            f"<h3>{title}</h3>"
            + world(
                [-6, 6, -2, 12],
                booster_anim(x, y, theta, f, phi, T=T),
            )
        )

    # 1. Free fall: f = 0 and phi = 0
    def f_phi_1(t, y):
        return np.array([0.0, 0.0])


    # 2. Vertical thrust: f = Mg and phi = 0
    def f_phi_2(t, y):
        return np.array([M * g, 0.0])


    # 3. Tilted thrust: f = Mg and phi = pi/8
    def f_phi_3(t, y):
        return np.array([M * g, np.pi / 8])


    # 4. Controlled landing
    def f_phi_4(t, y):
        return np.array([controlled_force(t), 0.0])


    y0_1 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
    y0_2 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
    y0_3 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
    y0_4 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

    mo.vstack(
        [
            simulation_animation(f_phi_1, y0_1, "1. Free fall: f = 0, phi = 0"),
            simulation_animation(f_phi_2, y0_2, "2. Vertical thrust: f = Mg, phi = 0"),
            simulation_animation(f_phi_3, y0_3, "3. Tilted thrust: f = Mg, phi = pi/8"),
            simulation_animation(f_phi_4, y0_4, "4. Controlled landing"),
        ]
    )
    return


if __name__ == "__main__":
    app.run()

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    
    fig, ax = plt.subplots()

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.set_facecolor('0.2')

    sun = plt.Circle((0, 0), 1, color='yellow')
    moon = plt.Circle((-2, 0), 0.97, color='0.1')

    ax.add_artist(sun)
    ax.add_artist(moon)

    frames = np.concatenate(
        [
            np.linspace(-2, -1, 20, endpoint=False),
            np.linspace(-1, -.5, 50, endpoint=False),
            np.linspace(-.5, 0, 75, endpoint=False),
            np.linspace(0, 0, 10, endpoint=False),
            np.linspace(0, 0.5, 75, endpoint=False),
            np.linspace(0.5, 1, 50, endpoint=False),
            np.linspace(1, 2, 50)
        ]
    )

    def animate(i):
        x = frames[i]

        moon.center = (x, 0)
        return moon,

    ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=50, blit=True)

    plt.show()



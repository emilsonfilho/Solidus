import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def createAnimation(X, Y, Z, n, interval=50):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = [ax.plot_surface(X[:0,:], Y[:0,:], Z[:0,:], alpha=0.8, color='blue')]
    
    def init():
        ax.set_xlim(X.min(), X.max())
        ax.set_ylim(Y.min(), Y.max())
        ax.set_zlim(Z.min(), Z.max())
        return surf

    def update(frame):
        for s in surf:
            s.remove()
        surf.clear()
        
        s = ax.plot_surface(X[:frame,:], Y[:frame,:], Z[:frame,:], alpha=0.8, color='blue')
        surf.append(s)
        return surf

    ani = FuncAnimation(fig, update, frames=n+1, init_func=init, 
                       blit=False, interval=16, repeat=False)
    
    return ani

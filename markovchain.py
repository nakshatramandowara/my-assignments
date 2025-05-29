import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Use interactive TkAgg backend\ nmatplotlib.use('tkagg')

# --- Finite Random Walk: States -a to b ---
a = 4  # negative bound
b = 5  # positive bound
states = np.arange(-a, b+1)
n_states = len(states)

# Transition matrix: absorbing at endpoints, 0.5 move left/right elsewhere
P = np.zeros((n_states, n_states))
p = 0.5
for i in range(n_states):
    if i == 0 or i == n_states - 1:
        P[i, i] = 1.0
    else:
        P[i, i - 1] = p
        P[i, i + 1] = 1 - p

# Initial distribution: start at state 0 (find its index)
pi = np.zeros(n_states)
start_index = np.where(states == 0)[0]
if start_index.size:
    pi[start_index[0]] = 1.0
else:
    pi[0] = 1.0  # default to first if 0 is out of range

# Colormap
cmap = plt.cm.viridis

# --- Plot Setup ---
fig, ax = plt.subplots(figsize=(12, 4))
manager = plt.get_current_fig_manager()
# Maximize window
try:
    manager.window.state('zoomed')
except Exception:
    try:
        manager.window.attributes('-zoomed', True)
    except Exception:
        fig.canvas.manager.full_screen_toggle()

ax.set_aspect('equal')
plt.axis('off')

# Layout: horizontal units
positions = [(s, 0) for s in states]
base_radius = 0.2
circles, texts = [], []
for i, (x, y) in enumerate(positions):
    color = cmap(pi[i])
    radius = base_radius + 0.3 * pi[i]
    circ = patches.Circle((x, y), radius, fill=True, color=color, ec='black')
    ax.add_patch(circ)
    txt = ax.text(x, y, f'{pi[i]:.2f}', ha='center', va='center', color='white')
    circles.append(circ)
    texts.append(txt)

# Center axes
ax.set_xlim(-a - 1, b + 1)
ax.set_ylim(-1, 1)
plt.title(f"Finite Random Walk ({-a} to {b}): Press Enter for Next Step")

# --- Update Function ---
def update():
    global pi
    pi = pi @ P
    for i, circ in enumerate(circles):
        circ.set_facecolor(cmap(pi[i]))
        circ.set_radius(base_radius + 0.5 * pi[i])
        texts[i].set_text(f'{pi[i]:.2f}')
    fig.canvas.draw()

# --- Key Press Handler ---
def on_key(event):
    if event.key == 'enter':
        update()

fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()

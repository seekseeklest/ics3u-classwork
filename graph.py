import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return 5 * x

def f_inverse(x):
    return x / 5

# Create an array of x values
x = np.linspace(-10, 10, 400)
y1 = f(x)
y2 = f_inverse(x)

# Set up the plot
plt.figure(figsize=(8, 8))

# Plot f(x)
plt.plot(x, y1, label='f(x) = 5x', color='blue')
# Plot f_inverse(x)
plt.plot(x, y2, label='f⁻¹(x) = x/5', color='red')

# Plot the line of symmetry y = x
plt.plot(x, x, label='y = x', color='green', linestyle='--')

# Set the limits
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Add grid, labels, and legend
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Function and its Inverse')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
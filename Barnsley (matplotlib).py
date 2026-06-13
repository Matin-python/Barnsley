import numpy as np
import matplotlib.pyplot as plt

formulas = ['formula1', 'formula2', 'formula3', 'formula4']
probabilities = [0.02, 0.15, 0.13, 0.7]

x, y = 0.0, 0.0

n_iterations = 50000
burn_in = 1000

points = []

for i in range(n_iterations + burn_in):
    selected = np.random.choice(formulas, p=probabilities)
    
    if selected == 'formula1':
        new_x = (0.5)
        new_y = (0.27 * y)
    elif selected == 'formula2':
        new_x = ((-0.14) * x) + (0.26 * y) + 0.57 
        new_y = (0.25 * x) + (0.22 * y) + (-0.04) 
    elif selected == 'formula3':
        new_x = (0.17 * x) + ((-0.21) * y) + (0.41) 
        new_y = (0.22 * x) + (0.18 * y) + (0.09)
    elif selected == 'formula4':
        new_x = (0.78 * x) + (0.03 * y) + (0.11)
        new_y = ((-0.03) * x) + (0.74 * y) + (0.27)
    
    x, y = new_x, new_y
    
    if i >= burn_in:  # Only store after burn-in
        points.append((x, y))

points = np.array(points)
plt.figure(figsize=(4, 7))
plt.scatter(points[:, 0], points[:, 1], s=0.3, c='green', alpha=0.6)
plt.axis('off')
plt.show()

import numpy as np
import turtle 

formulas = ['formula1', 'formula2', 'formula3', 'formula4']
probabilities = [0.02, 0.15, 0.13, 0.7]
x = 0.0
y = 0.0
turtle.speed(1000000)
enter = 10000
for i in range (enter):
    selected_formula = np.random.choice(formulas, p=probabilities)

    if selected_formula == 'formula1':
        new_x = (0.5)
        new_y = (0.27 * y)
    elif selected_formula == 'formula2':
        new_x = ((-0.14) * x) + (0.26 * y) + 0.57 
        new_y = (0.25 * x) + (0.22 * y) + (-0.04) 
    elif selected_formula == 'formula3':
        new_x = (0.17 * x) + ((-0.21) * y) + (0.41) 
        new_y = (0.22 * x) + (0.18 * y) + (0.09)
    elif selected_formula == 'formula4':
        new_x = (0.78 * x) + (0.03 * y) + (0.11)
        new_y = ((-0.03) * x) + (0.74 * y) + (0.27)

    x = new_x
    y = new_y
    
    turtle.penup()
    turtle.goto(x * 300, y * 300)
    turtle.pendown()
    turtle.dot(3, 'green')

turtle.done()
print('END')

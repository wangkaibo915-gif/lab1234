import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5,5))

left_center = (-0.7, 0.5)
left_radius = 0.7
left_start_angle = np.radians(270)  
left_end_angle = np.radians(360)   

right_center = (0.7, 0.5)
right_radius = 0.7
right_start_angle = np.radians(180)   
right_end_angle = np.radians(270)    

def arc_points(center, radius, start_angle, end_angle, num_points=100):
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y

x_left, y_left = arc_points(left_center, left_radius, left_start_angle, left_end_angle)
x_right, y_right = arc_points(right_center, right_radius, right_start_angle, right_end_angle)

ax.plot(x_left, y_left, color='black', linewidth=8) 
ax.plot(x_right, y_right, color='black', linewidth=8) 

ax.set_aspect('equal')  
ax.set_xlim(-2, 2)       
ax.set_ylim(-2, 2)       
ax.axis('off')          

plt.show()
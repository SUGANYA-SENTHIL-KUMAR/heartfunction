import numpy as np
import matplotlib.pyplot as plt

def heart_silhouette():
    m = np.linspace(0, 2 * np.pi, 1000)
    
    a = []
    b = []
    
    for value in m:
        a.append(16 * (np.sin(value) ** 3))
        b.append(13 * np.cos(value) - 5 * np.cos(2 * value) - 2 * np.cos(3 * value) - np.cos(4 * value))
    
    plt.figure(figsize=(6, 6))
    plt.plot(a, b, color='black', linewidth=3)
    plt.axhline(0, color='gray', linewidth=0.5) 
    plt.axvline(0, color='gray', linewidth=0.5) 
    plt.xlabel("X-axis")  
    plt.ylabel("Y-axis")  
    plt.axis("equal")
    plt.show()

heart_silhouette()

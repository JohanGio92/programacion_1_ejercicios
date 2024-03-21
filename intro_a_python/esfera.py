import math

def calculate_esphere_volume(radius):
    return 4/3 * math.pi * math.pow(radius, 3)

radius = input('enter the radius of the sphere: ')
radius = float(radius)

print(calculate_esphere_volume(radius))

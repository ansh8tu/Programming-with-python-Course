# This is a Python Program to find the volume of a tetrahedron 
import math 
def vol_tetra(side): 
    volume = (side ** 3 / (6 * math.sqrt(2))) 
    return round(volume, 2) 
  
# Driver Code 
side = 3
vol = vol_tetra(side) 
print(vol)

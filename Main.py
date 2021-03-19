import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt

#Task 1
A = np.array([[ 3, 1 ],[ 2, 6]])
B = np.array([[ -1, 4 ],[ 3, 8]])
#(A)
print(A.T)
print("\n")
#(B)
print(B.T)
print("\n")
#(C)
AB = A @ B
print(AB)
print("\n")
print(A * B)
print("\n")
#(D)
print(AB.T)
print("\n")
print(B.T@A.T)
print("\n")
#(F)
print((A.T).T)
print("\n")
#(G)
print(A@A.T)
print("\n")

#Task 2 - Ive added 2 so you know its A of task 2 and B of task 2 in the variable name
A2 = np.array([[ 2, 1 ],[ 3, 2]])
B2 = np.array([[ 1, 2 ],[ 3, 4]])

#(A)
print(A2@B2)
print("\n")
#(B)
print(B2@A2)
print("\n")

#Task 3
#(A)
print(inv(A2))
print("\n")
#(B)
print(inv(B2))
print("\n")
#(C)
print(A2@inv(A2))
print("\n")
#(D)
print(inv(A2)@A2)
print("\n")
#(E)
#Tell numpy to not use float, but round them as int
np.set_printoptions(suppress=True)
print(B2@inv(B2))
print("\n")
#(F)
print(inv(B2)@B2)
print("\n")

#Task 4
A4 = np.array([[ 2, 4 ],[ 1, 2]])
#Uncomment this print to see the result, You will get a LinAlgError because the matrix cannot be inverted because its determinant is 0
#print(inv(A4))

#Task 5
xs = np.array([0,0,3,3,0,1.5,3])# List of x coordinates
ys = np.array([1,0,0,1,1,2 ,1])# List of y coordinates

fig = plt.figure()
fig, ax = plt.subplots()

xs_ys = np.array([xs,ys])
ax.axis('equal')

# Plot the points
ax.plot( *xs_ys, '-', color='b')

#Create a rotation matrix

rot = np.array([[1, -1],[1, 1]])# <-- CHANGE THIS

# turn the two lists (xs, ys) into a list of (x,y) tuples
points = np.array([[x,y] for x,y in zip(xs,ys)])

# Make the transformation:
points_rot = (points @ rot)

# Turn it into a row of xs and a row of ys:
xs_ys_rot = np.array([points_rot[:,0], points_rot[:,1]])

# Finally, plot it
ax.plot( *xs_ys_rot, '-', color='r')
fig.show()
fig.savefig('rotatedFigure.png')
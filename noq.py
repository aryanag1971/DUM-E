import numpy as np
r=2
c=2
mat=list(map(float,input().split())) #taking input as x0 y0 x2 y2
l1=float(input())
l2=float(input())
cordi=np.array(mat).reshape(r,c) 
cos2=((cordi[1,0]-cordi[0,0])**2+(cordi[1,1]-cordi[0,1])**2-l1**2-l2**2)/(2*l1*l2) #costheta2=(x2-x0)^2+(y2-y0)^2-l1^2-l2^2/2*l1*l2
if(cos2>1):
  cos2=1
theta2=np.arccos(cos2)
theta=np.arctan((cordi[1,1]-cordi[0,1])/(cordi[1,0]-cordi[0,0]))# theta=theta1+theta2
theta1=theta-theta2
x1=l1*np.cos(theta1)
y1=l1*np.sin(theta1)
print(theta2)
print(x1)
print(y1)


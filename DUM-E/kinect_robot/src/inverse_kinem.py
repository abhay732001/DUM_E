import numpy as np
import math as m

pos0=[]
pos2=[]
length1=float(input())
length2=float(input())
for i in (0,1)
  pos0.append(float(input()))
for i in (0,1)
  pos2.append(float(input()))
pos0=np.asarray(pos0)
pos2=np.asarray(pos2)
offset=pos0
pos2=pos2-pos0
pos0=pos0-pos0
length3=(pos2[0]**2+pos2[1]**2)**0.5
theta2=m.acos(length1**2+length2**2-length3**2)/(2*length1*length2)
beta=m.atan(pos2[1]/pos2[0])
gamma=m.atan(length2*sin(theta2))/(length1+length2*cos(theta2))
theta1=beta-gamma
pos1=np.zeros(2)
pos1[0]=length1*cos(theta1)
pos1[1]=length1*sin(theta1)
pos1=pos1-pos0

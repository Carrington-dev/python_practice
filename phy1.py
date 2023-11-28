#vx_i = 3.2 
#delta_t = 1.9
#ax = -9.8

#delta_x = vx_i * delta_t + (1/2)*ax *((delta_t)**2)
#print(delta_x)


from matplotlib.pyplot import *

X=[1.0,1.5,2.2,2.8,3.4,3.8,4.4,4.8,4.8,4.8,4.8,4.8,4.6,4.4,4.2,4,3.8,3.6,3.4]
T=[0.00,0.33,0.67,1.00,1.33,1.67,2.00,2.33,2.67,3.00,3.33,3.67,4.00,4.33,4.67,5.00,5.33,5.67,6.00]
V_Ave=[]
n=0

while n < (len(X)-1):
  delta_x = X[n+1] - X[n]
  # delta_xn =X[n+1]-X[n]
  delta_t = T[n+1] - T[n]
  
  vx = delta_x / delta_t
  V_Ave.append(vx)
  
  
  n += 1



plot(T[1:],V_Ave,"go")

xlabel('t')
ylabel('v')

title("Plot of average velocity (m/s) vs t(s)")

show()

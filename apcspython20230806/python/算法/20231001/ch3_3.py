x = 2
fx = 0
ploy1 = [3,2,2,-3,1,1,0]
for j in range(ploy1[0]):
   fx +=  ploy1[2*j+1]*x**ploy1[2*(j+1)]
print(fx)

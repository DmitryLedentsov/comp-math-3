import numpy as np
from math import *
def f(x):
    return 2*(x**3)-9*x*x-7*x+11
I_ANSWER=-44 #точный ответ
N=5 # из условия
a=1 #интервалы
b=3
h = (b-a)/N
ACCURACY = 2 #точность округления
xi = [round(i,1) for i in np.arange(a,b+h,h)]
Fxi = [round(f(x),ACCURACY) for x in xi]

C_0_5 = 19*(b-a)/288
C_1_4 = 25*(b-a)/96
C_2_3 = 25*(b-a)/144

C_0_5 = round(C_0_5,ACCURACY)
C_1_4 = round(C_1_4, ACCURACY)
C_2_3 = round(C_2_3,ACCURACY)
Ci= [C_0_5, C_1_4, C_2_3, C_2_3, C_1_4, C_0_5]
print("xi ", xi)
print("Fxi ", Fxi)
print("Ci ", Ci)

I = [round(Fxi[i]*Ci[i],ACCURACY) for i in range(0,N+1)]

print("сетод ньютона котеса")
print("I = ",end="")
for i in I:
    print(i, " + ", end="")
print("\n","I = ", sum(I))
print("")

print("метод средних")
xi_1_2 =[round((xi[i-1] + xi[i])/2, ACCURACY) for i in range(1,N+1) ]
Fxi_1_2 = [round(f(xi_1_2[i]), ACCURACY) for i in range(0, len(xi_1_2))]
print("xi-1/2 ", xi_1_2)
print("Fxi-1/2", Fxi_1_2)

I= h*sum(Fxi_1_2)
delta_I = abs(round(I_ANSWER-I,ACCURACY))
print("I = ", I, "delta_I = ", delta_I, "~", round(delta_I/abs(I_ANSWER)*100,ACCURACY), "%")

print("")

print("метод трапеций")
I = h*((Fxi[0] + Fxi[N])/2 + sum([Fxi[i] for i in range(1,N)]))
delta_I = abs(round(I_ANSWER-I,ACCURACY))
print("I = ", I, "delta_I = ", delta_I, "~", round(delta_I/abs(I_ANSWER)*100,ACCURACY), "%")

print("")
print("метод Симпсона")
s1 = [Fxi[i] for i in range(0,N,2)]
s2 = [Fxi[i] for i in range(1,N,2)]
print(s1,s2,Fxi[N])
I = h/3* (Fxi[0] + 4* sum(s1) + 2*sum(s2) + Fxi[N])
I=round(I,ACCURACY)
delta_I = abs(round(I_ANSWER-I,ACCURACY))
print("I = ", I, "delta_I = ", delta_I, "~", round(delta_I/abs(I_ANSWER)*100,ACCURACY), "%")


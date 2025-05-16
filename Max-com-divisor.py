def Maximo_Comun_Divisor(A,R):

  if A<R:
    R,A=A,R
  D=A%R
  
  if D==0:
    return R
    
  else:
    return Maximo_Comun_Divisor(R,D)

A=int(input('Introduzca el primer valor: '))
R=int(input('Introduzca el segundo valor: '))
print(str(Maximo_Comun_Divisor(A,R)))
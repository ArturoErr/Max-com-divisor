-----------------------------------------------------------------------------------------------------------------------------------
Descripción

Este script en Python calcula el Máximo Común Divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides recursivo.

Contenido del archivo

Max-com-divisor.py: Código fuente que solicita al usuario ingresar dos valores y muestra el MCD.

----------------------------------------------------------------------------------------------------------------------------------
Requisitos

Python 3.x instalado en el sistema.

Uso

Clona el repositorio o descarga el archivo Max-com-divisor.py.

git clone <URL-del-repositorio>
cd <directorio-del-repositorio>

Ejecuta el script con Python:

python Max-com-divisor.py

Ingresa los dos números enteros cuando se te solicite:

Introduzca el primer valor: 48
Introduzca el segundo valor: 18

El programa mostrará el resultado:

6

-----------------------------------------------------------------------------------------------------------------------------------
Explicación del algoritmo

El algoritmo de Euclides para calcular el MCD funciona de la siguiente manera:

Dado dos números A y R, si A es menor que R, se intercambian.

Se calcula el resto D = A % R.

Si D es 0, entonces R es el MCD.

En caso contrario, se llama recursivamente a la función con los valores R y D.

-----------------------------------------------------------------------------------------------------------------------------------

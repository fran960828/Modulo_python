{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ¿Qué es la recursividad?\n",
    "La recursividad es un enfoque de resolución de problemas donde una función se llama a sí misma para abordar problemas más pequeños del mismo tipo. Es similar a la idea de un bucle, pero en lugar de iterar, se resuelven subproblemas a través de llamadas recursivas."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Características de las funciones recursivas:\n",
    "Deben tener un caso base: Un caso base es cuando la función deja de llamarse a sí misma y devuelve un resultado directamente.\n",
    "Deben acercarse al caso base: En cada llamada recursiva, el problema debe acercarse a una instancia más pequeña hasta que se alcance el caso base.\n",
    "Deben asegurar convergencia: Es importante asegurarse de que las llamadas recursivas eventualmente alcancen el caso base y no entren en un bucle infinito"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Ejemplo de una función recursiva: Factorial\n",
    "El factorial de un número entero positivo n, denotado por n!, es el producto de todos los números enteros positivos desde 1 hasta n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "def factorial(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n * factorial(n - 1)\n",
    "print(factorial(5))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Explicación:\n",
    "En esta función, el caso base es cuando n es igual a 0 o 1, en cuyo caso, se devuelve 1 directamente (el factorial de 0 y 1 es 1).\n",
    "Si n no es igual a 0 o 1, la función se llama a sí misma con el argumento n - 1.\n",
    "En cada llamada recursiva, se reduce el valor de n en uno, acercándose así al caso base.\n",
    "La multiplicación n * factorial(n - 1) se realiza en cada llamada recursiva, y el resultado final es el factorial de n."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Consideraciones finales:\n",
    "Las funciones recursivas pueden ser poderosas, pero también pueden ser ineficientes en términos de uso de memoria y tiempo de ejecución.\n",
    "En problemas que pueden resolverse de manera más eficiente con iteración o enfoques no recursivos, es preferible utilizar esas soluciones."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "cblocks",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

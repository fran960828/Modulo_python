{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1. Crea un array_1 lleno ceros con una longitud de 8 elementos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "# realizar los import\n",
    "import numpy as np\n",
    "\n",
    "# crear array\n",
    "array_1 = np.zeros(8)\n",
    "print(array_1)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Haz que todos los elementos de este array sean igual a 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array modificado  [2. 2. 2. 2. 2. 2. 2. 2. 2.]\n"
     ]
    }
   ],
   "source": [
    "# realizar los import\n",
    "import numpy as np\n",
    "\n",
    "# crear array\n",
    "array_1 = np.zeros(8)\n",
    "print(\"array original \", array_1)\n",
    "\n",
    "# cambiar valores a 2\n",
    "array_1[:] = 2\n",
    "print(\"array modificado \", array_1)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Crea un array_2 que contenga todos los números pares del 1 al 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  4  6  8 10]\n"
     ]
    }
   ],
   "source": [
    "# realizar los import\n",
    "import numpy as np\n",
    "\n",
    "# creamos el array\n",
    "array_2 = np.arange(2,11,2)\n",
    "print(array_2)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4. Suma todos los elementos del array_2 usando un bucle y después usando un método de numpy. Compara los resultados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Suma usando un bucle: 30\n",
      "Suma usando NumPy: 30\n",
      "Los resultados son iguales\n"
     ]
    }
   ],
   "source": [
    "# realizando los import\n",
    "import numpy as np\n",
    "\n",
    "array_2 = np.arange(2,11,2)\n",
    "\n",
    "# sumar elementos usando un bucle\n",
    "suma_bucle = 0\n",
    "for numero in array_2:\n",
    "    suma_bucle = suma_bucle + numero\n",
    "print(\"Suma usando un bucle:\", suma_bucle)\n",
    "\n",
    "# suma usando NumPy\n",
    "suma_numpy = np.sum(array_2)\n",
    "print(\"Suma usando NumPy:\", suma_numpy)\n",
    "\n",
    "# comparar los resultados\n",
    "if suma_bucle == suma_numpy:\n",
    "    print(\"Los resultados son iguales\")\n",
    "else:\n",
    "    print(\"Los resultados son diferentes\")\n",
    "\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 5. Revierte array_2 y guárdalo en una variable independiente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array original: [ 2  4  6  8 10]\n",
      "Array revertido: [10  8  6  4  2]\n",
      "Array revertido nuevo: [2 2 2 2 2]\n",
      "Array original nuevo: [ 2  4  6  8 10]\n"
     ]
    }
   ],
   "source": [
    "# realizando los import\n",
    "import numpy as np\n",
    "\n",
    "# creamos array original\n",
    "array_2 = np.arange(2,11,2)\n",
    "print(\"Array original:\", array_2)\n",
    "\n",
    "# creamos array revertido independiente\n",
    "#inicializacion\n",
    "array_2_revertido = np.zeros(len(array_2), dtype=int)\n",
    "#asigacion de valores\n",
    "array_2_revertido[:] = array_2[::-1]\n",
    "print(\"Array revertido:\", array_2_revertido)\n",
    "\n",
    "# comprobamos que son independientes\n",
    "array_2_revertido[:] = 2\n",
    "print(\"Array revertido nuevo:\", array_2_revertido)\n",
    "print(\"Array original nuevo:\", array_2)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_2_revertido"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2. 2. 2. 2. 2. 2. 2. 2.]\n",
      "[ 2  4  6  8 10]\n",
      "[10  8  6  4  2]\n",
      "Elementos comunes entre array_1 y array_2: [2.]\n",
      "Elementos comunes entre array_2 y array_2_revertido: [ 2  4  6  8 10]\n"
     ]
    }
   ],
   "source": [
    "# realizando los import\n",
    "import numpy as np\n",
    "\n",
    "# nuestros arrays\n",
    "array_2 = np.arange(2,11,2)\n",
    "array_2_revertido = np.zeros(len(array_2), dtype=int)\n",
    "array_2_revertido[:] = array_2[::-1]\n",
    "array_1 = np.zeros(8)\n",
    "array_1[:] = 2\n",
    "\n",
    "print(array_1)\n",
    "print(array_2)\n",
    "print(array_2_revertido)\n",
    "\n",
    "# Elementos comunes con array_1 y array_2\n",
    "interseccion_1 = np.intersect1d(array_1, array_2)\n",
    "print(\"Elementos comunes entre array_1 y array_2:\", interseccion_1)\n",
    "\n",
    "\n",
    "# Elementos comunes con array_2 y array_2_revertido\n",
    "interseccion_2 = np.intersect1d(array_2, array_2_revertido)\n",
    "print(\"Elementos comunes entre array_2 y array_2_revertido:\", interseccion_2)\n",
    "\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 7. Crea un arrays lleno de 1s con una longitud dada por el usuario"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 1. 1. 1. 1. 1. 1. 1.]\n"
     ]
    }
   ],
   "source": [
    "# realizar los import\n",
    "import numpy as np\n",
    "\n",
    "# pedir longitud al usuario\n",
    "longitud = int(input(\"Ingrese la longitud del array: \"))\n",
    "# cremaos array\n",
    "array_unos = np.ones(longitud)\n",
    "print(array_unos)\n"
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

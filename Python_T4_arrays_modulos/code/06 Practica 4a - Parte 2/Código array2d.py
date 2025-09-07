{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1. Crea un arrays lleno de 1s con una longitud dada por el usuario"
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
      "[1. 1. 1. 1. 1. 1. 1. 1. 1.]\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "longitud = int(input(\"Ingrese la longitud del array: \"))\n",
    "array_ones = np.ones(longitud)\n",
    "print(array_ones)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)"
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
      "[1. 1. 1. 1. 1. 1. 1. 1. 1.]\n",
      "Array con nueva forma: \n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "# pedir longitud del array\n",
    "longitud = int(input(\"Ingrese la longitud del array: \"))\n",
    "# crear array\n",
    "array_ones = np.ones(longitud)\n",
    "print(array_ones)\n",
    "\n",
    "# Pidiendo al usuario la nueva forma del array\n",
    "filas = int(input(\"Ingrese la cantidad de filas: \"))\n",
    "columnas = int(input(\"Ingrese la cantidad de columnas:\"))\n",
    "\n",
    "# comprobamos que el reshape es posible\n",
    "if filas * columnas == longitud:\n",
    "    # realizamos el reshape\n",
    "    nuevo_array = np.reshape(array_ones, (filas,columnas))\n",
    "    print(\"Array con nueva forma: \\n\", nuevo_array)\n",
    "else:\n",
    "    # indicamos que el reshape no es posible\n",
    "    print(\"La cantidad de filas y columnas no es compatible con la longitud del array\")\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)"
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
      "[1. 1. 1. 1. 1. 1.]\n",
      "Array con nueva forma: \n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]]\n",
      "No se puede crear una matriz identidad con diferente numero de filas que de columnas\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "# pedir longitud del array\n",
    "longitud = int(input(\"Ingrese la longitud del array: \"))\n",
    "# crear array\n",
    "array_ones = np.ones(longitud)\n",
    "print(array_ones)\n",
    "\n",
    "# Pidiendo al usuario la nueva forma del array\n",
    "filas = int(input(\"Ingrese la cantidad de filas: \"))\n",
    "columnas = int(input(\"Ingrese la cantidad de columnas:\"))\n",
    "\n",
    "# comprobamos que el reshape es posible\n",
    "if filas * columnas == longitud:\n",
    "    # realizamos el reshape\n",
    "    nuevo_array = np.reshape(array_ones, (filas,columnas))\n",
    "    print(\"Array con nueva forma: \\n\", nuevo_array)\n",
    "\n",
    "    if filas == columnas:\n",
    "        matriz_identidad = np.eye(filas)\n",
    "        print(\"Matriz identidad:\\n\", matriz_identidad)\n",
    "    else: \n",
    "        print(\"No se puede crear una matriz identidad con diferente numero de filas que de columnas\")\n",
    "\n",
    "else:\n",
    "    # indicamos que el reshape no es posible\n",
    "    print(\"La cantidad de filas y columnas no es compatible con la longitud del array\")\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4. Concatena ambas estructuras horizontalmente y verticalmente"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 1. 1. 1. 1. 1. 1. 1. 1.]\n",
      "Array con nueva forma: \n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]]\n",
      "Matriz identidad:\n",
      " [[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n",
      "\n",
      "Concatenacion horizontal:\n",
      " [[1. 1. 1. 1. 0. 0.]\n",
      " [1. 1. 1. 0. 1. 0.]\n",
      " [1. 1. 1. 0. 0. 1.]]\n",
      "\n",
      "Concatenacion vertical:\n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "# pedir longitud del array\n",
    "longitud = int(input(\"Ingrese la longitud del array: \"))\n",
    "# crear array\n",
    "array_ones = np.ones(longitud)\n",
    "print(array_ones)\n",
    "\n",
    "# Pidiendo al usuario la nueva forma del array\n",
    "filas = int(input(\"Ingrese la cantidad de filas: \"))\n",
    "columnas = int(input(\"Ingrese la cantidad de columnas:\"))\n",
    "\n",
    "# comprobamos que el reshape es posible\n",
    "if filas * columnas == longitud:\n",
    "    # realizamos el reshape\n",
    "    nuevo_array = np.reshape(array_ones, (filas,columnas))\n",
    "    print(\"Array con nueva forma: \\n\", nuevo_array)\n",
    "\n",
    "    if filas == columnas:\n",
    "        matriz_identidad = np.eye(filas)\n",
    "        print(\"Matriz identidad:\\n\", matriz_identidad)\n",
    "\n",
    "        # concatenar horizontalmente\n",
    "        concat_horizontal = np.concatenate((nuevo_array, matriz_identidad), axis = 1)\n",
    "        print(\"\\nConcatenacion horizontal:\\n\", concat_horizontal)\n",
    "\n",
    "        # concatenar vertical \n",
    "        concat_vertical = np.concatenate((nuevo_array, matriz_identidad), axis = 0)\n",
    "        print(\"\\nConcatenacion vertical:\\n\", concat_vertical)\n",
    "\n",
    "    else: \n",
    "        print(\"No se puede crear una matriz identidad con diferente numero de filas que de columnas\")\n",
    "\n",
    "else:\n",
    "    # indicamos que el reshape no es posible\n",
    "    print(\"La cantidad de filas y columnas no es compatible con la longitud del array\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 1. 1. 1. 1. 1. 1. 1. 1.]\n",
      "Array con nueva forma: \n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]]\n",
      "Matriz identidad:\n",
      " [[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n",
      "\n",
      "Concatenacion horizontal:\n",
      " [[1. 1. 1. 1. 0. 0.]\n",
      " [1. 1. 1. 0. 1. 0.]\n",
      " [1. 1. 1. 0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "# pedir longitud del array\n",
    "longitud = int(input(\"Ingrese la longitud del array: \"))\n",
    "# crear array\n",
    "array_ones = np.ones(longitud)\n",
    "print(array_ones)\n",
    "\n",
    "# Pidiendo al usuario la nueva forma del array\n",
    "filas = int(input(\"Ingrese la cantidad de filas: \"))\n",
    "columnas = int(input(\"Ingrese la cantidad de columnas:\"))\n",
    "\n",
    "# comprobamos que el reshape es posible\n",
    "if filas * columnas == longitud:\n",
    "    # realizamos el reshape\n",
    "    nuevo_array = np.reshape(array_ones, (filas,columnas))\n",
    "    print(\"Array con nueva forma: \\n\", nuevo_array)\n",
    "\n",
    "    if filas == columnas:\n",
    "        matriz_identidad = np.eye(filas)\n",
    "        print(\"Matriz identidad:\\n\", matriz_identidad)\n",
    "\n",
    "        # concatenar horizontalmente\n",
    "        concat_horizontal = np.hstack((nuevo_array, matriz_identidad))\n",
    "        print(\"\\nConcatenacion horizontal:\\n\", concat_horizontal)\n",
    "\n",
    "        # concatenar vertical \n",
    "        concat_vertical = np.vstack((nuevo_array, matriz_identidad))\n",
    "        print(\"\\nConcatenacion vertical:\\n\", concat_vertical)\n",
    "\n",
    "    else: \n",
    "        print(\"No se puede crear una matriz identidad con diferente numero de filas que de columnas\")\n",
    "\n",
    "else:\n",
    "    # indicamos que el reshape no es posible\n",
    "    print(\"La cantidad de filas y columnas no es compatible con la longitud del array\")"
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

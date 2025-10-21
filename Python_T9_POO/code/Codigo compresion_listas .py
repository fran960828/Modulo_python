{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " La compresion de listas permite crear listas de una manera más elegante y compacta. En lugar de utilizar bucles tradicionales, puedes utilizar la compresión de listas para generar listas de forma más eficiente. "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "nueva_lista = [expresion for elemento in lista_original]"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Crear una lista de numeros al cuadrado"
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
      "[1, 4, 9, 16, 25]\n"
     ]
    }
   ],
   "source": [
    "# Método tradicional con bucle\n",
    "numeros = [1, 2, 3, 4, 5]\n",
    "cuadrados = []\n",
    "for num in numeros:\n",
    "    cuadrados.append(num**2)\n",
    "\n",
    "# Con compresión de listas\n",
    "cuadrados = [num**2 for num in numeros]\n",
    "print(cuadrados)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. El intérprete de Python recorre cada elemento num en la lista numeros.\n",
    "2. Para cada num, se evalúa la expresión num**2, es decir, se eleva al cuadrado el valor de num.\n",
    "3. El resultado de la expresión se agrega a la lista resultante cuadrados.\n",
    "4. Este proceso se repite para cada elemento num en la lista numeros.\n",
    "5. Finalmente, se obtiene la lista cuadrados que contiene los cuadrados de los elementos de numeros."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Filtrar números pares de una lista"
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
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "# Método tradicional con bucle\n",
    "numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "pares = []\n",
    "for num in numeros:\n",
    "    if num % 2 == 0:\n",
    "        pares.append(num)\n",
    "\n",
    "# Con compresión de listas\n",
    "pares = [num for num in numeros if num % 2 == 0 ]\n",
    "print(pares)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Crear una lista de tuplas a partir de dos listas:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Juan', 25), ('María', 30), ('Carlos', 22)]\n"
     ]
    }
   ],
   "source": [
    "# Método tradicional con bucle\n",
    "nombres = ['Juan', 'María', 'Carlos']\n",
    "edades = [25, 30, 22]\n",
    "personas = []\n",
    "for i in range(len(nombres)):\n",
    "    personas.append((nombres[i], edades[i]))\n",
    "\n",
    "# Con compresión de listas\n",
    "personas = [(nombres[i], edades[i]) for i in range(len(nombres))]\n",
    "print(personas)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Crear una lista con elementos transformados condicionalmente:"
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
      "['impar', 'par', 'impar', 'par', 'impar']\n"
     ]
    }
   ],
   "source": [
    "# Método tradicional con bucle\n",
    "numeros = [1, 2, 3, 4, 5]\n",
    "transformados = []\n",
    "for num in numeros:\n",
    "    if num % 2 == 0:\n",
    "        transformados.append('par')\n",
    "    else:\n",
    "        transformados.append('impar')\n",
    "\n",
    "# Con compresión de listas\n",
    "transformados = ['par' if num % 2 == 0 else 'impar' for num in numeros]\n",
    "print(transformados)"
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

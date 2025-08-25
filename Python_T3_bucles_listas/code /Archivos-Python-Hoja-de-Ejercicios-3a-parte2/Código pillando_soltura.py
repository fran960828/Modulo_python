{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Escribe un programa en Python para encontrar los elementos duplicados de una lista, añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los elementos únicos."
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
      "Lista original: [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 8, 10]\n",
      "Elementos unicos: [1, 2, 4, 5, 6, 7, 9, 10]\n",
      "Elementos duplicados: [3, 8]\n",
      "Lista nueva: [1, 2, 4, 5, 6, 3, 7, 9, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "lista = [1,2,3,4,5,6,3,7,8,9,8,10]\n",
    "print(\"Lista original:\",lista)\n",
    "elementos_duplicados = []\n",
    "elementos_unicos = []\n",
    "for elemento in lista:\n",
    "    if lista.count(elemento) > 1:\n",
    "        if elemento not in elementos_duplicados:\n",
    "            elementos_duplicados.append(elemento)\n",
    "    else:\n",
    "        elementos_unicos.append(elemento)\n",
    "for elemento in elementos_duplicados:\n",
    "    lista.remove(elemento)\n",
    "\n",
    "print(\"Elementos unicos:\", elementos_unicos)\n",
    "print(\"Elementos duplicados:\", elementos_duplicados)\n",
    "print(\"Lista nueva:\", lista)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8]\n"
     ]
    }
   ],
   "source": [
    "lista1 = [3, 4, 1, 5]\n",
    "lista2 = [6, 2, 7, 8]\n",
    "\n",
    "lista_combinada = lista1 + lista2\n",
    "lista_combinada.sort()\n",
    "print(lista_combinada)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Escribe un script que encuentre el segundo número más grande de una lista."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "numbers = [3,4,1,5,6,2,7,8]\n",
    "numbers.sort(reverse=True)\n",
    "print(numbers[1])"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Crea un script que cuente el número de elementos más grandes que un determinado número dado por el usuario (supón una lista numérica)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "numeros = [3,4,1,5,6,2,7,1]\n",
    "numero_objetivo = 4\n",
    "\n",
    "contador = 0\n",
    "for num in numeros:\n",
    "    if num > numero_objetivo:\n",
    "        contador += 1\n",
    "\n",
    "print(contador)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Crea un script dado un número introducido por el usuario o determinado al inicio del programa, realice la suma de aquellos números que sean divisibles por este."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "numeros = [3,4,1,5,6,2,7,8]\n",
    "divisor = 2\n",
    "\n",
    "resultado = 0\n",
    "for num in numeros:\n",
    "    if num % divisor == 0:\n",
    "        resultado +=num\n",
    "print(resultado)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto que es inferior al número introducido o determinado al inicio del programa."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "numeros = [3,4,1,5,6,2,7,8]\n",
    "numero_objetivo = 8\n",
    "numeros.sort()\n",
    "\n",
    "for num in numeros:\n",
    "    if num < numero_objetivo:\n",
    "        resultado = num\n",
    "print(resultado)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Crea un script que extraiga los elementos comunes entre dos listas."
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
      "Elementos comunes: [4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "lista1 = [1,2,3,4,5,6]\n",
    "lista2 = [4,5,6,7,8,9]\n",
    "comunes =[]\n",
    "\n",
    "for elemento in lista1:\n",
    "    if elemento in lista2:\n",
    "        comunes.append(elemento)\n",
    "\n",
    "print(\"Elementos comunes:\", comunes)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista (P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "El elemento 23, aparece 2 veces en la lista\n",
      "El elemento 65, aparece 1 veces en la lista\n",
      "El elemento 23, aparece 2 veces en la lista\n"
     ]
    }
   ],
   "source": [
    "numeros = [23,65,23]\n",
    "objetivo = 23\n",
    "print(numeros.count(objetivo))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "numeros = [23,65,23]\n",
    "objetivo = 23\n",
    "\n",
    "contador = 0\n",
    "for numero in lista:\n",
    "    if numero == objetivo:\n",
    "        contador +=1\n",
    "        \n",
    "print(\"Numero de apariciones de\", elemento, \":\", contador)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9.Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo números positivos de la lista original."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista original: [-1, 2, -3, 4, -5, 6, -7, 8, -9]\n",
      "Lista de numeros positivos: [2, 4, 6, 8]\n"
     ]
    }
   ],
   "source": [
    "lista_original = [-1, 2, -3, 4, -5, 6, -7, 8, -9]\n",
    "lista_positivos = []\n",
    "\n",
    "for numero in lista_original:\n",
    "    if numero > 0:\n",
    "        lista_positivos.append(numero)\n",
    "\n",
    "print(\"Lista original:\", lista_original)\n",
    "print(\"Lista de numeros positivos:\", lista_positivos)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10.Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de\n",
    "los strings de la lista original."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista de strigs ['hola', 'estas', 'usando', 'python']\n",
      "Lista de longitudes [4, 5, 6, 6]\n"
     ]
    }
   ],
   "source": [
    "lista_strings = [\"hola\", \"estas\", \"usando\", \"python\"]\n",
    "lista_longitudes = []\n",
    "\n",
    "for string in lista_strings:\n",
    "    longitud = len(string)\n",
    "    lista_longitudes.append(longitud)\n",
    "\n",
    "print(\"Lista de strigs\", lista_strings)\n",
    "print(\"Lista de longitudes\", lista_longitudes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista de strigs ['hola', 'estas', 'usando', 'python']\n",
      "Lista de longitudes [4, 5, 6, 6]\n"
     ]
    }
   ],
   "source": [
    "lista_strings = [\"hola\", \"estas\", \"usando\", \"python\"]\n",
    "lista_longitudes = []\n",
    "\n",
    "for string in lista_strings:\n",
    "    longitud = 0\n",
    "    for caracter in string:\n",
    "        longitud +=1\n",
    "    lista_longitudes.append(longitud)\n",
    "\n",
    "print(\"Lista de strigs\", lista_strings)\n",
    "print(\"Lista de longitudes\", lista_longitudes)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en\n",
    "mayúscula."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista de strings: ['hola', 'estas', 'usando', 'python']\n",
      "Lista en mayusculas ['HOLA', 'ESTAS', 'USANDO', 'PYTHON']\n"
     ]
    }
   ],
   "source": [
    "lista_strings = [\"hola\", \"estas\", \"usando\", \"python\"]\n",
    "lista_mayusculas = []\n",
    "\n",
    "for string in lista_strings:\n",
    "    lista_mayusculas.append(string.upper())\n",
    "\n",
    "print(\"Lista de strings:\", lista_strings)\n",
    "print(\"Lista en mayusculas\", lista_mayusculas)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "work",
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
   "version": "3.9.15 (main, Nov 24 2022, 08:29:02) \n[Clang 14.0.6 ]"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b8e3f23012204b1b655a61e68bcec502af9aea10795c8cc22548649a458b784e"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

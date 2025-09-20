{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea."
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
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (1,2,3)\n",
    "for elemento in mi_tupla:\n",
    "    print(elemento)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla. ¿Cuáles son las diferencias?"
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
      "[4, 2, 3]\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 6\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[39mprint\u001b[39m(mi_lista)\n\u001b[1;32m      5\u001b[0m mi_tupla \u001b[39m=\u001b[39m (\u001b[39m1\u001b[39m,\u001b[39m2\u001b[39m,\u001b[39m3\u001b[39m)\n\u001b[0;32m----> 6\u001b[0m mi_tupla[\u001b[39m0\u001b[39m] \u001b[39m=\u001b[39m \u001b[39m4\u001b[39m\n",
      "\u001b[0;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "mi_lista = [1,2,3]\n",
    "mi_lista[0] = 4\n",
    "print(mi_lista)\n",
    "\n",
    "mi_tupla = (1,2,3)\n",
    "mi_tupla[0] = 4 #ERROR"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Crea una tupla de enteros y devuelve la suma de los elementos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (1,2,3)\n",
    "suma = sum(mi_tupla)\n",
    "print(suma)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4.Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string."
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
      "('m', 'p', 'n')\n",
      "('m', 'p', 'n')\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (\"manzana\", \"platano\", \"naranja\")\n",
    "lista = []\n",
    "for palabra in mi_tupla:\n",
    "    lista.append(palabra[0])\n",
    "mi_nueva_tupla = tuple(lista)\n",
    "print(mi_nueva_tupla)\n",
    "\n",
    "mi_nueva_tupla2 = tuple(palabra[0] for palabra in mi_tupla)\n",
    "print(mi_nueva_tupla2)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Crea un script que dada una tupla de números devuelva el producto de todos los números pares."
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
      "48\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (1,2,3,4,5,6) \n",
    "\n",
    "producto = 1\n",
    "for num in mi_tupla:\n",
    "    if num % 2 == 0:\n",
    "        producto = producto * num\n",
    "print(producto)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente."
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
      "(8, 6, 4, 2, 1)\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (4,1,6,2,8)\n",
    "mi_tupla_reordenada = tuple(sorted(mi_tupla, reverse=True))\n",
    "print(mi_tupla_reordenada)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 6)\n",
      "(1, 2, 3, 4, 5, 6)\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (1,1,2,3,4,4,5,6)\n",
    "mi_set = set(mi_tupla)\n",
    "mi_tupla_sin_duplicados = tuple(mi_set)\n",
    "print(mi_tupla_sin_duplicados)\n",
    "mi_tupla_sin_duplicados2 = tuple(set(mi_tupla))\n",
    "print(mi_tupla_sin_duplicados2)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla y falso en el caso contrario."
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
      "False\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (1,3,5,7,9)\n",
    "target = \"Manzana\"\n",
    "comprobacion = target in mi_tupla\n",
    "print(comprobacion)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas."
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
      "(1, 2, 3, 4, 5, 6)\n"
     ]
    }
   ],
   "source": [
    "mi_tupla1 = (1,2,3)\n",
    "mi_tupla2 = (4,5,6)\n",
    "tupla3 = mi_tupla1 + mi_tupla2\n",
    "print(tupla3)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10. Crea un script que dada una tupla de números devuelva e máximo y el mínimo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 3\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = 1,2,3\n",
    "\n",
    "minimo = min(mi_tupla)\n",
    "maximo = max(mi_tupla)\n",
    "\n",
    "print(minimo, maximo)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "11. Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. (Prueba añadiendo key=len a las funciones max y min).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pera manzana\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = \"manzana\", \"pera\", \"fresa\"\n",
    "\n",
    "minimo = min(mi_tupla, key = len)\n",
    "maximo = max(mi_tupla, key = len)\n",
    "print(minimo, maximo)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "12. Crea un script que dada una tupla devuelva el contenido en orden revertido."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 2, 1)\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = (1,2,3)\n",
    "mi_nueva_tupla = mi_tupla[::-1]\n",
    "print(mi_nueva_tupla)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "13. Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos elementos de la tupla interna correspondiente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 7, 11)\n"
     ]
    }
   ],
   "source": [
    "mi_tupla = ((1,2),(3,4),(5,6))\n",
    "mi_lista = []\n",
    "for tupla_interna in mi_tupla:\n",
    "    suma = sum(tupla_interna)\n",
    "    mi_lista.append(suma)\n",
    "mi_nueva_tupla = tuple(mi_lista)\n",
    "print(mi_nueva_tupla)\n",
    "\n",
    "mi_nueva_tupla2 = tuple(sum(tupla_interna) for tupla_interna in mi_tupla)\n",
    "print(mi_nueva_tupla2)"
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

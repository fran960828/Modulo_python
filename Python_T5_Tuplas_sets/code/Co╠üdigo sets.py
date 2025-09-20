{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "14.Crea un set y elimina uno de sus elementos."
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
      "{1, 2, 3, 4}\n"
     ]
    }
   ],
   "source": [
    "mi_set = {1,2,3,4}\n",
    "mi_set.discard(5) # o remove \n",
    "print(mi_set)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "15.Crea un set vacío."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'set'>\n"
     ]
    }
   ],
   "source": [
    "mi_set = set() # no se hace con {}\n",
    "print(type(mi_set))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "16.Crea dos sets y encuentra su union, su intersección y su diferencia."
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
      "{8, 6, 7}\n"
     ]
    }
   ],
   "source": [
    "set1 = {1,2,3,4,5}\n",
    "set2 = {4,5,6,7,8}\n",
    "\n",
    "union = set1.union(set2)\n",
    "interseccion = set1.intersection(set2)\n",
    "diferencia = set2.difference(set1)\n",
    "print(diferencia)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "17.Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos."
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
      "{4, 5}\n",
      "{4, 5}\n"
     ]
    }
   ],
   "source": [
    "set1 = {1,2,3,4,5}\n",
    "set2 = {4,5,6,7,8}\n",
    "\n",
    "set3 = set1.intersection(set2)\n",
    "set4 = set1 & set2\n",
    "print(set3)\n",
    "print(set4)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "18.Crea un script que dado un set con números devuelva el numero máximo y mínimo."
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
      "5 1\n"
     ]
    }
   ],
   "source": [
    "mi_set = {1,2,3,4,5}\n",
    "maximo = max(mi_set)\n",
    "minimo = min(mi_set)\n",
    "print(maximo, minimo)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "19.Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 6, 7, 8}\n"
     ]
    }
   ],
   "source": [
    "set1 = {1,2,3,4,5}\n",
    "set2 = {4,5,6,7,8}\n",
    "\n",
    "set3 = set1.symmetric_difference(set2)\n",
    "print(set3)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "20.Crea un set con colores y comprueba si cierto color se encuentra en el set."
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
      "True\n"
     ]
    }
   ],
   "source": [
    "mi_set = {\"azul\", \"verde\", \"lila\"}\n",
    "pertenencia = \"lila\" in mi_set\n",
    "print(pertenencia)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "21.Crea un script que dados dos sets cree un nuevo set con los elementos que están en el primer set pero no en el segundo."
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
      "{'azul', 'lila'}\n"
     ]
    }
   ],
   "source": [
    "mi_set1 = {\"azul\", \"verde\", \"lila\"}\n",
    "mi_set2 = {\"rojo\", \"verde\", \"turquesa\"}\n",
    "\n",
    "mi_set3 = mi_set1.difference(mi_set2)\n",
    "print(mi_set3)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "22.Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set."
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
      "40320\n"
     ]
    }
   ],
   "source": [
    "mi_set = {1,2,3,4}\n",
    "\n",
    "producto = 1\n",
    "for numero in mi_set:\n",
    "    producto = producto * numero\n",
    "print(producto)"
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

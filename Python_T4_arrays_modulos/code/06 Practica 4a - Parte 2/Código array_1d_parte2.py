{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1. Crea un array con 15 números enteros aleatorios entre 1 y 100\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "array_random = np.random.randint(1,101, size=15)\n",
    "\n",
    "print(array_random)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Multiplica todos los elementos del array usando un bucle y después usando un método de numpy. Compara los resultados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[31 44 92 28 96 13 42 10 56 91 68 81  9 98 65]\n",
      "Multiplicacion usando bucle: -5396937809527832576\n",
      "Multiplicacion usando NumPy: -5396937809527832576\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/c4/ghqdrvf12992ljw6glk6tkl80000gn/T/ipykernel_81380/474625701.py:10: RuntimeWarning: overflow encountered in long_scalars\n",
      "  multi_bucle = multi_bucle * numero\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "# creamos array con numeros aleatorios entre el 1 y el 100\n",
    "array_random = np.random.randint(1,101, size=15)\n",
    "print(array_random)\n",
    "# Multiplicacion usando un bucle\n",
    "multi_bucle = 1\n",
    "for numero in array_random:\n",
    "    multi_bucle = multi_bucle * numero\n",
    "\n",
    "print(\"Multiplicacion usando bucle:\", multi_bucle)\n",
    "\n",
    "# Multiplicacion usando el metodo numpy\n",
    "multi_numpy = np.prod(array_random)\n",
    "print(\"Multiplicacion usando NumPy:\", multi_numpy)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Crea otro array con 15 números decimales aleatorios entre 0 y 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.28507971 0.54096203 0.10618585 0.55746163 0.52827063 0.67442164\n",
      " 0.34083565 0.09305164 0.33652602 0.6883022  0.52367774 0.09571993\n",
      " 0.86611452 0.68201226 0.99850692]\n"
     ]
    }
   ],
   "source": [
    "# importamos modulos\n",
    "import numpy as np\n",
    "\n",
    "array_decimales = np.random.random(15)\n",
    "print(array_decimales)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un operador y después con una función de numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array random: [31 75 34 26 29 30 65 79 95 98 87 33 62 63 33]\n",
      "Array decimales [0.66489385 0.88620454 0.19423465 0.31944392 0.11213946 0.98678907\n",
      " 0.30543215 0.07342836 0.75470599 0.38250358 0.48520306 0.48107396\n",
      " 0.62940198 0.30781206 0.70196654]\n",
      "Suma usando operador: [31.66489385 75.88620454 34.19423465 26.31944392 29.11213946 30.98678907\n",
      " 65.30543215 79.07342836 95.75470599 98.38250358 87.48520306 33.48107396\n",
      " 62.62940198 63.30781206 33.70196654]\n",
      "Suma usando numpy: [31.66489385 75.88620454 34.19423465 26.31944392 29.11213946 30.98678907\n",
      " 65.30543215 79.07342836 95.75470599 98.38250358 87.48520306 33.48107396\n",
      " 62.62940198 63.30781206 33.70196654]\n"
     ]
    }
   ],
   "source": [
    "# improtamos modulos\n",
    "import numpy as np\n",
    "\n",
    "array_random = np.random.randint(1,101, size=15)\n",
    "array_decimales = np.random.random(15)\n",
    "\n",
    "print(\"Array random:\", array_random)\n",
    "print(\"Array decimales\", array_decimales)\n",
    "\n",
    "# Suma usando un operador\n",
    "suma_operador = array_random + array_decimales\n",
    "print(\"Suma usando operador:\", suma_operador)\n",
    "\n",
    "\n",
    "# Suma usando funcion de NumPy\n",
    "suma_numpy = np.add(array_random, array_decimales)\n",
    "print(\"Suma usando numpy:\", suma_numpy)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy (Pista: busca en google que función de numpy hace esto)"
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
      "Array random: [61 61 79 73 54 58 56 96 69 82 32  9 24 10  6]\n",
      "Array decimales [0.3637606  0.07060118 0.25463547 0.42222195 0.43483059 0.32199124\n",
      " 0.33393147 0.72330875 0.6655679  0.06354206 0.79225206 0.05596027\n",
      " 0.72787317 0.82802054 0.47509462]\n",
      "Resta usando operador: [60.6362394  60.92939882 78.74536453 72.57777805 53.56516941 57.67800876\n",
      " 55.66606853 95.27669125 68.3344321  81.93645794 31.20774794  8.94403973\n",
      " 23.27212683  9.17197946  5.52490538]\n",
      "Resta usando funcion de Numpy; [60.6362394  60.92939882 78.74536453 72.57777805 53.56516941 57.67800876\n",
      " 55.66606853 95.27669125 68.3344321  81.93645794 31.20774794  8.94403973\n",
      " 23.27212683  9.17197946  5.52490538]\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "array_random = np.random.randint(1,101, size=15)\n",
    "array_decimales = np.random.random(15)\n",
    "\n",
    "print(\"Array random:\", array_random)\n",
    "print(\"Array decimales\", array_decimales)\n",
    "\n",
    "# Resta usando un operador\n",
    "suma_operador = array_random - array_decimales\n",
    "print(\"Resta usando operador:\", suma_operador)\n",
    "\n",
    "# Resta usando funcion de NumPy\n",
    "resta_numpy = np.subtract(array_random, array_decimales)\n",
    "print(\"Resta usando funcion de Numpy;\", resta_numpy)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy"
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
      "Array random: [ 47  95  71  37  95  27  10  87 100  89  30  49  94  78  17]\n",
      "Array decimales [0.61935247 0.29045438 0.90517364 0.86599884 0.8309821  0.7862213\n",
      " 0.05243372 0.90910985 0.66809103 0.86376833 0.15079591 0.48865328\n",
      " 0.29521631 0.36530964 0.74025799]\n",
      "Multiplicacion usando operador: [29.10956603 27.59316592 64.26732809 32.04195693 78.94329997 21.22797499\n",
      "  0.52433718 79.09255727 66.8091027  76.87538108  4.52387737 23.94401059\n",
      " 27.75033286 28.49415187 12.58438577]\n",
      "Multipliacion usando funcion de NumPy: [29.10956603 27.59316592 64.26732809 32.04195693 78.94329997 21.22797499\n",
      "  0.52433718 79.09255727 66.8091027  76.87538108  4.52387737 23.94401059\n",
      " 27.75033286 28.49415187 12.58438577]\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "array_random = np.random.randint(1,101, size=15)\n",
    "array_decimales = np.random.random(15)\n",
    "\n",
    "print(\"Array random:\", array_random)\n",
    "print(\"Array decimales\", array_decimales)\n",
    "\n",
    "# Multiplicacion usando un operador\n",
    "suma_operador = array_random * array_decimales\n",
    "print(\"Multiplicacion usando operador:\", suma_operador)\n",
    "\n",
    "# Multipliacion con funcion de NumPy\n",
    "multi_numpy = np.multiply(array_random, array_decimales)\n",
    "print(\"Multipliacion usando funcion de NumPy:\", multi_numpy)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 7. Encuentra el valor más alto del primer array que has creado."
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
      "Array random: [14  3 40 54 74 39 70 24  9 89 48 38 44 53 24]\n",
      "Valor mas alto: 89\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "# crear array\n",
    "array_random = np.random.randint(1,101, size=15)\n",
    "print(\"Array random:\", array_random)\n",
    "\n",
    "# obtener el valor maximo\n",
    "max_valor = np.max(array_random)\n",
    "print(\"Valor mas alto:\", max_valor)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 8. Calcula la media (mean), la mediana (median) y al deviación estandar (standard deviation) de los arrays"
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
      "Array random: [  2  78  47  37  16  47  18  21  98 100  13  90  15  52  20]\n",
      "Array decimales: [0.7417481  0.96280691 0.20240953 0.90514162 0.75259369 0.18341499\n",
      " 0.2075122  0.60247092 0.91835528 0.72172426 0.80372786 0.05449768\n",
      " 0.56669849 0.17977416 0.8324161 ]\n",
      "Array random:\n",
      "Media: 43.6\n",
      "Mediana; 37.0\n",
      "Desviacion estandar: 32.23207512194439\n",
      "\n",
      "Array decimales:\n",
      "Media: 0.5756861204071733\n",
      "Mediana; 0.721724259679947\n",
      "Desviacion estandar: 0.30896438685316135\n"
     ]
    }
   ],
   "source": [
    "# importar modulos\n",
    "import numpy as np\n",
    "\n",
    "# crear arrays\n",
    "array_random = np.random.randint(1, 101, size=15)\n",
    "array_decimales = np.random.random(15)\n",
    "print(\"Array random:\", array_random)\n",
    "print(\"Array decimales:\", array_decimales)\n",
    "\n",
    "# calcular la media\n",
    "media_random = np.mean(array_random)\n",
    "media_decimales = np.mean(array_decimales)\n",
    "\n",
    "# calcular la mediana\n",
    "mediana_random = np.median(array_random)\n",
    "mediana_decimales = np.median(array_decimales)\n",
    "\n",
    "# desviacion estandar\n",
    "std_random = np.std(array_random)\n",
    "std_decimales = np.std(array_decimales)\n",
    "\n",
    "# imprimimos los resultados\n",
    "print(\"\\nArray random:\")\n",
    "print(\"Media:\", media_random)\n",
    "print(\"Mediana;\", mediana_random)\n",
    "print(\"Desviacion estandar:\", std_random)\n",
    "\n",
    "print(\"\\nArray decimales:\")\n",
    "print(\"Media:\", media_decimales)\n",
    "print(\"Mediana;\", mediana_decimales)\n",
    "print(\"Desviacion estandar:\", std_decimales)\n",
    "\n",
    "\n"
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

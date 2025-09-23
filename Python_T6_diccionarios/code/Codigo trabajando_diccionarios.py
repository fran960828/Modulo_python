{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. Crea un diccionario vacío llamado \"mi_diccionario\"."
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
      "<class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "mi_diccionario = {}\n",
    "print(type(mi_diccionario))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2. Agrega un par clave-valor a \"mi_diccionario\" donde la clave sea \"nombre\" y el valor sea tu nombre."
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
      "{'nombre': 'Elena'}\n"
     ]
    }
   ],
   "source": [
    "mi_diccionario[\"nombre\"] = \"Elena\"\n",
    "print(mi_diccionario)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3. Accede e imprime el valor asociado con la clave \"nombre\" en “mi_diccionario\"."
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
      "Elena\n"
     ]
    }
   ],
   "source": [
    "print(mi_diccionario[\"nombre\"])"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4. Verifica si la clave \"edad\" existe en \"mi_diccionario\". Imprime \"True\" si existe y \"False\" en caso contrario."
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
      "False\n"
     ]
    }
   ],
   "source": [
    "print(\"edad\" in mi_diccionario)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5. Crea un diccionario llamado \"estudiante\" con los siguientes pares clave-valor: \"nombre\" con el nombre del alumno, \"edad\" con su edad y \"materia\" con su materia favorita."
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
      "{'nombre': 'juan', 'edad': 20, 'materia': 'matematicas'}\n"
     ]
    }
   ],
   "source": [
    "estudiante = {\n",
    "    \"nombre\": \"juan\",\n",
    "    \"edad\":20,\n",
    "    \"materia\": \"matematicas\"\n",
    "}\n",
    "print(estudiante)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 6. Actualiza el valor de la clave \"edad\" en el diccionario \"estudiante\"."
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
      "{'nombre': 'juan', 'edad': 25, 'materia': 'matematicas'}\n"
     ]
    }
   ],
   "source": [
    "estudiante[\"edad\"] = 25\n",
    "print(estudiante)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 7. Elimina el par clave-valor con la clave \"materia\" del diccionario “estudiante\"."
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
      "{'nombre': 'juan', 'edad': 25} matematicas\n"
     ]
    }
   ],
   "source": [
    "valor_materia = estudiante.pop(\"materia\")\n",
    "print(estudiante, valor_materia)\n",
    "# del estudiante[\"materia\"]"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 8. Imprime todas las claves en el diccionario “estudiante\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nombre\n",
      "edad\n"
     ]
    }
   ],
   "source": [
    "for clave in estudiante.keys():\n",
    "    print(clave)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 9. Crea un diccionario llamado \"agenda\" con tres entradas:  \"Juan\" con el valor \"1234567890\", \"Joana\" con el valor \"9876543210\" y \"Jimena\" con el valor “5555555555”."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Juan': '1234567890', 'Joana': '9876543210', 'Jimena': '5555555555'}\n"
     ]
    }
   ],
   "source": [
    "agenda = {\n",
    "    \"Juan\": \"1234567890\",\n",
    "    \"Joana\": \"9876543210\",\n",
    "    \"Jimena\": \"5555555555\",\n",
    "    }\n",
    "print(agenda)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 10. Agrega una nueva entrada al diccionario \"agenda\" con la clave \"Julio\" y el valor “9998887777\"."
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
      "{'Juan': '1234567890', 'Joana': '9876543210', 'Jimena': '5555555555', 'Julio': '9998887777'}\n"
     ]
    }
   ],
   "source": [
    "agenda[\"Julio\"] = \"9998887777\"\n",
    "print(agenda)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 11. Imprime el número de entradas (pares clave-valor) en el diccionario “agenda\"."
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
      "4\n"
     ]
    }
   ],
   "source": [
    "print(len(agenda))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 12. Crea una lista llamada \"claves\" que contenga todas las claves del diccionario “agenda\"."
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
      "['Juan', 'Joana', 'Jimena', 'Julio']\n"
     ]
    }
   ],
   "source": [
    "claves = list(agenda.keys())\n",
    "print(claves)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 13. Verifica si la clave \"Juan\" existe en el diccionario \"agenda\"."
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
      "True\n"
     ]
    }
   ],
   "source": [
    "print(\"Juan\" in agenda)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 14. Elimina la entrada con la clave \"Jimena\" del diccionario \"agenda\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Juan': '1234567890', 'Joana': '9876543210', 'Julio': '9998887777'}\n"
     ]
    }
   ],
   "source": [
    "del agenda[\"Jimena\"]\n",
    "print(agenda)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 15. Utiliza un bucle for para iterar sobre todas las claves en el diccionario \"agenda\" e imprime cada par clave-valor."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Juan:1234567890\n",
      "Joana:9876543210\n",
      "Julio:9998887777\n"
     ]
    }
   ],
   "source": [
    "for tupla in agenda.items():\n",
    "    clave, valor = tupla\n",
    "    print(clave + \":\" + valor)"
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
      "Juan:1234567890\n",
      "Joana:9876543210\n",
      "Julio:9998887777\n"
     ]
    }
   ],
   "source": [
    "for clave in agenda:\n",
    "    valor = agenda[clave]\n",
    "    print(clave + \":\" + valor)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 16. Utiliza el método \"get()\" para obtener el valor asociado con la clave \"Juan\" en el diccionario \"agenda\".\n",
    "# Si la clave no existe, imprime \"Clave no encontrada\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Clave no encontrada\n"
     ]
    }
   ],
   "source": [
    "valor_juan = agenda.get(\"Pedro\", \"Clave no encontrada\")\n",
    "print(valor_juan)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 17. Borra todas las entradas del diccionario “agenda”."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Juan': '1234567890', 'Joana': '9876543210', 'Julio': '9998887777'}\n",
      "{}\n"
     ]
    }
   ],
   "source": [
    "print(agenda)\n",
    "agenda.clear()\n",
    "print(agenda)"
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

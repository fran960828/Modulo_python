{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 18. Crea una lista llamada \"estudiantes\" que contenga dos diccionarios. Cada diccionario representa a un estudiante y tiene las claves \"nombre\" y \"edad\" con sus respectivos valores. Recorre la lista e imprime el nombre y edad de cada estudiante.\n"
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
      "Nombre: Eduardo Edad: 20\n",
      "Nombre: Juan Edad: 22\n"
     ]
    }
   ],
   "source": [
    "estudiantes = [\n",
    "    {\"nombre\": \"Eduardo\", \"edad\": 20},\n",
    "    {\"nombre\": \"Juan\", \"edad\":22},\n",
    "]\n",
    "\n",
    "for estudiante in estudiantes:\n",
    "    nombre = estudiante[\"nombre\"]\n",
    "    edad = estudiante[\"edad\"]\n",
    "    print(\"Nombre:\", nombre, \"Edad:\", edad)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 19. Agrega un nuevo estudiante a la lista \"estudiantes\" utilizando un diccionario con las mismas claves \"nombre\" y \"edad\". Imprime la lista actualizada."
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
      "[{'nombre': 'Eduardo', 'edad': 20}, {'nombre': 'Juan', 'edad': 22}, {'nombre': 'Felipe', 'edad': 24}]\n"
     ]
    }
   ],
   "source": [
    "estudiantes.append({\"nombre\":\"Felipe\", \"edad\":24})\n",
    "print(estudiantes)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 20. Elimina el segundo estudiante de la lista \"estudiantes\". Imprime la lista actualizada."
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
      "[{'nombre': 'Eduardo', 'edad': 20}, {'nombre': 'Felipe', 'edad': 24}]\n"
     ]
    }
   ],
   "source": [
    "# estudiantes es una lista\n",
    "# eliminar el segundo elemento de la lista -- indice 1\n",
    "del estudiantes[1]\n",
    "print(estudiantes)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 21. Actualiza la edad del primer estudiante en la lista \"estudiantes\" a un nuevo valor. Imprime la lista actualizada."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'nombre': 'Eduardo', 'edad': 20}\n"
     ]
    }
   ],
   "source": [
    "# primer estudiante tendra inidice 0\n",
    "estudiantes[0][\"edad\"] = 23\n",
    "print(estudiantes)"
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

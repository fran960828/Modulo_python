{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 22. Crea un diccionario llamado \"productos\" que contenga dos entradas. Cada entrada representa un producto y tiene a su vez las claves \"nombre\" y \"precio\" con sus respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada producto."
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
      "Producto: manzanas Precio 10\n",
      "Producto: arandanos Precio 15\n"
     ]
    }
   ],
   "source": [
    "productos = {\n",
    "    \"producto1\": {\"nombre\": \"manzanas\", \"precio\": 10},\n",
    "    \"producto2\": {\"nombre\": \"arandanos\", \"precio\": 15},\n",
    "}\n",
    "\n",
    "for clave, valor in productos.items():\n",
    "    nombre = valor[\"nombre\"]\n",
    "    precio = valor[\"precio\"]\n",
    "    \n",
    "    print(\"Producto:\", nombre, \"Precio\", precio)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 23. Agrega un nuevo producto al diccionario \"productos\" utilizando una nueva clave y valor, y luego imprimir el diccionario actualizado"
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
      "{'producto1': {'nombre': 'manzanas', 'precio': 10}, 'producto2': {'nombre': 'arandanos', 'precio': 15}, 'Producto3': {'nombre': 'platanos', 'precio': 5}}\n"
     ]
    }
   ],
   "source": [
    "productos[\"Producto3\"] = {\"nombre\": \"platanos\", \"precio\": 5}\n",
    "\n",
    "print(productos)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 24. Crea un diccionario llamado \"equipos\" que contenga tres entradas. Cada entrada representa un equipo deportivo y tiene las claves \"nombre\" y \"jugadores\" con sus respectivos valores. Los valores de \"jugadores\" deben ser listas con los nombres de los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de jugadores."
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
      "Equipo: Real Madrid\n",
      "Jugadores ['Jugador1, Jugador2', 'Jugador3']\n",
      "Equipo: Real Sociedad\n",
      "Jugadores ['Jugador4, Jugador5', 'Jugador6']\n",
      "Equipo: Sevilla\n",
      "Jugadores ['Jugador7, Jugador8', 'Jugador9']\n"
     ]
    }
   ],
   "source": [
    "equipos = {\n",
    "    \"equipo1\": {\"nombre\": \"Real Madrid\", \"jugadores\": [\"Jugador1, Jugador2\", \"Jugador3\"]},\n",
    "    \"equipo2\": {\"nombre\": \"Real Sociedad\", \"jugadores\": [\"Jugador4, Jugador5\", \"Jugador6\"]},\n",
    "    \"equipo3\": {\"nombre\": \"Sevilla\", \"jugadores\": [\"Jugador7, Jugador8\", \"Jugador9\"]},\n",
    "}\n",
    "\n",
    "for valor in equipos.values():\n",
    "\n",
    "    nombre_equipo = valor[\"nombre\"]\n",
    "    jugadores = valor[\"jugadores\"]\n",
    "\n",
    "    print(\"Equipo:\", nombre_equipo)\n",
    "    print(\"Jugadores\", jugadores)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 25. Agrega un nuevo equipo al diccionario \"equipos\" utilizando una nueva clave y valor. La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario actualizado."
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
      "{'equipo1': {'nombre': 'Real Madrid', 'jugadores': ['Jugador1, Jugador2', 'Jugador3']}, 'equipo2': {'nombre': 'Real Sociedad', 'jugadores': ['Jugador4, Jugador5', 'Jugador6']}, 'equipo3': {'nombre': 'Sevilla', 'jugadores': ['Jugador7, Jugador8', 'Jugador9']}, 'equipo4': {'nombre': 'Valencia', 'jugadores': ['Jugador10', 'Jugador11', 'Jugador12']}}\n"
     ]
    }
   ],
   "source": [
    "equipos[\"equipo4\"] = {\"nombre\": \"Valencia\", \"jugadores\" : [\"Jugador10\",\"Jugador11\", \"Jugador12\"]}\n",
    "print(equipos)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 26. Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario \"equipos\". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado."
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
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "equipos[\"equipo1\"][\"jugadores\"].append(\"Jugador41\")\n",
    "print(equipos)"
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

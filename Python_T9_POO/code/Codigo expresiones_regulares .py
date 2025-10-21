{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Qué son las expresiones regulares?\n",
    "Las expresiones regulares (también conocidas como regex o regexp) en Python una secuencia de caracteres que define un patrón de búsqueda. Son utilizadas para buscar, extraer y manipular cadenas de texto de manera eficiente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# para trabajar con expresiones regulares \n",
    "# importaremos el modulo re\n",
    "import re"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## CONCEPTOS BASICOS"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Patrón de búsqueda\n",
    "Un patrón de búsqueda es una secuencia de caracteres que define el texto que queremos encontrar en una cadena. \n",
    "\n",
    "Por ejemplo, si deseamos buscar todas las direcciones de correo electrónico en un texto, el patrón podría ser algo como r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Caracteres especiales:\n",
    "En las expresiones regulares, algunos caracteres tienen significados especiales y se utilizan para definir el patrón. Por ejemplo:\n",
    ". (punto) coincide con cualquier carácter excepto una nueva línea.\n",
    "* (asterisco) coincide con cero o más repeticiones del carácter anterior.\n",
    "+ (más) coincide con una o más repeticiones del carácter anterior.\n",
    "\\ (barra invertida) se usa para escapar caracteres especiales y tratarlos literalmente.\n",
    "[ ] (corchetes) se usan para definir una clase de caracteres. Por ejemplo, [aeiou] coincide con cualquier vocal."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Métodos principales del módulo re:\n",
    "re.match(): Intenta hacer coincidir el patrón al principio de la cadena.\n",
    "re.search(): Busca el patrón en toda la cadena y devuelve la primera coincidencia.\n",
    "re.findall(): Busca todas las ocurrencias del patrón en la cadena y las devuelve como una lista.\n",
    "re.finditer(): Busca todas las ocurrencias del patrón en la cadena y las devuelve como un iterador.\n",
    "re.sub(): Reemplaza todas las ocurrencias del patrón con un texto dado.\n",
    "re.split(): Divide la cadena en función del patrón y devuelve una lista."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# EJEMPLO: Búsqueda de direcciones de correo electrónico"
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
      "['correoesusuario@example.com', 'otro_usuario@mail.com']\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "texto = \"Hola, mi correo es usuario@example.com y el tuyo es otro_usuario@mail.com.\"\n",
    "patron = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'\n",
    "\n",
    "direcciones_correo = re.findall(patron, texto)\n",
    "print(direcciones_correo)\n",
    "\n",
    "#En este ejemplo, re.findall() encuentra todas las direcciones de correo electrónico \n",
    "# que coinciden con el patrón y las devuelve como una lista."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# r (raw string):\n",
    "La r al inicio de la expresión regular indica que es una raw string, lo cual significa que los caracteres especiales dentro de la cadena no serán interpretados de manera especial por Python, lo que es especialmente útil para expresiones regulares."
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
      "Hola\n",
      "Mundo\n",
      "Hola\\nMundo\n"
     ]
    }
   ],
   "source": [
    "# Cadena normal sin procesar\n",
    "cadena_normal = \"Hola\\nMundo\"\n",
    "print(cadena_normal)  \n",
    "                      \n",
    "\n",
    "# Cadena raw string sin procesar\n",
    "cadena_raw = r\"Hola\\nMundo\"\n",
    "print(cadena_raw)     "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# \\b (word boundary):\n",
    "\\b es un delimitador que coincide con una posición en la cadena donde comienza o termina una palabra (es decir, donde hay un límite de palabra). No coincide con un carácter, sino con una posición en la cadena. Esto ayuda a asegurar que el patrón coincida con direcciones de correo electrónico completas y no con partes de palabras.\n"
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
      "['mundo', 'mundo']\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "cadena = \"hola mundo y otro mundo más y mundo123\"\n",
    "patron = r'\\bmundo\\b'\n",
    "\n",
    "ocurrencias = re.findall(patron, cadena)\n",
    "print(ocurrencias)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# [A-Za-z0-9._%+-]+:\n",
    "[A-Za-z0-9._%+-] es una clase de caracteres que coincide con letras mayúsculas y minúsculas, dígitos y algunos caracteres especiales como ., _, %, +, y -.\n",
    "El + después de la clase de caracteres indica que el carácter o conjunto de caracteres que lo preceden deben aparecer una o más veces en la cadena."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# @:\n",
    "El símbolo @ coincide literalmente con el carácter @. En las direcciones de correo electrónico, este carácter separa el nombre de usuario y el dominio.\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# [A-Za-z0-9.-]+:\n",
    "[A-Za-z0-9.-] es otra clase de caracteres que coincide con letras mayúsculas y minúsculas, dígitos y los caracteres . y -.\n",
    "El + indica que el carácter o conjunto de caracteres que lo preceden deben aparecer una o más veces en la cadena.\n",
    "En esta parte, estamos buscando el dominio del correo electrónico."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# .:\n",
    "El \\. coincide con un punto literal (.). El punto en una expresión regular normalmente coincide con cualquier carácter, pero al utilizar \\, estamos escapando el carácter especial . y buscando un punto literal en la cadena. Esto asegura que coincida con el punto que separa el dominio de nivel superior (TLD) del resto del dominio."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# [A-Z|a-z]{2,}:\n",
    "[A-Z|a-z] es una clase de caracteres que coincide con cualquier letra mayúscula o minúscula.\n",
    "{2,} indica que el carácter o conjunto de caracteres que lo preceden debe aparecer al menos dos veces en la cadena. En este caso, estamos buscando el TLD del dominio, que debe tener al menos dos letras."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# \\b (word boundary):\n",
    "Otro delimitador \\b que asegura que la expresión termine con un límite de palabra."
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

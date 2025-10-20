```python
"""
DOCUMENTACIÓN DEL VIDEO: Cómo configurar el PATH y cambiar entre diferentes versiones/ejecutables de Python (Mac y Linux)

Este tutorial busca solucionar problemas comunes que surgen al usar Python en la terminal, incluyendo:
1. Que la máquina no reconozca el comando 'python'.
2. Que se ejecute una versión antigua de Python, impidiendo usar características modernas (como las f-strings de Python 3.6).
3. Errores de importación (ImportError) de paquetes instalados con pip, lo cual suele ser un problema de que la máquina no está usando el intérprete de Python correcto.

El problema principal radica en que el sistema operativo no localiza el intérprete correcto en la variable de entorno 'PATH'.
"""

# python
"""
Se ejecuta el comando 'python' para ver qué versión está configurada por defecto.
En el ejemplo, se muestra que está usando Python 2.
"""

# exit()
"""
Sale del intérprete de Python.
"""

# python3
"""
En Mac y Linux, al instalar Python 3, a menudo se le asigna el comando 'python3' en lugar de sobrescribir 'python'.
Si este comando funciona, significa que el sistema encontró el comando 'python3' en el PATH.
"""

# exit()
"""
Sale del intérprete de Python 3.
"""

# which python3
"""
Se utiliza el comando 'which' para encontrar la ubicación exacta del ejecutable del comando 'python3' en la máquina (ejemplo: /usr/local/bin/python3).
"""

# type python3
"""
El comando 'type' es una alternativa a 'which' que funciona bien tanto con comandos directos como con 'aliases' (apodos), lo que lo hace más útil.
Muestra la ubicación del comando.
"""

# echo $PATH
"""
Muestra el valor actual de la variable de entorno 'PATH'. Esta variable contiene una lista de directorios separados por dos puntos (:) donde la máquina busca comandos.
La búsqueda se realiza en el orden en que aparecen los directorios en esta lista.
Si el directorio de un comando deseado no está en el PATH, o si encuentra una versión diferente antes, el comando no funcionará o utilizará la versión incorrecta.
"""

# /usr/local/bin/python3
"""
Se ejecuta Python utilizando la ruta completa (full path) al ejecutable.
Esta es una forma de ejecutar un programa cuyo directorio no está incluido en la variable PATH.
"""

# LS anaconda/bin
"""
Ejemplo de listar el contenido de un directorio donde se sabe que hay un ejecutable de Python (como el directorio 'bin' de una instalación de Anaconda).
"""

# anaconda/bin/python
"""
Ejecución de una versión de Python que no está en el PATH, utilizando su ruta completa (ejemplo: versión de Anaconda).
Si este comando se ejecutara como solo 'python', se usaría la versión que sí está en el PATH (en el ejemplo, Python 2).
"""

# cd
"""
Navega al directorio de inicio (home folder) del usuario. Es el lugar donde se encuentran los archivos de configuración del shell.
"""

# nano .bash_profile
"""
Abre el archivo de configuración del shell en el editor 'nano' (para Mac).
En Linux, el archivo de configuración equivalente suele ser '.bashrc'.
Estos archivos se utilizan para hacer permanentes los cambios en el PATH o para configurar aliases. Si el archivo no existe, se puede crear.
"""

"""
Para agregar manualmente un directorio al PATH dentro de .bash_profile (o .bashrc):
Se utiliza la sintaxis 'VARIABLE=VALOR' sin espacios alrededor del '=' (así es como funciona Bash).

Ejemplo de cómo se agrega una ruta (aquí se usa el ejemplo del video que prioriza Python 3.7):
PATH=/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}

1. Se especifica la ruta completa al directorio que contiene el ejecutable de Python 3.7.
2. Se usa un colon (:) como separador de directorios.
3. Se añade la variable '${PATH}' (la ruta actual) al final de la cadena.
Esto es fundamental; si se omite, se reestablecería el PATH entero solo a la nueva ruta, perdiendo todos los demás comandos.
4. El nuevo directorio se coloca al inicio de la cadena para que tenga la mayor prioridad.

export PATH
Esta línea se agrega para exportar y establecer el nuevo valor de la variable PATH.
"""

# (Ctrl + X)
# (Y)
# (Enter)
"""
Comandos para guardar las modificaciones realizadas en el editor Nano.
Se necesita reiniciar la terminal para que los cambios en el PATH surtan efecto.
"""

# echo $PATH
"""
Después de reiniciar, se verifica que la nueva y larga ruta de Python 3.7 se encuentra al principio del PATH, asegurando su prioridad.
"""

# type python3
"""
Verifica que 'python3' ahora apunta a la ubicación que se agregó al PATH.
"""

# alias python=python3
"""
Crea un alias (apodo) para que el comando 'python' ejecute la versión 'python3'.
Esto permite que los usuarios usen 'python' en lugar de 'python3' para acceder a la versión más reciente.
Al igual que con el PATH, no deben existir espacios entre 'alias', 'python', '=' y 'python3'.
Para que este alias sea permanente, debe ser añadido al archivo '.bash_profile' (o .bashrc).
"""

# type python
"""
Verifica que 'python' es ahora un alias que apunta a 'python3'.
"""

# alias pip=pip3
"""
Si la instalación de Python 3 usa 'pip3', se debe crear un alias para que 'pip' apunte a 'pip3'.
Esto ayuda a asegurar que los paquetes se instalen para la versión correcta de Python.
Este alias también debe ser permanente en '.bash_profile'.
"""

# type pip
"""
Verifica que 'pip' está configurado como un alias a 'pip3'.
"""

# pip list
"""
Se utiliza para probar si el comando 'pip' ahora funciona correctamente, listando los paquetes instalados.
"""

# python
# import sys
# sys.executable
"""
Dentro del intérprete de Python, se puede usar el módulo 'sys' (un módulo incorporado que no necesita instalación) para ver la ubicación exacta del intérprete de Python que se está ejecutando.
Esto es especialmente útil cuando hay muchas versiones o entornos virtuales que usan la misma versión de Python (ej: 3.7) y se necesita saber cuál es el ejecutable específico.
Si la ruta no es la esperada, es indicio de que se debe revisar y potencialmente reordenar el PATH.
"""

# exit()
"""
Sale del intérprete de Python.
"""

# pip install Django
"""
Ejemplo de instalación de un paquete.
Si se instala un paquete pero luego no se puede importar (ImportError), es probable que 'pip' esté instalando el paquete para una versión de Python diferente a la que se está usando.
"""

# pip show Django
"""
Muestra información detallada de un paquete instalado, incluyendo la ruta donde se encuentra el paquete (el directorio 'site-packages').
Es crucial que esta ubicación coincida con el directorio de 'sys.executable' para la versión de Python que se está utilizando.
"""

"""
Manejo de Entornos Virtuales:
Un entorno virtual permite tener ejecutables y paquetes de Python separados por proyecto.
Al activar un entorno virtual en la línea de comandos, el código de activación añade y elimina automáticamente el directorio 'bin' del entorno al principio del PATH, por lo que no es necesario configurarlo manualmente.
"""

# source anaconda/bin/activate flask_blog
"""
Comando de ejemplo para activar un entorno virtual (en este caso, un entorno conda llamado 'flask_blog').
El nombre del entorno aparece entre paréntesis al activarse.
"""

# which python
"""
Una vez activo el entorno, se verifica que 'python' apunta al ejecutable dentro del directorio 'bin' del entorno virtual recién activado.
"""

# echo $PATH
"""
Se confirma que el directorio 'bin' del entorno virtual ha sido agregado automáticamente al inicio del PATH, dándole la prioridad máxima.
"""

"""
Configuración en Editores/IDEs:
Los editores de código (como Sublime Text) pueden no usar la misma versión de Python que la línea de comandos, ya que a veces tienen métodos diferentes para determinar el ejecutable.
En editores como Sublime Text, se utiliza un sistema llamado 'build systems'.
Para configurar correctamente un editor o IDE, se debe usar la ruta completa al ejecutable de Python (o del entorno virtual) que se determinó previamente con 'sys.executable'.
"""
```
# ==============================================================================
# PROCESO DE GESTIÓN DE PROYECTOS Y ENTORNOS VIRTUALES CON CONDA (MAC/LINUX)
# ==============================================================================

# NOTA IMPORTANTE: Los comandos a continuación son comandos de terminal (Bash/Conda)
# que deben ejecutarse en la línea de comandos, no código Python ejecutable.

# ------------------------------------------------------------------------------
# FASE 1: CREACIÓN DEL PROYECTO Y EL ENTORNO VIRTUAL
# ------------------------------------------------------------------------------
# Activar conda (si no está activado):
#source /Users/francisconavarroguardiola/opt/anaconda3/etc/profile.d/conda.sh


# 1. CREAR EL DIRECTORIO DEL NUEVO PROYECTO
# Comando: mkdir my_project
# Propósito: Crea un directorio vacío llamado 'my_project' para el nuevo proyecto [1].
paso_1_comando_1 = "mkdir my_project"
paso_1_explicacion_1 = "Crea el directorio del proyecto."

# Comando: cd my_project
# Propósito: Cambia al directorio recién creado [1].
paso_1_comando_2 = "cd my_project"
paso_1_explicacion_2 = "Navega al directorio del proyecto."

# 2. CREAR EL ENTORNO VIRTUAL USANDO CONDA
# Comando de ejemplo (creando un entorno con Python, Flask, SQLAlchemy, Numpy y Pandas):
# conda create --name my_project_env flask sqlalchemy numpy pandas
# Propósito: Crea un nuevo entorno virtual llamado 'my_project_env', especificando
# las dependencias iniciales (paquetes y versión de Python) que se desean utilizar [1].
paso_2_comando = "conda create --name my_project_env flask sqlalchemy numpy pandas"
paso_2_explicacion = "Crea el entorno virtual de Conda con las dependencias iniciales."

# 3. ACTIVAR EL ENTORNO VIRTUAL
# Comando: source activate my_project_env
# Propósito: Activa el entorno virtual. Esto añade el nombre del entorno al 'prompt'
# de la terminal, indicando que se está trabajando dentro del entorno [2, 3].
paso_3_comando = "source activate my_project_env"
paso_3_explicacion = "Activa el entorno virtual del proyecto."

# 4. EXPORTAR EL ENTORNO A UN ARCHIVO YAML
# Comando: conda env export > environment.yaml
# Propósito: Captura toda la información del entorno, incluyendo el nombre y las
# dependencias con sus versiones exactas, en el archivo 'environment.yaml' [2, 4].
# Este archivo permite que otra persona (o el usuario mismo) pueda recrear
# exactamente el mismo entorno desde cero con un solo comando [4].
paso_4_comando = "conda env export > environment.yaml"
paso_4_explicacion = "Exporta la configuración completa del entorno a un archivo YAML."

# ------------------------------------------------------------------------------
# FASE 2: GESTIÓN DE VARIABLES DE ENTORNO ESPECÍFICAS DEL PROYECTO
# ------------------------------------------------------------------------------

# Para manejar variables de entorno específicas del proyecto (como URLs de bases de
# datos o claves secretas), se utilizan scripts que se ejecutan al activar o
# desactivar el entorno de Conda [5].

# 5. ENCONTRAR Y NAVEGAR A LA UBICACIÓN DEL ENTORNO
# Comando: conda env list
# Propósito: Lista todos los entornos Conda instalados y muestra la ubicación
# de los directorios de los entornos [6, 7].
paso_5_comando_1 = "conda env list"
paso_5_explicacion_1 = "Lista los entornos y muestra su ubicación en el sistema de archivos."

# Comando: cd [ubicación del entorno virtual]
# Propósito: Cambia el directorio a la ubicación del entorno virtual [6, 7].
paso_5_comando_2 = "cd /path/to/my_project_env"
paso_5_explicacion_2 = "Navega al directorio raíz del entorno virtual."

# 6. CREAR LOS DIRECTORIOS PARA SCRIPTS DE ACTIVACIÓN Y DESACTIVACIÓN
# Comando (Activación): mkdir -p etc/conda/activate.d
# Propósito: Crea la estructura de directorios necesaria para albergar scripts
# que se ejecutarán cuando el entorno se active [6, 8].
paso_6_comando_1 = "mkdir -p etc/conda/activate.d"
paso_6_explicacion_1 = "Crea el directorio para los scripts de activación."

# Comando (Desactivación): mkdir -p etc/conda/deactivate.d
# Propósito: Crea la estructura de directorios para albergar scripts
# que se ejecutarán cuando el entorno se desactive [8].
paso_6_comando_2 = "mkdir -p etc/conda/deactivate.d"
paso_6_explicacion_2 = "Crea el directorio para los scripts de desactivación."

# 7. CREAR LOS ARCHIVOS DE SCRIPT PARA LAS VARIABLES DE ENTORNO
# Comando (Activación): touch etc/conda/activate.d/env_vars.sh
# Propósito: Crea el archivo de script que contendrá las variables a *establecer* [8].
paso_7_comando_1 = "touch etc/conda/activate.d/env_vars.sh"
paso_7_explicacion_1 = "Crea el archivo shell para establecer variables al activar."

# Comando (Desactivación): touch etc/conda/deactivate.d/env_vars.sh
# Propósito: Crea el archivo de script que contendrá las variables a *desestablecer* [8].
paso_7_comando_2 = "touch etc/conda/deactivate.d/env_vars.sh"
paso_7_explicacion_2 = "Crea el archivo shell para desestablecer variables al desactivar."

# 8. EDITAR LOS ARCHIVOS DE SCRIPT
# Estos archivos de shell definen las variables (export) y las eliminan (unset).

# Contenido del script de ACTIVACIÓN (etc/conda/activate.d/env_vars.sh):
paso_8_script_activate = """
#!/bin/sh
export DATABASE_URI="postgre://user:password@hostname:port/testDB"
"""
paso_8_explicacion_activate = "Al activar el entorno, se establece la variable DATABASE_URI [9]."

# Contenido del script de DESACTIVACIÓN (etc/conda/deactivate.d/env_vars.sh):
paso_8_script_deactivate = """
#!/bin/sh
unset DATABASE_URI
"""
paso_8_explicacion_deactivate = "Al desactivar el entorno, se elimina (unset) la variable DATABASE_URI [3]."

# 9. VERIFICACIÓN (RE-ACTIVACIÓN Y PRUEBA)
# Comando: source deactivate
# Propósito: Desactiva el entorno actual, ejecutando el script de desactivación [3].
paso_9_comando_1 = "source deactivate"

# Comando: source activate my_project_env
# Propósito: Reactiva el entorno, ejecutando el script de activación [3].
paso_9_comando_2 = "source activate my_project_env"

# Comando: echo $DATABASE_URI
# Propósito: Muestra el valor de la variable de entorno, verificando que se haya establecido
# correctamente tras la activación [3].
paso_9_comando_3 = "echo $DATABASE_URI"

# ------------------------------------------------------------------------------
# FASE 3: AUTOMATIZACIÓN DE LA ACTIVACIÓN DE ENTORNOS (PASO OPCIONAL/AVANZADO)
# ------------------------------------------------------------------------------

# Para evitar olvidar activar o desactivar entornos al cambiar de proyecto [10],
# se configura una función bash que activa el entorno automáticamente al navegar
# a un directorio que contenga un archivo 'environment.yaml' [10-12].

# 10. EDITAR EL ARCHIVO DE PERFIL DE BASH (por ejemplo, ~/.bash_profile)
# Comando de edición: nano ~/.bash_profile (o usar otro editor de texto como Sublime) [11].

# Acción: Definir la función `conda_auto_env` y exportar `PROMPT_COMMAND`.

# La función `conda_auto_env` verifica si el archivo `environment.yaml` existe,
# extrae el nombre del entorno de dicho archivo, y si el usuario no está ya
# en ese entorno, lo activa automáticamente usando `source activate` [11, 13].

# Contenido para agregar al .bash_profile:
paso_10_funcion_bash = """
# Definición de la función de auto-activación de Conda
# (El contenido completo de la función se encuentra en las fuentes,
# pero su objetivo es: buscar environment.yaml, obtener el nombre del entorno,
# y activar si no está activo) [11, 13].
# Auto activate conda environments
function conda_auto_env() {
  if [ -e "environment.yaml" ]; then
    ENV_NAME=$(head -n 1 environment.yaml | cut -f2 -d ' ')
    # Check if you are already in the environment
    if [[ $CONDA_PREFIX != *$ENV_NAME* ]]; then
      # Try to activate environment
      source activate $ENV_NAME &>/dev/null
    fi
  fi
}

export PROMPT_COMMAND="conda_auto_env;$PROMPT_COMMAND"
# Establecer la variable PROMPT_COMMAND para ejecutar la función antes de cada prompt:
export PROMPT_COMMAND="conda_auto_env"
"""
paso_10_explicacion = "Establece la función 'conda_auto_env' para que se ejecute antes de cada solicitud de comando (prompt), activando automáticamente el entorno correcto al navegar a la carpeta del proyecto que contiene el 'environment.yaml' [11, 12, 14]."

# 11. REINICIAR LA TERMINAL
# Propósito: Cargar las nuevas configuraciones definidas en el archivo de perfil de Bash [13].
paso_11_accion = "Salir y volver a abrir la terminal."

# 12. VERIFICACIÓN DE LA ACTIVACIÓN AUTOMÁTICA
# Comando: cd /path/to/my_project
# Propósito: Al navegar a la carpeta que contiene el `environment.yaml` (si está bien
# escrito), el entorno se activa automáticamente [14].
paso_12_comando = "cd my_project"
paso_12_explicacion = "Al navegar a la carpeta del proyecto, el entorno se activa automáticamente, cambiando la versión de Python, las dependencias y configurando las variables de entorno [12, 14]."
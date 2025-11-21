# Ejercicios Progresivos de Expresiones Regulares

A continuación se presentan todos los ejercicios generados para
practicar RegEx en Python, organizados de forma progresiva desde nivel
básico hasta nivel profesional.

------------------------------------------------------------------------

## 🔹 NIVEL 1 --- Fundamentos (caracteres literales, escapes, secuencias especiales)

### **Ejercicio 1 -- Coincidencia literal sencilla**

Encuentra todas las ocurrencias exactas del texto:

    INFO

dentro del siguiente contenido:

    INFO: Inicio del proceso
    Error: información no disponible
    UserINFO: registro completo
    INFO

------------------------------------------------------------------------

### **Ejercicio 2 -- Escapar metacaracteres**

Detecta todas las cadenas que contengan el símbolo literal `+`:

    3+5=8
    Hello+World
    Increment++
    C++ language
    A+B no se captura

Capta únicamente las líneas donde el símbolo `+` aparece **literalmente
al menos una vez**, ignorando las que contienen `++`.

------------------------------------------------------------------------

### \*\*Ejercicio 3 -- Uso de secuencias `\d,`{=tex} `\w`{=tex}, `\s*`{=tex}\*

Dado este texto:

    ID001 Pedro 29
    ID014 Ana 33
    XYZ77 Juan 41
    AB_11 Luis   50

Escribe una expresión regular que capture: - un identificador (`\w+`) -
un nombre compuesto solo por letras - una edad de 2 dígitos

------------------------------------------------------------------------

## 🔹 NIVEL 2 --- Anclas, límites de palabra y patrones estructurados

### **Ejercicio 4 -- Uso de \^ y \$**

Valida que las siguientes líneas son únicamente códigos hexadecimales de
6 caracteres:

    A4FF20
    #A4FF20
    A4F
    FFFEEE1
    12DF9B

------------------------------------------------------------------------

### \*\*Ejercicio 5 -- Límites de palabra `\b**`{=tex}

Encuentra todas las palabras que empiecen exactamente con "pre":

    predecir
    aprender
    prevenir
    sorpresa
    preguntar
    emprender

------------------------------------------------------------------------

### \*\*Ejercicio 6 -- No límite de palabra `\B*`{=tex}\*

Encuentra todas las apariciones de "bar" donde **no** empiece la
palabra:

    barril
    disbarate
    barba
    submarino
    tubarada

------------------------------------------------------------------------

## 🔹 NIVEL 3 --- Conjuntos, rangos y negaciones

### **Ejercicio 7 -- Conjuntos y rangos**

Identifica caracteres del 4 al 7 y letras de f a k:

    abc4567XYZ-fghijk000

------------------------------------------------------------------------

### **Ejercicio 8 -- Negaciones en conjuntos**

Encuentra palabras que terminen en `at` excepto las que empiezan por `b`
o `c`:

    gat mat pat bat rat fat cat sat

------------------------------------------------------------------------

## 🔹 NIVEL 4 --- Cuantificadores

### **Ejercicio 9 -- Cuantificadores exactos**

Valida códigos: - 2 letras mayúsculas - 4 dígitos

------------------------------------------------------------------------

### **Ejercicio 10 -- + y **\*

Captura secuencias de dos o más signos `!`:

    Hola!!!!!  
    WOW!  
    Hey!!!a  

------------------------------------------------------------------------

### **Ejercicio 11 -- ? (opcional)**

Valida matrículas antiguas españolas:

    M-1234
    AB-1234
    B1234
    ABC-9999

------------------------------------------------------------------------

## 🔹 NIVEL 5 --- Grupos y alternancias

### **Ejercicio 12 -- Alternancias**

De este texto:

    Dr. House
    Prof Smith
    Ing. Torres
    Dra Lopez
    Profesor Martín

Captura solo títulos formales: - Dr. - Dra - Prof - Ing.

------------------------------------------------------------------------

### **Ejercicio 13 -- Captura de correos**

Extrae usuario, dominio y TLD:

    juan23@mail.com
    maria.santos@empresa.org
    root@localhost.local
    ventas-online@tienda.es

------------------------------------------------------------------------

### **Ejercicio 14 -- Grupos de teléfonos**

Extrae tres grupos: 1. código de país (opcional) 2. área (opcional) 3.
número De:

    (321) 555-8999
    +54 11 4555-8899
    555-8999
    0044 20 7946 0991

------------------------------------------------------------------------

## 🔹 NIVEL 6 --- Sustituciones y limpieza

### **Ejercicio 15 -- Sustitución de fechas**

Convierte dd/mm/yyyy → yyyy-mm-dd:

    23/01/2024
    5/12/2023
    01/01/2025

------------------------------------------------------------------------

### **Ejercicio 16 -- Eliminar HTML**

    <div><p>Hola <b>mundo</b></p></div>

------------------------------------------------------------------------

### **Ejercicio 17 -- Normalizar espacios**

    Este   texto   tiene     espacios   irregulares.

------------------------------------------------------------------------

## 🔹 NIVEL 7 --- Uso profesional

### **Ejercicio 18 -- Validación IPv4**

Valida direcciones IPv4 estrictas.

------------------------------------------------------------------------

### **Ejercicio 19 -- Validación de contraseñas**

Reglas: - 8+ caracteres - mayúscula - minúscula - número - símbolo

------------------------------------------------------------------------

### **Ejercicio 20 -- Análisis de logs**

Extrae: - fecha - hora - nivel - módulo - mensaje

    [2025-01-05 11:33:21] ERROR (moduleA): File not found
    [2025-01-05 11:33:25] INFO (moduleB): Started process
    [2025-01-05 11:33:40] WARNING (core): Low memory

------------------------------------------------------------------------

### **Ejercicio 21 -- Analizador JSON simplificado**

Extrae pares clave--valor de:

    {
      "user": "juan",
      "age": 30,
      "email": "juan@mail.com"
    }

------------------------------------------------------------------------

### **Ejercicio 22 -- Normalizar URLs**

Transforma:

    HTTPS://Example.COM/page
    http://blog.example.com
    www.Example.org

En versiones normalizadas con: - https:// obligatorio - minúsculas

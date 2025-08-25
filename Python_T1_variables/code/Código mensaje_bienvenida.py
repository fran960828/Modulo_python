# --- pedir nombre de usuario ----
#print("¿Cómo te llamas?")
#nombre = input()
nombre = input("¿Cómo te llamas? ") # de tipo string

# --- Reformatear nombre ---
nombre = nombre.replace(".", "")

# --- Escribimos mensaje en una variable ---
lenguaje = 'python'
mensaje = "¡Hola, " + nombre.title() + ", estás usando " + lenguaje.title() + "!"

# --- imprimimos el mensaje por pantalla ---
print(mensaje)

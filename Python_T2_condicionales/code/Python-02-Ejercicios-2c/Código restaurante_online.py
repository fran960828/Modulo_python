# --- Pedir al usuario el tipo de hamburguesa
hamburguesa = input("Que tipo de hamburguesa quieres? (clasica/vegana): ")

# --- Comprobamos que hamburguesa ha pedido el usuario
# Si ha elegido la clasica
if hamburguesa.lower() == "clasica":
    ## Ofrecemos la opción de elegir un ingresiente extra: queso, bacon, huevo
    ingrediente_extra = input("Los ingredientes extra disponibles son: Queso idiazabal, Bacon, Huevo. Elige un ingrediente extra. ") 
    ## Imprimiremos que tipo de hamburguesa ha elegido
    if ingrediente_extra.lower() == "queso idiazabal":
        print("Has elegido una hamburguesa clasica con queso idiazabal")
    elif ingrediente_extra.lower() == "bacon":
        print("Has elegido una hamburguesa clasica con bacon")
    elif ingrediente_extra.lower() == "huevo":
        print("Has elegido una hamburguesa clasica con huevo")
    else:
        print("El ingrediente selecionado no esta disponible")

#Si ha elegido la vegana
elif hamburguesa.lower() == "vegana":
## Ofrecemos la opción de elegir un ingresiente extra: tofu, cebolla caramelizada
    ingrediente_extra = input("Los ingredientes extra disponibles son: Tofu,Cebolla caramelizada. Elige un ingrediente extra. ") 
    ## Imprimiremos que tipo de hamburguesa ha elegido
    if ingrediente_extra.lower() == "tofu":
        print("Has elegido una hamburguesa vegana con tofu")
    elif ingrediente_extra.lower() == "cebolla caramelizada":
        print("Has elegido una hamburguesa vegana con cebolla caramelizada")
    else:
        print("El ingrediente selecionado no esta disponible")

#Si no elige ninguna de las dos
else:
    ## Imprimiremos un mensaje de error
    print("Ese tipo de hamburguesa no esta disponible. Por favor vuelve a iniciar tu pedido ")
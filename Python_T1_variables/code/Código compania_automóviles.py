# --- Preguntar al usuario cuantos coches ha vendido de cada tipo ---
rbm_serie1_vendidos = int(input("¿Cuántos RBM serie 1 has vendido? "))
rbm_plus_vendidos = int(input("¿Cuántps RBM plus has vendido? "))
rbm_todoterreno_vendidos = int(input("¿Cuántos RBM todoterreno has vendido?"))

# --- Guardamos los datos en variables ---
precio_rbm_serie1 = 20000
precio_rbm_plus = 35000
precio_rbm_todoterreno = 60000

comision_rbm_serie1 = 0.03
comision_rbm_plus = 0.05
comision_rbm_todoterreno = 0.07

# --- Calculamos la cantidad de euros a comisionar ese mes ---
ganancia_rbm_serie_1 = rbm_serie1_vendidos * precio_rbm_serie1 * comision_rbm_serie1
ganancia_rbm_plus = rbm_plus_vendidos * precio_rbm_plus * comision_rbm_plus
ganancia_rbm_todoterreno = rbm_todoterreno_vendidos * precio_rbm_todoterreno * comision_rbm_todoterreno

ganancia_total = ganancia_rbm_serie_1 + ganancia_rbm_plus + ganancia_rbm_todoterreno 

# --- Imprimimos la ganancia total ---

print("La cantidad total de euros a comisionar este més es de ", ganancia_total, "euros")
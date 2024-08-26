#12) Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia
#laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida
#que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor
#nuevamente. 
dia=int(input("Ingrese un dia de la semana"))
if dia < 1 or dia > 7:
    print("El valor ingresado no corresponde a un dia de la semana! ")
elif dia < 6:
    print("Es un dia LABORABLE")
else:
    print("Es un dia NO LABORABLE")


#12) Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia
#laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida
#que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor
#nuevamente. 

dia=int(input("Ingrese un dia de la semana: "))
while True:
    if dia <= 0 or dia > 7:
        dia = int(input("Valor no válido, vuelva a intentar: "))
        pass
    elif dia < 6:
        print("Es un dia LABORABLE")
        break
    else:
        print("Es un dia NO LABORABLE")
        break

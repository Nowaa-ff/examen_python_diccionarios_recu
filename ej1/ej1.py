notas= {
    "Smaha": [],
    "Iglesias": [],
    "Fischer": [],
    "Villalobos": [],
    "Olguin": []
}
menu= {
    1 : "Ver todas las notas.",
    2 : "Ver las notas de un alumno.",
    3 : "Cargar notas. ",
    4 : "Cargar promedio",
    5 : "Salir. "
}

while True: 
    print ("------------ Menu ------------")
    for key, value in menu.items():
        print(key, ": ", value)
    opcion=int(input("Elija una opcion \n -"))
    if opcion == 1:
        print ("------- Notas cargadas -------")
        for key, value in notas.items():
            print(key, ": ", value)
    elif opcion == 2:
        alumno = input("Ingrese el nombre del alumno: \n -")
        if alumno in notas:
            print(alumno, ": ", notas[alumno])
        else:
            print("No existe ese alumno.")
    elif opcion ==3:
        alumno_cargar=str(input("Ingrese el alumno al que le desea cragar una nota: \n -"))
        if alumno_cargar in notas:
            nota_cargar=int(input(f"Ingrese la nota del alumno {alumno_cargar} \n -"))
            notas[alumno_cargar].append(nota_cargar)
        else:
            print("No existe ese alumno.")
    elif opcion == 4:
        alumno_prom=str(input("Ingrese el alumno del cual quiere ver el promedio: \n -"))
        if alumno_prom in notas:
            suma=0
            for nota in notas[alumno_prom]:
                suma = suma +nota
            print(f"El promedio de {alumno_prom} es: {suma/5}")
            
        else:
            print("Ese alumno no existe...")
    elif opcion == 5:
        print ("Saliendo del programa...")
        break
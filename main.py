# Byron
# Isaac


juegos_Terminados=[]
juegos_en_progreso=[]
juegos_platinados=[]




def agregar_juego():
    while True:
        try:
            size=int(input("Ingrese la cantidad de juegos a agregar: "))
            if size <= 0:
                print("Ingrese numero valido")
                continue
            break
        except ValueError:
            print("Ingrese solo numeros: ")
            continue
        
    for j in range(size):
        nombre=input("Ingrese nombre de juego: ")
            
        plataforma=input("Ingrese nombre de plataforma del juego: ")
            
        estado=input("Ingrese estado del juego (Terminado, Progreso o Platinado): ").lower()
        
        
        
        genero=input("Ingrese genero del juego: ")
        
        while True:
          try:    
              precio=float(input(f"Ingrese precio de {nombre}: "))
              if precio <= 0:
                 print("Precio invalido")
                 continue
              break
          except ValueError:
              print("Ingrese solo numeros")
              continue
        
    
        if estado == "terminado":
            juegos_Terminados.append(nombre)
                
        elif estado == "progreso":
           juegos_en_progreso.append(nombre)
            
        elif estado == "platinado":
           juegos_platinados.append(nombre)
           juegos_Terminados.append(nombre)
        
    print(f"{nombre} agregado exitosamente")
        


opcion= 0

while opcion != 5:
    
    print("\n====================================")
    print("CONTROL DE VENTAS DE VIDEOJUEGOS")
    print("\n====================================")
    
     
    print("1.Agregar juego")
    print("2.Ver cantidad de juegos")
    print("3.ver precio")
    print("4.eliminar juego")
    print("5.Ver todos los juegos")
    print("6.salir")
    
    opcion=int(input("ingrese la opcion a la que quiera ingresar: "))
    
    if opcion == 1:
        agregar_juego()

        
        
       


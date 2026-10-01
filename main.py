# Byron
# Isaac


juegos_Terminados=[]
juegos_en_progreso=[]
juegos_platinados=[]
total_juegos=[]



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
        
    elif opcion == 2:
         print(f"la cantidad de juegos son, ")
         
    elif opcion == 3:
        precio=input("ingrese el juego al que quiera ver el precio: ")
        
        if precio not in total_juegos:
            print("el juego no esta en la lista")
        
            
            
            
    elif opcion == 4:
         for i in range(len(total_juegos)):
            print(total_juegos)
                                        
         eliminar_juego= float(input("ingrese el juego que quiera eliminar"))
        
         if eliminar_juego in total_juegos:
            total_juegos.remove(eliminar_juego)
         else:
            print("nota no registrada")
            
         for i in range(len(total_juegos)):
            print(total_juegos)
            
    # elif opcion == 5:
        
        
        
    elif opcion == 6:
        print("haz salido del sistema")
        break
    
        
        
            
        
         
   
        
        
    
    
   
        

        
        
       


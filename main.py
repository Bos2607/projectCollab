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


            juegos_Terminados.append((nombre,plataforma,estado,genero,precio))
            total_juegos.append(juegos_Terminados)
                
        elif estado == "progreso":
           juegos_en_progreso.append((nombre,plataforma,estado,genero,precio))
           total_juegos.append(juegos_en_progreso)
        
        elif estado == "platinado":
           juegos_platinados.append((nombre,plataforma,estado,genero,precio))
           total_juegos.append(juegos_platinados)

           

        

    print(f"{nombre} agregado exitosamente")
    
def cantidad_juegos():
    
    suma=len(juegos_en_progreso) + len(juegos_platinados) + len(juegos_Terminados)
    
    print(f"Cantidad de juegos actuales: {suma}")

def ver_precios():
    pass

opcion= 0

while opcion != 5:
    
    print("\n====================================")
    print("CONTROL DE VENTAS DE VIDEOJUEGOS")
    print("\n====================================")
    
     
    print("1.Agregar juego")
    print("2.Ver cantidad de juegos")
    print("3.ver precios de juegos")
    print("4.eliminar juego")
    print("5.Ver todos los juegos")
    print("6.salir")
    
    opcion=int(input("ingrese la opcion a la que quiera ingresar: "))
    
    if opcion == 1:
        agregar_juego()
        
    elif opcion == 2:
        cantidad_juegos()
         
         
    elif opcion == 3:
        pass
            
            
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

    #     if not total_juegos:
    #         print("no hay juegos en venta")
    #     else:
    #         print
            
        


    elif opcion == 5:
        pass

        
        
    elif opcion == 6:
        print("haz salido del sistema")
        break
    
    
        
            
        
         
   
        
        
    
    
   
        

        
        
       

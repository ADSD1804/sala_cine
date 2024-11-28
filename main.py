from usuarios.comprar_ticket import realizar_compra
from usuarios.create_user import ingresar_usuario
from usuarios.read_user import leer_usuario
from usuarios.update_user import actualizar_usuario
from usuarios.delete_user import borrar_usuario

while True:
    op=int(input('''
                Bienvenido al gestor de usuarios

                1.crear usuario
                2.buscar usuario
                3.actualizar usuario
                4.borrar usuario
                5.salir
                6.comprar pelicula
                opcion:  '''))
    
    
    match op:

        case 1:
            ingresar_usuario()
            
        case 2:
            cedula=input("Ingrese la cedula del usuario: ")
            leer_usuario(cedula)
            
        case 3:
            cedula=input("Ingrese la cedula del usuario a editar: ")
            leer_usuario(cedula)
            if cedula:
                nuevo_email=input("Ingrese el nuevo email o presione enter para continuar: ")
                nueva_edad=input("ingrese la nueva edad o presione enter para continuar: ")

                nuevas_hablidades=[]

                while True:
                    habilidad=input("ingrese una nueva hablidad o enter para terminar: ")
                    if habilidad:
                        nuevas_hablidades.append(habilidad)
                    else:
                        break
            actualizar_usuario(nombre,nuevo_email,nueva_edad,nuevas_hablidades if nuevas_hablidades else None)
    
        case 4:
            nombre=input("ingrese el nombre del usuario que desea buscar: ")
            confirmar=input("confirme la eliminacion del dato (s/n): ")
            if confirmar.lower()=='s':
                borrar_usuario(nombre)
                
        case 5:
            print("Bye")
            break

        case 6:
            cedula=input("Ingrese la cedula del usuario: ")
            nombre_pelicula=input("Ingrese el nombre de la pelicula que desea comprar: ")
            realizar_compra(cedula,nombre_pelicula)

        case _:
            print(f"{op} no es una opcion valida")

# HARM
project hack mty harm

import pandas as pd
ferreteria = pd.read_excel("Basededatosferreteria.xlsx")


#bienvenida al usuario

print('Hola, buen dia')
print ('Nombre del usuario')
nombre = input().title()
print ('Lindo día ' + nombre)
opcion="10"

while opcion!="c":
    Ultima_fila=79
    print('\n Selecciona la opción deseada')
    print(''75)
    print('a. Iventario')
    print('b. Ventas')
    print('c. Salir')
    opcion=input('      ===>').lower()

    if opcion == 'a':
        print('\n Selecciona la opción deseada')
        print(''75)
        print('1. Mostrar Inventario')
        print('2. Agregar productos al inventario')
        opcion=int(input('      ===>'))

        if opcion==1:
            print(ferreteria)
        elif opcion==2:
            Ultima_fila=Ultima_fila+1
            productoAgregar=input("Nombre Producto ")
            areaProducto=input("Introduce Area del producto: Plomeria, Electricidad, Ferreteria General, Quimicos ")
            semiArea=input("Introduce Semiarea Producto: Baño, Regadera,Tuberia,Refaccion,Adhesivos,Cableado,Hogar,Iluminacion,Construccion,Veneno,Disolventes")
            cantidadAlmacen=int(input("Introduce tu stock: "))

            ferreteria.loc[Ultima_fila]=[ areaProducto, semiArea, productoAgregar,Ultima_fila,cantidadAlmacen]
            print(ferreteria)
elif opcion=='b':

        print('\n Selecciona la opción deseada')
        print(''75)
        print('1. Venta Directa')
        print('2. Recomendacion de compras de productos')
        opcion=int(input('      ===>'))
        if opcion==1:
            seleccion=1
            nombres=[]
            productosComprados=[]
            while seleccion!=2:
                  #Nombres de los clientes

                nombre = input("Cual es el nombre del cliente?").title()
                nombres.append(nombre)
                #numeroNombres=len(nombres)
                #numeroFilas=len(ferreteria.index)
                ferreteria=ferreteria.assign(Nombres="Nan") 
                fila=0
                for i in nombres:
                    ferreteria.at[fila, 'Nombres']=i
                    fila=fila+1
                ferreteria=ferreteria.fillna("NaN")
                Producto=input("Que producto comprara?").title()
                piezas=int(input("Cuanta cantidad?"))
                ferreteria=ferreteria.assign(Faltantes="Nan") 
                cantidad=ferreteria[ferreteria['Producto']==Producto]["CantidadAlmacen"]
                cantidad=int(cantidad-piezas)
                if cantidad<=0:
                    productosComprados.append(Producto)
                    print("Compra denegada, no hay stock")
                    print(ferreteria)
                else:
                    print("Gracias por su compra")
                    nombres.remove(nombre)
                    print(ferreteria)
seleccion=int(input("Volvera a comprar? 1.Si 2.No"))
                #ferreteria=ferreteria.assign(Faltantes=7)
                #Buscar manera de quitar el 80
                filaFaltantes=0
                for i in productosComprados:
                    ferreteria.at[filaFaltantes, 'Faltantes']=i
                    filaFaltantes=filaFaltantes+1
                print(''75)
        elif opcion==2:
             while opcion!=4:
                print('1. Recomendacion por Area')
                print('2. Recomendacion por SemiArea')
                print('3. Recomendacion por cliente')
                print('4. Salir')
                opcion=int(input('      ===>'))
if opcion==1:
                    Area=input("Introduce Area del producto: Plomeria, Electricidad, Ferreteria General, Quimicos ")
                    porArea = ferreteria[ferreteria.Area.isin([Area])]
                    print("Estos pueden ser productos de su interes, ofrecelos")
                    print(porArea)

                elif opcion==2:
                    Semiarea=input("Introduce Semiarea del Producto: Baño, Regadera,Tuberia,Refaccion,Adhesivos,Cableado,Hogar,Iluminacion,Construccion,Veneno,Disolventes ")
                    porSemiarea = ferreteria[ferreteria.Subareas.isin([Semiarea])]
                    print("Estos pueden ser productos de su interes, ofrecelos")
                    print(porSemiarea)

                elif opcion==3:
                    nombreCliente=input("Cual es el nombre del cliente?:")
                    porNombre = ferreteria[ferreteria.Nombres.isin([nombreCliente])]
                    print("Estos pueden ser productos de su interes, ofrecelos")
                    print(porNombre)
                opcion=int(input('Continuar? 0-Si 4-No'))




else:
    pass
    
    

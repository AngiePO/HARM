#!/usr/bin/env python
# coding: utf-8

# In[263]:



import pandas as pd
import matplotlib.pyplot as plt
ferreteria = pd.read_excel("Basededatosferreteria.xlsx")


#bienvenida al usuario

print('Hola, buen dia')
print ('Ingrese nombre del usuario')
nombre = input().title()
print ('Lindo día ' + nombre)
opcion="10"

while opcion!="c":
    Ultima_fila=79
    print('\n Selecciona la opción deseada ')
    print('*'*75)
    print('a. Iventario ')
    print('b. Ventas ')
    print('c. Salir ')
    opcion=input('      ===>').lower()
    
    if opcion == 'a':
        print('\n Selecciona la opción deseada ')
        print('*'*75)
        print('1. Mostrar Inventario ')
        print('2. Agregar productos al inventario ')
        opcion=int(input('      ===>'))
        
        if opcion==1:
            print(ferreteria)
        elif opcion==2:
            Ultima_fila=Ultima_fila+1
            productoAgregar=input("Nombre Producto ").title()
            areaProducto=input("Introduce Area del producto: Plomeria, Electricidad, Ferreteria General, Quimicos ")
            semiArea=input("Introduce Semiarea Producto: Baño, Regadera,Tuberia,Refaccion,Adhesivos,Cableado,Hogar,Iluminacion,Construccion,Veneno,Disolventes").title()
            cantidadAlmacen=int(input("Introduce tu stock: "))

            ferreteria.loc[Ultima_fila]=[ areaProducto, semiArea, productoAgregar,Ultima_fila+1,cantidadAlmacen]
            print(ferreteria)
            
    
  

    elif opcion=='b':
        
        print('\n Selecciona la opción deseada ')
        print('*'*75)
        print('1. Venta Directa ')
        print('2. Recomendacion de compras de productos ')
        print('3.Más Vendidos ')
        opcion=int(input('      ===>'))
        if opcion==1:
            seleccion=1
            nombres=[]
            productosComprados=[]
            productosVendidos=[]
            cantidadVendida=[]
            while seleccion!=2:
                #Nombres de los clientes          
                nombre = input("Cual es el nombre del cliente? ").title()
                nombres.append(nombre)
                ferreteria=ferreteria.assign(Nombres="Nan") 
                fila=0
                filaFaltantes=0
                filaVendidos=0
                #Llenado de columna de nombres
                for i in nombres:
                    ferreteria.at[fila, 'Nombres']=i
                    fila=fila+1
                ferreteria=ferreteria.fillna("NaN")
                #Preguntar por producto y cantidad
                Producto=input("Que producto comprara? ").title()
                piezas=int(input("Cuanta cantidad?"))
                ferreteria=ferreteria.assign(Faltantes="Nan") 
                ferreteria=ferreteria.assign(ProductosVendidos="Nan") 
                #Buscar producto en almacen
                cantidad=ferreteria[ferreteria['Producto']==Producto]["CantidadAlmacen"]
                cantidad=int(cantidad-piezas)
                #Revisar existencias
                if cantidad<=0:
                    productosComprados.append(Producto)
                    for i in productosComprados:
                        ferreteria.at[filaFaltantes, 'Faltantes']=i
                        filaFaltantes=filaFaltantes+1
                    print("Compra denegada, no hay stock")
                    print(ferreteria)
                else:
                    cantidadVendida.append(piezas)
                    productosVendidos.append(Producto)
                    for i in productosVendidos:
                        ferreteria.at[filaVendidos, 'ProductosVendidos']=i
                        filaVendidos=filaVendidos+1
                    print("Gracias por su compra")
                    nombres.remove(nombre)
                    print(ferreteria)
                seleccion=int(input("Volvera a comprar? 1.Si 2.No"))
                filaFaltantes=0
                for i in productosComprados:
                    ferreteria.at[filaFaltantes, 'Faltantes']=i
                    filaFaltantes=filaFaltantes+1
                print('*'*75)
        elif opcion==2:
             while opcion!=4:
                #Recomendaciones de productos por areas
                
                #Escoger forma de recomendacion
                print('1. Recomendacion por Area ')
                print('2. Recomendacion por SemiArea ')
                print('3. Recomendacion por cliente ')
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
        elif opcion==3:
            #Grafico
             while opcion!=4:
                plt.bar(productosVendidos,cantidadVendida,color=['r','b','g'])
                plt.show()

                
                opcion=int(input('Continuar? 0-Si 4-No'))
                



    else:
        print("Hasta pronto")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





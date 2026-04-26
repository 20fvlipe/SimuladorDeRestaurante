import os, time
os.system("cls")

#creo 2 banderas, 1 para controlar el ciclo de repeticion (menú)
#y el otro, para saber si tengo alguna venta realizada.
bandera = True


while bandera:
    print("1. Realizar Venta")
    print("2. Ver Resumen")
    print("3. Descargar Boleta")
    print("4. Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            nombre = ""
            rut = ""
            pedido = False
            cantidad = 0
            opcion_producto = 0
            print("1. Realizar Venta")
            while len(nombre) < 3 or len(nombre) > 20:
                nombre = input("ingrese su nombre\n")
            while len(rut) < 8:
                rut = input("ingrese su rut\n")
            print("1. Hamburguesa $5000")
            print("2. Pizza $8000")
            print("3. Ensalada $4000")
            while opcion_producto < 1 or opcion_producto > 3:
                opcion_producto = int(input("ingrese producto\n"))
            while cantidad <= 0:
                cantidad = int(input("ingrese cantidad\n"))
            if opcion_producto == 1:
                producto = "Hamburguesa"
                precio = 5000
            elif opcion == 2:
                producto = "Pizza"
                precio = 8000
            else:
                producto = "Ensalada"
                precio = 4000
            
            total = precio * cantidad   
            pedido = True
            print("orden registrada con exito")
            time.sleep(3)
        elif opcion == 2:
            print("2. Ver Resumen")
            if pedido:
                print(f"Cliente: {nombre}")
                print(f"Rut: {rut}")
                print(f"Producto: {producto}")
                print(f"Cantidad: {cantidad}")
                print(f"Total a pagar: $ {total}")
                time.sleep(3)
            else:
                print("no existen pedidos para visualizar")
            
            
        elif opcion == 3:
            print("3. Descargar Boleta")
            if pedido:
                with open("boleta.txt", "w") as archivo:
                    archivo.write(f"Cliente: {nombre}\n")
                    archivo.write(f"Rut: {rut}\n")
                    archivo.write(f"Producto: {producto}\n")
                    archivo.write(f"Cantidad: {cantidad}\n")
                    archivo.write(f"Total a pagar: $ {total}\n")
            else:
                print("no existen pedidos para visualizar")    
            
            
        elif opcion == 4:
            print("muchas gracias por su compra")
            bandera = False
        else:
            print("opcion ingresa no es valida")
    except:
        print("el valor ingresado debe ser numerico")
    
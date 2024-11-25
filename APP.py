from CLASES import Cliente, Empleado, Servicio, Turno, Turnero

def mostrar_menu():
      print("\n--- MENÚ PRINCIPAL ---")
      print("1. Agregar Turno")
      print("2. Listar Turnos")
      print("3. Buscar Turno por Cliente")
      print("4. Buscar Turno por Empleado")
      print("5. Buscar Turno por Fecha")
      print("6. Listar Turnos pagados")
      print("7. Confirmar Turno")
      print("8. Modificar Turno")
      print("9. Cancelar Turno")
      print("0 . Salir")

def agregar_turno(turnero):
      while True:
          id_turno = input("Ingrese el número del turno: ")

          #Chequeo si se ingresa un número o no.
          es_numerico = True
          for caracter in id_turno:
            if caracter not in "0123456789":
                es_numerico = False
                break
        
          if not es_numerico:
            print("El ID solo puede contener números, intentar de nuevo.")
            continue
          
          
          if any(turno.id_turno == id_turno for turno in turnero.turnos):
              print("El ID de turno ya existe, ingrese uno diferente.")
          else:
              break
          
      while True:
          nombre_cliente = input("Ingrese el nombre del cliente: ")
          
          # Verificar que todos los caracteres sean letras o espacios
          
          es_valido = True
          for caracter in nombre_cliente:
                if caracter not in ("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
                  es_valido = False
                  break
          
          if es_valido:
              break  # Salimos del bucle si el nombre es válido
          
          else:
              print("El nombre del cliente tiene que contener letras, intentar de nuevo.")
              
      while True:
        telefono_cliente = input("Ingrese el teléfono del cliente: ")

        # Verificar que telefono_cliente solo contenga números
        es_numerico = True
        for caracter in telefono_cliente:
            if caracter not in "0123456789":
                es_numerico = False
                break
                
        if es_numerico:
            break  # Salimos del bucle si el teléfono es válido
        else:
            print("el teléfono del cliente tiene que contener números. Intentar de nuevo.")
      
      
      email_cliente = input("Ingrese el email del cliente: ")
      
      while True:
        nombre_servicio = input("Ingrese el nombre del servicio: ")

        # Verificar que todos los caracteres sean letras o espacios
        es_valido = True
        for caracter in nombre_servicio:
            if caracter not in ("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
                es_valido = False
                break

        if es_valido:
            break  # Salimos del bucle si el nombre del servicio es válido
        else:
            print("El nombre del servicio tiene que contener letras. intentar de nuevo.")
            
      while True:
        abona_servicio = input("¿El servicio está pagado? S/N: ")

        # Verificar que la respuesta sea solo "s" o "n"
        if abona_servicio in ("s", "n", "S", "N"):
            abonado = abona_servicio.lower() == 's'
            break
        else:
            print("Respuesta inválida, ingrese 'S' para Sí o 'N' para No.")

      while True:
        duracion_servicio = input("Ingrese la duración del servicio en minutos: ")

        # Verificar que duracion_servicio solo contenga números
        es_numerico = True
        for caracter in duracion_servicio:
            if caracter not in "0123456789":
                es_numerico = False
                break

        if es_numerico:
            break  # Salimos del bucle si la duración es válida
        else:
            print("La duración tiene que contener números. Intentar de nuevo.")

      
      while True:
        precio_servicio = input("Ingrese el precio del servicio: ")

        # Verificar que precio_servicio solo contenga dígitos
        es_numerico = True
        for caracter in precio_servicio:
            if caracter not in "0123456789":
                es_numerico = False
                break
        
        if es_numerico:
            break  # Salimos del bucle si el precio es válido
        else:
            print("El precio tiene que contener números, intentar de nuevo.")
        
      while True:
        nombre_empleado = input("Ingrese el nombre del empleado: ")

        # Verificar que cada carácter en nombre_empleado sea una letra
        es_valido = True
        for caracter in nombre_empleado:
            if caracter not in ("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
                es_valido = False
                break

        if es_valido:
            break  # Salir del bucle si el nombre es válido
        else:
            print("El nombre del empleado tiene que contener letras. intentar de nuevo.")

      while True:
        especialidad_empleado = input("Ingrese la especialidad del empleado: ")

        # Verificar que cada carácter en especialidad_empleado sea una letra
        es_valido = True
        for caracter in especialidad_empleado:
            if caracter not in ("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
                es_valido = False
                break

        if es_valido:
            break  # Salir del bucle si el nombre es válido
        else:
            print("la especialidad del empleado tiene que contener letras. intentar de nuevo.")
      
      while True:
        disponibilidad_empleado = input("Ingrese la disponibilidad del empleado (Mañana o Tarde): ")

        # Verificar que cada carácter en disponibilidad_empleado sea una letra
        es_valido = True
        for caracter in disponibilidad_empleado:
            if caracter not in ("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
                es_valido = False
                break

        if es_valido:
            break  # Salir del bucle si el nombre es válido
        else:
            print("la disponibilidad del empleado tiene que contener letras. intentar de nuevo.")
    
      
      while True:
        fecha_hora = input("Ingrese la fecha y hora del turno (YYYY-MM-DD HH:MM): ")

        # Verificar que fecha y hora solo contenga dígitos
        es_numerico = True
        for caracter in precio_servicio:
            if caracter not in "0123456789" and ":" and "-":
                es_numerico = False
                break
        
        if es_numerico:
            break  # Salimos del bucle si el precio es válido
        else:
            print("La fecha y hora tiene que contener números, intentar de nuevo.")
     
     
      productos_adicionales = input("Ingrese los productos adicionales (separados por comas): ")
      productos_adicionales = (producto.strip() for producto in productos_adicionales.split(","))

      cliente = Cliente(nombre=nombre_cliente, telefono=telefono_cliente, email=email_cliente)
      servicio = Servicio(nombre=nombre_servicio, duracion=duracion_servicio, precio=precio_servicio)
      empleado = Empleado(nombre=nombre_empleado, especialidad=especialidad_empleado, disponibilidad=disponibilidad_empleado)

      turno = Turno(
          id_turno=id_turno,
          cliente=cliente,
          servicio=servicio,
          empleado=empleado,
          fecha_hora=fecha_hora,
          productos_adicionales=productos_adicionales,
          abonado=abonado
      )

      turnero.agregar_turno(turno)


def listar_turnos(turnero):
      print("\n--- LISTA DE TURNOS ---")
      turnero.listar_turnos()

def buscar_turnos_por_cliente(turnero):
      nombre_cliente = input("Ingrese el nombre del cliente: ")
      turnero.buscar_turnos_por_cliente(nombre_cliente)

def buscar_turnos_por_empleado(turnero):
      nombre_empleado = input("Ingrese el nombre del empleado: ")
      turnero.buscar_turnos_por_empleado(nombre_empleado)

def buscar_turnos_por_fecha(turnero):
      fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
      turnero.buscar_turnos_por_fecha(fecha)

def confirmar_turno(turnero):
      turno_id = input("Ingrese el numero del turno a confirmar: ")
      turnero.confirmar_turno(turno_id)

def modificar_turno(turnero):
      turno_id = input("Ingrese el numero del turno a modificar: ")
      nuevo_servicio = input("Ingrese el nuevo servicio (o presione Enter para mantener el actual): ")
      nuevo_empleado = input("Ingrese el nuevo empleado (o presione Enter para mantener el actual): ")
      nueva_fecha_hora = input("Ingrese la nueva fecha y hora (o presione Enter para mantener la actual): ")

      turnero.modificar_turno(turno_id, nuevo_servicio, nuevo_empleado, nueva_fecha_hora)

def cancelar_turno(turnero):
      turno_id = input("Ingrese el numero del turno a cancelar: ")
      turnero.cancelar_turno(turno_id)


def main():
      turnero = Turnero()

      while True:
          mostrar_menu()  # Muestra el menú
          opcion = input("Seleccione una opción: ")

          if opcion == "1":
              agregar_turno(turnero)
          elif opcion == "2":
              listar_turnos(turnero)
          elif opcion == "3":
              buscar_turnos_por_cliente(turnero)
          elif opcion == "4":
              buscar_turnos_por_empleado(turnero)
          elif opcion == "5":
              buscar_turnos_por_fecha(turnero)
          elif opcion == "6":
              turnero.listar_turnos_abonados()
          elif opcion == "7":
              confirmar_turno(turnero)
          elif opcion == "8":
              modificar_turno(turnero)
          elif opcion == "9":
              cancelar_turno(turnero)
          elif opcion == "0":
              print("Nos vemos!")
              break
          else:
              print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
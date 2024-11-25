from CLASES import Cliente, Empleado, Servicio, Turno, Turnero


#class Cliente

cliente1 = Cliente(nombre="Juan Pérez", telefono="123456789", email="juan@example.com")
print(cliente1)

#class Empleado
empleado1 = Empleado(nombre="Julian", especialidad="Peluquero", disponibilidad="Tarde")
print(empleado1)

#class Servicio
servicio1 = Servicio(nombre="Pedicura", duracion="60", precio="7000")
print(servicio1)

#class Turno
turno1 = Turno(id_turno="1", cliente=cliente1, servicio=servicio1, empleado=empleado1, fecha_hora="8", productos_adicionales="nada", abonado="S")
print(turno1)

#class Turnero
turnero1 = Turnero()

#Agregar turnos
turnero1.agregar_turno(turno1)

#Listar turnos
turnero1.listar_turnos()

#Confirmar turnos
turnero1.confirmar_turno("1")

#Modificar turno ficticio
#turnero1.modificar_turno("2", nuevo_servicio=servicio1, nueva_fecha_hora="2024-11-12 11:00")

#Cancelar turno
turnero1.cancelar_turno("1")

#Listar turnos abonados
turnero1.listar_turnos_abonados()

#Buscar turnos por cliente
turnero1.buscar_turnos_por_cliente("Juan Pérez")

#Buscar turnos por empleado2
turnero1.buscar_turnos_por_empleado("Julian")
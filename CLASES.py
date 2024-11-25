class Cliente:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Empleado:
    def __init__(self, nombre, especialidad, disponibilidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad

    def __str__(self):
        return f"Empleado: {self.nombre}, Especialidad: {self.especialidad}, Disponibilidad: {self.disponibilidad}"

class Servicio:
    def __init__(self, nombre, duracion, precio):
        self.nombre = nombre
        self.duracion = duracion  # en minutos
        self.precio = precio

    def __str__(self):
        return f"Servicio: {self.nombre}, Duración: {self.duracion} minutos, Precio: ${self.precio}"

class Turno:
    def __init__(self, id_turno, cliente, servicio, empleado, fecha_hora, productos_adicionales, abonado):
        if productos_adicionales is None:
            productos_adicionales = ""
        self.id_turno = id_turno
        self.cliente = cliente
        self.servicio = servicio
        self.empleado = empleado
        self.fecha_hora = fecha_hora
        self.productos_adicionales = productos_adicionales
        self.abonado = abonado
        self.estado = "pendiente"

    def __str__(self):
        return f"Turno: ID: {self.id_turno}, Cliente: {self.cliente.nombre}, Servicio: {self.servicio.nombre}, Empleado: {self.empleado.nombre}, Fecha y Hora: {self.fecha_hora}, Productos Adicionales: {self.productos_adicionales}, Abonado: {self.abonado}"


class Turnero:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)
        

    def listar_turnos(self):
        if not self.turnos:
            print("No hay turnos registrados.")
        else:
            for turno in self.turnos:
                print(turno)

    def listar_turnos_abonados(self):
        abonados = [turno for turno in self.turnos if turno.abonado]

        if abonados:
            for turno in abonados:
                print(turno)
        else:
            print("No hay turnos abonados.")

    def buscar_turnos_por_cliente(self, nombre_cliente):
        turnos_cliente = [turno for turno in self.turnos if turno.cliente.nombre == nombre_cliente]
        if not turnos_cliente:
            print(f"No se encontraron turnos para el cliente {nombre_cliente}.")
        else:
            for turno in turnos_cliente:
                print(turno)

    def buscar_turnos_por_empleado(self, nombre_empleado):
        turnos_empleado = [turno for turno in self.turnos if turno.empleado.nombre == nombre_empleado]
        if not turnos_empleado:
            print(f"No se encontraron turnos para el empleado {nombre_empleado}.")
        else:
            for turno in turnos_empleado:
                print(turno)

    def buscar_turnos_por_fecha(self, fecha):
        turnos_fecha = [turno for turno in self.turnos if turno.fecha_hora.startswith(fecha)]
        if not turnos_fecha:
            print(f"No se encontraron turnos para la fecha {fecha}.")
        else:
            for turno in turnos_fecha:
                print(turno)

    def buscar_turno_por_id(self, turno_id):
        for turno in self.turnos:
            if turno.id_turno == turno_id:
                return turno
        return None



# metodo para confirmar un turno
    def confirmar_turno(self, turno_id):
        turno = self.buscar_turno_por_id(turno_id)
        if turno:
            turno.estado = "confirmado"
        else:
            print("Turno no encontrado.")

# metodo para modificar un turno
    def modificar_turno(self, turno_id, nuevo_servicio=None, nuevo_empleado=None, nueva_fecha_hora=None):
        turno = self.buscar_turno_por_id(turno_id)  # Cambiar aquí el nombre del método
        if turno:
            if nuevo_servicio:
                turno.servicio = nuevo_servicio
            if nuevo_empleado:
                turno.empleado = nuevo_empleado
            if nueva_fecha_hora:
                turno.fecha_hora = nueva_fecha_hora
        else:
            print("Turno no encontrado.")

# metodo para cancelar un turno
    def cancelar_turno(self, turno_id):
        turno = self.buscar_turno_por_id(turno_id)
        if turno:
            turno.estado = "cancelado"
        else:
            print("Turno no encontrado.")
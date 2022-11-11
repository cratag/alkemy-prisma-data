from datetime import date


class Empleados:
    """
    Clase que contiene datos personales del empleado.

    :param nombre: Nombre del empelado
    :type nombre: str
    :param apellido: Apellido del empelado
    :type apellido: str
    :param fecha_nacimiento: Fecha de nacimiento del empelado
    :type fecha_nacimiento: date
    :param nro_dni: Número de DNI del empelado
    :type nro_dni: int

    """

    def __init__(self, nombre, apellido, fecha_nacimiento, nro_dni):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_dni = nro_dni

    def edad(self):
        """Esta función no recibe parámetros. Toma por sistema la fecha actual y por instancia de clase la fecha de nacimiento. Luego calcula su edad restando al año actual el año en que nacio, y si cumplió ya este año, le resta 1 (TRUE). Si no, resta 0 (FALSE).

        :return: Edad del empleado.
        :rtype: string
        """
        fecha_actual = date.today()
        fecha_nacimiento_empleado = self.fecha_nacimiento
        edad_actual = fecha_actual.year - fecha_nacimiento_empleado.year - (
            (fecha_actual.month, fecha_actual.day) < (
                fecha_nacimiento_empleado.month, fecha_nacimiento_empleado.day))

        return edad_actual

    def presentacion(self):
        """ Esta función no recibe parámetros

        :return: Presentación del empleado. Nombre, apellido, fecha de nacimiento y DNI.
        :rtype: string
        """

        return f"Hola. Soy {self.nombre} {self.apellido}. Nací el {self.fecha_nacimiento} y mi DNI es {self.nro_dni}."


empleado = Empleados('John', 'Doe', date(1996, 2, 17), '38384621')

# print(empleado.edad())
# print(empleado.presentacion())

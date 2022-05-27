class Cliente:
    """
    Una clase para representar un cliente
    ........................................
    Atributos
    ----------------------------------------
    nombre : str
        primer nombre del cliente
    telefono : str
        telefono del cliente
    estado : str
        estado del cliente
    ----------------------------------------
    Métodos
    ----------------------------------------
    regCuenta(self, usuario, contra, contra1)
        registra una cuenta mediante usuario y validación de contraseña
    """
    def __init__(self, nombre, telefono, estado):
        """
        Construye todos los atributos necesarios para el objeto empleado.
        -----------------------------
        Parámetros
        -----------------------------
        nombre : str
            primer nombre del cliente
        telefono : str
            telefono del cliente
        estado : str
            estado del cliente 
        """
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado


    def regCuenta(self, usuario, contra, contra1):
        '''
        Devuelve la resta del sueldoBase y descuentos más bonos

        Parámetros:
                usuario    : str
                contra     : str
                contra1    : str
        ----------------------------------------------
        Devoluciones
                self.sueldoBase-descuentos+bonos (str)
        '''
        print("-------------------------------------------")
        print("               REGISTRO")
        print("-------------------------------------------")
        print(input("Ingrese el usuario", usuario ))
        print(input("Ingrese la contraseña", contra ))
        print(input("Repita la contraseña", contra1 ))
        #Condicional if para validar las contraseñas
        if self.contra == self.contra1:
           print("Registro se ha completado")
        else:
           print("Contraseñas no coinciden")
        
#Instancia del objeto cliente y su llamado
d=Cliente("Steve", "+593992808552", "Caso")
#Imprimir los atributos
print("Los datos del cliente son: ")
print(d.nombre)
print(d.telefono)
print(d.estado)

class Tienda:
    """
    Una clase para representar una tienda
    ........................................
    Atributos
    ----------------------------------------
    nombre : str
        nombre de la tienda
    telefono : str
        telefono del tienda
    estado : str
        estado de la tienda
    gerente: str
        gerente de la tienda
    """
    def __init__(self, nombre, telefono, estado, gerente):
        
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado
        self.gerente=gerente

#instanciar el objeto Tienda
p=Tienda("SuperTienda", "3052021", "Normal", "Carlos Miller")
#imprimir atributos
print(p.nombre)
print(p.telefono)
print(p.estado)
print(p.gerente)

class Admin:
    """
    Una clase para representar un administrador
    ........................................
    Atributos
    ----------------------------------------
    Ninguno
    ----------------------------------------
    Métodos
    ----------------------------------------
    verDetClien():
        Muestra los detalles del cliente y de la tienda
    cambEstado():
        Imprime detalles del Cliente en caso de ser un "Caso"
    """
    def verDetClien():
        print("Detalles de los clientes", Cliente)
   
    def cambEstado():
        print("La tienda como Caso")
        print("Familiares clasificados como 'Cercanos' ")
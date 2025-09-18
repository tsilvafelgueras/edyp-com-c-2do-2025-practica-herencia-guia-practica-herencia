"""
Siguiendo con el proyecto de la biblioteca, deseamos obtener ciertos datos en relación con los préstamos realizados por los usuarios:

1. Nombre de los usuarios que solicitaron más libros en total. Deseamos promover dichos usuarios a “Lectores de Honor”.

2. Listado de los libros que nunca fueron prestados. Deseamos retirarlos del catálogo o derivarlos a otra biblioteca. Previamente debemos imprimir los títulos y pedir la confirmación al usuario del sistema para proceder con la derivación.

3. Promedio de cantidad de libros prestados por usuario hasta el momento. Debemos mostrar dicha información.
 “Promedio por usuario: nn libros”

4. Libro más antiguo prestado por cada usuario de la biblioteca (basado en el año de publicación). Si no realizó préstamos, se debe imprimir “N/A”. Se debe mostrar:
 Usuario: nombre, título, año de publicación

5. Lista de géneros por orden de popularidad. Se debe mostrar la lista de mayor a menor popularidad, junto al número de préstamos por género. Luego se procederá a incorporar a la biblioteca más ejemplares de los 3 géneros más populares, solicitando previamente la confirmación del usuario del sistema. Informar los títulos de los nuevos libros agregados para cada género.

Para realizar estos ejercicios, deberán agregar a las clases ya realizadas los atributos que consideren pertinentes, evitando modificar el código ya implementado en las clases. Para cada uno de los puntos solicitados, deberán definir métodos de instancia y probar la funcionalidad de su código. Empecemos: ¿En qué clase o clases deberían encapsular los distintos métodos?
"""
from typing import Dict, List

class Libro:
    posibles_estados = ["disponible", "prestado"]
    contador_libros = 0

    def __init__(self, titulo: str, autor:str, editorial:str, ISBN: str, estado= 'disponible'):
        self.titulo = self.validar_cadena(titulo)
        self.autor = self.validar_cadena(autor)
        self.editorial = self.validar_cadena(editorial)
        self.ISBN = ISBN
        self.estado = self.setter_estado(estado)
        self.veces_prestado = 0
        Libro.contador_libros += 1

    @classmethod #siempre cuando venga a intervenir con un atributo de clase
    def mostrar_contador_libros (cls):
        print(f'el numero de libros creados es: {cls.contador_libros}')

    #METODO DE VISUALIZACION
    def __str__(self):
        return f'El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial} con ISBN {self.ISBN}, y su estado es {self.estado}'

    #METODO CREADO POR MI
    def mostrar(self):
        return f'El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial} con ISBN {self.ISBN}, y su estado es {self.estado}'
    
    #MÉTODOS GETTER
    def getter_estado(self): #para obtener el estado
        return self.estado
    
    def getter_ISBN(self):
        return self.ISBN

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor

    def get_editorial(self):
        return self.editorial
    
    #MÉTODOS SETTER
    def setter_estado(self, estado):
        estado = estado.lower()
        if estado not in Libro.posibles_estados:
            raise ValueError(f"El estado debe ser uno de los siguientes: {self.posibles_estados}")
        self.estado = estado
        return self.estado
    
    def set_titulo(self, titulo):
        self.titulo = titulo
        
    def set_autor(self, autor:str):
        self.autor = autor
    
    def set_editorial(self, editorial:str):
        self.editorial = editorial
    
    def set_isbn(self, isbn:str):
        self.ISBN = isbn

    #MÉTODOS DE FUNCIONALIDAD
    def devolver_libro(self):
        if self.getter_estado()=="disponible":
            print("El libro ya se encuentra disponible")
        else:
            self.setter_estado('disponible')
            print("El libro ha sido devuelto y se encuentra disponible")

    def prestar_libro(self):
        if self.getter_estado() == "disponible":
            self.setter_estado("prestado")
            print(f"El libro {self.titulo} fue prestado con éxito")
            self.veces_prestado += 1
        else:
            print(f"El libro {self.titulo} no se encuentra disponible para prestar")

    def validar_cadena(self,cadena):
        if not isinstance(cadena, str):
            raise TypeError(f"{cadena} debe ser una cadena de texto")
        if len(cadena)<1:
            raise ValueError(f"{cadena} no puede ser una cadena vacía")
        return cadena
    
    def ver_informacion_libro(self):
        if self.estado == 'disponible':
            estado = 'Disponible'
        else:
            estado = 'Prestado'
        
        return f'''
        Titutlo: {self.titulo}
        Autor: {self.autor}
        ISBN: {self.ISBN}
        Editorial: {self.editorial}
        Estado: {estado}'''
    
    def __eq__(self, otro):
        if not isinstance(otro,Libro):
            raise TypeError("El objeto debe ser una instancia de la clase Libro")
        elif id(self)==id(otro):
            return True
        elif self.ISBN == otro.ISBN:
            return True
        else:
            return False

class Usuario:
    def __init__(self, nombre:str, dni:str):
        self._nombre = nombre
        self._dni = dni
        self.__libros_prestados: Dict[str, Libro] = {} #Diccionario {isbn:Libro} de libros prestados

    @property
    def nombre(self):
        return self._nombre.title()
    
    @property
    def dni(self):
        return self._dni
    
    def get_libros_prestados(self) -> List[Libro]:
        return self.__libros_prestados.copy()

    @nombre.setter
    def nombre(self,valor):
        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser una cadena")
        if len(valor.strip())==0:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip() #le borra los espacios de atrás y adelante

    def pedir_libro_prestado(self, libro:Libro):
        isbn = libro.get_isbn()
        if isbn in self.__libros_prestados:
            raise ValueError("El usuario ya tiene este libro prestado.")

        # Intentar prestar el libro
        try:
            libro.prestar()
            self.__libros_prestados[isbn] = libro
        except ValueError as e:
            raise ValueError(f"No se pudo prestar el libro: {e}")
    
    def devolver_libro_prestado(self, libro:Libro):
        isbn = libro.get_isbn()
        if isbn not in self.__libros_prestados:
            raise ValueError("El usuario no tiene este libro prestado.")

        # Intentar devolver el libro
        try:
            libro.devolver()
            del self.__libros_prestados[isbn]
        except ValueError as e:
            raise ValueError(f"No se pudo devolver el libro: {e}")
    
    def ver_libros_prestados(self):
        if not self.__libros_prestados:
            return 'No tienes libros prestados actualmente'
        
        libros = f'Libros prestados {self._nombre}: \n'
        for libro in self.__libros_prestados.values():
            libros += f'{libro} \n'

        return libros

    def __str__(self):
        return f'{self._nombre} (DNI: {self._dni})'
    
class Biblioteca:
    #gestiona libros y usuarios
    def __init__(self, nombre:str):
        self.__nombre = nombre
        self.__libros: Dict[str,Libro] = {}
        self.__usuarios: Dict[str,Usuario] = {}

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre:str):
        self.__nombre = nombre
    
    def agregar_libro(self, libro:Libro):
        isbn = libro.getter_ISBN()
        if isbn in self.__libros:
            print("El libro con este ISBN ya existe en la biblioteca")
            return

        self.__libros[isbn] = libro
    
    def eliminar_libro(self, isbn:str):
        if isbn not in self.__libros:
            print("No se encontró un libro con este ISBN")
            return

        libro = self.__libros[isbn]
        if not libro.get_disponible():
            print("No se puede eliminar: el libro está prestado")
            return

        del self.__libros[isbn]

    def buscar_libro(self, isbn:str):
        return self.__libros.get(isbn)
    
    def modificar_informacion_libro(self, isbn:str, titulo:str, autor:str, editorial:str):
        libro = self.buscar_libro(isbn)
        if not libro:
            print(f"No se encontró un libro con este ISBN {isbn}")
            return
        
        libro.set_titulo(titulo)
        libro.set_autor(autor)
        libro.set_editorial(editorial)

    def agregar_usuario(self, usuario:Usuario):
        dni = usuario.get_dni()
        if dni in self.__usuarios:
            print("El usuario con este DNI ya existe en la biblioteca")
            return

        self.__usuarios[dni] = usuario
    
    def eliminar_usuario(self, dni:str):
        if dni not in self.__usuarios:
            print("No se encontró un usuario con este DNI")
            return

        # Verificar que no tenga libros prestados
        usuario = self.__usuarios[dni]
        if usuario.get_libros_prestados():
            print("No se puede eliminar: el usuario tiene libros prestados")
            return

        del self.__usuarios[dni]
    
    def buscar_usuario(self, dni:str):
        return self.__usuarios.get(dni) 
        
    def modificar_info_usuario(self, dni:str, nombre:str):
        #modifica la info de un usuario

        usuario = self.buscar_usuario(dni)

        if not usuario:
            print("No se encontró un usuario con este dni:", dni)
        
        usuario.nombre = nombre
    
    #métodos de gestión de préstamos

    def prestar_libro(self, dni_usuario:str, isbn_libro:str):
        usuario = self.buscar_usuario(dni_usuario)
        if not usuario:
            print("Usuario no encontrado")
            return
        
        libro = self.buscar_libro(isbn_libro)
        if not libro:
            print("Libro no encontrado")
            return
        
        try:
            usuario.pedir_libro_prestado(libro)
            print(f'Préstamo exitoso: {libro.get_titulo()} prestado a {usuario.nombre}')
        except ValueError as e:
            print(f'No se pudo realizar el préstamos: {e}')
    
    def devolver_libro(self, dni_usuario:str, isbn_libro:str):
        usuario = self.buscar_usuario(dni_usuario)
        if not usuario:
            print("Usuario no encontrado")
            return
        
        libro = self.buscar_libro(isbn_libro)
        if not libro:
            print("Libro no encontrado")
            return

        try:
            usuario.devolver_libro_prestado(libro)
            print(f'Devolución exitosa: {libro.get_titulo()} devuelto por {usuario.nombre}')
        except ValueError as e:
            print(f'No se pudo realizar la devolución: {e}')
    
    # Métodos de utilidad
    def listar_libros(self):
        if not self.__libros:
            return 'No  hay libros en la biblioteca'

        lista = f'Libros en {self.__nombre}: \n'
        for i, libro in enumerate(self.__libros.values(), 1):
            if libro.getter_estado() == 'disponible':
                estado = 'Disponible'
            else:
                estado = 'Prestado'
            lista += f'{i}. {libro} - {estado}\n'
        
        return lista

    def listar_usuarios(self):
        if not self.__usuarios:
            return 'No hay usuarios registrados'
        
        lista = f'Usuarios de {self.__nombre}:\n'
        for i, usuario in enumerate(self.__usuarios.values(), 1):
            libros_prestados = len(usuario.get_libros_prestados())
            lista += f'{i}.{usuario} - Libros prestados: {libros_prestados}\n'
        
        return lista
    
    def __str__(self):
        return f'Biblioteca: {self.__nombre} ({len(self.__libros)} libros, {len(self.__usuarios)} usuarios)'
    
    def identificar_lector_honor(self):
        dict_usuario_libros = {}
        if not self.__usuarios:
            print('No hay usuarios registrados')
            return []
        
        for usuario in self.__usuarios.values():
            cantidad = len(usuario.get_libros_prestados())
            dict_usuario_libros[usuario] = cantidad
        
        max_cantidad = 0
        if dict_usuario_libros:
            max_cantidad = max(dict_usuario_libros.values())
        
        if max_cantidad == 0:
            print("No hay libros registrados")
            return []

        lectores_honor = []
        for usuario, cantidad in dict_usuario_libros.items():
            if cantidad == max_cantidad:
                lectores_honor.append(usuario)

        return lectores_honor
    
    # def gestionar_libros_no_prestados(self):
    #     for libro in self.__libros.values():
    #         if libro.veces_prestado == 0:
    #             eleccion = input(f"Desea eliminar el libro {libro.get_titulo()}? Responda con si o no.")
    #             isbn = libro.getter_ISBN()
    #             if eleccion.lower() == 'si':
    #                 self.eliminar_libro(isbn)
    #             elif eleccion.lower() == 'no':
    #                 print("El libro no será eliminado") 
    #             else:
    #                 raise ValueError("No ingreso una respuesta valida.")

    def gestionar_libros_no_prestados(self):
        libros_a_eliminar = []
        for libro in self.__libros.values():
            if libro.veces_prestado == 0:
                libros_a_eliminar.append(libro)
        
        if not libros_a_eliminar:
            print("No hay libros para eliminar")
            return
        
        print("Libros que nunca fueron prestados:\n")
        for libro in libros_a_eliminar:
            print(f'{libro.get_titulo()}\n')
        
        eleccion = input(f"Desea eliminar los {len(libros_a_eliminar)} libros? Responda con si/no.")
        if eleccion.lower() == 'si':
            for libro in libros_a_eliminar:
                isbn = libro.getter_ISBN()
                self.eliminar_libro(isbn)
            print("Los libros han sido eliminados exitosamente.")
        else:
            print("La operación ha sido cancelada, no se ha eliminado ningún libro.")
    
    def promedio_prestados(self): #chequear si esta bien, o si lo correcto sería por usuarios que se llevaron libros
        conteo_prestados = 0
        for libro in self.__libros.values():
            if libro.veces_prestado != 0:
                conteo_prestados += libro.veces_prestado
        
        cantidad_usuarios = len(self.__usuarios)

        if conteo_prestados == 0:
            print("Ningún libro fue prestado.")
            return 0
        else:
            if cantidad_usuarios == 0:
                print("No hay usuarios registrados")
                return 0
            elif cantidad_usuarios != 0:
                promedio = conteo_prestados / cantidad_usuarios
                print(f"Promedio Prestados: {promedio}")
                return promedio
    

# if __name__ == "__main__":

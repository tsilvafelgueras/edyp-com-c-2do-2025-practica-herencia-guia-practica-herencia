"""
### Ejercicio 1: Herencia y Polimorfismo en Vehículos *[Ejercicio obligatorio]*
Recuerda implementar la restricción de unicidad de patentes de manera que aplique a todos los vehículos terrestres (autos y camiones) simultáneamente, pero no a las embarcaciones.

#### Clase Auto
- Similar al Camión, pero sin atributo de carga.
- Tiene exactamente 4 ruedas (los camiones tienen 8).
- Atributo `posicion_inicial` que inicia en 0 al crear el objeto.
- Implementa el método `trasladarse(desplazamiento: int)`, que actualiza la posición sumando el desplazamiento y retorna un mensaje indicando el movimiento por tierra.

#### Clase Lancha
- Puede desplazarse, con `posicion_inicial` iniciando en 0.
- Atributos: marca, año y marca de motor (no tiene ruedas ni carga).
- Las patentes de lanchas son independientes (no comparten restricción con vehículos terrestres).
- Método `trasladarse(desplazamiento: int)` que actualiza la posición y retorna un mensaje indicando movimiento por agua a motor.

```python
class Lancha:
    def __init__(self, patente, marca, año, marca_motor):
        pass

    def trasladarse(self, desplazamiento):
        # Actualiza posición y retorna mensaje específico
        pass
```

#### Clase Velero
- Similar a la Lancha, se desplaza por agua, pero con cantidad de velas en lugar de motor.
- Método `trasladarse(desplazamiento: int)` que retorna un mensaje indicando movimiento por agua a vela.

```python
class Velero:
    def __init__(self, patente, marca, año, cantidad_velas):
        pass

    def trasladarse(self, desplazamiento):
        # Actualiza posición y retorna mensaje específico
        pass
```

#### Clase Anfibio
- Vehículo que puede trasladarse por tierra o por agua (a motor).
- Por defecto, `trasladarse(desplazamiento: int)` lo hace por tierra.
- Implementa un método adicional para trasladarse por agua.

```python
class Anfibio:
    def __init__(self, patente, ...):  # Completa con atributos heredados y propios
        pass

    def trasladarse(self, desplazamiento):
        # Por defecto, por tierra
        pass

    def trasladarse_por_agua(self, desplazamiento):
        # Método adicional para agua
        pass
```

Recuerda utilizar herencia para evitar duplicación de código. Los mensajes de retorno deben ser específicos según el tipo de vehículo y medio de transporte. 
"""
class VehiculosTerrestres:
    patentes_registradas = set()
    def __init__(self, patente:str, marca: str, anio: int, cantidad_ruedas:int):
        if patente in VehiculosTerrestres.patentes_registradas:
            raise ValueError(f"La patente {patente} ya existe.")
        
        self.patente = patente
        VehiculosTerrestres.patentes_registradas.add(self.patente)
        
        self.cantidad_ruedas = cantidad_ruedas
        self.posicion_inicial = 0 
        self.marca= marca
        self.anio = anio
    
    def trasladarse(self, desplazamiento: int):
        self.posicion_inicial += desplazamiento
        return f'El vehiculo con patente {self.patente} se ha desplazado {desplazamiento}km por tierra'

class Auto(VehiculosTerrestres):
    def __init__(self, patente:str, marca:str, anio:int):  # Completa con los atributos necesarios
        super().__init__(patente, marca, anio, cantidad_ruedas = 4)
        

class VehiculosAcuaticos:
    patentes_registradas = set()
    def __init__(self, patente:str, marca:str, anio:str):
        if patente in VehiculosAcuaticos.patentes_registradas:
            raise ValueError(f'La patente {patente} ya está registrada.')

        self.patente = patente
        VehiculosAcuaticos.patentes_registradas.add(self.patente)
        self.marca = marca
        self.anio = anio
        self.posicion = 0
    
    def actualizar_posicion(self, desplazamiento:int):
        self.posicion += desplazamiento


class Lancha(VehiculosAcuaticos):
    def __init__(self, patente, marca, anio, marca_motor:str):
        super().__init__(patente, marca, anio)
        self.marca_motor = marca_motor

    def trasladarse(self, desplazamiento:int):
        self.actualizar_posicion(desplazamiento)
        return f'El vehiculo se ha desplazado {desplazamiento} km por agua a motor.'

class Velero(VehiculosAcuaticos):
    def __init__(self, patente, marca, anio, cantidad_velas:int):
        super().__init__(patente, marca, anio)
        self.cantidad_velas = cantidad_velas
    
    def trasladarse(self,desplazamiento:int):
        self.actualizar_posicion(desplazamiento)
        return f'El vehículo se ha desplazado {desplazamiento}km por agua a vela.'

class Anfibio(VehiculosTerrestres):
    def __init__(self, patente, marca, anio, marca_motor:str):
        super().__init__(patente, marca, anio, cantidad_ruedas=4)
        self.cantidad_ruedas = 4
        self.marca_motor = marca_motor

    def trasladarse_por_agua(self, desplazamiento):
        self.posicion_inicial += desplazamiento
        return f'El vehiculo se ha desplazado {desplazamiento}km por agua a motor'

try:
    anf1 = Anfibio('A123', 'Honda', 2025, 'Honda Motors')
    print(anf1.trasladarse(100))
    print(f'Posición actual: {anf1.posicion_inicial} km')

    print(anf1.trasladarse_por_agua(20))
    print(f'Posición actual: {anf1.posicion_inicial} km')


except Exception as e:
    print("El error es", e)
# Guia Práctica

## Tema: Herencia y objetos

### Ejercicio 1: Herencia y Polimorfismo en Vehículos *[Ejercicio obligatorio]*

Siguiendo el ejercicio del Camión realizado en la actividad anterior, el objetivo es crear nuevas clases reutilizando la mayor cantidad de código posible mediante herencia. A continuación, se detallan los requisitos para cada clase. Recuerda implementar la restricción de unicidad de patentes de manera que aplique a todos los vehículos terrestres (autos y camiones) simultáneamente, pero no a las embarcaciones.

#### Clase Auto
- Similar al Camión, pero sin atributo de carga.
- Tiene exactamente 4 ruedas (los camiones tienen 8).
- Atributo `posicion_inicial` que inicia en 0 al crear el objeto.
- Implementa el método `trasladarse(desplazamiento: int)`, que actualiza la posición sumando el desplazamiento y retorna un mensaje indicando el movimiento por tierra.

```python
class Auto:
    def __init__(self, patente, ...):  # Completa con los atributos necesarios
        pass

    def trasladarse(self, desplazamiento):
        # Actualiza posición y retorna mensaje
        pass
```

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

### Ejercicio 2: Análisis de Datos de Uso de la Tarjeta SUBE

Como parte de un proyecto de movilidad en el territorio argentino, el gobierno ha recolectado datos diarios del uso de la tarjeta SUBE para entender patrones de viaje y preferencias de transporte público. Tu tarea es procesar el archivo `"total-usuarios-por-dia.csv"` y extraer información clave. Debes implementar soluciones utilizando **Programación Orientada a Objetos (POO)** para estructurar el código (por ejemplo, clases para manejar datos y análisis) y **programación funcional** donde sea apropiado (como el uso de funciones `map`, `filter`, `reduce` para procesar listas de datos de manera eficiente y declarativa).

#### Requisitos Generales
- Lee el archivo CSV y procesa los datos en estructuras de datos adecuadas (por ejemplo, listas de diccionarios o objetos personalizados).
- Utiliza POO para crear clases como `AnalizadorSUBE` que encapsule métodos de análisis.
- Aplica principios funcionales para operaciones de agregación y filtrado, evitando bucles imperativos cuando sea posible.
- Maneja errores potenciales, como archivos inexistentes o datos inválidos.
- Muestra resultados de manera clara, utilizando prints o funciones de salida.

#### Tareas Específicas
1. **Análisis de Uso de Lancha**:
    - Determina el mes del año 2020 en el que se registró el mayor uso del medio de transporte "lancha".
    - Implementa un método en tu clase que filtre datos por medio de transporte y calcule el máximo por mes.

2. **Análisis por Mes Ingresado**:
    - Solicita al usuario un mes (como número, ej. 1 para enero) y un año (como número, ej. 2020).
    - Determina el medio de transporte más utilizado en ese mes en ese año.
    - Usa map, filter y reduce para agrupar y comparar datos.

3. **Tendencias Mensuales**:
    - Analiza patrones estacionales en el uso del transporte público a lo largo de los meses.
    - Identifica posibles tendencias, como mayor uso en invierno (debido al clima) o verano.
    - Genera un resumen mensual con totales por medio de transporte, utilizando agregaciones funcionales.

4. **Promedio Mensual de Usuarios**:
    - Calcula el promedio de usuarios totales que utilizan la tarjeta SUBE cada mes.
    - Implementa un método que sume usuarios diarios y divida por el número de días en el mes.

5. **Orden Ascendente de Medios de Transporte**:
    - Muestra todos los medios de transporte ordenados de menor a mayor según su uso total en el año 2021.
    - Utiliza funciones de ordenamiento funcionales para procesar y mostrar la lista.

Recuerda documentar tu código con docstrings y comentarios. Asegúrate de que el programa sea modular y reutilizable, aplicando herencia si es necesario para extender funcionalidades.

### Ejercicio 3: Análisis de Datos de la Biblioteca *[Ejercicio obligatorio]*

Siguiendo con el proyecto de la biblioteca, deseamos obtener ciertos datos en relación con los préstamos realizados por los usuarios:

1. Nombre de los usuarios que solicitaron más libros en total. Deseamos promover dichos usuarios a “Lectores de Honor”.

1. Listado de los libros que nunca fueron prestados. Deseamos retirarlos del catálogo o derivarlos a otra biblioteca. Previamente debemos imprimir los títulos y pedir la confirmación al usuario del sistema para proceder con la derivación.

1. Promedio de cantidad de libros prestados por usuario hasta el momento. Debemos mostrar dicha información.
 “Promedio por usuario: nn libros”

1. Libro más antiguo prestado por cada usuario de la biblioteca (basado en el año de publicación). Si no realizó préstamos, se debe imprimir “N/A”. Se debe mostrar:
 Usuario: nombre, título, año de publicación

1. Lista de géneros por orden de popularidad. Se debe mostrar la lista de mayor a menor popularidad, junto al número de préstamos por género. Luego se procederá a incorporar a la biblioteca más ejemplares de los 3 géneros más populares, solicitando previamente la confirmación del usuario del sistema. Informar los títulos de los nuevos libros agregados para cada género.

Para realizar estos ejercicios, deberán agregar a las clases ya realizadas los atributos que consideren pertinentes, evitando modificar el código ya implementado en las clases. Para cada uno de los puntos solicitados, deberán definir métodos de instancia y probar la funcionalidad de su código. Empecemos: ¿En qué clase o clases deberían encapsular los distintos métodos?

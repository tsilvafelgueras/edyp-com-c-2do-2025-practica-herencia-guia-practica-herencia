"""
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
"""

import csv
from functools import reduce
from datetime import datetime

class AnalizadorSUBE:
    medios_transporte = ['colectivo', 'lancha', 'subte', 'tren'] #atributos de clase

    def __init__(self, ruta:str):
        self.ruta = ruta
        self.datos = [] #atributo de instancia
        self._cargar_datos() #poner el self delante porque es un método de la clase
    
    def _cargar_datos(self):
        try:
            with open(self.ruta, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.DictReader(archivo)
                for fila in lector_csv:
                    self.datos.append(fila)
        except FileNotFoundError as e:
            print(f"El archivo no fue encontrado. El error es", e)
        except Exception as e:
            print(f'El error es', e)

    def analisis_uso_lancha(self, anio:int, medio_transporte:str):
        
        datosdelanio = list(filter(lambda x: x['indice_tiempo'][:4]==str(anio), self.datos))
        if not datosdelanio:
            print(f"No se encontraron datos para el {anio}.")
            return

        totales_por_mes = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        for fila in datosdelanio:
            try:
                fecha_obj = datetime.strptime(fila['indice_tiempo'], "%Y-%m-%d")
                mes = fecha_obj.month
                usuarios_transporte = int(fila[medio_transporte]) 
                totales_por_mes[mes] += usuarios_transporte
            except (ValueError, TypeError) as e:
                print("El error es", e)

        mes_mayor_uso = max(totales_por_mes, key=totales_por_mes.get)

        print(f'El mes de mayor uso de lancha en el anio {anio} fue {mes_mayor_uso}, con un total de {totales_por_mes[mes_mayor_uso]}')
    
    def analisis_mes_ingresado(self, anio:int, mes:int):
        totales = {}
        if mes<10:
            mes = "0"+ str(mes)
        
        datosfiltrados = list(filter(lambda x: x['indice_tiempo'][:4] == str(anio) and x['indice_tiempo'][5:7]==str(mes), self.datos))

        for transporte in self.medios_transporte:
            numeros_transporte = map(lambda x: int(x[transporte]), datosfiltrados)
            total_transporte = reduce(lambda valoracumulado, valor: valoracumulado + valor, numeros_transporte, 0)
            totales[transporte] = total_transporte

        print("totales del mes", totales)

        transporte_mas_usado = max(totales, key = totales.get)
    
        print(f"El transporte más utilizado en el mes {mes} de {anio} fue {transporte_mas_usado}.")

    def tendencias_mensuales(self):
        totales_por_mes = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        totales_verano = 0
        totales_otonio = 0
        totales_invierno = 0
        totales_primavera = 0
        resumen_detallado = {1:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0},
        2:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 3:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 4:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 5:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 6:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 7:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 8:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 9:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 10:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 11:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0}, 12:{'colectivo':0, 'lancha':0, 'subte':0, 'tren':0} }

        for fila in self.datos:
            try:
                mes = int(fila['indice_tiempo'][5:7])
                total_usuarios = int(fila['total'])
                totales_por_mes[mes]+= total_usuarios
                for transporte in self.medios_transporte:
                    valor = int(fila[transporte])
                    resumen_detallado[mes][transporte] += valor                   

            except Exception as e:
                print("El error es", e)
        
        meses_verano = [12, 1, 2]
        for mes in meses_verano:
            totales_verano += totales_por_mes[mes]

        meses_primavera = [9, 10, 11]
        for mes in meses_primavera:
            totales_primavera += totales_por_mes[mes]
        meses_invierno = [6, 7, 8]
        for mes in meses_invierno:
            totales_invierno += totales_por_mes[mes]
        meses_otonio = [3, 4, 5]
        for mes in meses_otonio:
            totales_otonio += totales_por_mes[mes] 

        totales_estaciones = {'Verano': totales_verano, 'Invierno': totales_invierno, 'Otoño': totales_otonio, 'Primavera': totales_primavera}

        estacion_max = max(totales_estaciones, key=totales_estaciones.get)
        print(f"la estación en la que mas se uso transporte público fue {estacion_max}")

        print(resumen_detallado)

    def promedio_usuarios_mensual(self):
        sumas_mensuales = {}
        dias_por_mes = {}

        for fila in self.datos:
            try:
                anio = int(fila['indice_tiempo'][:4])
                mes = int(fila['indice_tiempo'][5:7])
                if anio not in sumas_mensuales:
                    sumas_mensuales[anio] ={mes:0 for mes in range(1,13)}
                    dias_por_mes[anio] = {mes:0 for mes in range(1,13)}

                sumas_mensuales[anio][mes] += int(fila['total'])
                dias_por_mes[anio][mes] += 1
            except (ValueError, KeyError) as e:
                print("El error es", e)
        
        promedio = {}

        for anio in sumas_mensuales:
            promedio[anio]={}
            for mes in range(1,13):
                if dias_por_mes[anio][mes] > 0:
                    promedio[anio][mes] = sumas_mensuales[anio][mes] // dias_por_mes[anio][mes]
                else:
                    promedio[anio][mes] =0
        
        print(dias_por_mes)
        print(promedio)
    

if __name__ == "__main__":
    analizador = AnalizadorSUBE("total-usuarios-por-dia.csv")

    if analizador.datos:
        # analizador.analisis_uso_lancha(2020, 'lancha')
        # analizador.analisis_mes_ingresado(2020, 1)
        # analizador.tendencias_mensuales()
        analizador.promedio_usuarios_mensual()
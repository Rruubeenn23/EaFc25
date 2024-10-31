import pandas as pd
from formaciones import Formacion, Equipo, crear_formaciones

class SeleccionarJugadores:
    def __init__(self, csv_path):
        # Cargar los datos desde el CSV
        self.jugadores_df = pd.read_csv(csv_path)
        self.equipo = Equipo("Mi Equipo")
        self.formacion_actual = None
        self.jugadores_seleccionados = set()  # Lista de IDs o nombres de jugadores seleccionados

    def elegir_formacion(self):
        # Crear formaciones y agregarlas al equipo
        formaciones_creadas = crear_formaciones()
        for formacion in formaciones_creadas:
            self.equipo.agregar_formacion(formacion)

        # Elegir una formación para trabajar
        self.formacion_actual = formaciones_creadas[0]  # Por ejemplo, seleccionamos la primera formación
        print(f"Formación actual seleccionada: {self.formacion_actual.nombre} ({self.formacion_actual.formacion})")

    def mostrar_formaciones(self):
        self.equipo.mostrar_formaciones()

    def mostrar_jugadores_por_posicion(self, posicion):
        # Verificar si el DataFrame de jugadores está vacío
        if self.jugadores_df.empty:
            print("No hay ningún jugador en el club. ¿Por qué no pruebas a abrir algún sobre?")
            return  # Salir del método si no hay jugadores
    
        # Determinar el código de posición correcto
        if posicion == "GK":
            posicion_filtrada = "GK"  # Para el portero
        elif posicion == "DEF":
            posicion_filtrada = "CB"  # Cambiar según los tipos de defensores que tengas
        elif posicion == "LI":
            posicion_filtrada = "LB"  # Cambiar según los tipos de defensores que tengas
        elif posicion == "LD":
            posicion_filtrada = "RB"  # Cambiar según los tipos de defensores que tengas
        elif posicion == "MID":
            posicion_filtrada = "CM"   # Cambiar según los tipos de mediocampistas que tengas
        elif posicion == "FWD":
            posicion_filtrada = "ST"   # Cambiar según los tipos de delanteros que tengas
        elif posicion == "EI":
            posicion_filtrada = "LW"  # Cambiar según los tipos de defensores que tengas
        elif posicion == "ED":
            posicion_filtrada = "RW"  # Cambiar según los tipos de defensores que tengas
        else:
            print(f"Posición {posicion} no reconocida.")
            return
    
        # Obtener los jugadores en la posición deseada, excluyendo los seleccionados
        jugadores_posicion = self.jugadores_df[
            (self.jugadores_df['Position'] == posicion_filtrada) &
            (~self.jugadores_df['Name'].isin(self.jugadores_seleccionados))
        ]
    
        if jugadores_posicion.empty:
            print(f"No hay jugadores disponibles en la posición {posicion}.")
            return  # Salir del método si no hay jugadores en esta posición
    
        # Ordenar por OVR y mostrar jugadores
        jugadores_posicion = jugadores_posicion.sort_values(by='OVR', ascending=False)
        print(f"Jugadores disponibles en la posición {posicion}:")
    
        # Imprimir jugadores con índice comenzando en 1
        for idx, (index, jugador) in enumerate(jugadores_posicion.iterrows(), start=1):
            print(f"{idx}: {jugador['Name']} - OVR: {jugador['OVR']} - Equipo: {jugador['Team']}")
    
        return jugadores_posicion.reset_index(drop=True)

    def cambiar_jugador(self, posicion):
        print(f"Seleccionando jugador para la posición: {posicion}")
        jugadores = self.mostrar_jugadores_por_posicion(posicion)
        if jugadores is None:
            return

        # Solicitar índice del jugador, ajustado a nuevo índice comenzando en 1
        try:
            indice = int(input("Escribe el índice del jugador que deseas seleccionar: ")) - 1
            if 0 <= indice < len(jugadores):
                jugador_seleccionado = jugadores.iloc[indice]
                print(f"Jugador seleccionado: {jugador_seleccionado['Name']} para la posición {posicion}.")
                
                # Actualizar la formación con el jugador seleccionado
                self.formacion_actual.seleccionar_jugador(posicion, jugador_seleccionado['Name'])

                # Marcar al jugador como seleccionado
                self.jugadores_seleccionados.add(jugador_seleccionado['Name'])

                # Mostrar la formación actualizada
                self.formacion_actual.mostrar_display()
            else:
                print("Índice no válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")
            
    def hacer_plantilla(self):
        self.jugadores_df = pd.read_csv('APIs/jugadores_obtenidos.csv')

        
        # Elegir formaciones
        self.elegir_formacion()

        # Mostrar formaciones del equipo
        self.mostrar_formaciones()

        # Cambiar jugadores en la formación (ejemplo para cada posición)
        posiciones = ["GK", "LI", "DEF", "DEF", "LD", "MID", "MID", "MID", "EI", "FWD", "ED",]
        for posicion in posiciones:
            self.cambiar_jugador(posicion)
            
            
    def ver_plantilla(self):
        """Muestra la plantilla actual de jugadores seleccionados."""
        if self.formacion_actual:
            print("Plantilla actual:")
            self.formacion_actual.mostrar_display()  # Llama a un método de Formacion para mostrar los jugadores
            return self.formacion_actual
        else:
            print("No se ha seleccionado ninguna formación.")



# Ejemplo de uso
if __name__ == "__main__":
    seleccionador = SeleccionarJugadores('APIs/jugadores_obtenidos.csv')
    
    # Elegir formaciones
    seleccionador.elegir_formacion()

    # Mostrar formaciones del equipo
    seleccionador.mostrar_formaciones()

    # Cambiar jugadores en la formación (ejemplo para cada posición)
    posiciones = ["GK", "DEF", "MID", "FWD"]
    for posicion in posiciones:
        seleccionador.cambiar_jugador(posicion)
        
    seleccionador.ver_plantilla()


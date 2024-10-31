import pandas as pd
import random
from formaciones import Formacion, Equipo

class Partido:
    def __init__(self, equipo_usuario, seleccionador):
        self.equipo_usuario = equipo_usuario
        self.jugadores_df = pd.read_csv('APIs/all_players.csv')  # Cargar jugadores desde el CSV
        self.plantilla_usuario = seleccionador.ver_plantilla()  # Inicializa la plantilla del usuario aquí
        self.formacion_rival = None
        self.seleccionador = seleccionador

    def seleccionar_dificultad(self):
        """Solicita la dificultad del usuario y retorna la dificultad seleccionada."""
        print("\nSelecciona la dificultad del partido:")
        print("1. Facil")
        print("2. Normal")
        print("3. Dificil")
        print("4. Leyenda")

        opcion = input("\nSeleccione una dificultad: ")
        dificultades = {
            '1': "Facil",
            '2': "Normal",
            '3': "Dificil",
            '4': "Leyenda"
        }
        return dificultades.get(opcion)

    def generar_plantilla_rival(self, dificultad):
        """Genera una plantilla rival basada en la dificultad y las posiciones requeridas."""
        
        # Definir rangos de media según dificultad
        if dificultad == "Facil":
            media_min, media_max = 60, 70
        elif dificultad == "Normal":
            media_min, media_max = 70, 80
        elif dificultad == "Dificil":
            media_min, media_max = 80, 85
        elif dificultad == "Leyenda":
            media_min, media_max = 85, 90
        else:
            print("Dificultad no reconocida.")
            return None
        
        # Filtrar jugadores por media
        jugadores_filtrados = self.jugadores_df[
            (self.jugadores_df['OVR'] >= media_min) & (self.jugadores_df['OVR'] <= media_max)
        ]
        
        # Comprobar que hay suficientes jugadores en el rango
        if len(jugadores_filtrados) < 11:
            print(f"No hay suficientes jugadores para la dificultad {dificultad}.")
            return None
    
        # Lista de posiciones requeridas
        posiciones_requeridas = ["GK", "DEF", "DEF", "DEF", "DEF", "MID", "MID", "MID", "FWD", "EI", "ED"]
        plantilla_rival = pd.DataFrame(columns=jugadores_filtrados.columns)
    
        # Seleccionar jugadores para cada posición
        for posicion in posiciones_requeridas:
            # Filtrar jugadores de la posición actual
            if posicion == "GK":
                jugadores_posicion = jugadores_filtrados[jugadores_filtrados['Position'] == "GK"]
            elif posicion == "DEF":
                jugadores_posicion = jugadores_filtrados[jugadores_filtrados['Position'].isin(["CB", "LB", "RB"])]
            elif posicion == "MID":
                jugadores_posicion = jugadores_filtrados[jugadores_filtrados['Position'] == "CM"]
            elif posicion == "FWD":
                jugadores_posicion = jugadores_filtrados[jugadores_filtrados['Position'] == "ST"]
            elif posicion == "EI":
                jugadores_posicion = jugadores_filtrados[jugadores_filtrados['Position'] == "LW"]
            elif posicion == "ED":
                jugadores_posicion = jugadores_filtrados[jugadores_filtrados['Position'] == "RW"]
            else:
                print(f"Posición {posicion} no reconocida.")
                continue
            
            # Seleccionar aleatoriamente un jugador de esta posición
            if not jugadores_posicion.empty:
                jugador_seleccionado = jugadores_posicion.sample(n=1)
                plantilla_rival = pd.concat([plantilla_rival, jugador_seleccionado])
                # Eliminar el jugador seleccionado para evitar duplicados
                jugadores_filtrados = jugadores_filtrados.drop(jugador_seleccionado.index)
            else:
                print(f"No se encontraron jugadores para la posición {posicion} en el rango de media.")
        
        # Comprobar si se logró seleccionar 11 jugadores
        if len(plantilla_rival) < 11:
            print("No se pudo completar la plantilla rival con las posiciones necesarias.")
            return None
    
        # Resetear el índice para claridad
        plantilla_rival = plantilla_rival.reset_index(drop=True)
        return plantilla_rival



    def calcular_media_equipo(self, plantilla_usuario, plantilla_rival):
        """Compara las medias de los jugadores en las plantillas del usuario y rival."""
    
           
        # Obtener los nombres y medias de los jugadores del usuario
        jugadores_usuario = plantilla_usuario.get_jugadores()
        medias_usuario = [self.jugadores_df.loc[self.jugadores_df['Name'] == jugador, 'OVR'].values[0] for jugador in jugadores_usuario]
        
        # Obtener los nombres y medias de los jugadores del equipo rival
        jugadores_rival = plantilla_rival['Name'].tolist()  # Confirma que esta columna existe
        medias_rival = plantilla_rival['OVR'].tolist()
        
        # Crear un DataFrame para comparar las medias
        comparacion = pd.DataFrame({
            'Jugador Usuario': jugadores_usuario,
            'Media Usuario': medias_usuario,
            'Jugador Rival': jugadores_rival,
            'Media Rival': medias_rival
        })
    
        comparacion['Diferencia'] = comparacion['Media Usuario'] - comparacion['Media Rival']
        # Mostrar los resultados de la comparación
        print("\nComparación de medias jugador por jugador:")
        print(comparacion.to_string(index=False))  # `index=False` elimina la columna de índice
        
        return comparacion



    def jugar_partido(self):
        """Ejecuta el partido en función de la dificultad y muestra el resultado."""
        
        plantilla_usuario = self.seleccionador.ver_plantilla()
        if plantilla_usuario is None:
            print("No se ha definido ninguna plantilla de usuario.")
            return
    
        dificultad = self.seleccionar_dificultad()
        if dificultad is None:
            print("Dificultad no válida. Regresando al menú.")
            return
    
        print(f"\nJugando partido en dificultad: {dificultad}")
        
        # Generar la plantilla rival y verificar su contenido
        self.formacion_rival = self.generar_plantilla_rival(dificultad)
        if self.formacion_rival is None:
            print("No se pudo generar la plantilla rival.")
            return
        
        
        formacion_rival = Formacion("Rival", "4-3-3", self.formacion_rival['Name'].tolist())
        formacion_rival.mostrar_display()
        
        # Calcular y mostrar las medias de ambos equipos usando el método `calcular_media_equipo`
        comparacion = self.calcular_media_equipo(plantilla_usuario, self.formacion_rival)

    
        # Calcular las medias generales de ambos equipos para la probabilidad de victoria
        media_usuario = comparacion['Media Usuario'].mean()
        media_rival = comparacion['Media Rival'].mean()
    
        # Calcular la probabilidad de victoria
        if dificultad == "Facil":
            prob_victoria = 0.8
        elif dificultad == "Normal":
            prob_victoria = 0.6
        elif dificultad == "Dificil":
            prob_victoria = 0.4
        elif dificultad == "Leyenda":
            prob_victoria = 0.2
    
        diferencia = media_usuario - media_rival
        prob_victoria += diferencia * 0.01
    
        # Asegurar que la probabilidad esté dentro del rango [0, 1]
        prob_victoria = max(0, min(1, prob_victoria))
    
        # Determinar el resultado del partido
        resultado = random.random() < prob_victoria
        if resultado:
            print("\n¡Victoria! Has ganado el partido.")
        else:
            print("\nDerrota. Has perdido el partido.")

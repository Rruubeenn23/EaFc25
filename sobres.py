import time
import pandas as pd
import random
from abc import ABC, abstractmethod
from guardarJugadores import guardar_jugadores

# Cargar datos desde el archivo CSV
players_data = pd.read_csv('APIs/all_players.csv')

class Sobre(ABC):
    def __init__(self, probabilities, OVR_ranges):
        """
        Constructor base para la clase Sobre.
        :param probabilities: Diccionario con las probabilidades para cada rango de media.
        :param ovr_ranges: Diccionario que define los rangos de media para cada categoría.
        """
        self.probabilities = probabilities
        self.OVR_ranges = OVR_ranges
        self.categories = self._categorize_players()
        
    def _categorize_players(self):
        """
        Clasifica a los jugadores en categorías basadas en los rangos de media.
        :return: Diccionario con DataFrames de jugadores divididos por categorías de media.
        """
        categories = {}
        for category, (min_OVR, max_OVR) in self.OVR_ranges.items():
            categories[category] = players_data[(players_data['OVR'] >= min_OVR) & (players_data['OVR'] <= max_OVR)]
        return categories

    @abstractmethod
    def open_pack(self):
        """
        Método abstracto para abrir un sobre.
        Debe ser implementado por cada clase hija.
        """
        pass

# Clases hijas para cada tipo de sobre

class SobreBronce(Sobre):
    def __init__(self):
        probabilities = {
            '50-58': 0.7,
            '59-62': 0.25,
            '63-64': 0.05
        }
        OVR_ranges = {
            '50-58': (50, 58),
            '59-62': (59, 62),
            '63-64': (63, 64)
        }
        super().__init__(probabilities, OVR_ranges)

    def open_pack(self):
        players = []
        for _ in range(12):
            category = random.choices(
                list(self.probabilities.keys()),
                list(self.probabilities.values())
            )[0]
            
            if not self.categories[category].empty:
                player = self.categories[category].sample(1).iloc[0]
                players.append(player)
        if players:
            guardar_jugadores(pd.DataFrame(players))
        
        players = sorted(players, key=lambda x: x['OVR'], reverse=True)

        # Ordenar jugadores por OVR de mayor a menor
        best_player = players[0]
        print("\nEstadísticas del Jugador Portada:")
        print(f"Position: {best_player['Position']}")
        time.sleep(1)
        print(f"Nation: {best_player['Nation']}")
        time.sleep(1)
        print(f"League: {best_player['League']}")
        time.sleep(1)
        print(f"Team: {best_player['Team']}")
        time.sleep(1)
        print(f"\nNombre del Jugador: {best_player['Name']}")
        print(f"OVR: {best_player['OVR']}")
        print("\nEstadísticas:")
        print(f"{'PAC':<5} {'SHO':<5} {'PAS':<5}   {'DRI':<5} {'DEF':<5} {'PHY':<5}")
        print(f"{best_player['PAC']:<5} {best_player['SHO']:<5} {best_player['PAS']:<5}   {best_player['DRI']:<5} {best_player['DEF']:<5} {best_player['PHY']:<5}\n")
       
        time.sleep(5)

        for player in players:
            print(f"\nNombre: {player['Name']}, OVR: {player['OVR']}")
        
# Implementación similar para las otras clases de sobres:

class SobrePlata(Sobre):
    def __init__(self):
        probabilities = {
            '65-68': 0.7,
            '69-72': 0.25,
            '73-74': 0.05
        }
        OVR_ranges = {
            '65-68': (65, 68),
            '69-72': (69, 72),
            '73-74': (73, 74)
        }
        super().__init__(probabilities, OVR_ranges)

    def open_pack(self):
        players = []
        for _ in range(12):
            category = random.choices(
                list(self.probabilities.keys()),
                list(self.probabilities.values())
            )[0]
            
            if not self.categories[category].empty:
                player = self.categories[category].sample(1).iloc[0]
                players.append(player)
        if players:
            guardar_jugadores(pd.DataFrame(players))
        
        players = sorted(players, key=lambda x: x['OVR'], reverse=True)

        best_player = players[0]
        print("\nEstadísticas del Jugador Portada:")
        print(f"Position: {best_player['Position']}")
        time.sleep(1)
        print(f"Nation: {best_player['Nation']}")
        time.sleep(1)
        print(f"League: {best_player['League']}")
        time.sleep(1)
        print(f"Team: {best_player['Team']}")
        time.sleep(1)
        print(f"\nNombre del Jugador: {best_player['Name']}")
        print(f"OVR: {best_player['OVR']}")
        print("\nEstadísticas:")
        print(f"{'PAC':<5} {'SHO':<5} {'PAS':<5}   {'DRI':<5} {'DEF':<5} {'PHY':<5}")
        print(f"{best_player['PAC']:<5} {best_player['SHO']:<5} {best_player['PAS']:<5}   {best_player['DRI']:<5} {best_player['DEF']:<5} {best_player['PHY']:<5}\n")
       
        time.sleep(5)

        for player in players:
            print(f"\nNombre: {player['Name']}, OVR: {player['OVR']}")
        
# Repite de manera similar para las c
class SobreOroNormal(Sobre):
    def __init__(self):
        probabilities = {
            '75-79': 0.7,
            '80-84': 0.25,
            '85+': 0.05
        }
        OVR_ranges = {
            '75-79': (75, 79),
            '80-84': (80, 84),
            '85+': (85, 99)
        }
        super().__init__(probabilities, OVR_ranges)

    def open_pack(self):
        players = []
        for _ in range(12):
            category = random.choices(
                list(self.probabilities.keys()),
                list(self.probabilities.values())
            )[0]
            
            if not self.categories[category].empty:
                player = self.categories[category].sample(1).iloc[0]
                players.append(player)
        if players:
            guardar_jugadores(pd.DataFrame(players))
        
        players = sorted(players, key=lambda x: x['OVR'], reverse=True)

        best_player = players[0]
        print("\nEstadísticas del Jugador Portada:")
        print(f"Position: {best_player['Position']}")
        time.sleep(1)
        print(f"Nation: {best_player['Nation']}")
        time.sleep(1)
        print(f"League: {best_player['League']}")
        time.sleep(1)
        print(f"Team: {best_player['Team']}")
        time.sleep(1)
        print(f"\nNombre del Jugador: {best_player['Name']}")
        print(f"OVR: {best_player['OVR']}")
        print("\nEstadísticas:")
        print(f"{'PAC':<5} {'SHO':<5} {'PAS':<5}   {'DRI':<5} {'DEF':<5} {'PHY':<5}")
        print(f"{best_player['PAC']:<5} {best_player['SHO']:<5} {best_player['PAS']:<5}   {best_player['DRI']:<5} {best_player['DEF']:<5} {best_player['PHY']:<5}\n")
       
        time.sleep(5)

        players = sorted(players, key=lambda x: x['OVR'], reverse=True)
        for player in players:
            print(f"\nNombre: {player['Name']}, OVR: {player['OVR']}")
        
        
class SobreOroPromocional(Sobre):
    def __init__(self):
        probabilities = {
            '86-88': 0.7,
            '89-90': 0.25,
            '90+': 0.05
        }
        OVR_ranges = {
            '86-88': (86, 88),
            '89-90': (89, 90),
            '90+': (90, 99)
        }
        super().__init__(probabilities, OVR_ranges)

    def open_pack(self):
        players = []
        for _ in range(5):
            category = random.choices(
                list(self.probabilities.keys()),
                list(self.probabilities.values())
            )[0]
            
            if not self.categories[category].empty:
                player = self.categories[category].sample(1).iloc[0]
                players.append(player)
        if players:
            guardar_jugadores(pd.DataFrame(players))
            
        players = sorted(players, key=lambda x: x['OVR'], reverse=True)

        best_player = players[0]
        print("\nEstadísticas del Jugador Portada:")
        print(f"Position: {best_player['Position']}")
        time.sleep(1)
        print(f"Nation: {best_player['Nation']}")
        time.sleep(1)
        print(f"League: {best_player['League']}")
        time.sleep(1)
        print(f"Team: {best_player['Team']}")
        time.sleep(1)
        print(f"\nNombre del Jugador: {best_player['Name']}")
        print(f"OVR: {best_player['OVR']}")
        print("\nEstadísticas:")
        print(f"{'PAC':<5} {'SHO':<5} {'PAS':<5}   {'DRI':<5} {'DEF':<5} {'PHY':<5}")
        print(f"{best_player['PAC']:<5} {best_player['SHO']:<5} {best_player['PAS']:<5}   {best_player['DRI']:<5} {best_player['DEF']:<5} {best_player['PHY']:<5}\n")
        
        time.sleep(5)

        players = sorted(players, key=lambda x: x['OVR'], reverse=True)
        for player in players:
            print(f"\nNombre: {player['Name']}, OVR: {player['OVR']}")
        
# menu.py
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:28:50 2024

@author: ruben
"""

import time
import sys
import pandas as pd
from menuSobres import mostrar_menu_sobres  
from mostrarJugadores import mostrar_jugadores
from plantilla import SeleccionarJugadores
from partido import Partido  # Importar la clase Partido

class MenuPrincipal:
    def __init__(self): 
        self.seleccionador = SeleccionarJugadores('APIs/jugadores_obtenidos.csv')
        self.jugadores_df = pd.read_csv('APIs/all_players.csv')

    def mostrar_menu(self):
        while True:
            print("\nMenu Principal:")
            print("1. Abrir sobres")
            print("2. Ver Club")
            print("3. Hacer Plantilla")
            print("4. Ver Plantilla")
            print("5. Jugar Partido")
            print("6. Salir")

            choice = input("\nSeleccione una opción: ")

            if choice == '1':
                mostrar_menu_sobres()  
            elif choice == '2':
                mostrar_jugadores()
            elif choice == '3':
                self.seleccionador.hacer_plantilla()
            elif choice == '4':
                self.seleccionador.ver_plantilla()
            elif choice == '5':
                equipo_usuario = self.seleccionador.formacion_actual.obtener_plantilla()
                partido = Partido(equipo_usuario, self.seleccionador)  # Pass the seleccionador
                partido.jugar_partido()
            elif choice == '6':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

# Ejemplo de uso
if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.mostrar_menu()

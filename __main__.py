# menu.py
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:28:50 2024

@author: ruben
"""

import time
import sys
import pandas as pd
import git
import datetime
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


import git  # Asegúrate de tener instalado GitPython
from datetime import datetime

def git_push(repo_path):
    """
    Realiza un commit y un push de todos los cambios en el repositorio local de Git.

    Parámetros:
        repo_path (str): Ruta local del repositorio de Git donde se encuentran los archivos.
    """
    try:
        # Clona el repositorio usando GitPython
        repo = git.Repo(repo_path)
        
        # Verifica que no haya problemas en el repositorio
        if repo.is_dirty(untracked_files=True):
            # Obtener la fecha actual en formato dd/mm/aaaa
            fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
            commit_message = f"Actualización {fecha_actual}"

            # Agrega y confirma los cambios
            repo.git.add(A=True)
            repo.index.commit(commit_message)

            # Hace push a la rama principal
            origin = repo.remote(name='origin')
            origin.push()

            print(f"Commit realizado con el mensaje: '{commit_message}'")
            print("Archivos subidos a GitHub correctamente.")
        else:
            print("No hay cambios para hacer commit.")

    except git.exc.GitCommandError as e:
        print(f"Error durante la ejecución de Git: {e}")

# Ruta a tu repositorio local
repo_path = r"C:\Users\ruben\Documents\2ºDAM\Desarrollo de Interfaces\Desarrollo de Interfaces Python\Proyecto1RubenCereceda"

# Llamada a la función para subir los archivos
git_push(repo_path)

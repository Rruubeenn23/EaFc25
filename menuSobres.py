# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:09:04 2024

@author: ruben
"""

import sys
from sobres import SobreBronce, SobrePlata, SobreOroNormal, SobreOroPromocional

def mostrar_menu_sobres():
    """
    Muestra el menú de selección de sobres.
    """
    print("\nSeleccione el tipo de sobre que desea abrir:")
    print("1. Sobre Bronce")
    print("2. Sobre Plata")
    print("3. Sobre Oro Normal")
    print("4. Sobre Oro Promocional")
    print("5. Salir")

    opcion = input("Ingrese el número de su opción: ")
    abrir_sobre(opcion)

def abrir_sobre(opcion):
    """
    Llama a la clase correspondiente para abrir un sobre según la opción seleccionada.
    :param opcion: La opción seleccionada por el usuario.
    """
    if opcion == '1':
        sobre = SobreBronce()
        sobre.open_pack()

    elif opcion == '2':
        sobre = SobrePlata()
        sobre.open_pack()

    elif opcion == '3':
        sobre = SobreOroNormal()
        sobre.open_pack()

    elif opcion == '4':
        sobre = SobreOroPromocional()
        sobre.open_pack()

    elif opcion == '5':
        print("Saliendo del programa...")
        sys.exit()

    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")

if __name__ == "__main__":
    while True:
        mostrar_menu_sobres()

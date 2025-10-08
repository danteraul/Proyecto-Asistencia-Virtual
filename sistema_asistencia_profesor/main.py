"""
Proyecto Asistencia Virtual - Tecnicatura en Desarrollo de Software
Sistema ecológico para reemplazar el uso de papel en asistencias
Archivo principal que inicia la aplicación
"""

import tkinter as tk
from database import Database
from asistencia import GestorAsistencia
from interfaz_grafica import InterfazAsistencia

def main():
    """
    Función principal que inicia la aplicación de Asistencia Virtual
    """
    print("=" * 50)
    print("PROYECTO ASISTENCIA VIRTUAL")
    print("Tecnicatura en Desarrollo de Software - Año 3")
    print("Sistema ecológico - Cero papel")
    print("=" * 50)
    
    # Inicializar componentes del sistema
    database = Database()
    gestor_asistencia = GestorAsistencia(database)
    
    # Crear ventana principal de la aplicación
    root = tk.Tk()
    
    # Configurar la interfaz gráfica
    app = InterfazAsistencia(root, gestor_asistencia, database)
    
    # Ejecutar la aplicación
    print("✅ Sistema iniciado correctamente")
    print("📊 Cargando interfaz gráfica...")
    root.mainloop()

if __name__ == "__main__":
    # Punto de entrada principal de la aplicación
    main()
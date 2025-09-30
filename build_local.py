#!/usr/bin/env python3
"""
Script para compilar la aplicación localmente a APK
Requiere que tengas instalado Flutter SDK y Android SDK
"""

import subprocess
import sys
import os

def check_requirements():
    """Verificar que los requisitos estén instalados"""
    print("🔍 Verificando requisitos...")
    
    # Verificar flet
    try:
        import flet
        print(f"✅ Flet {flet.__version__} está instalado")
    except ImportError:
        print("❌ Flet no está instalado. Ejecuta: pip install flet[build]")
        return False
    
    # Verificar Flutter
    try:
        result = subprocess.run(['flutter', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Flutter SDK está instalado")
        else:
            print("❌ Flutter SDK no está disponible")
            return False
    except FileNotFoundError:
        print("❌ Flutter SDK no está instalado")
        return False
    
    return True

def build_apk():
    """Compilar la aplicación a APK"""
    print("🏗️  Compilando aplicación a APK...")
    
    cmd = [
        'flet', 'build', 'apk',
        '--project', 'Diario Personal',
        '--description', 'Una aplicación de diario personal',
        '--org', 'com.diarioflet.app',
        '--verbose'
    ]
    
    try:
        result = subprocess.run(cmd, check=True)
        print("✅ APK compilado exitosamente!")
        print("📱 Busca el archivo APK en la carpeta 'build/apk/'")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al compilar APK: {e}")
        return False

def main():
    print("🚀 Script de compilación local para Diario Personal")
    print("=" * 50)
    
    if not check_requirements():
        print("\n❌ No se pueden cumplir los requisitos.")
        print("Instala los requisitos y vuelve a intentar.")
        sys.exit(1)
    
    if build_apk():
        print("\n🎉 ¡Compilación completada!")
    else:
        print("\n💥 Compilación fallida.")
        sys.exit(1)

if __name__ == "__main__":
    main()
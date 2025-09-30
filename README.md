# 📖 Diario Personal con Flet

Una aplicación de diario personal desarrollada en Python con Flet que permite a los usuarios escribir y guardar entradas con fecha y hora.

## ✨ Características

- 📝 Interfaz intuitiva para escribir entradas de diario
- 💾 Almacenamiento local con SQLite
- 📅 Registro automático de fecha y hora
- 🗑️ Funcionalidad para eliminar entradas
- 📱 Compatible con dispositivos móviles (Android APK)
- 🎨 Interfaz moderna y responsive

## 🚀 Instalación y Uso

### Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación local

1. Clona el repositorio:
```bash
git clone https://github.com/cucarraca/diario-flet.git
cd diario-flet
```

2. Crea un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```bash
python main.py
```

## 📱 Compilación a APK

Para compilar la aplicación a APK para Android, sigue estos pasos:

### Opción 1: Script automático (recomendado)

```bash
python build_local.py
```

### Opción 2: Comando manual

1. Instala las herramientas de build:
```bash
pip install flet[build]
```

2. Compila la APK:
```bash
flet build apk --project "Diario Personal" --description "Una aplicación de diario personal" --org com.diarioflet.app
```

**Nota:** Para compilar APK necesitas tener instalado:
- Flutter SDK
- Android SDK
- Java JDK 11 o superior

## 🤖 GitHub Actions (CI/CD)

El repositorio incluye configuración de GitHub Actions que **intentará** compilar automáticamente la APK en cada push al branch principal. Sin embargo, debido a las limitaciones del entorno de CI y las dependencias complejas de Flutter/Android SDK, este proceso puede fallar.

### Alternativas para obtener la APK:

1. **Compilación local** (más confiable): Usa los scripts proporcionados arriba
2. **GitHub Codespaces**: Ejecuta el build en un entorno de desarrollo en la nube
3. **Releases manuales**: Compila localmente y sube manualmente a GitHub Releases

## 📄 Estructura del Proyecto

```
diario-flet/
├── main.py              # Aplicación principal
├── build_local.py       # Script para compilar APK localmente
├── requirements.txt     # Dependencias de Python
├── README.md           # Documentación
├── .gitignore          # Archivos a ignorar por git
├── LICENSE             # Licencia MIT
└── .github/
    └── workflows/
        └── build.yml   # GitHub Actions para APK (experimental)
```

## 🛠️ Desarrollo

La aplicación está construida con:

- **Flet**: Framework multiplataforma para Python
- **SQLite**: Base de datos local para persistencia
- **GitHub Actions**: CI/CD para compilación automática de APK (experimental)

### Características técnicas:

- **Interfaz responsive**: Se adapta a diferentes tamaños de pantalla
- **Base de datos local**: Los datos se guardan en `diario.db`
- **Sin dependencias externas**: Funciona completamente offline
- **Multiplataforma**: Windows, macOS, Linux, Android, iOS (con compilación apropiada)

## 📦 Funcionalidades de la aplicación

### Escribir entrada
- Campo de texto multilínea para escribir
- Botón de "Guardar Entrada" 
- Timestamp automático

### Ver entradas anteriores
- Lista scrolleable de entradas
- Cada entrada muestra fecha/hora y contenido
- Botón de eliminación por entrada

### Gestión de datos
- Almacenamiento automático en SQLite
- No requiere configuración de base de datos
- Datos persistentes entre sesiones

## 🔧 Troubleshooting

### Error de libmpv.so.1
Si obtienes un error sobre libmpv.so.1:
```bash
# Ubuntu/Debian
sudo apt install libmpv1

# Arch/Manjaro
sudo pacman -S mpv

# macOS
brew install mpv
```

### Error de Flutter SDK
Para compilar APK, instala Flutter:
```bash
# Sigue las instrucciones en https://flutter.dev/docs/get-started/install
```

### Error de Android SDK
Para compilar APK, instala Android Studio o Android SDK:
```bash
# Descarga desde https://developer.android.com/studio
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una branch para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🔧 Soporte

Si tienes algún problema o sugerencia, por favor abre un [issue](https://github.com/cucarraca/diario-flet/issues) en GitHub.

---

### 📝 Notas del desarrollador

Este proyecto fue creado como demostración de las capacidades de Flet para crear aplicaciones multiplataforma con Python. La compilación a APK puede ser compleja debido a las dependencias de Flutter y Android SDK, por lo que se recomienda la compilación local para mejores resultados.
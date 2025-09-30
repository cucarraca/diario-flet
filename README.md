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
git clone https://github.com/TU_USUARIO/diario-flet.git
cd diario-flet
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
python main.py
```

## 📱 Descarga de APK

Las versiones compiladas para Android están disponibles en la sección [Releases](https://github.com/TU_USUARIO/diario-flet/releases) de este repositorio. Cada commit al branch principal genera automáticamente una nueva APK.

## 🛠️ Desarrollo

La aplicación está construida con:

- **Flet**: Framework multiplataforma para Python
- **SQLite**: Base de datos local para persistencia
- **GitHub Actions**: CI/CD para compilación automática de APK

## 📄 Estructura del Proyecto

```
diario-flet/
├── main.py              # Aplicación principal
├── requirements.txt     # Dependencias de Python
├── README.md           # Documentación
└── .github/
    └── workflows/
        └── build.yml   # GitHub Actions para APK
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

Si tienes algún problema o sugerencia, por favor abre un [issue](https://github.com/TU_USUARIO/diario-flet/issues) en GitHub.
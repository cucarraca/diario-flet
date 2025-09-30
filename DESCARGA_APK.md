# 📱 Guía para Descargar APK

## Método 1: Desde GitHub Actions (cuando funcione)

1. Ve a la pestaña [Actions](https://github.com/cucarraca/diario-flet/actions) del repositorio
2. Busca el workflow "Build Android APK" que haya completado exitosamente (✅)
3. Haz clic en el workflow exitoso
4. En la sección "Artifacts", descarga "diario-personal-apk"
5. Descomprime el archivo ZIP descargado para obtener la APK

## Método 2: Desde Releases (recomendado)

1. Ve a la sección [Releases](https://github.com/cucarraca/diario-flet/releases)
2. Busca la última release
3. En "Assets", descarga el archivo `.apk`

## Método 3: Compilación Local (más confiable)

### Usando el script automático:
```bash
git clone https://github.com/cucarraca/diario-flet.git
cd diario-flet
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python build_local.py
```

### Usando comandos manuales:
```bash
# Después de instalar Flutter SDK y Android SDK
pip install flet[build]
flet build apk --project "Diario Personal" --description "Una aplicación de diario personal" --org com.diarioflet.app
```

## Método 4: Descarga mediante GitHub CLI

Si tienes GitHub CLI instalado:

```bash
# Listar workflows recientes
gh run list --repo cucarraca/diario-flet

# Descargar artifacts del último workflow exitoso
gh run download [RUN_ID] --repo cucarraca/diario-flet

# O descargar todos los artifacts
gh run download --repo cucarraca/diario-flet
```

## 📥 Script de descarga automática

Aquí tienes un script que puedes usar para descargar automáticamente la APK:

```bash
#!/bin/bash
# download_apk.sh

REPO="cucarraca/diario-flet"
WORKFLOW="Build Android APK"

echo "🔍 Buscando el último workflow exitoso..."

# Obtener el ID del último workflow exitoso
RUN_ID=$(gh run list --repo $REPO --workflow "$WORKFLOW" --status success --limit 1 --json databaseId --jq '.[0].databaseId')

if [ -z "$RUN_ID" ]; then
    echo "❌ No se encontró ningún workflow exitoso."
    echo "💡 Intenta compilar localmente con: python build_local.py"
    exit 1
fi

echo "📥 Descargando artifacts del workflow $RUN_ID..."

# Descargar artifacts
gh run download $RUN_ID --repo $REPO --name diario-personal-apk

echo "✅ APK descargada exitosamente!"
echo "📱 Busca el archivo .apk en el directorio actual"
```

## 🛠️ Requisitos para compilación local

Para compilar la APK localmente necesitas:

1. **Python 3.8+** con pip
2. **Flutter SDK**: https://flutter.dev/docs/get-started/install
3. **Android SDK**: Instala Android Studio o solo el SDK
4. **Java JDK 11+**: OpenJDK o Oracle JDK

### Verificar instalación:
```bash
python --version
flutter --version
flutter doctor
java --version
```

## 🚨 Troubleshooting

### GitHub Actions falla
- Los workflows de GitHub Actions pueden fallar por limitaciones del runner
- La compilación de Flutter/Android en CI es compleja
- **Solución**: Compila localmente para resultados más confiables

### Error de dependencias
- Instala las dependencias del sistema necesarias
- En Ubuntu/Debian: `sudo apt install libmpv1`
- En Arch/Manjaro: `sudo pacman -S mpv`

### Error de Flutter
- Verifica que Flutter esté en tu PATH
- Ejecuta `flutter doctor` para diagnosticar problemas
- Acepta las licencias de Android: `flutter doctor --android-licenses`

## 📞 Soporte

Si tienes problemas:
1. Revisa los [Issues](https://github.com/cucarraca/diario-flet/issues) del repositorio
2. Crea un nuevo issue con detalles del problema
3. Incluye el output de `flutter doctor` si es relevante
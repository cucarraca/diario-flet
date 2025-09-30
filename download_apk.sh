#!/bin/bash
# Script para descargar automáticamente la APK desde GitHub Actions

REPO="cucarraca/diario-flet"
WORKFLOW="Build Android APK"

echo "🚀 Script de descarga automática de APK"
echo "📱 Diario Personal - Flet App"
echo "=" $(printf '%.0s' {1..40})

# Verificar que gh CLI esté instalado
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) no está instalado."
    echo "💡 Instálalo desde: https://cli.github.com/"
    exit 1
fi

# Verificar autenticación
if ! gh auth status &> /dev/null; then
    echo "🔑 No estás autenticado en GitHub CLI."
    echo "💡 Ejecuta: gh auth login"
    exit 1
fi

echo "🔍 Buscando el último workflow exitoso..."

# Obtener el ID del último workflow exitoso
RUN_ID=$(gh run list --repo $REPO --workflow "$WORKFLOW" --status success --limit 1 --json databaseId --jq '.[0].databaseId' 2>/dev/null)

if [ -z "$RUN_ID" ] || [ "$RUN_ID" = "null" ]; then
    echo "❌ No se encontró ningún workflow exitoso para '$WORKFLOW'."
    echo ""
    echo "📋 Workflows disponibles:"
    gh run list --repo $REPO --limit 5 --json conclusion,headSha,workflowName,createdAt --template '{{range .}}{{.workflowName}} - {{.conclusion}} ({{timeago .createdAt}}){{"\n"}}{{end}}'
    echo ""
    echo "🛠️  Alternativas:"
    echo "   1. Espera a que un workflow complete exitosamente"
    echo "   2. Compila localmente: python build_local.py"
    echo "   3. Verifica la sección Releases: https://github.com/$REPO/releases"
    exit 1
fi

echo "✅ Encontrado workflow exitoso: $RUN_ID"
echo "📥 Descargando artifacts..."

# Crear directorio para la descarga
DOWNLOAD_DIR="./apk_download_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$DOWNLOAD_DIR"
cd "$DOWNLOAD_DIR"

# Descargar artifacts
if gh run download $RUN_ID --repo $REPO --name diario-personal-apk 2>/dev/null; then
    echo "✅ APK descargada exitosamente!"
    echo "📍 Ubicación: $DOWNLOAD_DIR"
    echo "📱 Archivos descargados:"
    find . -name "*.apk" -type f -exec ls -lh {} \;
    
    # Mover APK al directorio padre con un nombre más limpio
    APK_FILE=$(find . -name "*.apk" -type f | head -1)
    if [ -n "$APK_FILE" ]; then
        NEW_NAME="diario-personal-$(date +%Y%m%d_%H%M%S).apk"
        cp "$APK_FILE" "../$NEW_NAME"
        echo "📋 APK copiada como: $NEW_NAME"
    fi
else
    echo "❌ Error al descargar artifacts."
    echo "💡 Posibles causas:"
    echo "   - El workflow no generó artifacts"
    echo "   - Los artifacts expiraron (duran 90 días)"
    echo "   - Permisos insuficientes"
    echo ""
    echo "🔍 Verifica manualmente en:"
    echo "   https://github.com/$REPO/actions/runs/$RUN_ID"
fi

echo ""
echo "🎉 Proceso completado!"
echo "📖 Para más información, ve: README.md y DESCARGA_APK.md"
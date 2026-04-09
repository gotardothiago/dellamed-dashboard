#!/bin/bash
# Script para apresentar dashboard no Canvas

# Configurações
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CANVAS_ROOT="${HOME}/clawd/canvas"
DASHBOARD_FILE="canvas_dashboard.html"

# Cria diretório Canvas se não existir
mkdir -p "${CANVAS_ROOT}"

# Copia dashboard
cp "${SCRIPT_DIR}/${DASHBOARD_FILE}" "${CANVAS_ROOT}/"

echo "✅ Dashboard copiado para ${CANVAS_ROOT}/${DASHBOARD_FILE}"
echo ""
echo "🎯 Para apresentar no Canvas:"
echo ""
echo "1. Liste os nodes disponíveis:"
echo "   openclaw nodes list"
echo ""
echo "2. Apresente no node desejado:"
echo "   openclaw canvas action:present node:<NODE_ID> target:http://<HOST>:18793/__openclaw__/canvas/${DASHBOARD_FILE}"
echo ""
echo "📱 Dashboard será exibido no Mac/iPhone conectado"

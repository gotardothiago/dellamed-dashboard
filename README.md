# Dellamed Dashboard - Super Edition 🚀

Dashboard executivo completo para Dellamed com 4 camadas de visualização.

## 🎯 Funcionalidades

### 1. Streamlit Dashboard (Web)
- **URL:** https://dellamed-dashboard.streamlit.app
- **Acesso:** Qualquer dispositivo, compartilhável
- **Features:**
  - ✅ Auto-refresh a cada 5 minutos
  - ✅ Integração Qlik Cloud (API REST)
  - ✅ 4 abas: Performance, LATAM, Eventos, Alertas
  - ✅ Gráficos interativos Plotly
  - ✅ KPIs em tempo real

### 2. Canvas Dashboard (Mac/iPhone)
- **Arquivo:** `canvas_dashboard.html`
- **Execução:** Local via skill Canvas
- **Features:**
  - ✅ Design premium dark mode
  - ✅ Animações e transições
  - ✅ Auto-refresh
  - ✅ Responsivo para mobile
  - ✅ Gráficos Chart.js

### 3. ChartGen Analysis (AI)
- **Arquivo:** `chartgen_analysis.py`
- **Features:**
  - ✅ Análise automática de dados
  - ✅ Geração de insights
  - ✅ Criação de PPTs
  - ✅ Projeções e tendências

### 4. Chart-Image (Alerts)
- **Skill:** chart-image
- **Uso:** Gráficos PNG para notificações
- **Features:**
  - ✅ Geração rápida (<500ms)
  - ✅ Dark mode automático
  - ✅ Perfeito para alerts Telegram

## 🚀 Deploy

### Streamlit Cloud
```bash
git push origin main
# Deploy automático em https://share.streamlit.io
```

### Canvas (Local)
```bash
# Copiar para diretório Canvas
mkdir -p ~/clawd/canvas
cp canvas_dashboard.html ~/clawd/canvas/

# Apresentar no node
openclaw canvas action:present node:<node-id> target:http://<host>:18793/__openclaw__/canvas/canvas_dashboard.html
```

## 📊 Estrutura de Dados

```
dellamed-dashboard/
├── app.py                  # Streamlit principal
├── qlik_connector.py       # Conector Qlik Cloud
├── canvas_dashboard.html   # Dashboard Canvas
├── chartgen_analysis.py    # Análise ChartGen
├── requirements.txt        # Dependências
└── README.md              # Documentação
```

## 🔌 Integrações

| Fonte | Status | Descrição |
|-------|--------|-----------|
| Qlik Cloud | ✅ Configurado | API REST com Bearer Token |
| Notion | ✅ Configurado | Sync bidirecional |
| SAP CX | 🔄 Pendente | Aguardando credenciais |
| ChartGen | ✅ Configurado | API key necessária |

## 🎨 Design System

- **Cores:** Azul (#3b82f6), Roxo (#8b5cf6), Dark (#0f172a)
- **Fontes:** System UI, Inter
- **Gráficos:** Plotly (web), Chart.js (Canvas)
- **Temas:** Dark mode padrão

## 👨‍💻 Desenvolvido por

Axis para Thiago Gotardo / Dellamed

---

**Versão:** 2.0 Super Edition  
**Última atualização:** Abril 2026

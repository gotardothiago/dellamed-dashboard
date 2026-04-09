import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="Dellamed - Dashboard Executivo",
    page_icon="🏥",
    layout="wide"
)

# Título
st.title("🏥 Dellamed - Dashboard Executivo")
st.markdown("*Painel de vendas, expansão LATAM e performance*")

# Sidebar
st.sidebar.header("📊 Filtros")
periodo = st.sidebar.selectbox(
    "Período",
    ["Últimos 30 dias", "Últimos 3 meses", "Últimos 6 meses", "Ano atual"]
)

regiao = st.sidebar.multiselect(
    "Região",
    ["Brasil", "México", "Colômbia", "Argentina", "Chile"],
    default=["Brasil"]
)

# Dados simulados (substituir por dados reais do Qlik)
@st.cache_data
def load_data():
    # Simulação de dados de vendas
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = {
        'Data': dates,
        'Faturamento': [1000000 + i * 1000 + (i % 30) * 50000 for i in range(len(dates))],
        'Pedidos': [50 + i % 20 for i in range(len(dates))],
        'Região': ['Brasil' if i % 5 != 0 else 'México' if i % 5 == 1 else 'Colômbia' for i in range(len(dates))]
    }
    return pd.DataFrame(data)

df = load_data()

# KPIs em cards
st.subheader("📈 KPIs Principais")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Faturamento Total",
        value="R$ 12.3M",
        delta="+10.5%"
    )

with col2:
    st.metric(
        label="Pedidos no Mês",
        value="1,247",
        delta="+8.2%"
    )

with col3:
    st.metric(
        label="Ticket Médio",
        value="R$ 9.850",
        delta="+2.1%"
    )

with col4:
    st.metric(
        label="Churn",
        value="20.82%",
        delta="-1.5%",
        delta_color="inverse"
    )

st.divider()

# Gráficos
st.subheader("📊 Análises")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("#### Faturamento por Região")
    fig_regiao = px.pie(
        df.groupby('Região')['Faturamento'].sum().reset_index(),
        values='Faturamento',
        names='Região',
        hole=0.4
    )
    st.plotly_chart(fig_regiao, use_container_width=True)

with col_right:
    st.markdown("#### Evolução de Vendas")
    fig_evolucao = px.line(
        df.groupby('Data')['Faturamento'].sum().reset_index(),
        x='Data',
        y='Faturamento',
        title=None
    )
    st.plotly_chart(fig_evolucao, use_container_width=True)

st.divider()

# Expansão LATAM
st.subheader("🌎 Expansão LATAM")

col_lat1, col_lat2, col_lat3 = st.columns(3)

with col_lat1:
    st.markdown("#### México 🇲🇽")
    st.metric("Potencial", "US$ 10.9B", "CAGR 7.9%")
    st.progress(35, text="35% - Em prospecção")

with col_lat2:
    st.markdown("#### Colômbia 🇨🇴")
    st.metric("Potencial", "US$ 3.15B", "CAGR 10.3%")
    st.progress(20, text="20% - Mapeamento")

with col_lat3:
    st.markdown("#### Argentina 🇦🇷")
    st.metric("Potencial", "US$ 2.8B", "CAGR 6.5%")
    st.progress(10, text="10% - Análise inicial")

st.divider()

# Feiras e Eventos
st.subheader("📅 Próximas Feiras")

eventos = [
    {"nome": "Hospitalar 2026 + CAD", "local": "São Paulo, Brasil", "data": "19-22 Maio", "status": "✅ Confirmado"},
    {"nome": "MEDITECH 2026", "local": "Bogotá, Colômbia", "data": "28-31 Julho", "status": "📋 Planejando"},
    {"nome": "ExpoMEDICAL 2026", "local": "Buenos Aires, Argentina", "data": "A confirmar", "status": "🔍 Avaliando"}
]

for evento in eventos:
    with st.expander(f"{evento['nome']} - {evento['data']}"):
        st.markdown(f"**Local:** {evento['local']}")
        st.markdown(f"**Status:** {evento['status']}")

st.divider()

# Alertas
st.subheader("🚨 Alertas e Ações")

alertas = [
    "📦 64 pedidos em aberto com data expirada - revisar comercial",
    "📉 Churn de 20.82% em março - investigar causas",
    "🎯 Meta Q2: R$ 15M - 85% alcançado",
    "🌎 Lead Colômbia: 3 distribuidores mapeados para contato"
]

for alerta in alertas:
    st.warning(alerta)

# Footer
st.divider()
st.caption(f"📊 Dashboard atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M')} | Fonte: Qlik + SAP CX")

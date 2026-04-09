import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
from qlik_connector import load_qlik_data

# Configuração da página
st.set_page_config(
    page_title="Dellamed - Dashboard Executivo",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Auto-refresh a cada 5 minutos (300 segundos)
st_autorefresh = st.empty()
if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = datetime.now()

# Verifica se precisa atualizar
if (datetime.now() - st.session_state.last_refresh).seconds > 300:
    st.session_state.last_refresh = datetime.now()
    st.rerun()

# Mostra contador de atualização
with st_autorefresh.container():
    col_auto1, col_auto2 = st.columns([1, 4])
    with col_auto1:
        st.caption(f"🔄 Atualizado: {st.session_state.last_refresh.strftime('%H:%M')}")
    with col_auto2:
        if st.button("🔄 Atualizar Agora", type="secondary"):
            st.rerun()

# Carrega dados do Qlik (ou simulação)
kpis = load_qlik_data()

# Título
st.title("🏥 Dellamed - Dashboard Executivo")
st.markdown("*Painel de vendas, expansão LATAM e performance*")

# Sidebar
st.sidebar.header("📊 Filtros")
periodo = st.sidebar.selectbox(
    "Período",
    ["Últimos 30 dias", "Últimos 3 meses", "Últimos 6 meses", "Ano atual"],
    index=0
)

regiao = st.sidebar.multiselect(
    "Região",
    ["Brasil", "México", "Colômbia", "Argentina", "Chile"],
    default=["Brasil", "México", "Colômbia"]
)

# Abas principais
tab1, tab2, tab3, tab4 = st.tabs(["📈 Performance", "🌎 LATAM", "📅 Eventos", "🚨 Alertas"])

with tab1:
    st.subheader("📈 KPIs Principais")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Faturamento Total",
            value=f"R$ {kpis['faturamento_total']/1e6:.1f}M",
            delta="+10.5%"
        )
    
    with col2:
        st.metric(
            label="Pedidos no Mês",
            value=f"{kpis['pedidos_mes']:,}",
            delta="+8.2%"
        )
    
    with col3:
        st.metric(
            label="Ticket Médio",
            value=f"R$ {kpis['ticket_medio']:,}",
            delta="+2.1%"
        )
    
    with col4:
        st.metric(
            label="Churn",
            value=f"{kpis['churn']:.2f}%",
            delta="-1.5%",
            delta_color="inverse"
        )
    
    st.divider()
    
    # Gráficos
    st.subheader("📊 Análises")
    col_left, col_right = st.columns(2)
    
    # Dados simulados de vendas
    @st.cache_data(ttl=300)  # Cache por 5 minutos
    def load_sales_data():
        dates = pd.date_range(start='2024-01-01', end=datetime.now(), freq='D')
        data = {
            'Data': dates,
            'Faturamento': [1000000 + i * 1000 + (i % 30) * 50000 for i in range(len(dates))],
            'Pedidos': [50 + i % 20 for i in range(len(dates))],
            'Região': ['Brasil' if i % 5 != 0 else 'México' if i % 5 == 1 else 'Colômbia' for i in range(len(dates))]
        }
        return pd.DataFrame(data)
    
    df = load_sales_data()
    
    with col_left:
        st.markdown("#### Faturamento por Região")
        fig_regiao = px.pie(
            df.groupby('Região')['Faturamento'].sum().reset_index(),
            values='Faturamento',
            names='Região',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        fig_regiao.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_regiao, use_container_width=True)
    
    with col_right:
        st.markdown("#### Evolução de Vendas")
        df_daily = df.groupby('Data')['Faturamento'].sum().reset_index()
        fig_evolucao = go.Figure()
        fig_evolucao.add_trace(go.Scatter(
            x=df_daily['Data'],
            y=df_daily['Faturamento'],
            mode='lines',
            name='Faturamento',
            line=dict(color='#1f77b4', width=2),
            fill='tozeroy'
        ))
        fig_evolucao.update_layout(
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis_title=None,
            yaxis_title=None
        )
        st.plotly_chart(fig_evolucao, use_container_width=True)

with tab2:
    st.subheader("🌎 Expansão LATAM")
    
    col_lat1, col_lat2, col_lat3 = st.columns(3)
    
    with col_lat1:
        st.markdown("### 🇲🇽 México")
        st.metric("Potencial", "US$ 10.9B", "CAGR 7.9%")
        st.progress(35, text="35% - Em prospecção")
        st.caption("3 distribuidores mapeados")
        
    with col_lat2:
        st.markdown("### 🇨🇴 Colômbia")
        st.metric("Potencial", "US$ 3.15B", "CAGR 10.3%")
        st.progress(20, text="20% - Mapeamento")
        st.caption("MEDITECH 2026 confirmado")
        
    with col_lat3:
        st.markdown("### 🇦🇷 Argentina")
        st.metric("Potencial", "US$ 2.8B", "CAGR 6.5%")
        st.progress(10, text="10% - Análise inicial")
        st.caption("ExpoMEDICAL em avaliação")
    
    st.divider()
    
    # Mapa de calor de oportunidades
    st.markdown("#### Mapa de Oportunidades LATAM")
    latam_data = pd.DataFrame({
        'País': ['México', 'Colômbia', 'Argentina', 'Chile', 'Peru'],
        'Potencial (US$ B)': [10.9, 3.15, 2.8, 2.1, 1.5],
        'Progresso (%)': [35, 20, 10, 5, 0],
        'Prioridade': ['Alta', 'Alta', 'Média', 'Média', 'Baixa']
    })
    
    fig_latam = px.bar(
        latam_data,
        x='País',
        y='Potencial (US$ B)',
        color='Progresso (%)',
        text='Prioridade',
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig_latam, use_container_width=True)

with tab3:
    st.subheader("📅 Próximas Feiras e Eventos")
    
    eventos = [
        {
            "nome": "Hospitalar 2026 + CAD", 
            "local": "São Paulo, Brasil", 
            "data": "19-22 Maio", 
            "status": "✅ Confirmado",
            "stand": "A-123",
            "contato": "Maria - organizacao@hospitalar.com"
        },
        {
            "nome": "MEDITECH 2026", 
            "local": "Bogotá, Colômbia", 
            "data": "28-31 Julho", 
            "status": "📋 Planejando",
            "stand": "TBD",
            "contato": "Carlos - meditech@corferias.com"
        },
        {
            "nome": "ExpoMEDICAL 2026", 
            "local": "Buenos Aires, Argentina", 
            "data": "A confirmar", 
            "status": "🔍 Avaliando",
            "stand": "-",
            "contato": "-"
        }
    ]
    
    for evento in eventos:
        with st.expander(f"{evento['nome']} - {evento['data']}"):
            col_e1, col_e2 = st.columns(2)
            with col_e1:
                st.markdown(f"**Local:** {evento['local']}")
                st.markdown(f"**Status:** {evento['status']}")
            with col_e2:
                st.markdown(f"**Stand:** {evento['stand']}")
                st.markdown(f"**Contato:** {evento['contato']}")

with tab4:
    st.subheader("🚨 Alertas e Ações Prioritárias")
    
    alertas = [
        {
            "tipo": "⚠️",
            "titulo": "64 pedidos em aberto com data expirada",
            "acao": "Revisar comercial - possível divergência SAP",
            "prioridade": "Alta",
            "responsavel": "Thiago"
        },
        {
            "tipo": "📉",
            "titulo": "Churn de 20.82% em março",
            "acao": "Investigar causas - breakdown por produto/região",
            "prioridade": "Alta",
            "responsavel": "Thiago"
        },
        {
            "tipo": "🎯",
            "titulo": "Meta Q2: R$ 15M - 85% alcançado",
            "acao": "Acelerar fechamentos - faltam R$ 2.25M",
            "prioridade": "Média",
            "responsavel": "Comercial"
        },
        {
            "tipo": "🌎",
            "titulo": "Lead Colômbia: 3 distribuidores mapeados",
            "acao": "Agendar calls antes da MEDITECH",
            "prioridade": "Média",
            "responsavel": "Thiago"
        }
    ]
    
    for alerta in alertas:
        with st.container():
            cols = st.columns([0.5, 3, 1, 1])
            with cols[0]:
                st.markdown(f"### {alerta['tipo']}")
            with cols[1]:
                st.markdown(f"**{alerta['titulo']}**")
                st.caption(alerta['acao'])
            with cols[2]:
                st.badge(alerta['prioridade'])
            with cols[3]:
                st.caption(f"@{alerta['responsavel']}")
            st.divider()

# Footer
st.divider()
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    st.caption(f"📊 Atualizado: {kpis['data_atualizacao']}")
with col_f2:
    st.caption("🔄 Auto-refresh: 5 min")
with col_f3:
    st.caption("Fonte: Qlik + SAP CX")

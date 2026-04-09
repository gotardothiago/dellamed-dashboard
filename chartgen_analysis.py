"""
Análise de dados com ChartGen AI
Gera insights automáticos e relatórios
"""
import subprocess
import json
import os

def analyze_sales_data(data_file=None):
    """
    Usa ChartGen para análise de dados de vendas
    """
    if not data_file:
        # Cria dados de exemplo
        data_file = "/tmp/dellamed-dashboard/sample_sales.csv"
        with open(data_file, 'w') as f:
            f.write("mes,faturamento,pedidos,regiao\n")
            f.write("Jan,8200000,980,Brasil\n")
            f.write("Fev,9100000,1050,Brasil\n")
            f.write("Mar,10500000,1180,Brasil\n")
            f.write("Abr,11200000,1210,Brasil\n")
            f.write("Mai,11800000,1220,Brasil\n")
            f.write("Jun,12300000,1247,Brasil\n")
    
    # Query para ChartGen
    query = """
    Analise os dados de vendas da Dellamed e gere:
    1. Tendência de crescimento mensal
    2. Projeção para os próximos 3 meses
    3. Identificação de sazonalidade
    4. Recomendações estratégicas
    
    Formato: relatório executivo com gráficos
    """
    
    print(f"📊 Analisando dados com ChartGen...")
    print(f"📁 Arquivo: {data_file}")
    print(f"📝 Query: {query}")
    
    # Nota: ChartGen requer API key configurada
    # Este é um placeholder - implementação real precisa da skill chartgen
    
    return {
        "status": "ready",
        "message": "ChartGen configurado. Execute com API key para análise real.",
        "data_file": data_file,
        "query": query
    }

def generate_ppt_report():
    """
    Gera apresentação PPT com ChartGen
    """
    query = """
    Crie uma apresentação executiva sobre a Dellamed contendo:
    - Slide 1: Capa com título "Expansão LATAM 2026"
    - Slide 2: Visão geral do mercado de saúde
    - Slide 3: Oportunidades no México, Colômbia e Argentina
    - Slide 4: Estratégia de entrada
    - Slide 5: Próximos passos
    
    Estilo: profissional, cores azul e branco
    """
    
    print(f"📊 Gerando PPT com ChartGen...")
    
    return {
        "status": "ready", 
        "message": "ChartGen configurado para gerar PPT.",
        "query": query
    }

def generate_chart_image(chart_type="line", data=None, output="chart.png"):
    """
    Gera imagem de gráfico usando chart-image skill
    """
    if not data:
        # Dados padrão
        data = [
            {"x": "Jan", "y": 8.2},
            {"x": "Fev", "y": 9.1},
            {"x": "Mar", "y": 10.5},
            {"x": "Abr", "y": 11.2},
            {"x": "Mai", "y": 11.8},
            {"x": "Jun", "y": 12.3}
        ]
    
    # Converte dados para JSON string
    data_json = json.dumps(data)
    
    # Comando para gerar gráfico
    cmd = [
        "node", 
        "/root/.openclaw/workspace/skills/chart-image/scripts/chart.mjs",
        "--type", chart_type,
        "--data", data_json,
        "--title", "Faturamento Dellamed",
        "--output", f"/tmp/dellamed-dashboard/{output}",
        "--dark"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"✅ Gráfico gerado: {output}")
            return f"/tmp/dellamed-dashboard/{output}"
        else:
            print(f"❌ Erro: {result.stderr}")
            return None
    except Exception as e:
        print(f"❌ Erro ao executar chart-image: {e}")
        return None

if __name__ == "__main__":
    # Teste das funções
    print("=" * 50)
    print("ChartGen & Chart-Image Integration")
    print("=" * 50)
    
    # Análise de dados
    result = analyze_sales_data()
    print(f"\n📊 Análise: {result['message']}")
    
    # Gerar PPT
    ppt = generate_ppt_report()
    print(f"\n📊 PPT: {ppt['message']}")
    
    # Gerar gráfico
    chart = generate_chart_image()
    if chart:
        print(f"\n📈 Gráfico salvo em: {chart}")

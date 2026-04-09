"""
Conector Qlik Cloud para Dellamed Dashboard
Usa REST API com Bearer Token
"""
import requests
import json
import os
from datetime import datetime

class QlikConnector:
    def __init__(self, tenant_url, api_key):
        self.base_url = f"https://{tenant_url}/api/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def get_apps(self):
        """Lista todos os apps disponíveis"""
        try:
            response = requests.get(
                f"{self.base_url}/apps",
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Erro ao buscar apps: {e}")
            return []
    
    def get_kpis(self):
        """Retorna KPIs simulados (enquanto não temos acesso real)"""
        # TODO: Substituir por chamadas reais quando tivermos os IDs corretos
        return {
            "faturamento_total": 12300000,
            "pedidos_mes": 1247,
            "ticket_medio": 9850,
            "churn": 20.82,
            "data_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

# Função para carregar dados
def load_qlik_data():
    """Carrega dados do Qlik ou retorna simulação"""
    tenant = os.getenv("QLIK_TENANT", "dellasense.us.qlikcloud.com")
    api_key = os.getenv("QLIK_API_KEY", "")
    
    if api_key:
        qlik = QlikConnector(tenant, api_key)
        return qlik.get_kpis()
    else:
        # Dados simulados para desenvolvimento
        return {
            "faturamento_total": 12300000,
            "pedidos_mes": 1247,
            "ticket_medio": 9850,
            "churn": 20.82,
            "data_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

import pytest
from services.api_client import APIClient

@pytest.fixture
def api_client():
    """
    Fixture para inicializar el cliente API.
    """
    return APIClient()

def test_mercadolibre_departments(api_client):
    """
    Caso de prueba: Validar que el endpoint de Mercado Libre contiene departamentos.
    """
    url = "https://www.mercadolibre.com.ar/menu/departments"
    response = api_client.get(url)

    # Verificar que la respuesta es exitosa
    assert response.status_code == 200, f"Esperado código 200, pero obtuvo {response.status_code}"

    # Verificar que el contenido incluye la palabra "departments"
    response_json = response.json()
    assert "departments" in response_json, "La clave 'departments' no se encuentra en la respuesta"

    # Validar que existan departamentos
    assert len(response_json["departments"]) > 0, "No se encontraron departamentos en la respuesta"


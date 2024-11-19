import requests

class APIClient:
    """
    Cliente para manejar solicitudes a APIs REST.
    """

    @staticmethod
    def get(endpoint, params=None, headers=None):
        """
        Realiza una solicitud GET a un endpoint específico.
        """
        try:
            response = requests.get(endpoint, params=params, headers=headers)
            response.raise_for_status()  # Lanza una excepción si el código HTTP es 4xx o 5xx
            return response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error en la solicitud GET: {e}")

    @staticmethod
    def post(endpoint, data=None, json=None, headers=None):
        """
        Realiza una solicitud POST a un endpoint específico.
        """
        try:
            response = requests.post(endpoint, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error en la solicitud POST: {e}")

    @staticmethod
    def patch(endpoint, data=None, json=None, headers=None):
        """
        Realiza una solicitud PATCH a un endpoint específico.
        """
        try:
            response = requests.patch(endpoint, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error en la solicitud PATCH: {e}")

    @staticmethod
    def delete(endpoint, headers=None):
        """
        Realiza una solicitud DELETE a un endpoint específico.
        """
        try:
            response = requests.delete(endpoint, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error en la solicitud DELETE: {e}")
import os
import uuid
from typing import Dict, Any
from requests import Session, Response

class ResponseError(Exception):
    """Exception for HTTP response errors."""
    def __init__(self, response: Response):
        self.response = response
        try:
            content = response.json() if response.content else None
            super().__init__(content)
        except Exception:
            super().__init__(response.text)

class ApiClient(Session):
    def __init__(self, base_url_env: str):
        super().__init__()
        self.base_url = os.getenv(base_url_env)
        if not self.base_url:
            raise ValueError(f"Environment variable '{base_url_env}' not set.")
        self.headers = {}

    def _build_url(self, url_path: str) -> str:
        return self.base_url + url_path

    def _set_headers(self, accept: str = '*/*') -> Dict[str, str]:
        headers = self.headers.copy()
        headers['Accept'] = accept
        headers['x-correlation-id'] = str(uuid.uuid4())
        return headers

    def _verify_response(self, response: Response) -> Any:
        if not response.ok:
            raise ResponseError(response)
        try:
            return response.json()
        except Exception:
            return response.text

    def get(self, url: str, **kwargs) -> Any:
        full_url = self._build_url(url)
        headers = self._set_headers()
        response = super().get(full_url, headers=headers, **kwargs)
        return self._verify_response(response)

    def post(self, url: str, **kwargs) -> Any:
        full_url = self._build_url(url)
        headers = self._set_headers()
        response = super().post(full_url, headers=headers, **kwargs)
        return self._verify_response(response)

    def put(self, url: str, **kwargs) -> Any:
        full_url = self._build_url(url)
        headers = self._set_headers()
        response = super().put(full_url, headers=headers, **kwargs)
        return self._verify_response(response)

    def patch(self, url: str, **kwargs) -> Any:
        full_url = self._build_url(url)
        headers = self._set_headers()
        response = super().patch(full_url, headers=headers, **kwargs)
        return self._verify_response(response)

    def delete(self, url: str, **kwargs) -> Any:
        full_url = self._build_url(url)
        headers = self._set_headers()
        response = super().delete(full_url, headers=headers, **kwargs)
        return self._verify_response(response)
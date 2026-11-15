from typing import Optional, Set

RETRYABLE_STATUS_CODES: Set[int] = {408, 429, 500, 502, 503, 504}
PERMANENT_STATUS_CODES: Set[int] = {400, 401, 403, 404}


class LLMGatewayException(Exception):
    """Base exception for all LLM Gateway errors."""
    is_retryable: bool = False


class LLMProviderNotFoundError(LLMGatewayException):
    """Raised when a requested LLM provider is not registered in the provider factory."""
    is_retryable: bool = False

    def __init__(self, provider_name: str):
        super().__init__(f"LLM Provider '{provider_name}' is not registered or supported.")
        self.provider_name = provider_name


class LLMProviderAPIError(LLMGatewayException):
    """Raised when an LLM provider returns an API error."""
    def __init__(self, provider_name: str, message: str, status_code: int = 500):
        super().__init__(f"Provider '{provider_name}' API Error ({status_code}): {message}")
        self.provider_name = provider_name
        self.message = message
        self.status_code = status_code
        
        # Smart classification: If status code is in permanent set (400, 401, 403, 404), it is non-retryable
        if status_code in PERMANENT_STATUS_CODES:
            self.is_retryable = False
        elif status_code in RETRYABLE_STATUS_CODES:
            self.is_retryable = True
        else:
            # Default: 5xx errors retryable, 4xx non-retryable
            self.is_retryable = status_code >= 500


class LLMTimeoutError(LLMGatewayException):
    """Raised when an LLM request times out."""
    is_retryable: bool = True

    def __init__(self, provider_name: str, timeout_seconds: float):
        super().__init__(f"Provider '{provider_name}' timed out after {timeout_seconds} seconds.")
        self.provider_name = provider_name
        self.timeout_seconds = timeout_seconds


class LLMAllProvidersFailedError(LLMGatewayException):
    """Raised when both main and fallback LLM providers exhaust all retry attempts."""
    is_retryable: bool = False

    def __init__(self, message: str = "All configured LLM providers (Main & Fallback) failed."):
        super().__init__(message)


def classify_error_retryability(exc: Exception) -> bool:
    """
    Helper to determine if an error is transient (retryable) or permanent (non-retryable).
    - Retryable: 429 Rate Limit, 408 Timeout, 500, 502, 503, 504, Connection/Network errors, Timeouts.
    - Permanent: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Model Not Found.
    """
    if isinstance(exc, LLMGatewayException):
        return exc.is_retryable

    # Handle HTTP or standard library exceptions
    status_code = getattr(exc, "status_code", getattr(exc, "code", None))
    if status_code is not None and isinstance(status_code, int):
        if status_code in PERMANENT_STATUS_CODES:
            return False
        if status_code in RETRYABLE_STATUS_CODES:
            return True
        return status_code >= 500

    # Network, Connection, Timeout errors are retryable
    exc_name = type(exc).__name__.lower()
    if any(keyword in exc_name for keyword in ["timeout", "connection", "network", "socket", "reset"]):
        return True

    return False

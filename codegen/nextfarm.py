"""Convenience entry point for the NextFarm API.

    from nextfarm_sdk import create_client, SANDBOX_URL
    from nextfarm_sdk.api.iot import get_api_v1_iot_devices

    nf = create_client(api_key=os.environ["NEXTFARM_API_KEY"], base_url=SANDBOX_URL)
    page = get_api_v1_iot_devices.sync(client=nf, page=1)
"""

from __future__ import annotations

from typing import Literal

from .client import AuthenticatedClient
from ._version import VERSION

PROD_URL = "https://api-prod.nextfarm.vn"
SANDBOX_URL = "https://api-dev.nextfarm.vn"


def create_client(
    api_key: str,
    base_url: str = PROD_URL,
    language: Literal["vi", "en"] = "vi",
    timeout: float = 30.0,
    raise_on_unexpected_status: bool = True,
) -> AuthenticatedClient:
    """Create a client authenticated with an API key (`nfk_...`) or an OAuth access token."""
    if not api_key:
        raise ValueError("NextFarm SDK: api_key is required")
    import httpx

    return AuthenticatedClient(
        base_url=base_url.rstrip("/"),
        token=api_key,
        headers={"Accept-Language": language, "User-Agent": f"nextfarm-sdk-python/{VERSION}"},
        timeout=httpx.Timeout(timeout),
        raise_on_unexpected_status=raise_on_unexpected_status,
    )

"""Offline tests: package import, headers and URL building."""
import httpx
import pytest

import nextfarm_sdk
from nextfarm_sdk import SANDBOX_URL, VERSION, create_client
from nextfarm_sdk.api.iot import get_api_v1_iot_devices


def test_exports():
    assert nextfarm_sdk.PROD_URL == "https://api-prod.nextfarm.vn"
    assert VERSION and VERSION != "0.0.0"


def test_requires_api_key():
    with pytest.raises(ValueError):
        create_client(api_key="")


def test_headers_and_url():
    seen = {}

    def handler(req: httpx.Request) -> httpx.Response:
        seen["req"] = req
        return httpx.Response(200, json={"items": [], "total": 0, "page": 2, "pageSize": 50})

    nf = create_client(api_key="nfk_test", base_url=SANDBOX_URL + "/", language="en")
    nf.set_httpx_client(httpx.Client(base_url=SANDBOX_URL, transport=httpx.MockTransport(handler), headers=nf._headers | {"Authorization": "Bearer nfk_test"}))
    r = get_api_v1_iot_devices.sync_detailed(client=nf, page=2)
    assert r.status_code == 200
    req = seen["req"]
    assert str(req.url).startswith(f"{SANDBOX_URL}/api/v1/iot/devices?")
    assert "page=2" in str(req.url)
    assert req.headers["authorization"] == "Bearer nfk_test"
    assert req.headers["accept-language"] == "en"
    assert req.headers["user-agent"].startswith("nextfarm-sdk-python/")

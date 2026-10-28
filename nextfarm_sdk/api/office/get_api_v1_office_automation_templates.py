from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_template_dto import OfficeAutomationTemplateDto
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automation-templates",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeAutomationTemplateDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeAutomationTemplateDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeAutomationTemplateDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeAutomationTemplateDto]]:
    """ Danh sách mẫu của công ty, mới nhất trước

     `steps` là tóm tắt theo thứ tự (kiểu bước + hành động) để kho mẫu hiện dòng "Gửi tin → Chờ → Rẽ
    nhánh".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationTemplateDto]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeAutomationTemplateDto] | None:
    """ Danh sách mẫu của công ty, mới nhất trước

     `steps` là tóm tắt theo thứ tự (kiểu bước + hành động) để kho mẫu hiện dòng "Gửi tin → Chờ → Rẽ
    nhánh".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationTemplateDto]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeAutomationTemplateDto]]:
    """ Danh sách mẫu của công ty, mới nhất trước

     `steps` là tóm tắt theo thứ tự (kiểu bước + hành động) để kho mẫu hiện dòng "Gửi tin → Chờ → Rẽ
    nhánh".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationTemplateDto]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeAutomationTemplateDto] | None:
    """ Danh sách mẫu của công ty, mới nhất trước

     `steps` là tóm tắt theo thứ tự (kiểu bước + hành động) để kho mẫu hiện dòng "Gửi tin → Chờ → Rẽ
    nhánh".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationTemplateDto]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed

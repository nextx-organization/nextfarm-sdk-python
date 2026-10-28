from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_diagnosis_dto import OfficeAutomationDiagnosisDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automations/{id}/diagnosis".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeAutomationDiagnosisDto | None:
    if response.status_code == 200:
        response_200 = OfficeAutomationDiagnosisDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeAutomationDiagnosisDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeAutomationDiagnosisDto]:
    """ Chẩn đoán: vì sao luật chạy / không chạy

     Các phép kiểm theo thứ tự (`status` · `trigger` · `steps` · `quota` · `recent_failures`), `canRun` =
    không phép kiểm chặn nào hỏng, 5 lần BỎ QUA gần nhất kèm lý do đã dịch, và lần hỏng gần nhất. Chỉ
    đọc.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationDiagnosisDto]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeAutomationDiagnosisDto | None:
    """ Chẩn đoán: vì sao luật chạy / không chạy

     Các phép kiểm theo thứ tự (`status` · `trigger` · `steps` · `quota` · `recent_failures`), `canRun` =
    không phép kiểm chặn nào hỏng, 5 lần BỎ QUA gần nhất kèm lý do đã dịch, và lần hỏng gần nhất. Chỉ
    đọc.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationDiagnosisDto
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeAutomationDiagnosisDto]:
    """ Chẩn đoán: vì sao luật chạy / không chạy

     Các phép kiểm theo thứ tự (`status` · `trigger` · `steps` · `quota` · `recent_failures`), `canRun` =
    không phép kiểm chặn nào hỏng, 5 lần BỎ QUA gần nhất kèm lý do đã dịch, và lần hỏng gần nhất. Chỉ
    đọc.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationDiagnosisDto]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeAutomationDiagnosisDto | None:
    """ Chẩn đoán: vì sao luật chạy / không chạy

     Các phép kiểm theo thứ tự (`status` · `trigger` · `steps` · `quota` · `recent_failures`), `canRun` =
    không phép kiểm chặn nào hỏng, 5 lần BỎ QUA gần nhất kèm lý do đã dịch, và lần hỏng gần nhất. Chỉ
    đọc.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationDiagnosisDto
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed

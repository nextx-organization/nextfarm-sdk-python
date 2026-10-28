from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_problem_details import OfficeProblemDetails
from ...models.office_record_history_entry_dto import OfficeRecordHistoryEntryDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,
    record_id: UUID,
    *,
    limit: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tables/{table_id}/records/{record_id}/history".format(table_id=quote(str(table_id), safe=""),record_id=quote(str(record_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeProblemDetails | list[OfficeRecordHistoryEntryDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeRecordHistoryEntryDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = OfficeProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeProblemDetails | list[OfficeRecordHistoryEntryDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,

) -> Response[OfficeProblemDetails | list[OfficeRecordHistoryEntryDto]]:
    """ Lịch sử sửa của record, tách theo từng ô (đã lọc theo quyền cột)

    Args:
        table_id (UUID):
        record_id (UUID):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | list[OfficeRecordHistoryEntryDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
record_id=record_id,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,

) -> OfficeProblemDetails | list[OfficeRecordHistoryEntryDto] | None:
    """ Lịch sử sửa của record, tách theo từng ô (đã lọc theo quyền cột)

    Args:
        table_id (UUID):
        record_id (UUID):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | list[OfficeRecordHistoryEntryDto]
     """


    return sync_detailed(
        table_id=table_id,
record_id=record_id,
client=client,
limit=limit,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,

) -> Response[OfficeProblemDetails | list[OfficeRecordHistoryEntryDto]]:
    """ Lịch sử sửa của record, tách theo từng ô (đã lọc theo quyền cột)

    Args:
        table_id (UUID):
        record_id (UUID):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | list[OfficeRecordHistoryEntryDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
record_id=record_id,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,

) -> OfficeProblemDetails | list[OfficeRecordHistoryEntryDto] | None:
    """ Lịch sử sửa của record, tách theo từng ô (đã lọc theo quyền cột)

    Args:
        table_id (UUID):
        record_id (UUID):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | list[OfficeRecordHistoryEntryDto]
     """


    return (await asyncio_detailed(
        table_id=table_id,
record_id=record_id,
client=client,
limit=limit,

    )).parsed

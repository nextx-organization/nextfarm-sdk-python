from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_batch_update_records_request import OfficeBatchUpdateRecordsRequest
from ...models.office_problem_details import OfficeProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,
    *,
    body: OfficeBatchUpdateRecordsRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/office/tables/{table_id}/records/batch".format(table_id=quote(str(table_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | OfficeProblemDetails | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = OfficeProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | OfficeProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: OfficeBatchUpdateRecordsRequest | Unset = UNSET,

) -> Response[Any | OfficeProblemDetails]:
    """ Cập nhật nhiều record (tối đa 1000, all-or-nothing)

    Args:
        table_id (UUID):
        body (OfficeBatchUpdateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: OfficeBatchUpdateRecordsRequest | Unset = UNSET,

) -> Any | OfficeProblemDetails | None:
    """ Cập nhật nhiều record (tối đa 1000, all-or-nothing)

    Args:
        table_id (UUID):
        body (OfficeBatchUpdateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OfficeProblemDetails
     """


    return sync_detailed(
        table_id=table_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: OfficeBatchUpdateRecordsRequest | Unset = UNSET,

) -> Response[Any | OfficeProblemDetails]:
    """ Cập nhật nhiều record (tối đa 1000, all-or-nothing)

    Args:
        table_id (UUID):
        body (OfficeBatchUpdateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: OfficeBatchUpdateRecordsRequest | Unset = UNSET,

) -> Any | OfficeProblemDetails | None:
    """ Cập nhật nhiều record (tối đa 1000, all-or-nothing)

    Args:
        table_id (UUID):
        body (OfficeBatchUpdateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OfficeProblemDetails
     """


    return (await asyncio_detailed(
        table_id=table_id,
client=client,
body=body,

    )).parsed

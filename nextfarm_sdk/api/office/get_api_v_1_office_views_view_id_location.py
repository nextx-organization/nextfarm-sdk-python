from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_problem_details import OfficeProblemDetails
from ...models.office_view_location_dto import OfficeViewLocationDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    view_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/views/{view_id}/location".format(view_id=quote(str(view_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeProblemDetails | OfficeViewLocationDto | None:
    if response.status_code == 200:
        response_200 = OfficeViewLocationDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = OfficeProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeProblemDetails | OfficeViewLocationDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeProblemDetails | OfficeViewLocationDto]:
    """ Lần ngược từ mã khung nhìn lên bảng và ứng dụng chứa nó

    Args:
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | OfficeViewLocationDto]
     """


    kwargs = _get_kwargs(
        view_id=view_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeProblemDetails | OfficeViewLocationDto | None:
    """ Lần ngược từ mã khung nhìn lên bảng và ứng dụng chứa nó

    Args:
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | OfficeViewLocationDto
     """


    return sync_detailed(
        view_id=view_id,
client=client,

    ).parsed

async def asyncio_detailed(
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeProblemDetails | OfficeViewLocationDto]:
    """ Lần ngược từ mã khung nhìn lên bảng và ứng dụng chứa nó

    Args:
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | OfficeViewLocationDto]
     """


    kwargs = _get_kwargs(
        view_id=view_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeProblemDetails | OfficeViewLocationDto | None:
    """ Lần ngược từ mã khung nhìn lên bảng và ứng dụng chứa nó

    Args:
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | OfficeViewLocationDto
     """


    return (await asyncio_detailed(
        view_id=view_id,
client=client,

    )).parsed

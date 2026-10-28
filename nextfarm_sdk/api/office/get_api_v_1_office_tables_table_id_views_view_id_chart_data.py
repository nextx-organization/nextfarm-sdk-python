from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_chart_data_dto import OfficeChartDataDto
from ...models.office_problem_details import OfficeProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,
    view_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tables/{table_id}/views/{view_id}/chart-data".format(table_id=quote(str(table_id), safe=""),view_id=quote(str(view_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeChartDataDto | OfficeProblemDetails | None:
    if response.status_code == 200:
        response_200 = OfficeChartDataDto.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = OfficeProblemDetails.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = OfficeProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeChartDataDto | OfficeProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeChartDataDto | OfficeProblemDetails]:
    """ Dữ liệu đã gộp của view kiểu Chart

     Gộp theo cấu hình trong property (groupField + aggregation count/sum/avg). FE tự vẽ.

    Args:
        table_id (UUID):
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeChartDataDto | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
view_id=view_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeChartDataDto | OfficeProblemDetails | None:
    """ Dữ liệu đã gộp của view kiểu Chart

     Gộp theo cấu hình trong property (groupField + aggregation count/sum/avg). FE tự vẽ.

    Args:
        table_id (UUID):
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeChartDataDto | OfficeProblemDetails
     """


    return sync_detailed(
        table_id=table_id,
view_id=view_id,
client=client,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeChartDataDto | OfficeProblemDetails]:
    """ Dữ liệu đã gộp của view kiểu Chart

     Gộp theo cấu hình trong property (groupField + aggregation count/sum/avg). FE tự vẽ.

    Args:
        table_id (UUID):
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeChartDataDto | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
view_id=view_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeChartDataDto | OfficeProblemDetails | None:
    """ Dữ liệu đã gộp của view kiểu Chart

     Gộp theo cấu hình trong property (groupField + aggregation count/sum/avg). FE tự vẽ.

    Args:
        table_id (UUID):
        view_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeChartDataDto | OfficeProblemDetails
     """


    return (await asyncio_detailed(
        table_id=table_id,
view_id=view_id,
client=client,

    )).parsed

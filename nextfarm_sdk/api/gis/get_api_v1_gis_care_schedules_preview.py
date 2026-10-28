from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_care_preview_dto import GisCarePreviewDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    template_id: UUID | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    plot_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,
    from_: str | Unset = UNSET,
    days: int | Unset = 30,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_template_id: str | Unset = UNSET
    if not isinstance(template_id, Unset):
        json_template_id = str(template_id)
    params["templateId"] = json_template_id

    json_parcel_id: str | Unset = UNSET
    if not isinstance(parcel_id, Unset):
        json_parcel_id = str(parcel_id)
    params["parcelId"] = json_parcel_id

    json_plot_id: str | Unset = UNSET
    if not isinstance(plot_id, Unset):
        json_plot_id = str(plot_id)
    params["plotId"] = json_plot_id

    json_season_id: str | Unset = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    params["from"] = from_

    params["days"] = days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/care-schedules/preview",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisCarePreviewDto | None:
    if response.status_code == 200:
        response_200 = GisCarePreviewDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisCarePreviewDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    template_id: UUID | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    plot_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,
    from_: str | Unset = UNSET,
    days: int | Unset = 30,

) -> Response[GisCarePreviewDto]:
    """ Xem trước lịch (không ghi gì)

     `from` yyyy-MM-dd (mặc định hôm nay giờ VN), `days` 1–400 (mặc định 30).

    Args:
        template_id (UUID | Unset):
        parcel_id (UUID | Unset):
        plot_id (UUID | Unset):
        season_id (UUID | Unset):
        from_ (str | Unset):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisCarePreviewDto]
     """


    kwargs = _get_kwargs(
        template_id=template_id,
parcel_id=parcel_id,
plot_id=plot_id,
season_id=season_id,
from_=from_,
days=days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    template_id: UUID | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    plot_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,
    from_: str | Unset = UNSET,
    days: int | Unset = 30,

) -> GisCarePreviewDto | None:
    """ Xem trước lịch (không ghi gì)

     `from` yyyy-MM-dd (mặc định hôm nay giờ VN), `days` 1–400 (mặc định 30).

    Args:
        template_id (UUID | Unset):
        parcel_id (UUID | Unset):
        plot_id (UUID | Unset):
        season_id (UUID | Unset):
        from_ (str | Unset):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisCarePreviewDto
     """


    return sync_detailed(
        client=client,
template_id=template_id,
parcel_id=parcel_id,
plot_id=plot_id,
season_id=season_id,
from_=from_,
days=days,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    template_id: UUID | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    plot_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,
    from_: str | Unset = UNSET,
    days: int | Unset = 30,

) -> Response[GisCarePreviewDto]:
    """ Xem trước lịch (không ghi gì)

     `from` yyyy-MM-dd (mặc định hôm nay giờ VN), `days` 1–400 (mặc định 30).

    Args:
        template_id (UUID | Unset):
        parcel_id (UUID | Unset):
        plot_id (UUID | Unset):
        season_id (UUID | Unset):
        from_ (str | Unset):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisCarePreviewDto]
     """


    kwargs = _get_kwargs(
        template_id=template_id,
parcel_id=parcel_id,
plot_id=plot_id,
season_id=season_id,
from_=from_,
days=days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    template_id: UUID | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    plot_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,
    from_: str | Unset = UNSET,
    days: int | Unset = 30,

) -> GisCarePreviewDto | None:
    """ Xem trước lịch (không ghi gì)

     `from` yyyy-MM-dd (mặc định hôm nay giờ VN), `days` 1–400 (mặc định 30).

    Args:
        template_id (UUID | Unset):
        parcel_id (UUID | Unset):
        plot_id (UUID | Unset):
        season_id (UUID | Unset):
        from_ (str | Unset):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisCarePreviewDto
     """


    return (await asyncio_detailed(
        client=client,
template_id=template_id,
parcel_id=parcel_id,
plot_id=plot_id,
season_id=season_id,
from_=from_,
days=days,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_problem_details import OfficeProblemDetails
from ...models.office_task_workload_dto import OfficeTaskWorkloadDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    task_list_id: UUID | Unset = UNSET,
    list_group_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_task_list_id: str | Unset = UNSET
    if not isinstance(task_list_id, Unset):
        json_task_list_id = str(task_list_id)
    params["taskListId"] = json_task_list_id

    json_list_group_id: str | Unset = UNSET
    if not isinstance(list_group_id, Unset):
        json_list_group_id = str(list_group_id)
    params["listGroupId"] = json_list_group_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tasks/workload",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeProblemDetails | list[OfficeTaskWorkloadDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeTaskWorkloadDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = OfficeProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeProblemDetails | list[OfficeTaskWorkloadDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    task_list_id: UUID | Unset = UNSET,
    list_group_id: UUID | Unset = UNSET,

) -> Response[OfficeProblemDetails | list[OfficeTaskWorkloadDto]]:
    """ Khối lượng theo người

     isOverloaded so với ngưỡng quá tải, mặc định 10 việc đang mở; mỗi dòng trả kèm overloadThreshold =
    ngưỡng đang áp. Khối lượng CHỈ để tham khảo, không dùng tính tiến độ. taskListId thu hẹp vào một
    danh sách; listGroupId thu hẹp vào một thư mục (đội) GỒM mọi thư mục con. Có cả hai thì là GIAO.
    Danh sách/thư mục không tồn tại ⇒ 404.

    Args:
        task_list_id (UUID | Unset):
        list_group_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | list[OfficeTaskWorkloadDto]]
     """


    kwargs = _get_kwargs(
        task_list_id=task_list_id,
list_group_id=list_group_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    task_list_id: UUID | Unset = UNSET,
    list_group_id: UUID | Unset = UNSET,

) -> OfficeProblemDetails | list[OfficeTaskWorkloadDto] | None:
    """ Khối lượng theo người

     isOverloaded so với ngưỡng quá tải, mặc định 10 việc đang mở; mỗi dòng trả kèm overloadThreshold =
    ngưỡng đang áp. Khối lượng CHỈ để tham khảo, không dùng tính tiến độ. taskListId thu hẹp vào một
    danh sách; listGroupId thu hẹp vào một thư mục (đội) GỒM mọi thư mục con. Có cả hai thì là GIAO.
    Danh sách/thư mục không tồn tại ⇒ 404.

    Args:
        task_list_id (UUID | Unset):
        list_group_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | list[OfficeTaskWorkloadDto]
     """


    return sync_detailed(
        client=client,
task_list_id=task_list_id,
list_group_id=list_group_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    task_list_id: UUID | Unset = UNSET,
    list_group_id: UUID | Unset = UNSET,

) -> Response[OfficeProblemDetails | list[OfficeTaskWorkloadDto]]:
    """ Khối lượng theo người

     isOverloaded so với ngưỡng quá tải, mặc định 10 việc đang mở; mỗi dòng trả kèm overloadThreshold =
    ngưỡng đang áp. Khối lượng CHỈ để tham khảo, không dùng tính tiến độ. taskListId thu hẹp vào một
    danh sách; listGroupId thu hẹp vào một thư mục (đội) GỒM mọi thư mục con. Có cả hai thì là GIAO.
    Danh sách/thư mục không tồn tại ⇒ 404.

    Args:
        task_list_id (UUID | Unset):
        list_group_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | list[OfficeTaskWorkloadDto]]
     """


    kwargs = _get_kwargs(
        task_list_id=task_list_id,
list_group_id=list_group_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    task_list_id: UUID | Unset = UNSET,
    list_group_id: UUID | Unset = UNSET,

) -> OfficeProblemDetails | list[OfficeTaskWorkloadDto] | None:
    """ Khối lượng theo người

     isOverloaded so với ngưỡng quá tải, mặc định 10 việc đang mở; mỗi dòng trả kèm overloadThreshold =
    ngưỡng đang áp. Khối lượng CHỈ để tham khảo, không dùng tính tiến độ. taskListId thu hẹp vào một
    danh sách; listGroupId thu hẹp vào một thư mục (đội) GỒM mọi thư mục con. Có cả hai thì là GIAO.
    Danh sách/thư mục không tồn tại ⇒ 404.

    Args:
        task_list_id (UUID | Unset):
        list_group_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | list[OfficeTaskWorkloadDto]
     """


    return (await asyncio_detailed(
        client=client,
task_list_id=task_list_id,
list_group_id=list_group_id,

    )).parsed

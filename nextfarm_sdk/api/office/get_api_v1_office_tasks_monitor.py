from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_problem_details import OfficeProblemDetails
from ...models.office_task_monitor_dto import OfficeTaskMonitorDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    scope: str | Unset = UNSET,
    task_list_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["scope"] = scope

    json_task_list_id: str | Unset = UNSET
    if not isinstance(task_list_id, Unset):
        json_task_list_id = str(task_list_id)
    params["taskListId"] = json_task_list_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tasks/monitor",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeProblemDetails | OfficeTaskMonitorDto | None:
    if response.status_code == 200:
        response_200 = OfficeTaskMonitorDto.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = OfficeProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeProblemDetails | OfficeTaskMonitorDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
    task_list_id: UUID | Unset = UNSET,

) -> Response[OfficeProblemDetails | OfficeTaskMonitorDto]:
    """ Màn Theo dõi: sáu ô số liệu + bảng toàn đội + việc của từng người

     Một lần gọi trả cả ba phần vì chúng đọc CÙNG một tập việc — tách ra thì ô số liệu và bảng bên dưới
    rơi vào hai thời điểm khác nhau và lệch số. elapsedMinutes là thời gian TRÔI QUA kể từ lúc bắt tay
    vào việc (started_at), KHÔNG phải giờ công. loadState: overloaded · normal · free. isExact=false
    nghĩa là công ty vượt trần số dòng nên mọi con số là ước lượng. taskListId thu hẹp MỌI con số vào
    một dự án — nó chỉ thu hẹp, không bao giờ cho thấy thêm việc mà scope vốn không cho thấy. Khi có
    taskListId, mỗi dòng thành viên mang thêm openCountAll = số việc mở của người đó trên toàn phạm vi.
    items của mỗi thành viên tối đa 200 (quá hạn trước); openTotal = tổng THẬT việc mở của người đó
    trong cùng phạm vi — so với số items để báo “đang hiện n/N”. dueSoonDays = cửa sổ “sắp đến hạn” đang
    áp (cạnh staleAfterDays).

    Args:
        scope (str | Unset):
        task_list_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | OfficeTaskMonitorDto]
     """


    kwargs = _get_kwargs(
        scope=scope,
task_list_id=task_list_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
    task_list_id: UUID | Unset = UNSET,

) -> OfficeProblemDetails | OfficeTaskMonitorDto | None:
    """ Màn Theo dõi: sáu ô số liệu + bảng toàn đội + việc của từng người

     Một lần gọi trả cả ba phần vì chúng đọc CÙNG một tập việc — tách ra thì ô số liệu và bảng bên dưới
    rơi vào hai thời điểm khác nhau và lệch số. elapsedMinutes là thời gian TRÔI QUA kể từ lúc bắt tay
    vào việc (started_at), KHÔNG phải giờ công. loadState: overloaded · normal · free. isExact=false
    nghĩa là công ty vượt trần số dòng nên mọi con số là ước lượng. taskListId thu hẹp MỌI con số vào
    một dự án — nó chỉ thu hẹp, không bao giờ cho thấy thêm việc mà scope vốn không cho thấy. Khi có
    taskListId, mỗi dòng thành viên mang thêm openCountAll = số việc mở của người đó trên toàn phạm vi.
    items của mỗi thành viên tối đa 200 (quá hạn trước); openTotal = tổng THẬT việc mở của người đó
    trong cùng phạm vi — so với số items để báo “đang hiện n/N”. dueSoonDays = cửa sổ “sắp đến hạn” đang
    áp (cạnh staleAfterDays).

    Args:
        scope (str | Unset):
        task_list_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | OfficeTaskMonitorDto
     """


    return sync_detailed(
        client=client,
scope=scope,
task_list_id=task_list_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
    task_list_id: UUID | Unset = UNSET,

) -> Response[OfficeProblemDetails | OfficeTaskMonitorDto]:
    """ Màn Theo dõi: sáu ô số liệu + bảng toàn đội + việc của từng người

     Một lần gọi trả cả ba phần vì chúng đọc CÙNG một tập việc — tách ra thì ô số liệu và bảng bên dưới
    rơi vào hai thời điểm khác nhau và lệch số. elapsedMinutes là thời gian TRÔI QUA kể từ lúc bắt tay
    vào việc (started_at), KHÔNG phải giờ công. loadState: overloaded · normal · free. isExact=false
    nghĩa là công ty vượt trần số dòng nên mọi con số là ước lượng. taskListId thu hẹp MỌI con số vào
    một dự án — nó chỉ thu hẹp, không bao giờ cho thấy thêm việc mà scope vốn không cho thấy. Khi có
    taskListId, mỗi dòng thành viên mang thêm openCountAll = số việc mở của người đó trên toàn phạm vi.
    items của mỗi thành viên tối đa 200 (quá hạn trước); openTotal = tổng THẬT việc mở của người đó
    trong cùng phạm vi — so với số items để báo “đang hiện n/N”. dueSoonDays = cửa sổ “sắp đến hạn” đang
    áp (cạnh staleAfterDays).

    Args:
        scope (str | Unset):
        task_list_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | OfficeTaskMonitorDto]
     """


    kwargs = _get_kwargs(
        scope=scope,
task_list_id=task_list_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
    task_list_id: UUID | Unset = UNSET,

) -> OfficeProblemDetails | OfficeTaskMonitorDto | None:
    """ Màn Theo dõi: sáu ô số liệu + bảng toàn đội + việc của từng người

     Một lần gọi trả cả ba phần vì chúng đọc CÙNG một tập việc — tách ra thì ô số liệu và bảng bên dưới
    rơi vào hai thời điểm khác nhau và lệch số. elapsedMinutes là thời gian TRÔI QUA kể từ lúc bắt tay
    vào việc (started_at), KHÔNG phải giờ công. loadState: overloaded · normal · free. isExact=false
    nghĩa là công ty vượt trần số dòng nên mọi con số là ước lượng. taskListId thu hẹp MỌI con số vào
    một dự án — nó chỉ thu hẹp, không bao giờ cho thấy thêm việc mà scope vốn không cho thấy. Khi có
    taskListId, mỗi dòng thành viên mang thêm openCountAll = số việc mở của người đó trên toàn phạm vi.
    items của mỗi thành viên tối đa 200 (quá hạn trước); openTotal = tổng THẬT việc mở của người đó
    trong cùng phạm vi — so với số items để báo “đang hiện n/N”. dueSoonDays = cửa sổ “sắp đến hạn” đang
    áp (cạnh staleAfterDays).

    Args:
        scope (str | Unset):
        task_list_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | OfficeTaskMonitorDto
     """


    return (await asyncio_detailed(
        client=client,
scope=scope,
task_list_id=task_list_id,

    )).parsed

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_task_monitor_current_dto import OfficeTaskMonitorCurrentDto
  from ..models.office_task_monitor_item_dto import OfficeTaskMonitorItemDto





T = TypeVar("T", bound="OfficeTaskMonitorMemberDto")



@_attrs_define
class OfficeTaskMonitorMemberDto:
    

    current: OfficeTaskMonitorCurrentDto | Unset = UNSET
    due_soon_count: int | Unset = UNSET
    has_on_time_data: bool | Unset = UNSET
    in_progress_count: int | Unset = UNSET
    items: list[OfficeTaskMonitorItemDto] | None | Unset = UNSET
    last_activity_at: datetime.datetime | None | Unset = UNSET
    load_state: None | str | Unset = UNSET
    on_time_rate: int | Unset = UNSET
    open_count: int | Unset = UNSET
    open_count_all: int | Unset = UNSET
    open_total: int | Unset = UNSET
    overdue_count: int | Unset = UNSET
    pending_review_count: int | Unset = UNSET
    stale_count: int | Unset = UNSET
    todo_count: int | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_monitor_current_dto import OfficeTaskMonitorCurrentDto # noqa: PLC0415
        from ..models.office_task_monitor_item_dto import OfficeTaskMonitorItemDto # noqa: PLC0415
        current: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current, Unset):
            current = self.current.to_dict()

        due_soon_count = self.due_soon_count

        has_on_time_data = self.has_on_time_data

        in_progress_count = self.in_progress_count

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        elif isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        load_state: None | str | Unset
        if isinstance(self.load_state, Unset):
            load_state = UNSET
        else:
            load_state = self.load_state

        on_time_rate = self.on_time_rate

        open_count = self.open_count

        open_count_all = self.open_count_all

        open_total = self.open_total

        overdue_count = self.overdue_count

        pending_review_count = self.pending_review_count

        stale_count = self.stale_count

        todo_count = self.todo_count

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current is not UNSET:
            field_dict["current"] = current
        if due_soon_count is not UNSET:
            field_dict["dueSoonCount"] = due_soon_count
        if has_on_time_data is not UNSET:
            field_dict["hasOnTimeData"] = has_on_time_data
        if in_progress_count is not UNSET:
            field_dict["inProgressCount"] = in_progress_count
        if items is not UNSET:
            field_dict["items"] = items
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if load_state is not UNSET:
            field_dict["loadState"] = load_state
        if on_time_rate is not UNSET:
            field_dict["onTimeRate"] = on_time_rate
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if open_count_all is not UNSET:
            field_dict["openCountAll"] = open_count_all
        if open_total is not UNSET:
            field_dict["openTotal"] = open_total
        if overdue_count is not UNSET:
            field_dict["overdueCount"] = overdue_count
        if pending_review_count is not UNSET:
            field_dict["pendingReviewCount"] = pending_review_count
        if stale_count is not UNSET:
            field_dict["staleCount"] = stale_count
        if todo_count is not UNSET:
            field_dict["todoCount"] = todo_count
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_monitor_current_dto import OfficeTaskMonitorCurrentDto # noqa: PLC0415
        from ..models.office_task_monitor_item_dto import OfficeTaskMonitorItemDto # noqa: PLC0415
        d = dict(src_dict)
        _current = d.pop("current", UNSET)
        current: OfficeTaskMonitorCurrentDto | Unset
        if isinstance(_current,  Unset):
            current = UNSET
        else:
            current = OfficeTaskMonitorCurrentDto.from_dict(_current)




        due_soon_count = d.pop("dueSoonCount", UNSET)

        has_on_time_data = d.pop("hasOnTimeData", UNSET)

        in_progress_count = d.pop("inProgressCount", UNSET)

        def _parse_items(data: object) -> list[OfficeTaskMonitorItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = OfficeTaskMonitorItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskMonitorItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_last_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt", UNSET))


        def _parse_load_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        load_state = _parse_load_state(d.pop("loadState", UNSET))


        on_time_rate = d.pop("onTimeRate", UNSET)

        open_count = d.pop("openCount", UNSET)

        open_count_all = d.pop("openCountAll", UNSET)

        open_total = d.pop("openTotal", UNSET)

        overdue_count = d.pop("overdueCount", UNSET)

        pending_review_count = d.pop("pendingReviewCount", UNSET)

        stale_count = d.pop("staleCount", UNSET)

        todo_count = d.pop("todoCount", UNSET)

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_task_monitor_member_dto = cls(
            current=current,
            due_soon_count=due_soon_count,
            has_on_time_data=has_on_time_data,
            in_progress_count=in_progress_count,
            items=items,
            last_activity_at=last_activity_at,
            load_state=load_state,
            on_time_rate=on_time_rate,
            open_count=open_count,
            open_count_all=open_count_all,
            open_total=open_total,
            overdue_count=overdue_count,
            pending_review_count=pending_review_count,
            stale_count=stale_count,
            todo_count=todo_count,
            user_id=user_id,
        )

        return office_task_monitor_member_dto


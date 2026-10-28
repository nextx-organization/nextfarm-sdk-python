from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_monitor_member_dto import OfficeTaskMonitorMemberDto
  from ..models.office_task_monitor_summary_dto import OfficeTaskMonitorSummaryDto





T = TypeVar("T", bound="OfficeTaskMonitorDto")



@_attrs_define
class OfficeTaskMonitorDto:
    

    due_soon_days: int | Unset = UNSET
    is_exact: bool | Unset = UNSET
    members: list[OfficeTaskMonitorMemberDto] | None | Unset = UNSET
    stale_after_days: int | Unset = UNSET
    summary: OfficeTaskMonitorSummaryDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_monitor_member_dto import OfficeTaskMonitorMemberDto # noqa: PLC0415
        from ..models.office_task_monitor_summary_dto import OfficeTaskMonitorSummaryDto # noqa: PLC0415
        due_soon_days = self.due_soon_days

        is_exact = self.is_exact

        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)


        else:
            members = self.members

        stale_after_days = self.stale_after_days

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if due_soon_days is not UNSET:
            field_dict["dueSoonDays"] = due_soon_days
        if is_exact is not UNSET:
            field_dict["isExact"] = is_exact
        if members is not UNSET:
            field_dict["members"] = members
        if stale_after_days is not UNSET:
            field_dict["staleAfterDays"] = stale_after_days
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_monitor_member_dto import OfficeTaskMonitorMemberDto # noqa: PLC0415
        from ..models.office_task_monitor_summary_dto import OfficeTaskMonitorSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        due_soon_days = d.pop("dueSoonDays", UNSET)

        is_exact = d.pop("isExact", UNSET)

        def _parse_members(data: object) -> list[OfficeTaskMonitorMemberDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in (_members_type_0):
                    members_type_0_item = OfficeTaskMonitorMemberDto.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskMonitorMemberDto] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


        stale_after_days = d.pop("staleAfterDays", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: OfficeTaskMonitorSummaryDto | Unset
        if isinstance(_summary,  Unset):
            summary = UNSET
        else:
            summary = OfficeTaskMonitorSummaryDto.from_dict(_summary)




        office_task_monitor_dto = cls(
            due_soon_days=due_soon_days,
            is_exact=is_exact,
            members=members,
            stale_after_days=stale_after_days,
            summary=summary,
        )

        return office_task_monitor_dto


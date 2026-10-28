from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeTaskMonitorSummaryDto")



@_attrs_define
class OfficeTaskMonitorSummaryDto:
    

    due_soon: int | Unset = UNSET
    has_on_time_data: bool | Unset = UNSET
    on_time_rate: int | Unset = UNSET
    open_: int | Unset = UNSET
    overdue: int | Unset = UNSET
    stale: int | Unset = UNSET
    unassigned: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        due_soon = self.due_soon

        has_on_time_data = self.has_on_time_data

        on_time_rate = self.on_time_rate

        open_ = self.open_

        overdue = self.overdue

        stale = self.stale

        unassigned = self.unassigned


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if due_soon is not UNSET:
            field_dict["dueSoon"] = due_soon
        if has_on_time_data is not UNSET:
            field_dict["hasOnTimeData"] = has_on_time_data
        if on_time_rate is not UNSET:
            field_dict["onTimeRate"] = on_time_rate
        if open_ is not UNSET:
            field_dict["open"] = open_
        if overdue is not UNSET:
            field_dict["overdue"] = overdue
        if stale is not UNSET:
            field_dict["stale"] = stale
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        due_soon = d.pop("dueSoon", UNSET)

        has_on_time_data = d.pop("hasOnTimeData", UNSET)

        on_time_rate = d.pop("onTimeRate", UNSET)

        open_ = d.pop("open", UNSET)

        overdue = d.pop("overdue", UNSET)

        stale = d.pop("stale", UNSET)

        unassigned = d.pop("unassigned", UNSET)

        office_task_monitor_summary_dto = cls(
            due_soon=due_soon,
            has_on_time_data=has_on_time_data,
            on_time_rate=on_time_rate,
            open_=open_,
            overdue=overdue,
            stale=stale,
            unassigned=unassigned,
        )

        return office_task_monitor_summary_dto


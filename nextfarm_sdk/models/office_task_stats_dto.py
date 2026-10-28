from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeTaskStatsDto")



@_attrs_define
class OfficeTaskStatsDto:
    

    completed: int | Unset = UNSET
    is_exact: bool | Unset = UNSET
    on_time_rate: int | Unset = UNSET
    open_: int | Unset = UNSET
    overdue: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        completed = self.completed

        is_exact = self.is_exact

        on_time_rate = self.on_time_rate

        open_ = self.open_

        overdue = self.overdue


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if completed is not UNSET:
            field_dict["completed"] = completed
        if is_exact is not UNSET:
            field_dict["isExact"] = is_exact
        if on_time_rate is not UNSET:
            field_dict["onTimeRate"] = on_time_rate
        if open_ is not UNSET:
            field_dict["open"] = open_
        if overdue is not UNSET:
            field_dict["overdue"] = overdue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed = d.pop("completed", UNSET)

        is_exact = d.pop("isExact", UNSET)

        on_time_rate = d.pop("onTimeRate", UNSET)

        open_ = d.pop("open", UNSET)

        overdue = d.pop("overdue", UNSET)

        office_task_stats_dto = cls(
            completed=completed,
            is_exact=is_exact,
            on_time_rate=on_time_rate,
            open_=open_,
            overdue=overdue,
        )

        return office_task_stats_dto


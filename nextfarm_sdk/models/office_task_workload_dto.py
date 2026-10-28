from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskWorkloadDto")



@_attrs_define
class OfficeTaskWorkloadDto:
    

    is_overloaded: bool | Unset = UNSET
    open_count: int | Unset = UNSET
    overdue_count: int | Unset = UNSET
    overload_threshold: int | Unset = UNSET
    total_workload: float | Unset = UNSET
    user_id: UUID | Unset = UNSET
    workload_day: float | Unset = UNSET
    workload_hour: float | Unset = UNSET
    workload_point: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_overloaded = self.is_overloaded

        open_count = self.open_count

        overdue_count = self.overdue_count

        overload_threshold = self.overload_threshold

        total_workload = self.total_workload

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        workload_day = self.workload_day

        workload_hour = self.workload_hour

        workload_point = self.workload_point


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_overloaded is not UNSET:
            field_dict["isOverloaded"] = is_overloaded
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if overdue_count is not UNSET:
            field_dict["overdueCount"] = overdue_count
        if overload_threshold is not UNSET:
            field_dict["overloadThreshold"] = overload_threshold
        if total_workload is not UNSET:
            field_dict["totalWorkload"] = total_workload
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if workload_day is not UNSET:
            field_dict["workloadDay"] = workload_day
        if workload_hour is not UNSET:
            field_dict["workloadHour"] = workload_hour
        if workload_point is not UNSET:
            field_dict["workloadPoint"] = workload_point

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_overloaded = d.pop("isOverloaded", UNSET)

        open_count = d.pop("openCount", UNSET)

        overdue_count = d.pop("overdueCount", UNSET)

        overload_threshold = d.pop("overloadThreshold", UNSET)

        total_workload = d.pop("totalWorkload", UNSET)

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        workload_day = d.pop("workloadDay", UNSET)

        workload_hour = d.pop("workloadHour", UNSET)

        workload_point = d.pop("workloadPoint", UNSET)

        office_task_workload_dto = cls(
            is_overloaded=is_overloaded,
            open_count=open_count,
            overdue_count=overdue_count,
            overload_threshold=overload_threshold,
            total_workload=total_workload,
            user_id=user_id,
            workload_day=workload_day,
            workload_hour=workload_hour,
            workload_point=workload_point,
        )

        return office_task_workload_dto


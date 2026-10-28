from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeProjectPortfolioKpisDto")



@_attrs_define
class OfficeProjectPortfolioKpisDto:
    

    late: int | Unset = UNSET
    overdue_tasks: int | Unset = UNSET
    running: int | Unset = UNSET
    stalled: int | Unset = UNSET
    unassigned_tasks: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        late = self.late

        overdue_tasks = self.overdue_tasks

        running = self.running

        stalled = self.stalled

        unassigned_tasks = self.unassigned_tasks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if late is not UNSET:
            field_dict["late"] = late
        if overdue_tasks is not UNSET:
            field_dict["overdueTasks"] = overdue_tasks
        if running is not UNSET:
            field_dict["running"] = running
        if stalled is not UNSET:
            field_dict["stalled"] = stalled
        if unassigned_tasks is not UNSET:
            field_dict["unassignedTasks"] = unassigned_tasks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        late = d.pop("late", UNSET)

        overdue_tasks = d.pop("overdueTasks", UNSET)

        running = d.pop("running", UNSET)

        stalled = d.pop("stalled", UNSET)

        unassigned_tasks = d.pop("unassignedTasks", UNSET)

        office_project_portfolio_kpis_dto = cls(
            late=late,
            overdue_tasks=overdue_tasks,
            running=running,
            stalled=stalled,
            unassigned_tasks=unassigned_tasks,
        )

        return office_project_portfolio_kpis_dto


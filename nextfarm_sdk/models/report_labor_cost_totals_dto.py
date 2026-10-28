from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReportLaborCostTotalsDto")



@_attrs_define
class ReportLaborCostTotalsDto:
    

    piecework_cost: int | Unset = UNSET
    time_cost: int | Unset = UNSET
    total_cost: int | Unset = UNSET
    work_units: float | Unset = UNSET
    worker_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        piecework_cost = self.piecework_cost

        time_cost = self.time_cost

        total_cost = self.total_cost

        work_units = self.work_units

        worker_count = self.worker_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if piecework_cost is not UNSET:
            field_dict["pieceworkCost"] = piecework_cost
        if time_cost is not UNSET:
            field_dict["timeCost"] = time_cost
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if work_units is not UNSET:
            field_dict["workUnits"] = work_units
        if worker_count is not UNSET:
            field_dict["workerCount"] = worker_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        piecework_cost = d.pop("pieceworkCost", UNSET)

        time_cost = d.pop("timeCost", UNSET)

        total_cost = d.pop("totalCost", UNSET)

        work_units = d.pop("workUnits", UNSET)

        worker_count = d.pop("workerCount", UNSET)

        report_labor_cost_totals_dto = cls(
            piecework_cost=piecework_cost,
            time_cost=time_cost,
            total_cost=total_cost,
            work_units=work_units,
            worker_count=worker_count,
        )

        return report_labor_cost_totals_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestPlanLineRequest")



@_attrs_define
class HarvestPlanLineRequest:
    

    area_ha: float | Unset = UNSET
    expected_yield_kg: float | Unset = UNSET
    planned_on: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        area_ha = self.area_ha

        expected_yield_kg = self.expected_yield_kg

        planned_on: None | str | Unset
        if isinstance(self.planned_on, Unset):
            planned_on = UNSET
        elif isinstance(self.planned_on, datetime.date):
            planned_on = self.planned_on.isoformat()
        else:
            planned_on = self.planned_on


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if area_ha is not UNSET:
            field_dict["area_ha"] = area_ha
        if expected_yield_kg is not UNSET:
            field_dict["expected_yield_kg"] = expected_yield_kg
        if planned_on is not UNSET:
            field_dict["planned_on"] = planned_on

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        area_ha = d.pop("area_ha", UNSET)

        expected_yield_kg = d.pop("expected_yield_kg", UNSET)

        def _parse_planned_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_on_type_0 = datetime.date.fromisoformat(data)



                return planned_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        planned_on = _parse_planned_on(d.pop("planned_on", UNSET))


        harvest_plan_line_request = cls(
            area_ha=area_ha,
            expected_yield_kg=expected_yield_kg,
            planned_on=planned_on,
        )

        return harvest_plan_line_request


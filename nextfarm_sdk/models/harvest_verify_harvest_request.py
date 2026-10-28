from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestVerifyHarvestRequest")



@_attrs_define
class HarvestVerifyHarvestRequest:
    

    actual_quantity_kg: float | Unset = UNSET
    quality_grade: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        actual_quantity_kg = self.actual_quantity_kg

        quality_grade: None | str | Unset
        if isinstance(self.quality_grade, Unset):
            quality_grade = UNSET
        else:
            quality_grade = self.quality_grade


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actual_quantity_kg is not UNSET:
            field_dict["actual_quantity_kg"] = actual_quantity_kg
        if quality_grade is not UNSET:
            field_dict["quality_grade"] = quality_grade

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actual_quantity_kg = d.pop("actual_quantity_kg", UNSET)

        def _parse_quality_grade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_grade = _parse_quality_grade(d.pop("quality_grade", UNSET))


        harvest_verify_harvest_request = cls(
            actual_quantity_kg=actual_quantity_kg,
            quality_grade=quality_grade,
        )

        return harvest_verify_harvest_request


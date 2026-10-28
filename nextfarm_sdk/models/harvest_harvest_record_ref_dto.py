from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestHarvestRecordRefDto")



@_attrs_define
class HarvestHarvestRecordRefDto:
    

    actual_quantity_kg: float | None | Unset = UNSET
    declared_quantity_kg: float | Unset = UNSET
    id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        actual_quantity_kg: float | None | Unset
        if isinstance(self.actual_quantity_kg, Unset):
            actual_quantity_kg = UNSET
        else:
            actual_quantity_kg = self.actual_quantity_kg

        declared_quantity_kg = self.declared_quantity_kg

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actual_quantity_kg is not UNSET:
            field_dict["actual_quantity_kg"] = actual_quantity_kg
        if declared_quantity_kg is not UNSET:
            field_dict["declared_quantity_kg"] = declared_quantity_kg
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_actual_quantity_kg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        actual_quantity_kg = _parse_actual_quantity_kg(d.pop("actual_quantity_kg", UNSET))


        declared_quantity_kg = d.pop("declared_quantity_kg", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        harvest_harvest_record_ref_dto = cls(
            actual_quantity_kg=actual_quantity_kg,
            declared_quantity_kg=declared_quantity_kg,
            id=id,
        )

        return harvest_harvest_record_ref_dto


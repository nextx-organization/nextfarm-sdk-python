from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestHarvestOrganismInput")



@_attrs_define
class HarvestHarvestOrganismInput:
    

    fruit_count: int | None | Unset = UNSET
    organism_id: UUID | Unset = UNSET
    quantity_kg: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        fruit_count: int | None | Unset
        if isinstance(self.fruit_count, Unset):
            fruit_count = UNSET
        else:
            fruit_count = self.fruit_count

        organism_id: str | Unset = UNSET
        if not isinstance(self.organism_id, Unset):
            organism_id = str(self.organism_id)

        quantity_kg: float | None | Unset
        if isinstance(self.quantity_kg, Unset):
            quantity_kg = UNSET
        else:
            quantity_kg = self.quantity_kg


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if fruit_count is not UNSET:
            field_dict["fruit_count"] = fruit_count
        if organism_id is not UNSET:
            field_dict["organism_id"] = organism_id
        if quantity_kg is not UNSET:
            field_dict["quantity_kg"] = quantity_kg

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_fruit_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fruit_count = _parse_fruit_count(d.pop("fruit_count", UNSET))


        _organism_id = d.pop("organism_id", UNSET)
        organism_id: UUID | Unset
        if isinstance(_organism_id,  Unset):
            organism_id = UNSET
        else:
            organism_id = UUID(_organism_id)




        def _parse_quantity_kg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quantity_kg = _parse_quantity_kg(d.pop("quantity_kg", UNSET))


        harvest_harvest_organism_input = cls(
            fruit_count=fruit_count,
            organism_id=organism_id,
            quantity_kg=quantity_kg,
        )

        return harvest_harvest_organism_input


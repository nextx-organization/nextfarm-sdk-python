from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestNormLineInput")



@_attrs_define
class HarvestNormLineInput:
    

    age_from: int | None | Unset = UNSET
    age_to: int | None | Unset = UNSET
    basis: None | str | Unset = UNSET
    item_id: None | Unset | UUID = UNSET
    kind: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    quantity_per_ha: float | Unset = UNSET
    ref_price: int | Unset = UNSET
    stage: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        age_from: int | None | Unset
        if isinstance(self.age_from, Unset):
            age_from = UNSET
        else:
            age_from = self.age_from

        age_to: int | None | Unset
        if isinstance(self.age_to, Unset):
            age_to = UNSET
        else:
            age_to = self.age_to

        basis: None | str | Unset
        if isinstance(self.basis, Unset):
            basis = UNSET
        else:
            basis = self.basis

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        quantity_per_ha = self.quantity_per_ha

        ref_price = self.ref_price

        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        else:
            stage = self.stage

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if age_from is not UNSET:
            field_dict["age_from"] = age_from
        if age_to is not UNSET:
            field_dict["age_to"] = age_to
        if basis is not UNSET:
            field_dict["basis"] = basis
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if quantity_per_ha is not UNSET:
            field_dict["quantity_per_ha"] = quantity_per_ha
        if ref_price is not UNSET:
            field_dict["ref_price"] = ref_price
        if stage is not UNSET:
            field_dict["stage"] = stage
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_age_from(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age_from = _parse_age_from(d.pop("age_from", UNSET))


        def _parse_age_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age_to = _parse_age_to(d.pop("age_to", UNSET))


        def _parse_basis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basis = _parse_basis(d.pop("basis", UNSET))


        def _parse_item_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                item_id_type_0 = UUID(data)



                return item_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        item_id = _parse_item_id(d.pop("item_id", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        quantity_per_ha = d.pop("quantity_per_ha", UNSET)

        ref_price = d.pop("ref_price", UNSET)

        def _parse_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        harvest_norm_line_input = cls(
            age_from=age_from,
            age_to=age_to,
            basis=basis,
            item_id=item_id,
            kind=kind,
            name=name,
            quantity_per_ha=quantity_per_ha,
            ref_price=ref_price,
            stage=stage,
            unit=unit,
        )

        return harvest_norm_line_input


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestPesticideBridgeDto")



@_attrs_define
class HarvestPesticideBridgeDto:
    

    active_ingredient: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    phi_days: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        active_ingredient: None | str | Unset
        if isinstance(self.active_ingredient, Unset):
            active_ingredient = UNSET
        else:
            active_ingredient = self.active_ingredient

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        phi_days: int | None | Unset
        if isinstance(self.phi_days, Unset):
            phi_days = UNSET
        else:
            phi_days = self.phi_days


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active_ingredient is not UNSET:
            field_dict["active_ingredient"] = active_ingredient
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if phi_days is not UNSET:
            field_dict["phi_days"] = phi_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_active_ingredient(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_ingredient = _parse_active_ingredient(d.pop("active_ingredient", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_phi_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        phi_days = _parse_phi_days(d.pop("phi_days", UNSET))


        harvest_pesticide_bridge_dto = cls(
            active_ingredient=active_ingredient,
            id=id,
            name=name,
            phi_days=phi_days,
        )

        return harvest_pesticide_bridge_dto


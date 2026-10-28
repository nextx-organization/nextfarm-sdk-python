from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestPesticideDto")



@_attrs_define
class HarvestPesticideDto:
    

    active_ingredient: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    phi_days: int | None | Unset = UNSET
    source: None | str | Unset = UNSET
    trade_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        active_ingredient: None | str | Unset
        if isinstance(self.active_ingredient, Unset):
            active_ingredient = UNSET
        else:
            active_ingredient = self.active_ingredient

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        phi_days: int | None | Unset
        if isinstance(self.phi_days, Unset):
            phi_days = UNSET
        else:
            phi_days = self.phi_days

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        trade_name: None | str | Unset
        if isinstance(self.trade_name, Unset):
            trade_name = UNSET
        else:
            trade_name = self.trade_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active_ingredient is not UNSET:
            field_dict["active_ingredient"] = active_ingredient
        if id is not UNSET:
            field_dict["id"] = id
        if phi_days is not UNSET:
            field_dict["phi_days"] = phi_days
        if source is not UNSET:
            field_dict["source"] = source
        if trade_name is not UNSET:
            field_dict["trade_name"] = trade_name

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




        def _parse_phi_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        phi_days = _parse_phi_days(d.pop("phi_days", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_trade_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_name = _parse_trade_name(d.pop("trade_name", UNSET))


        harvest_pesticide_dto = cls(
            active_ingredient=active_ingredient,
            id=id,
            phi_days=phi_days,
            source=source,
            trade_name=trade_name,
        )

        return harvest_pesticide_dto


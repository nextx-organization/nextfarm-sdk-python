from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestAddFarmPesticideRequest")



@_attrs_define
class HarvestAddFarmPesticideRequest:
    

    active_ingredient: None | str | Unset = UNSET
    phi_days: int | Unset = UNSET
    trade_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        active_ingredient: None | str | Unset
        if isinstance(self.active_ingredient, Unset):
            active_ingredient = UNSET
        else:
            active_ingredient = self.active_ingredient

        phi_days = self.phi_days

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
        if phi_days is not UNSET:
            field_dict["phi_days"] = phi_days
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


        phi_days = d.pop("phi_days", UNSET)

        def _parse_trade_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_name = _parse_trade_name(d.pop("trade_name", UNSET))


        harvest_add_farm_pesticide_request = cls(
            active_ingredient=active_ingredient,
            phi_days=phi_days,
            trade_name=trade_name,
        )

        return harvest_add_farm_pesticide_request


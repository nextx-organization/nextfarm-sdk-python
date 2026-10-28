from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestMarketPricePointDto")



@_attrs_define
class HarvestMarketPricePointDto:
    

    recorded_on: datetime.date | Unset = UNSET
    unit_price: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        recorded_on: str | Unset = UNSET
        if not isinstance(self.recorded_on, Unset):
            recorded_on = self.recorded_on.isoformat()

        unit_price = self.unit_price


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if recorded_on is not UNSET:
            field_dict["recorded_on"] = recorded_on
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _recorded_on = d.pop("recorded_on", UNSET)
        recorded_on: datetime.date | Unset
        if isinstance(_recorded_on,  Unset):
            recorded_on = UNSET
        else:
            recorded_on = datetime.date.fromisoformat(_recorded_on)




        unit_price = d.pop("unit_price", UNSET)

        harvest_market_price_point_dto = cls(
            recorded_on=recorded_on,
            unit_price=unit_price,
        )

        return harvest_market_price_point_dto


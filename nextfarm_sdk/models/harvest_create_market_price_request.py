from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestCreateMarketPriceRequest")



@_attrs_define
class HarvestCreateMarketPriceRequest:
    

    commodity_code: None | str | Unset = UNSET
    commodity_name: None | str | Unset = UNSET
    grade: None | str | Unset = UNSET
    market: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    recorded_by_name: None | str | Unset = UNSET
    recorded_on: datetime.date | Unset = UNSET
    unit: None | str | Unset = UNSET
    unit_price: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        commodity_code: None | str | Unset
        if isinstance(self.commodity_code, Unset):
            commodity_code = UNSET
        else:
            commodity_code = self.commodity_code

        commodity_name: None | str | Unset
        if isinstance(self.commodity_name, Unset):
            commodity_name = UNSET
        else:
            commodity_name = self.commodity_name

        grade: None | str | Unset
        if isinstance(self.grade, Unset):
            grade = UNSET
        else:
            grade = self.grade

        market: None | str | Unset
        if isinstance(self.market, Unset):
            market = UNSET
        else:
            market = self.market

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        recorded_by_name: None | str | Unset
        if isinstance(self.recorded_by_name, Unset):
            recorded_by_name = UNSET
        else:
            recorded_by_name = self.recorded_by_name

        recorded_on: str | Unset = UNSET
        if not isinstance(self.recorded_on, Unset):
            recorded_on = self.recorded_on.isoformat()

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        unit_price = self.unit_price


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if commodity_code is not UNSET:
            field_dict["commodity_code"] = commodity_code
        if commodity_name is not UNSET:
            field_dict["commodity_name"] = commodity_name
        if grade is not UNSET:
            field_dict["grade"] = grade
        if market is not UNSET:
            field_dict["market"] = market
        if note is not UNSET:
            field_dict["note"] = note
        if recorded_by_name is not UNSET:
            field_dict["recorded_by_name"] = recorded_by_name
        if recorded_on is not UNSET:
            field_dict["recorded_on"] = recorded_on
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_commodity_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commodity_code = _parse_commodity_code(d.pop("commodity_code", UNSET))


        def _parse_commodity_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commodity_name = _parse_commodity_name(d.pop("commodity_name", UNSET))


        def _parse_grade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grade = _parse_grade(d.pop("grade", UNSET))


        def _parse_market(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market = _parse_market(d.pop("market", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_recorded_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recorded_by_name = _parse_recorded_by_name(d.pop("recorded_by_name", UNSET))


        _recorded_on = d.pop("recorded_on", UNSET)
        recorded_on: datetime.date | Unset
        if isinstance(_recorded_on,  Unset):
            recorded_on = UNSET
        else:
            recorded_on = datetime.date.fromisoformat(_recorded_on)




        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        unit_price = d.pop("unit_price", UNSET)

        harvest_create_market_price_request = cls(
            commodity_code=commodity_code,
            commodity_name=commodity_name,
            grade=grade,
            market=market,
            note=note,
            recorded_by_name=recorded_by_name,
            recorded_on=recorded_on,
            unit=unit,
            unit_price=unit_price,
        )

        return harvest_create_market_price_request


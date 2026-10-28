from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GisCloseSeasonRequest")



@_attrs_define
class GisCloseSeasonRequest:
    

    closed_on: datetime.date | Unset = UNSET
    yield_kg: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        closed_on: str | Unset = UNSET
        if not isinstance(self.closed_on, Unset):
            closed_on = self.closed_on.isoformat()

        yield_kg: float | None | Unset
        if isinstance(self.yield_kg, Unset):
            yield_kg = UNSET
        else:
            yield_kg = self.yield_kg


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if closed_on is not UNSET:
            field_dict["closed_on"] = closed_on
        if yield_kg is not UNSET:
            field_dict["yield_kg"] = yield_kg

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _closed_on = d.pop("closed_on", UNSET)
        closed_on: datetime.date | Unset
        if isinstance(_closed_on,  Unset):
            closed_on = UNSET
        else:
            closed_on = datetime.date.fromisoformat(_closed_on)




        def _parse_yield_kg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        yield_kg = _parse_yield_kg(d.pop("yield_kg", UNSET))


        gis_close_season_request = cls(
            closed_on=closed_on,
            yield_kg=yield_kg,
        )

        return gis_close_season_request


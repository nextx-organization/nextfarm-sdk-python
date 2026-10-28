from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestQrScanDayDto")



@_attrs_define
class HarvestQrScanDayDto:
    

    day: datetime.date | Unset = UNSET
    visitors: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        day: str | Unset = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.isoformat()

        visitors = self.visitors


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if day is not UNSET:
            field_dict["day"] = day
        if visitors is not UNSET:
            field_dict["visitors"] = visitors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _day = d.pop("day", UNSET)
        day: datetime.date | Unset
        if isinstance(_day,  Unset):
            day = UNSET
        else:
            day = datetime.date.fromisoformat(_day)




        visitors = d.pop("visitors", UNSET)

        harvest_qr_scan_day_dto = cls(
            day=day,
            visitors=visitors,
        )

        return harvest_qr_scan_day_dto


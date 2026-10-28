from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="IotShiftSlotRequest")



@_attrs_define
class IotShiftSlotRequest:
    

    date: datetime.date | Unset = UNSET
    new_time: str | Unset = UNSET
    via: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        new_time = self.new_time

        via: None | str | Unset
        if isinstance(self.via, Unset):
            via = UNSET
        else:
            via = self.via


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if new_time is not UNSET:
            field_dict["new_time"] = new_time
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)




        new_time = d.pop("new_time", UNSET)

        def _parse_via(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        via = _parse_via(d.pop("via", UNSET))


        iot_shift_slot_request = cls(
            date=date,
            new_time=new_time,
            via=via,
        )

        return iot_shift_slot_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeCalendarEventDto")



@_attrs_define
class OfficeCalendarEventDto:
    

    data: None | str | Unset = UNSET
    end: datetime.datetime | None | Unset = UNSET
    record_id: UUID | Unset = UNSET
    start: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        data: None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        end: None | str | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        elif isinstance(self.end, datetime.datetime):
            end = self.end.isoformat()
        else:
            end = self.end

        record_id: str | Unset = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = str(self.record_id)

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if end is not UNSET:
            field_dict["end"] = end
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        def _parse_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_0 = datetime.datetime.fromisoformat(data)



                return end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end = _parse_end(d.pop("end", UNSET))


        _record_id = d.pop("recordId", UNSET)
        record_id: UUID | Unset
        if isinstance(_record_id,  Unset):
            record_id = UNSET
        else:
            record_id = UUID(_record_id)




        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start,  Unset):
            start = UNSET
        else:
            start = datetime.datetime.fromisoformat(_start)




        office_calendar_event_dto = cls(
            data=data,
            end=end,
            record_id=record_id,
            start=start,
        )

        return office_calendar_event_dto


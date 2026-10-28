from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeRescheduleEventRequest")



@_attrs_define
class OfficeRescheduleEventRequest:
    

    all_day: bool | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    occurrence_start: datetime.datetime | None | Unset = UNSET
    scope: None | str | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        all_day = self.all_day

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        occurrence_start: None | str | Unset
        if isinstance(self.occurrence_start, Unset):
            occurrence_start = UNSET
        elif isinstance(self.occurrence_start, datetime.datetime):
            occurrence_start = self.occurrence_start.isoformat()
        else:
            occurrence_start = self.occurrence_start

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if all_day is not UNSET:
            field_dict["allDay"] = all_day
        if end_at is not UNSET:
            field_dict["endAt"] = end_at
        if occurrence_start is not UNSET:
            field_dict["occurrenceStart"] = occurrence_start
        if scope is not UNSET:
            field_dict["scope"] = scope
        if start_at is not UNSET:
            field_dict["startAt"] = start_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_day = d.pop("allDay", UNSET)

        _end_at = d.pop("endAt", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at,  Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)




        def _parse_occurrence_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                occurrence_start_type_0 = datetime.datetime.fromisoformat(data)



                return occurrence_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        occurrence_start = _parse_occurrence_start(d.pop("occurrenceStart", UNSET))


        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        _start_at = d.pop("startAt", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at,  Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)




        office_reschedule_event_request = cls(
            all_day=all_day,
            end_at=end_at,
            occurrence_start=occurrence_start,
            scope=scope,
            start_at=start_at,
        )

        return office_reschedule_event_request


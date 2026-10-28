from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeProposeTimeRequest")



@_attrs_define
class OfficeProposeTimeRequest:
    

    note: None | str | Unset = UNSET
    occurrence_start: datetime.datetime | None | Unset = UNSET
    proposed_end_at: datetime.datetime | Unset = UNSET
    proposed_start_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        occurrence_start: None | str | Unset
        if isinstance(self.occurrence_start, Unset):
            occurrence_start = UNSET
        elif isinstance(self.occurrence_start, datetime.datetime):
            occurrence_start = self.occurrence_start.isoformat()
        else:
            occurrence_start = self.occurrence_start

        proposed_end_at: str | Unset = UNSET
        if not isinstance(self.proposed_end_at, Unset):
            proposed_end_at = self.proposed_end_at.isoformat()

        proposed_start_at: str | Unset = UNSET
        if not isinstance(self.proposed_start_at, Unset):
            proposed_start_at = self.proposed_start_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if note is not UNSET:
            field_dict["note"] = note
        if occurrence_start is not UNSET:
            field_dict["occurrenceStart"] = occurrence_start
        if proposed_end_at is not UNSET:
            field_dict["proposedEndAt"] = proposed_end_at
        if proposed_start_at is not UNSET:
            field_dict["proposedStartAt"] = proposed_start_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


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


        _proposed_end_at = d.pop("proposedEndAt", UNSET)
        proposed_end_at: datetime.datetime | Unset
        if isinstance(_proposed_end_at,  Unset):
            proposed_end_at = UNSET
        else:
            proposed_end_at = datetime.datetime.fromisoformat(_proposed_end_at)




        _proposed_start_at = d.pop("proposedStartAt", UNSET)
        proposed_start_at: datetime.datetime | Unset
        if isinstance(_proposed_start_at,  Unset):
            proposed_start_at = UNSET
        else:
            proposed_start_at = datetime.datetime.fromisoformat(_proposed_start_at)




        office_propose_time_request = cls(
            note=note,
            occurrence_start=occurrence_start,
            proposed_end_at=proposed_end_at,
            proposed_start_at=proposed_start_at,
        )

        return office_propose_time_request


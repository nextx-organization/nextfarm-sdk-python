from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestAddOrganismEventRequest")



@_attrs_define
class HarvestAddOrganismEventRequest:
    

    kind: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    occurred_at: datetime.datetime | None | Unset = UNSET
    photo_url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        occurred_at: None | str | Unset
        if isinstance(self.occurred_at, Unset):
            occurred_at = UNSET
        elif isinstance(self.occurred_at, datetime.datetime):
            occurred_at = self.occurred_at.isoformat()
        else:
            occurred_at = self.occurred_at

        photo_url: None | str | Unset
        if isinstance(self.photo_url, Unset):
            photo_url = UNSET
        else:
            photo_url = self.photo_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if note is not UNSET:
            field_dict["note"] = note
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if photo_url is not UNSET:
            field_dict["photo_url"] = photo_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_occurred_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                occurred_at_type_0 = datetime.datetime.fromisoformat(data)



                return occurred_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        occurred_at = _parse_occurred_at(d.pop("occurred_at", UNSET))


        def _parse_photo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_url = _parse_photo_url(d.pop("photo_url", UNSET))


        harvest_add_organism_event_request = cls(
            kind=kind,
            note=note,
            occurred_at=occurred_at,
            photo_url=photo_url,
        )

        return harvest_add_organism_event_request


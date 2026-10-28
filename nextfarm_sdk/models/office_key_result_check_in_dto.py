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






T = TypeVar("T", bound="OfficeKeyResultCheckInDto")



@_attrs_define
class OfficeKeyResultCheckInDto:
    

    confidence: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    key_result_id: UUID | Unset = UNSET
    kind: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    previous_value: float | Unset = UNSET
    value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        confidence: None | str | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        key_result_id: str | Unset = UNSET
        if not isinstance(self.key_result_id, Unset):
            key_result_id = str(self.key_result_id)

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

        previous_value = self.previous_value

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if key_result_id is not UNSET:
            field_dict["keyResultId"] = key_result_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if note is not UNSET:
            field_dict["note"] = note
        if previous_value is not UNSET:
            field_dict["previousValue"] = previous_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_confidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _created_by = d.pop("createdBy", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _key_result_id = d.pop("keyResultId", UNSET)
        key_result_id: UUID | Unset
        if isinstance(_key_result_id,  Unset):
            key_result_id = UNSET
        else:
            key_result_id = UUID(_key_result_id)




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


        previous_value = d.pop("previousValue", UNSET)

        value = d.pop("value", UNSET)

        office_key_result_check_in_dto = cls(
            confidence=confidence,
            created_at=created_at,
            created_by=created_by,
            id=id,
            key_result_id=key_result_id,
            kind=kind,
            note=note,
            previous_value=previous_value,
            value=value,
        )

        return office_key_result_check_in_dto


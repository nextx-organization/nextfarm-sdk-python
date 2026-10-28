from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCompleteTaskWithMessagePhotosRequest")



@_attrs_define
class OfficeCompleteTaskWithMessagePhotosRequest:
    

    message_id: UUID | Unset = UNSET
    result_note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        result_note: None | str | Unset
        if isinstance(self.result_note, Unset):
            result_note = UNSET
        else:
            result_note = self.result_note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if result_note is not UNSET:
            field_dict["resultNote"] = result_note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        def _parse_result_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_note = _parse_result_note(d.pop("resultNote", UNSET))


        office_complete_task_with_message_photos_request = cls(
            message_id=message_id,
            result_note=result_note,
        )

        return office_complete_task_with_message_photos_request


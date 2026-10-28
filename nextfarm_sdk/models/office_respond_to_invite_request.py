from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeRespondToInviteRequest")



@_attrs_define
class OfficeRespondToInviteRequest:
    

    note: None | str | Unset = UNSET
    response_status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        response_status: None | str | Unset
        if isinstance(self.response_status, Unset):
            response_status = UNSET
        else:
            response_status = self.response_status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if note is not UNSET:
            field_dict["note"] = note
        if response_status is not UNSET:
            field_dict["responseStatus"] = response_status

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


        def _parse_response_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_status = _parse_response_status(d.pop("responseStatus", UNSET))


        office_respond_to_invite_request = cls(
            note=note,
            response_status=response_status,
        )

        return office_respond_to_invite_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeQuotedMessageDto")



@_attrs_define
class OfficeQuotedMessageDto:
    

    id: UUID | Unset = UNSET
    is_recalled: bool | Unset = UNSET
    sender_id: UUID | Unset = UNSET
    snippet: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_recalled = self.is_recalled

        sender_id: str | Unset = UNSET
        if not isinstance(self.sender_id, Unset):
            sender_id = str(self.sender_id)

        snippet: None | str | Unset
        if isinstance(self.snippet, Unset):
            snippet = UNSET
        else:
            snippet = self.snippet


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_recalled is not UNSET:
            field_dict["isRecalled"] = is_recalled
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if snippet is not UNSET:
            field_dict["snippet"] = snippet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_recalled = d.pop("isRecalled", UNSET)

        _sender_id = d.pop("senderId", UNSET)
        sender_id: UUID | Unset
        if isinstance(_sender_id,  Unset):
            sender_id = UNSET
        else:
            sender_id = UUID(_sender_id)




        def _parse_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snippet = _parse_snippet(d.pop("snippet", UNSET))


        office_quoted_message_dto = cls(
            id=id,
            is_recalled=is_recalled,
            sender_id=sender_id,
            snippet=snippet,
        )

        return office_quoted_message_dto


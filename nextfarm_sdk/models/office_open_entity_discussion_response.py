from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeOpenEntityDiscussionResponse")



@_attrs_define
class OfficeOpenEntityDiscussionResponse:
    

    channel_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        office_open_entity_discussion_response = cls(
            channel_id=channel_id,
        )

        return office_open_entity_discussion_response


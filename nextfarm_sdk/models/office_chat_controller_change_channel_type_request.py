from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerChangeChannelTypeRequest")



@_attrs_define
class OfficeChatControllerChangeChannelTypeRequest:
    

    channel_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_type: None | str | Unset
        if isinstance(self.channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = self.channel_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_type = _parse_channel_type(d.pop("channelType", UNSET))


        office_chat_controller_change_channel_type_request = cls(
            channel_type=channel_type,
        )

        return office_chat_controller_change_channel_type_request


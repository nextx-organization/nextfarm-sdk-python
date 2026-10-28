from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerSetChannelAvatarRequest")



@_attrs_define
class OfficeChatControllerSetChannelAvatarRequest:
    

    storage_path: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        storage_path: None | str | Unset
        if isinstance(self.storage_path, Unset):
            storage_path = UNSET
        else:
            storage_path = self.storage_path


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if storage_path is not UNSET:
            field_dict["storagePath"] = storage_path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_storage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_path = _parse_storage_path(d.pop("storagePath", UNSET))


        office_chat_controller_set_channel_avatar_request = cls(
            storage_path=storage_path,
        )

        return office_chat_controller_set_channel_avatar_request


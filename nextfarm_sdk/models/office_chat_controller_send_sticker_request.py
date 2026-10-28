from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerSendStickerRequest")



@_attrs_define
class OfficeChatControllerSendStickerRequest:
    

    client_message_id: None | str | Unset = UNSET
    sticker_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        client_message_id: None | str | Unset
        if isinstance(self.client_message_id, Unset):
            client_message_id = UNSET
        else:
            client_message_id = self.client_message_id

        sticker_id: str | Unset = UNSET
        if not isinstance(self.sticker_id, Unset):
            sticker_id = str(self.sticker_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if client_message_id is not UNSET:
            field_dict["clientMessageId"] = client_message_id
        if sticker_id is not UNSET:
            field_dict["stickerId"] = sticker_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_client_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_message_id = _parse_client_message_id(d.pop("clientMessageId", UNSET))


        _sticker_id = d.pop("stickerId", UNSET)
        sticker_id: UUID | Unset
        if isinstance(_sticker_id,  Unset):
            sticker_id = UNSET
        else:
            sticker_id = UUID(_sticker_id)




        office_chat_controller_send_sticker_request = cls(
            client_message_id=client_message_id,
            sticker_id=sticker_id,
        )

        return office_chat_controller_send_sticker_request


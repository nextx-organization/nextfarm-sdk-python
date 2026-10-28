from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerMarkReadRequest")



@_attrs_define
class OfficeChatControllerMarkReadRequest:
    

    up_to_message_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        up_to_message_id: None | str | Unset
        if isinstance(self.up_to_message_id, Unset):
            up_to_message_id = UNSET
        elif isinstance(self.up_to_message_id, UUID):
            up_to_message_id = str(self.up_to_message_id)
        else:
            up_to_message_id = self.up_to_message_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if up_to_message_id is not UNSET:
            field_dict["upToMessageId"] = up_to_message_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_up_to_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                up_to_message_id_type_0 = UUID(data)



                return up_to_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        up_to_message_id = _parse_up_to_message_id(d.pop("upToMessageId", UNSET))


        office_chat_controller_mark_read_request = cls(
            up_to_message_id=up_to_message_id,
        )

        return office_chat_controller_mark_read_request


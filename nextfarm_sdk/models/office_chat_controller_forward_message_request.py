from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerForwardMessageRequest")



@_attrs_define
class OfficeChatControllerForwardMessageRequest:
    

    comment: None | str | Unset = UNSET
    target_channel_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        target_channel_ids: list[str] | None | Unset
        if isinstance(self.target_channel_ids, Unset):
            target_channel_ids = UNSET
        elif isinstance(self.target_channel_ids, list):
            target_channel_ids = []
            for target_channel_ids_type_0_item_data in self.target_channel_ids:
                target_channel_ids_type_0_item = str(target_channel_ids_type_0_item_data)
                target_channel_ids.append(target_channel_ids_type_0_item)


        else:
            target_channel_ids = self.target_channel_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if comment is not UNSET:
            field_dict["comment"] = comment
        if target_channel_ids is not UNSET:
            field_dict["targetChannelIds"] = target_channel_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_target_channel_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                target_channel_ids_type_0 = []
                _target_channel_ids_type_0 = data
                for target_channel_ids_type_0_item_data in (_target_channel_ids_type_0):
                    target_channel_ids_type_0_item = UUID(target_channel_ids_type_0_item_data)



                    target_channel_ids_type_0.append(target_channel_ids_type_0_item)

                return target_channel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        target_channel_ids = _parse_target_channel_ids(d.pop("targetChannelIds", UNSET))


        office_chat_controller_forward_message_request = cls(
            comment=comment,
            target_channel_ids=target_channel_ids,
        )

        return office_chat_controller_forward_message_request


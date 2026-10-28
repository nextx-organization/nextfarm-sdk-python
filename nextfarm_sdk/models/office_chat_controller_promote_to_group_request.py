from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerPromoteToGroupRequest")



@_attrs_define
class OfficeChatControllerPromoteToGroupRequest:
    

    member_ids: list[UUID] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    sync_messages: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        member_ids: list[str] | None | Unset
        if isinstance(self.member_ids, Unset):
            member_ids = UNSET
        elif isinstance(self.member_ids, list):
            member_ids = []
            for member_ids_type_0_item_data in self.member_ids:
                member_ids_type_0_item = str(member_ids_type_0_item_data)
                member_ids.append(member_ids_type_0_item)


        else:
            member_ids = self.member_ids

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sync_messages = self.sync_messages


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if member_ids is not UNSET:
            field_dict["memberIds"] = member_ids
        if name is not UNSET:
            field_dict["name"] = name
        if sync_messages is not UNSET:
            field_dict["syncMessages"] = sync_messages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_member_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_ids_type_0 = []
                _member_ids_type_0 = data
                for member_ids_type_0_item_data in (_member_ids_type_0):
                    member_ids_type_0_item = UUID(member_ids_type_0_item_data)



                    member_ids_type_0.append(member_ids_type_0_item)

                return member_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        member_ids = _parse_member_ids(d.pop("memberIds", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        sync_messages = d.pop("syncMessages", UNSET)

        office_chat_controller_promote_to_group_request = cls(
            member_ids=member_ids,
            name=name,
            sync_messages=sync_messages,
        )

        return office_chat_controller_promote_to_group_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerVotePollRequest")



@_attrs_define
class OfficeChatControllerVotePollRequest:
    

    option_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        option_ids: list[str] | None | Unset
        if isinstance(self.option_ids, Unset):
            option_ids = UNSET
        elif isinstance(self.option_ids, list):
            option_ids = []
            for option_ids_type_0_item_data in self.option_ids:
                option_ids_type_0_item = str(option_ids_type_0_item_data)
                option_ids.append(option_ids_type_0_item)


        else:
            option_ids = self.option_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if option_ids is not UNSET:
            field_dict["optionIds"] = option_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_option_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                option_ids_type_0 = []
                _option_ids_type_0 = data
                for option_ids_type_0_item_data in (_option_ids_type_0):
                    option_ids_type_0_item = UUID(option_ids_type_0_item_data)



                    option_ids_type_0.append(option_ids_type_0_item)

                return option_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        option_ids = _parse_option_ids(d.pop("optionIds", UNSET))


        office_chat_controller_vote_poll_request = cls(
            option_ids=option_ids,
        )

        return office_chat_controller_vote_poll_request


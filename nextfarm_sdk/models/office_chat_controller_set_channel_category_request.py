from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerSetChannelCategoryRequest")



@_attrs_define
class OfficeChatControllerSetChannelCategoryRequest:
    

    category_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        elif isinstance(self.category_id, UUID):
            category_id = str(self.category_id)
        else:
            category_id = self.category_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_category_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_id_type_0 = UUID(data)



                return category_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))


        office_chat_controller_set_channel_category_request = cls(
            category_id=category_id,
        )

        return office_chat_controller_set_channel_category_request


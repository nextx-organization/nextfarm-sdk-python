from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerSaveMyTabOrderRequest")



@_attrs_define
class OfficeChatControllerSaveMyTabOrderRequest:
    

    hidden_ids: list[str] | None | Unset = UNSET
    ordered_ids: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hidden_ids: list[str] | None | Unset
        if isinstance(self.hidden_ids, Unset):
            hidden_ids = UNSET
        elif isinstance(self.hidden_ids, list):
            hidden_ids = self.hidden_ids


        else:
            hidden_ids = self.hidden_ids

        ordered_ids: list[str] | None | Unset
        if isinstance(self.ordered_ids, Unset):
            ordered_ids = UNSET
        elif isinstance(self.ordered_ids, list):
            ordered_ids = self.ordered_ids


        else:
            ordered_ids = self.ordered_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if hidden_ids is not UNSET:
            field_dict["hiddenIds"] = hidden_ids
        if ordered_ids is not UNSET:
            field_dict["orderedIds"] = ordered_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_hidden_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hidden_ids_type_0 = cast(list[str], data)

                return hidden_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        hidden_ids = _parse_hidden_ids(d.pop("hiddenIds", UNSET))


        def _parse_ordered_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ordered_ids_type_0 = cast(list[str], data)

                return ordered_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ordered_ids = _parse_ordered_ids(d.pop("orderedIds", UNSET))


        office_chat_controller_save_my_tab_order_request = cls(
            hidden_ids=hidden_ids,
            ordered_ids=ordered_ids,
        )

        return office_chat_controller_save_my_tab_order_request


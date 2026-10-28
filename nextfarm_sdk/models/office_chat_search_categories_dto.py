from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatSearchCategoriesDto")



@_attrs_define
class OfficeChatSearchCategoriesDto:
    

    hidden: list[str] | None | Unset = UNSET
    order: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hidden: list[str] | None | Unset
        if isinstance(self.hidden, Unset):
            hidden = UNSET
        elif isinstance(self.hidden, list):
            hidden = self.hidden


        else:
            hidden = self.hidden

        order: list[str] | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        elif isinstance(self.order, list):
            order = self.order


        else:
            order = self.order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_hidden(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hidden_type_0 = cast(list[str], data)

                return hidden_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        hidden = _parse_hidden(d.pop("hidden", UNSET))


        def _parse_order(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                order_type_0 = cast(list[str], data)

                return order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))


        office_chat_search_categories_dto = cls(
            hidden=hidden,
            order=order,
        )

        return office_chat_search_categories_dto


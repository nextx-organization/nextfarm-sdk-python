from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeNotificationCategoryCountDto")



@_attrs_define
class OfficeNotificationCategoryCountDto:
    

    category: None | str | Unset = UNSET
    total: int | Unset = UNSET
    unread: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        total = self.total

        unread = self.unread


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if total is not UNSET:
            field_dict["total"] = total
        if unread is not UNSET:
            field_dict["unread"] = unread

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        total = d.pop("total", UNSET)

        unread = d.pop("unread", UNSET)

        office_notification_category_count_dto = cls(
            category=category,
            total=total,
            unread=unread,
        )

        return office_notification_category_count_dto


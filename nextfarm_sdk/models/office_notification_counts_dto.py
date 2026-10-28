from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_notification_category_count_dto import OfficeNotificationCategoryCountDto





T = TypeVar("T", bound="OfficeNotificationCountsDto")



@_attrs_define
class OfficeNotificationCountsDto:
    

    categories: list[OfficeNotificationCategoryCountDto] | None | Unset = UNSET
    total: int | Unset = UNSET
    unread: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_notification_category_count_dto import OfficeNotificationCategoryCountDto # noqa: PLC0415
        categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)


        else:
            categories = self.categories

        total = self.total

        unread = self.unread


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if categories is not UNSET:
            field_dict["categories"] = categories
        if total is not UNSET:
            field_dict["total"] = total
        if unread is not UNSET:
            field_dict["unread"] = unread

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_notification_category_count_dto import OfficeNotificationCategoryCountDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_categories(data: object) -> list[OfficeNotificationCategoryCountDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in (_categories_type_0):
                    categories_type_0_item = OfficeNotificationCategoryCountDto.from_dict(categories_type_0_item_data)



                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeNotificationCategoryCountDto] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))


        total = d.pop("total", UNSET)

        unread = d.pop("unread", UNSET)

        office_notification_counts_dto = cls(
            categories=categories,
            total=total,
            unread=unread,
        )

        return office_notification_counts_dto


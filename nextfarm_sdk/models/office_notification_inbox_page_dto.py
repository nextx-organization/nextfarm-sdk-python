from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_notification_inbox_item_dto import OfficeNotificationInboxItemDto





T = TypeVar("T", bound="OfficeNotificationInboxPageDto")



@_attrs_define
class OfficeNotificationInboxPageDto:
    

    has_more: bool | Unset = UNSET
    items: list[OfficeNotificationInboxItemDto] | None | Unset = UNSET
    next_cursor: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_notification_inbox_item_dto import OfficeNotificationInboxItemDto # noqa: PLC0415
        has_more = self.has_more

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if items is not UNSET:
            field_dict["items"] = items
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_notification_inbox_item_dto import OfficeNotificationInboxItemDto # noqa: PLC0415
        d = dict(src_dict)
        has_more = d.pop("hasMore", UNSET)

        def _parse_items(data: object) -> list[OfficeNotificationInboxItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = OfficeNotificationInboxItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeNotificationInboxItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        office_notification_inbox_page_dto = cls(
            has_more=has_more,
            items=items,
            next_cursor=next_cursor,
        )

        return office_notification_inbox_page_dto


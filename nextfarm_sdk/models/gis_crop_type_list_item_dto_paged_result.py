from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_crop_type_list_item_dto import GisCropTypeListItemDto





T = TypeVar("T", bound="GisCropTypeListItemDtoPagedResult")



@_attrs_define
class GisCropTypeListItemDtoPagedResult:
    

    items: list[GisCropTypeListItemDto] | None | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    page_size_capped: bool | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_crop_type_list_item_dto import GisCropTypeListItemDto # noqa: PLC0415
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

        page = self.page

        page_size = self.page_size

        page_size_capped = self.page_size_capped

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if page_size_capped is not UNSET:
            field_dict["page_size_capped"] = page_size_capped
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_crop_type_list_item_dto import GisCropTypeListItemDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[GisCropTypeListItemDto] | None | Unset:
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
                    items_type_0_item = GisCropTypeListItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisCropTypeListItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        page_size_capped = d.pop("page_size_capped", UNSET)

        total = d.pop("total", UNSET)

        gis_crop_type_list_item_dto_paged_result = cls(
            items=items,
            page=page,
            page_size=page_size,
            page_size_capped=page_size_capped,
            total=total,
        )

        return gis_crop_type_list_item_dto_paged_result


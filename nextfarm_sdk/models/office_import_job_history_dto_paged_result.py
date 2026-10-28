from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_import_job_history_dto import OfficeImportJobHistoryDto





T = TypeVar("T", bound="OfficeImportJobHistoryDtoPagedResult")



@_attrs_define
class OfficeImportJobHistoryDtoPagedResult:
    

    has_next_page: bool | Unset = UNSET
    has_previous_page: bool | Unset = UNSET
    items: list[OfficeImportJobHistoryDto] | None | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    total_count: int | Unset = UNSET
    total_pages: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_import_job_history_dto import OfficeImportJobHistoryDto # noqa: PLC0415
        has_next_page = self.has_next_page

        has_previous_page = self.has_previous_page

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

        total_count = self.total_count

        total_pages = self.total_pages


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if has_next_page is not UNSET:
            field_dict["hasNextPage"] = has_next_page
        if has_previous_page is not UNSET:
            field_dict["hasPreviousPage"] = has_previous_page
        if items is not UNSET:
            field_dict["items"] = items
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_import_job_history_dto import OfficeImportJobHistoryDto # noqa: PLC0415
        d = dict(src_dict)
        has_next_page = d.pop("hasNextPage", UNSET)

        has_previous_page = d.pop("hasPreviousPage", UNSET)

        def _parse_items(data: object) -> list[OfficeImportJobHistoryDto] | None | Unset:
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
                    items_type_0_item = OfficeImportJobHistoryDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportJobHistoryDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total_count = d.pop("totalCount", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        office_import_job_history_dto_paged_result = cls(
            has_next_page=has_next_page,
            has_previous_page=has_previous_page,
            items=items,
            page=page,
            page_size=page_size,
            total_count=total_count,
            total_pages=total_pages,
        )

        return office_import_job_history_dto_paged_result


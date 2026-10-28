from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_bulk_approval_item_dto import OfficeBulkApprovalItemDto





T = TypeVar("T", bound="OfficeBulkApprovalResultDto")



@_attrs_define
class OfficeBulkApprovalResultDto:
    

    failed: int | Unset = UNSET
    items: list[OfficeBulkApprovalItemDto] | None | Unset = UNSET
    succeeded: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_bulk_approval_item_dto import OfficeBulkApprovalItemDto # noqa: PLC0415
        failed = self.failed

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

        succeeded = self.succeeded

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if failed is not UNSET:
            field_dict["failed"] = failed
        if items is not UNSET:
            field_dict["items"] = items
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_bulk_approval_item_dto import OfficeBulkApprovalItemDto # noqa: PLC0415
        d = dict(src_dict)
        failed = d.pop("failed", UNSET)

        def _parse_items(data: object) -> list[OfficeBulkApprovalItemDto] | None | Unset:
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
                    items_type_0_item = OfficeBulkApprovalItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeBulkApprovalItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        succeeded = d.pop("succeeded", UNSET)

        total = d.pop("total", UNSET)

        office_bulk_approval_result_dto = cls(
            failed=failed,
            items=items,
            succeeded=succeeded,
            total=total,
        )

        return office_bulk_approval_result_dto


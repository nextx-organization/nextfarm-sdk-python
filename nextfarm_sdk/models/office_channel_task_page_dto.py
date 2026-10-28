from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_channel_task_counts_dto import OfficeChannelTaskCountsDto
  from ..models.office_channel_task_dto import OfficeChannelTaskDto





T = TypeVar("T", bound="OfficeChannelTaskPageDto")



@_attrs_define
class OfficeChannelTaskPageDto:
    

    counts: OfficeChannelTaskCountsDto | Unset = UNSET
    items: list[OfficeChannelTaskDto] | None | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_channel_task_counts_dto import OfficeChannelTaskCountsDto # noqa: PLC0415
        from ..models.office_channel_task_dto import OfficeChannelTaskDto # noqa: PLC0415
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

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

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if counts is not UNSET:
            field_dict["counts"] = counts
        if items is not UNSET:
            field_dict["items"] = items
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_channel_task_counts_dto import OfficeChannelTaskCountsDto # noqa: PLC0415
        from ..models.office_channel_task_dto import OfficeChannelTaskDto # noqa: PLC0415
        d = dict(src_dict)
        _counts = d.pop("counts", UNSET)
        counts: OfficeChannelTaskCountsDto | Unset
        if isinstance(_counts,  Unset):
            counts = UNSET
        else:
            counts = OfficeChannelTaskCountsDto.from_dict(_counts)




        def _parse_items(data: object) -> list[OfficeChannelTaskDto] | None | Unset:
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
                    items_type_0_item = OfficeChannelTaskDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChannelTaskDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        total = d.pop("total", UNSET)

        office_channel_task_page_dto = cls(
            counts=counts,
            items=items,
            total=total,
        )

        return office_channel_task_page_dto


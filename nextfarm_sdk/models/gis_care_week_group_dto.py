from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto





T = TypeVar("T", bound="GisCareWeekGroupDto")



@_attrs_define
class GisCareWeekGroupDto:
    

    items: list[GisCareOccurrenceDto] | None | Unset = UNSET
    week_end: None | str | Unset = UNSET
    week_start: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto # noqa: PLC0415
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

        week_end: None | str | Unset
        if isinstance(self.week_end, Unset):
            week_end = UNSET
        else:
            week_end = self.week_end

        week_start: None | str | Unset
        if isinstance(self.week_start, Unset):
            week_start = UNSET
        else:
            week_start = self.week_start


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if week_end is not UNSET:
            field_dict["week_end"] = week_end
        if week_start is not UNSET:
            field_dict["week_start"] = week_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[GisCareOccurrenceDto] | None | Unset:
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
                    items_type_0_item = GisCareOccurrenceDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisCareOccurrenceDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_week_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        week_end = _parse_week_end(d.pop("week_end", UNSET))


        def _parse_week_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        week_start = _parse_week_start(d.pop("week_start", UNSET))


        gis_care_week_group_dto = cls(
            items=items,
            week_end=week_end,
            week_start=week_start,
        )

        return gis_care_week_group_dto


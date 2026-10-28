from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_timesheet_entry_dto import OfficeTimesheetEntryDto





T = TypeVar("T", bound="OfficeTimesheetEntryListDto")



@_attrs_define
class OfficeTimesheetEntryListDto:
    

    items: list[OfficeTimesheetEntryDto] | None | Unset = UNSET
    scope: None | str | Unset = UNSET
    total_hours: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_timesheet_entry_dto import OfficeTimesheetEntryDto # noqa: PLC0415
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

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        total_hours = self.total_hours


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if scope is not UNSET:
            field_dict["scope"] = scope
        if total_hours is not UNSET:
            field_dict["totalHours"] = total_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_timesheet_entry_dto import OfficeTimesheetEntryDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[OfficeTimesheetEntryDto] | None | Unset:
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
                    items_type_0_item = OfficeTimesheetEntryDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTimesheetEntryDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        total_hours = d.pop("totalHours", UNSET)

        office_timesheet_entry_list_dto = cls(
            items=items,
            scope=scope,
            total_hours=total_hours,
        )

        return office_timesheet_entry_list_dto


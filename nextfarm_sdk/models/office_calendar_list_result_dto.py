from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_calendar_entry_dto import OfficeCalendarEntryDto





T = TypeVar("T", bound="OfficeCalendarListResultDto")



@_attrs_define
class OfficeCalendarListResultDto:
    

    entries: list[OfficeCalendarEntryDto] | None | Unset = UNSET
    truncated: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_calendar_entry_dto import OfficeCalendarEntryDto # noqa: PLC0415
        entries: list[dict[str, Any]] | None | Unset
        if isinstance(self.entries, Unset):
            entries = UNSET
        elif isinstance(self.entries, list):
            entries = []
            for entries_type_0_item_data in self.entries:
                entries_type_0_item = entries_type_0_item_data.to_dict()
                entries.append(entries_type_0_item)


        else:
            entries = self.entries

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entries is not UNSET:
            field_dict["entries"] = entries
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_calendar_entry_dto import OfficeCalendarEntryDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_entries(data: object) -> list[OfficeCalendarEntryDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entries_type_0 = []
                _entries_type_0 = data
                for entries_type_0_item_data in (_entries_type_0):
                    entries_type_0_item = OfficeCalendarEntryDto.from_dict(entries_type_0_item_data)



                    entries_type_0.append(entries_type_0_item)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCalendarEntryDto] | None | Unset, data)

        entries = _parse_entries(d.pop("entries", UNSET))


        truncated = d.pop("truncated", UNSET)

        office_calendar_list_result_dto = cls(
            entries=entries,
            truncated=truncated,
        )

        return office_calendar_list_result_dto


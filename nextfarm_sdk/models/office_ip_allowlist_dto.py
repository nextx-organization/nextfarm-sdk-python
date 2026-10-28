from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_ip_allowlist_entry_dto import OfficeIpAllowlistEntryDto





T = TypeVar("T", bound="OfficeIpAllowlistDto")



@_attrs_define
class OfficeIpAllowlistDto:
    

    enabled: bool | Unset = UNSET
    entries: list[OfficeIpAllowlistEntryDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_ip_allowlist_entry_dto import OfficeIpAllowlistEntryDto # noqa: PLC0415
        enabled = self.enabled

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_ip_allowlist_entry_dto import OfficeIpAllowlistEntryDto # noqa: PLC0415
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_entries(data: object) -> list[OfficeIpAllowlistEntryDto] | None | Unset:
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
                    entries_type_0_item = OfficeIpAllowlistEntryDto.from_dict(entries_type_0_item_data)



                    entries_type_0.append(entries_type_0_item)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeIpAllowlistEntryDto] | None | Unset, data)

        entries = _parse_entries(d.pop("entries", UNSET))


        office_ip_allowlist_dto = cls(
            enabled=enabled,
            entries=entries,
        )

        return office_ip_allowlist_dto


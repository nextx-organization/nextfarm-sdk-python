from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestHarvestSummaryRowDto")



@_attrs_define
class HarvestHarvestSummaryRowDto:
    

    key: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    parcel_count: int | Unset = UNSET
    record_count: int | Unset = UNSET
    total_kg: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        elif isinstance(self.key, UUID):
            key = str(self.key)
        else:
            key = self.key

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parcel_count = self.parcel_count

        record_count = self.record_count

        total_kg = self.total_kg


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_count is not UNSET:
            field_dict["parcel_count"] = parcel_count
        if record_count is not UNSET:
            field_dict["record_count"] = record_count
        if total_kg is not UNSET:
            field_dict["total_kg"] = total_kg

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_key(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                key_type_0 = UUID(data)



                return key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        parcel_count = d.pop("parcel_count", UNSET)

        record_count = d.pop("record_count", UNSET)

        total_kg = d.pop("total_kg", UNSET)

        harvest_harvest_summary_row_dto = cls(
            key=key,
            name=name,
            parcel_count=parcel_count,
            record_count=record_count,
            total_kg=total_kg,
        )

        return harvest_harvest_summary_row_dto


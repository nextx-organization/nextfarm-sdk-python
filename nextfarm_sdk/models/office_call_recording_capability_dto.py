from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeCallRecordingCapabilityDto")



@_attrs_define
class OfficeCallRecordingCapabilityDto:
    

    available: bool | Unset = UNSET
    retention_days: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        available = self.available

        retention_days = self.retention_days


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if available is not UNSET:
            field_dict["available"] = available
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        office_call_recording_capability_dto = cls(
            available=available,
            retention_days=retention_days,
        )

        return office_call_recording_capability_dto


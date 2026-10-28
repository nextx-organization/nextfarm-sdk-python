from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="HarvestTraceSettingsDto")



@_attrs_define
class HarvestTraceSettingsDto:
    

    scan_warn_threshold: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        scan_warn_threshold = self.scan_warn_threshold


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if scan_warn_threshold is not UNSET:
            field_dict["scan_warn_threshold"] = scan_warn_threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scan_warn_threshold = d.pop("scan_warn_threshold", UNSET)

        harvest_trace_settings_dto = cls(
            scan_warn_threshold=scan_warn_threshold,
        )

        return harvest_trace_settings_dto


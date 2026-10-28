from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeAutomationRunStatsDto")



@_attrs_define
class OfficeAutomationRunStatsDto:
    

    failed: int | Unset = UNSET
    skipped: int | Unset = UNSET
    success: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        failed = self.failed

        skipped = self.skipped

        success = self.success

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if failed is not UNSET:
            field_dict["failed"] = failed
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if success is not UNSET:
            field_dict["success"] = success
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed = d.pop("failed", UNSET)

        skipped = d.pop("skipped", UNSET)

        success = d.pop("success", UNSET)

        total = d.pop("total", UNSET)

        office_automation_run_stats_dto = cls(
            failed=failed,
            skipped=skipped,
            success=success,
            total=total,
        )

        return office_automation_run_stats_dto


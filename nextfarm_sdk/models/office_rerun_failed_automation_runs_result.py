from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeRerunFailedAutomationRunsResult")



@_attrs_define
class OfficeRerunFailedAutomationRunsResult:
    

    already_rerun: int | Unset = UNSET
    candidates: int | Unset = UNSET
    refused: int | Unset = UNSET
    remaining: int | Unset = UNSET
    started: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        already_rerun = self.already_rerun

        candidates = self.candidates

        refused = self.refused

        remaining = self.remaining

        started = self.started


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if already_rerun is not UNSET:
            field_dict["alreadyRerun"] = already_rerun
        if candidates is not UNSET:
            field_dict["candidates"] = candidates
        if refused is not UNSET:
            field_dict["refused"] = refused
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if started is not UNSET:
            field_dict["started"] = started

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        already_rerun = d.pop("alreadyRerun", UNSET)

        candidates = d.pop("candidates", UNSET)

        refused = d.pop("refused", UNSET)

        remaining = d.pop("remaining", UNSET)

        started = d.pop("started", UNSET)

        office_rerun_failed_automation_runs_result = cls(
            already_rerun=already_rerun,
            candidates=candidates,
            refused=refused,
            remaining=remaining,
            started=started,
        )

        return office_rerun_failed_automation_runs_result


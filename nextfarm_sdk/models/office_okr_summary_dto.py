from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeOkrSummaryDto")



@_attrs_define
class OfficeOkrSummaryDto:
    

    at_risk_count: int | Unset = UNSET
    expected_progress: int | Unset = UNSET
    key_result_count: int | Unset = UNSET
    metric_key_result_count: int | Unset = UNSET
    objective_count: int | Unset = UNSET
    overall_progress: int | Unset = UNSET
    source_error_key_result_count: int | Unset = UNSET
    stale_key_result_count: int | Unset = UNSET
    watch_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        at_risk_count = self.at_risk_count

        expected_progress = self.expected_progress

        key_result_count = self.key_result_count

        metric_key_result_count = self.metric_key_result_count

        objective_count = self.objective_count

        overall_progress = self.overall_progress

        source_error_key_result_count = self.source_error_key_result_count

        stale_key_result_count = self.stale_key_result_count

        watch_count = self.watch_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if at_risk_count is not UNSET:
            field_dict["atRiskCount"] = at_risk_count
        if expected_progress is not UNSET:
            field_dict["expectedProgress"] = expected_progress
        if key_result_count is not UNSET:
            field_dict["keyResultCount"] = key_result_count
        if metric_key_result_count is not UNSET:
            field_dict["metricKeyResultCount"] = metric_key_result_count
        if objective_count is not UNSET:
            field_dict["objectiveCount"] = objective_count
        if overall_progress is not UNSET:
            field_dict["overallProgress"] = overall_progress
        if source_error_key_result_count is not UNSET:
            field_dict["sourceErrorKeyResultCount"] = source_error_key_result_count
        if stale_key_result_count is not UNSET:
            field_dict["staleKeyResultCount"] = stale_key_result_count
        if watch_count is not UNSET:
            field_dict["watchCount"] = watch_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at_risk_count = d.pop("atRiskCount", UNSET)

        expected_progress = d.pop("expectedProgress", UNSET)

        key_result_count = d.pop("keyResultCount", UNSET)

        metric_key_result_count = d.pop("metricKeyResultCount", UNSET)

        objective_count = d.pop("objectiveCount", UNSET)

        overall_progress = d.pop("overallProgress", UNSET)

        source_error_key_result_count = d.pop("sourceErrorKeyResultCount", UNSET)

        stale_key_result_count = d.pop("staleKeyResultCount", UNSET)

        watch_count = d.pop("watchCount", UNSET)

        office_okr_summary_dto = cls(
            at_risk_count=at_risk_count,
            expected_progress=expected_progress,
            key_result_count=key_result_count,
            metric_key_result_count=metric_key_result_count,
            objective_count=objective_count,
            overall_progress=overall_progress,
            source_error_key_result_count=source_error_key_result_count,
            stale_key_result_count=stale_key_result_count,
            watch_count=watch_count,
        )

        return office_okr_summary_dto


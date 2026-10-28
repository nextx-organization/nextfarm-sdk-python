from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_automation_quota_dto import OfficeAutomationQuotaDto





T = TypeVar("T", bound="OfficeAutomationMetricsDto")



@_attrs_define
class OfficeAutomationMetricsDto:
    

    active_runs: int | Unset = UNSET
    days: int | Unset = UNSET
    due_runs: int | Unset = UNSET
    failed: int | Unset = UNSET
    failure_rate: float | Unset = UNSET
    oldest_due_seconds: int | None | Unset = UNSET
    quota: OfficeAutomationQuotaDto | Unset = UNSET
    quota_blocked: int | Unset = UNSET
    skipped: int | Unset = UNSET
    success: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automation_quota_dto import OfficeAutomationQuotaDto # noqa: PLC0415
        active_runs = self.active_runs

        days = self.days

        due_runs = self.due_runs

        failed = self.failed

        failure_rate = self.failure_rate

        oldest_due_seconds: int | None | Unset
        if isinstance(self.oldest_due_seconds, Unset):
            oldest_due_seconds = UNSET
        else:
            oldest_due_seconds = self.oldest_due_seconds

        quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quota, Unset):
            quota = self.quota.to_dict()

        quota_blocked = self.quota_blocked

        skipped = self.skipped

        success = self.success

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active_runs is not UNSET:
            field_dict["activeRuns"] = active_runs
        if days is not UNSET:
            field_dict["days"] = days
        if due_runs is not UNSET:
            field_dict["dueRuns"] = due_runs
        if failed is not UNSET:
            field_dict["failed"] = failed
        if failure_rate is not UNSET:
            field_dict["failureRate"] = failure_rate
        if oldest_due_seconds is not UNSET:
            field_dict["oldestDueSeconds"] = oldest_due_seconds
        if quota is not UNSET:
            field_dict["quota"] = quota
        if quota_blocked is not UNSET:
            field_dict["quotaBlocked"] = quota_blocked
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if success is not UNSET:
            field_dict["success"] = success
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automation_quota_dto import OfficeAutomationQuotaDto # noqa: PLC0415
        d = dict(src_dict)
        active_runs = d.pop("activeRuns", UNSET)

        days = d.pop("days", UNSET)

        due_runs = d.pop("dueRuns", UNSET)

        failed = d.pop("failed", UNSET)

        failure_rate = d.pop("failureRate", UNSET)

        def _parse_oldest_due_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        oldest_due_seconds = _parse_oldest_due_seconds(d.pop("oldestDueSeconds", UNSET))


        _quota = d.pop("quota", UNSET)
        quota: OfficeAutomationQuotaDto | Unset
        if isinstance(_quota,  Unset):
            quota = UNSET
        else:
            quota = OfficeAutomationQuotaDto.from_dict(_quota)




        quota_blocked = d.pop("quotaBlocked", UNSET)

        skipped = d.pop("skipped", UNSET)

        success = d.pop("success", UNSET)

        total = d.pop("total", UNSET)

        office_automation_metrics_dto = cls(
            active_runs=active_runs,
            days=days,
            due_runs=due_runs,
            failed=failed,
            failure_rate=failure_rate,
            oldest_due_seconds=oldest_due_seconds,
            quota=quota,
            quota_blocked=quota_blocked,
            skipped=skipped,
            success=success,
            total=total,
        )

        return office_automation_metrics_dto


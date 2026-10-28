from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_automation_diagnosis_check_dto import OfficeAutomationDiagnosisCheckDto
  from ..models.office_automation_run_log_dto import OfficeAutomationRunLogDto





T = TypeVar("T", bound="OfficeAutomationDiagnosisDto")



@_attrs_define
class OfficeAutomationDiagnosisDto:
    

    can_run: bool | Unset = UNSET
    checks: list[OfficeAutomationDiagnosisCheckDto] | None | Unset = UNSET
    last_failure: OfficeAutomationRunLogDto | Unset = UNSET
    recent_skips: list[OfficeAutomationRunLogDto] | None | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automation_diagnosis_check_dto import OfficeAutomationDiagnosisCheckDto # noqa: PLC0415
        from ..models.office_automation_run_log_dto import OfficeAutomationRunLogDto # noqa: PLC0415
        can_run = self.can_run

        checks: list[dict[str, Any]] | None | Unset
        if isinstance(self.checks, Unset):
            checks = UNSET
        elif isinstance(self.checks, list):
            checks = []
            for checks_type_0_item_data in self.checks:
                checks_type_0_item = checks_type_0_item_data.to_dict()
                checks.append(checks_type_0_item)


        else:
            checks = self.checks

        last_failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_failure, Unset):
            last_failure = self.last_failure.to_dict()

        recent_skips: list[dict[str, Any]] | None | Unset
        if isinstance(self.recent_skips, Unset):
            recent_skips = UNSET
        elif isinstance(self.recent_skips, list):
            recent_skips = []
            for recent_skips_type_0_item_data in self.recent_skips:
                recent_skips_type_0_item = recent_skips_type_0_item_data.to_dict()
                recent_skips.append(recent_skips_type_0_item)


        else:
            recent_skips = self.recent_skips

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_run is not UNSET:
            field_dict["canRun"] = can_run
        if checks is not UNSET:
            field_dict["checks"] = checks
        if last_failure is not UNSET:
            field_dict["lastFailure"] = last_failure
        if recent_skips is not UNSET:
            field_dict["recentSkips"] = recent_skips
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automation_diagnosis_check_dto import OfficeAutomationDiagnosisCheckDto # noqa: PLC0415
        from ..models.office_automation_run_log_dto import OfficeAutomationRunLogDto # noqa: PLC0415
        d = dict(src_dict)
        can_run = d.pop("canRun", UNSET)

        def _parse_checks(data: object) -> list[OfficeAutomationDiagnosisCheckDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                checks_type_0 = []
                _checks_type_0 = data
                for checks_type_0_item_data in (_checks_type_0):
                    checks_type_0_item = OfficeAutomationDiagnosisCheckDto.from_dict(checks_type_0_item_data)



                    checks_type_0.append(checks_type_0_item)

                return checks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAutomationDiagnosisCheckDto] | None | Unset, data)

        checks = _parse_checks(d.pop("checks", UNSET))


        _last_failure = d.pop("lastFailure", UNSET)
        last_failure: OfficeAutomationRunLogDto | Unset
        if isinstance(_last_failure,  Unset):
            last_failure = UNSET
        else:
            last_failure = OfficeAutomationRunLogDto.from_dict(_last_failure)




        def _parse_recent_skips(data: object) -> list[OfficeAutomationRunLogDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recent_skips_type_0 = []
                _recent_skips_type_0 = data
                for recent_skips_type_0_item_data in (_recent_skips_type_0):
                    recent_skips_type_0_item = OfficeAutomationRunLogDto.from_dict(recent_skips_type_0_item_data)



                    recent_skips_type_0.append(recent_skips_type_0_item)

                return recent_skips_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAutomationRunLogDto] | None | Unset, data)

        recent_skips = _parse_recent_skips(d.pop("recentSkips", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_automation_diagnosis_dto = cls(
            can_run=can_run,
            checks=checks,
            last_failure=last_failure,
            recent_skips=recent_skips,
            status=status,
        )

        return office_automation_diagnosis_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ReportLaborCostFreshness")



@_attrs_define
class ReportLaborCostFreshness:
    

    last_payroll_finalized_at: datetime.datetime | None | Unset = UNSET
    last_piecework_received_at: datetime.datetime | None | Unset = UNSET
    last_season_synced_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        last_payroll_finalized_at: None | str | Unset
        if isinstance(self.last_payroll_finalized_at, Unset):
            last_payroll_finalized_at = UNSET
        elif isinstance(self.last_payroll_finalized_at, datetime.datetime):
            last_payroll_finalized_at = self.last_payroll_finalized_at.isoformat()
        else:
            last_payroll_finalized_at = self.last_payroll_finalized_at

        last_piecework_received_at: None | str | Unset
        if isinstance(self.last_piecework_received_at, Unset):
            last_piecework_received_at = UNSET
        elif isinstance(self.last_piecework_received_at, datetime.datetime):
            last_piecework_received_at = self.last_piecework_received_at.isoformat()
        else:
            last_piecework_received_at = self.last_piecework_received_at

        last_season_synced_at: None | str | Unset
        if isinstance(self.last_season_synced_at, Unset):
            last_season_synced_at = UNSET
        elif isinstance(self.last_season_synced_at, datetime.datetime):
            last_season_synced_at = self.last_season_synced_at.isoformat()
        else:
            last_season_synced_at = self.last_season_synced_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if last_payroll_finalized_at is not UNSET:
            field_dict["lastPayrollFinalizedAt"] = last_payroll_finalized_at
        if last_piecework_received_at is not UNSET:
            field_dict["lastPieceworkReceivedAt"] = last_piecework_received_at
        if last_season_synced_at is not UNSET:
            field_dict["lastSeasonSyncedAt"] = last_season_synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_last_payroll_finalized_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_payroll_finalized_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_payroll_finalized_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_payroll_finalized_at = _parse_last_payroll_finalized_at(d.pop("lastPayrollFinalizedAt", UNSET))


        def _parse_last_piecework_received_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_piecework_received_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_piecework_received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_piecework_received_at = _parse_last_piecework_received_at(d.pop("lastPieceworkReceivedAt", UNSET))


        def _parse_last_season_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_season_synced_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_season_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_season_synced_at = _parse_last_season_synced_at(d.pop("lastSeasonSyncedAt", UNSET))


        report_labor_cost_freshness = cls(
            last_payroll_finalized_at=last_payroll_finalized_at,
            last_piecework_received_at=last_piecework_received_at,
            last_season_synced_at=last_season_synced_at,
        )

        return report_labor_cost_freshness


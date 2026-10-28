from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_timesheet_week_row_dto import OfficeTimesheetWeekRowDto





T = TypeVar("T", bound="OfficeTimesheetWeekDto")



@_attrs_define
class OfficeTimesheetWeekDto:
    

    daily_totals: list[float] | None | Unset = UNSET
    is_editable: bool | Unset = UNSET
    is_working_day: list[bool] | None | Unset = UNSET
    period_id: None | Unset | UUID = UNSET
    period_status: None | str | Unset = UNSET
    rows: list[OfficeTimesheetWeekRowDto] | None | Unset = UNSET
    total: float | Unset = UNSET
    user_id: UUID | Unset = UNSET
    week_end: datetime.date | Unset = UNSET
    week_start: datetime.date | Unset = UNSET
    working_days: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_timesheet_week_row_dto import OfficeTimesheetWeekRowDto # noqa: PLC0415
        daily_totals: list[float] | None | Unset
        if isinstance(self.daily_totals, Unset):
            daily_totals = UNSET
        elif isinstance(self.daily_totals, list):
            daily_totals = self.daily_totals


        else:
            daily_totals = self.daily_totals

        is_editable = self.is_editable

        is_working_day: list[bool] | None | Unset
        if isinstance(self.is_working_day, Unset):
            is_working_day = UNSET
        elif isinstance(self.is_working_day, list):
            is_working_day = self.is_working_day


        else:
            is_working_day = self.is_working_day

        period_id: None | str | Unset
        if isinstance(self.period_id, Unset):
            period_id = UNSET
        elif isinstance(self.period_id, UUID):
            period_id = str(self.period_id)
        else:
            period_id = self.period_id

        period_status: None | str | Unset
        if isinstance(self.period_status, Unset):
            period_status = UNSET
        else:
            period_status = self.period_status

        rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)


        else:
            rows = self.rows

        total = self.total

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        week_end: str | Unset = UNSET
        if not isinstance(self.week_end, Unset):
            week_end = self.week_end.isoformat()

        week_start: str | Unset = UNSET
        if not isinstance(self.week_start, Unset):
            week_start = self.week_start.isoformat()

        working_days = self.working_days


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if daily_totals is not UNSET:
            field_dict["dailyTotals"] = daily_totals
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if is_working_day is not UNSET:
            field_dict["isWorkingDay"] = is_working_day
        if period_id is not UNSET:
            field_dict["periodId"] = period_id
        if period_status is not UNSET:
            field_dict["periodStatus"] = period_status
        if rows is not UNSET:
            field_dict["rows"] = rows
        if total is not UNSET:
            field_dict["total"] = total
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if week_end is not UNSET:
            field_dict["weekEnd"] = week_end
        if week_start is not UNSET:
            field_dict["weekStart"] = week_start
        if working_days is not UNSET:
            field_dict["workingDays"] = working_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_timesheet_week_row_dto import OfficeTimesheetWeekRowDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_daily_totals(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                daily_totals_type_0 = cast(list[float], data)

                return daily_totals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        daily_totals = _parse_daily_totals(d.pop("dailyTotals", UNSET))


        is_editable = d.pop("isEditable", UNSET)

        def _parse_is_working_day(data: object) -> list[bool] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                is_working_day_type_0 = cast(list[bool], data)

                return is_working_day_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool] | None | Unset, data)

        is_working_day = _parse_is_working_day(d.pop("isWorkingDay", UNSET))


        def _parse_period_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_id_type_0 = UUID(data)



                return period_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        period_id = _parse_period_id(d.pop("periodId", UNSET))


        def _parse_period_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_status = _parse_period_status(d.pop("periodStatus", UNSET))


        def _parse_rows(data: object) -> list[OfficeTimesheetWeekRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in (_rows_type_0):
                    rows_type_0_item = OfficeTimesheetWeekRowDto.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTimesheetWeekRowDto] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        total = d.pop("total", UNSET)

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        _week_end = d.pop("weekEnd", UNSET)
        week_end: datetime.date | Unset
        if isinstance(_week_end,  Unset):
            week_end = UNSET
        else:
            week_end = datetime.date.fromisoformat(_week_end)




        _week_start = d.pop("weekStart", UNSET)
        week_start: datetime.date | Unset
        if isinstance(_week_start,  Unset):
            week_start = UNSET
        else:
            week_start = datetime.date.fromisoformat(_week_start)




        working_days = d.pop("workingDays", UNSET)

        office_timesheet_week_dto = cls(
            daily_totals=daily_totals,
            is_editable=is_editable,
            is_working_day=is_working_day,
            period_id=period_id,
            period_status=period_status,
            rows=rows,
            total=total,
            user_id=user_id,
            week_end=week_end,
            week_start=week_start,
            working_days=working_days,
        )

        return office_timesheet_week_dto


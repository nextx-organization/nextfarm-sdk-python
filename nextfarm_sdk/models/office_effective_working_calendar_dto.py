from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeEffectiveWorkingCalendarDto")



@_attrs_define
class OfficeEffectiveWorkingCalendarDto:
    

    covered_years: list[int] | None | Unset = UNSET
    holidays: list[datetime.date] | None | Unset = UNSET
    utc_offset_minutes: int | Unset = UNSET
    weekend_days: list[int] | None | Unset = UNSET
    work_day_start: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        covered_years: list[int] | None | Unset
        if isinstance(self.covered_years, Unset):
            covered_years = UNSET
        elif isinstance(self.covered_years, list):
            covered_years = self.covered_years


        else:
            covered_years = self.covered_years

        holidays: list[str] | None | Unset
        if isinstance(self.holidays, Unset):
            holidays = UNSET
        elif isinstance(self.holidays, list):
            holidays = []
            for holidays_type_0_item_data in self.holidays:
                holidays_type_0_item = holidays_type_0_item_data.isoformat()
                holidays.append(holidays_type_0_item)


        else:
            holidays = self.holidays

        utc_offset_minutes = self.utc_offset_minutes

        weekend_days: list[int] | None | Unset
        if isinstance(self.weekend_days, Unset):
            weekend_days = UNSET
        elif isinstance(self.weekend_days, list):
            weekend_days = self.weekend_days


        else:
            weekend_days = self.weekend_days

        work_day_start = self.work_day_start


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if covered_years is not UNSET:
            field_dict["coveredYears"] = covered_years
        if holidays is not UNSET:
            field_dict["holidays"] = holidays
        if utc_offset_minutes is not UNSET:
            field_dict["utcOffsetMinutes"] = utc_offset_minutes
        if weekend_days is not UNSET:
            field_dict["weekendDays"] = weekend_days
        if work_day_start is not UNSET:
            field_dict["workDayStart"] = work_day_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_covered_years(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                covered_years_type_0 = cast(list[int], data)

                return covered_years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        covered_years = _parse_covered_years(d.pop("coveredYears", UNSET))


        def _parse_holidays(data: object) -> list[datetime.date] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                holidays_type_0 = []
                _holidays_type_0 = data
                for holidays_type_0_item_data in (_holidays_type_0):
                    holidays_type_0_item = datetime.date.fromisoformat(holidays_type_0_item_data)



                    holidays_type_0.append(holidays_type_0_item)

                return holidays_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[datetime.date] | None | Unset, data)

        holidays = _parse_holidays(d.pop("holidays", UNSET))


        utc_offset_minutes = d.pop("utcOffsetMinutes", UNSET)

        def _parse_weekend_days(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weekend_days_type_0 = cast(list[int], data)

                return weekend_days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        weekend_days = _parse_weekend_days(d.pop("weekendDays", UNSET))


        work_day_start = d.pop("workDayStart", UNSET)

        office_effective_working_calendar_dto = cls(
            covered_years=covered_years,
            holidays=holidays,
            utc_offset_minutes=utc_offset_minutes,
            weekend_days=weekend_days,
            work_day_start=work_day_start,
        )

        return office_effective_working_calendar_dto


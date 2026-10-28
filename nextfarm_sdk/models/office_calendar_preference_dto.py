from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeCalendarPreferenceDto")



@_attrs_define
class OfficeCalendarPreferenceDto:
    

    day_end_hour: int | Unset = UNSET
    day_start_hour: int | Unset = UNSET
    default_event_minutes: int | Unset = UNSET
    default_view: None | str | Unset = UNSET
    show_declined: bool | Unset = UNSET
    show_weekends: bool | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    week_start_day: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        day_end_hour = self.day_end_hour

        day_start_hour = self.day_start_hour

        default_event_minutes = self.default_event_minutes

        default_view: None | str | Unset
        if isinstance(self.default_view, Unset):
            default_view = UNSET
        else:
            default_view = self.default_view

        show_declined = self.show_declined

        show_weekends = self.show_weekends

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        week_start_day = self.week_start_day


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if day_end_hour is not UNSET:
            field_dict["dayEndHour"] = day_end_hour
        if day_start_hour is not UNSET:
            field_dict["dayStartHour"] = day_start_hour
        if default_event_minutes is not UNSET:
            field_dict["defaultEventMinutes"] = default_event_minutes
        if default_view is not UNSET:
            field_dict["defaultView"] = default_view
        if show_declined is not UNSET:
            field_dict["showDeclined"] = show_declined
        if show_weekends is not UNSET:
            field_dict["showWeekends"] = show_weekends
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if week_start_day is not UNSET:
            field_dict["weekStartDay"] = week_start_day

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day_end_hour = d.pop("dayEndHour", UNSET)

        day_start_hour = d.pop("dayStartHour", UNSET)

        default_event_minutes = d.pop("defaultEventMinutes", UNSET)

        def _parse_default_view(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_view = _parse_default_view(d.pop("defaultView", UNSET))


        show_declined = d.pop("showDeclined", UNSET)

        show_weekends = d.pop("showWeekends", UNSET)

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))


        week_start_day = d.pop("weekStartDay", UNSET)

        office_calendar_preference_dto = cls(
            day_end_hour=day_end_hour,
            day_start_hour=day_start_hour,
            default_event_minutes=default_event_minutes,
            default_view=default_view,
            show_declined=show_declined,
            show_weekends=show_weekends,
            time_zone=time_zone,
            week_start_day=week_start_day,
        )

        return office_calendar_preference_dto


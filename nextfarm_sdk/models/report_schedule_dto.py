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






T = TypeVar("T", bound="ReportScheduleDto")



@_attrs_define
class ReportScheduleDto:
    

    attach_pdf: bool | Unset = UNSET
    channels: list[str] | None | Unset = UNSET
    code: None | str | Unset = UNSET
    condition: None | str | Unset = UNSET
    created_by: UUID | Unset = UNSET
    frequency: None | str | Unset = UNSET
    hour: int | Unset = UNSET
    id: UUID | Unset = UNSET
    is_active: bool | Unset = UNSET
    last_error: None | str | Unset = UNSET
    last_run_at: datetime.datetime | None | Unset = UNSET
    last_status: None | str | Unset = UNSET
    month_day: int | None | Unset = UNSET
    next_run_at: datetime.datetime | None | Unset = UNSET
    period: None | str | Unset = UNSET
    recipients: list[UUID] | None | Unset = UNSET
    title: None | str | Unset = UNSET
    weekday: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        attach_pdf = self.attach_pdf

        channels: list[str] | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, list):
            channels = self.channels


        else:
            channels = self.channels

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        condition: None | str | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        frequency: None | str | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        hour = self.hour

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_active = self.is_active

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        last_run_at: None | str | Unset
        if isinstance(self.last_run_at, Unset):
            last_run_at = UNSET
        elif isinstance(self.last_run_at, datetime.datetime):
            last_run_at = self.last_run_at.isoformat()
        else:
            last_run_at = self.last_run_at

        last_status: None | str | Unset
        if isinstance(self.last_status, Unset):
            last_status = UNSET
        else:
            last_status = self.last_status

        month_day: int | None | Unset
        if isinstance(self.month_day, Unset):
            month_day = UNSET
        else:
            month_day = self.month_day

        next_run_at: None | str | Unset
        if isinstance(self.next_run_at, Unset):
            next_run_at = UNSET
        elif isinstance(self.next_run_at, datetime.datetime):
            next_run_at = self.next_run_at.isoformat()
        else:
            next_run_at = self.next_run_at

        period: None | str | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        recipients: list[str] | None | Unset
        if isinstance(self.recipients, Unset):
            recipients = UNSET
        elif isinstance(self.recipients, list):
            recipients = []
            for recipients_type_0_item_data in self.recipients:
                recipients_type_0_item = str(recipients_type_0_item_data)
                recipients.append(recipients_type_0_item)


        else:
            recipients = self.recipients

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        weekday: int | None | Unset
        if isinstance(self.weekday, Unset):
            weekday = UNSET
        else:
            weekday = self.weekday


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attach_pdf is not UNSET:
            field_dict["attachPdf"] = attach_pdf
        if channels is not UNSET:
            field_dict["channels"] = channels
        if code is not UNSET:
            field_dict["code"] = code
        if condition is not UNSET:
            field_dict["condition"] = condition
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if hour is not UNSET:
            field_dict["hour"] = hour
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if last_run_at is not UNSET:
            field_dict["lastRunAt"] = last_run_at
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if month_day is not UNSET:
            field_dict["monthDay"] = month_day
        if next_run_at is not UNSET:
            field_dict["nextRunAt"] = next_run_at
        if period is not UNSET:
            field_dict["period"] = period
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if title is not UNSET:
            field_dict["title"] = title
        if weekday is not UNSET:
            field_dict["weekday"] = weekday

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attach_pdf = d.pop("attachPdf", UNSET)

        def _parse_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = cast(list[str], data)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))


        _created_by = d.pop("createdBy", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)




        def _parse_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))


        hour = d.pop("hour", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_active = d.pop("isActive", UNSET)

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))


        def _parse_last_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_at = _parse_last_run_at(d.pop("lastRunAt", UNSET))


        def _parse_last_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_status = _parse_last_status(d.pop("lastStatus", UNSET))


        def _parse_month_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        month_day = _parse_month_day(d.pop("monthDay", UNSET))


        def _parse_next_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_run_at_type_0 = datetime.datetime.fromisoformat(data)



                return next_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_run_at = _parse_next_run_at(d.pop("nextRunAt", UNSET))


        def _parse_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period = _parse_period(d.pop("period", UNSET))


        def _parse_recipients(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipients_type_0 = []
                _recipients_type_0 = data
                for recipients_type_0_item_data in (_recipients_type_0):
                    recipients_type_0_item = UUID(recipients_type_0_item_data)



                    recipients_type_0.append(recipients_type_0_item)

                return recipients_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        recipients = _parse_recipients(d.pop("recipients", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_weekday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weekday = _parse_weekday(d.pop("weekday", UNSET))


        report_schedule_dto = cls(
            attach_pdf=attach_pdf,
            channels=channels,
            code=code,
            condition=condition,
            created_by=created_by,
            frequency=frequency,
            hour=hour,
            id=id,
            is_active=is_active,
            last_error=last_error,
            last_run_at=last_run_at,
            last_status=last_status,
            month_day=month_day,
            next_run_at=next_run_at,
            period=period,
            recipients=recipients,
            title=title,
            weekday=weekday,
        )

        return report_schedule_dto


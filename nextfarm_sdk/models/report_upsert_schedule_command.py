from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ReportUpsertScheduleCommand")



@_attrs_define
class ReportUpsertScheduleCommand:
    

    attach_pdf: bool | Unset = UNSET
    channels: list[str] | None | Unset = UNSET
    code: None | str | Unset = UNSET
    condition: None | str | Unset = UNSET
    frequency: None | str | Unset = UNSET
    hour: int | Unset = UNSET
    id: None | Unset | UUID = UNSET
    month_day: int | None | Unset = UNSET
    period: None | str | Unset = UNSET
    recipients: list[UUID] | None | Unset = UNSET
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

        frequency: None | str | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        hour = self.hour

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        month_day: int | None | Unset
        if isinstance(self.month_day, Unset):
            month_day = UNSET
        else:
            month_day = self.month_day

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
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if hour is not UNSET:
            field_dict["hour"] = hour
        if id is not UNSET:
            field_dict["id"] = id
        if month_day is not UNSET:
            field_dict["monthDay"] = month_day
        if period is not UNSET:
            field_dict["period"] = period
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
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


        def _parse_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))


        hour = d.pop("hour", UNSET)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)



                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_month_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        month_day = _parse_month_day(d.pop("monthDay", UNSET))


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


        def _parse_weekday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weekday = _parse_weekday(d.pop("weekday", UNSET))


        report_upsert_schedule_command = cls(
            attach_pdf=attach_pdf,
            channels=channels,
            code=code,
            condition=condition,
            frequency=frequency,
            hour=hour,
            id=id,
            month_day=month_day,
            period=period,
            recipients=recipients,
            weekday=weekday,
        )

        return report_upsert_schedule_command


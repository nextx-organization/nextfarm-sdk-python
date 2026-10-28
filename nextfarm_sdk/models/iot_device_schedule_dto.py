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






T = TypeVar("T", bound="IotDeviceScheduleDto")



@_attrs_define
class IotDeviceScheduleDto:
    

    device_id: UUID | Unset = UNSET
    duration_minutes: int | None | Unset = UNSET
    duration_seconds: int | None | Unset = UNSET
    enabled: bool | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    family: None | str | Unset = UNSET
    field: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    idx: int | None | Unset = UNSET
    label: None | str | Unset = UNSET
    last_fired_on: datetime.date | None | Unset = UNSET
    name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    stop_mode: None | str | Unset = UNSET
    target_liters: int | None | Unset = UNSET
    time_of_day: str | Unset = UNSET
    value: int | Unset = UNSET
    weekdays: int | Unset = UNSET
    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        duration_minutes: int | None | Unset
        if isinstance(self.duration_minutes, Unset):
            duration_minutes = UNSET
        else:
            duration_minutes = self.duration_minutes

        duration_seconds: int | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        enabled = self.enabled

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        idx: int | None | Unset
        if isinstance(self.idx, Unset):
            idx = UNSET
        else:
            idx = self.idx

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        last_fired_on: None | str | Unset
        if isinstance(self.last_fired_on, Unset):
            last_fired_on = UNSET
        elif isinstance(self.last_fired_on, datetime.date):
            last_fired_on = self.last_fired_on.isoformat()
        else:
            last_fired_on = self.last_fired_on

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        stop_mode: None | str | Unset
        if isinstance(self.stop_mode, Unset):
            stop_mode = UNSET
        else:
            stop_mode = self.stop_mode

        target_liters: int | None | Unset
        if isinstance(self.target_liters, Unset):
            target_liters = UNSET
        else:
            target_liters = self.target_liters

        time_of_day = self.time_of_day

        value = self.value

        weekdays = self.weekdays

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if duration_minutes is not UNSET:
            field_dict["duration_minutes"] = duration_minutes
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if family is not UNSET:
            field_dict["family"] = family
        if field is not UNSET:
            field_dict["field"] = field
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if label is not UNSET:
            field_dict["label"] = label
        if last_fired_on is not UNSET:
            field_dict["last_fired_on"] = last_fired_on
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if stop_mode is not UNSET:
            field_dict["stop_mode"] = stop_mode
        if target_liters is not UNSET:
            field_dict["target_liters"] = target_liters
        if time_of_day is not UNSET:
            field_dict["time_of_day"] = time_of_day
        if value is not UNSET:
            field_dict["value"] = value
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _device_id = d.pop("device_id", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        def _parse_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_minutes = _parse_duration_minutes(d.pop("duration_minutes", UNSET))


        def _parse_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))


        enabled = d.pop("enabled", UNSET)

        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)



                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))


        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))


        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_idx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idx = _parse_idx(d.pop("idx", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_last_fired_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fired_on_type_0 = datetime.date.fromisoformat(data)



                return last_fired_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_fired_on = _parse_last_fired_on(d.pop("last_fired_on", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.date.fromisoformat(data)



                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))


        def _parse_stop_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stop_mode = _parse_stop_mode(d.pop("stop_mode", UNSET))


        def _parse_target_liters(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        target_liters = _parse_target_liters(d.pop("target_liters", UNSET))


        time_of_day = d.pop("time_of_day", UNSET)

        value = d.pop("value", UNSET)

        weekdays = d.pop("weekdays", UNSET)

        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        iot_device_schedule_dto = cls(
            device_id=device_id,
            duration_minutes=duration_minutes,
            duration_seconds=duration_seconds,
            enabled=enabled,
            end_date=end_date,
            family=family,
            field=field,
            id=id,
            idx=idx,
            label=label,
            last_fired_on=last_fired_on,
            name=name,
            note=note,
            start_date=start_date,
            stop_mode=stop_mode,
            target_liters=target_liters,
            time_of_day=time_of_day,
            value=value,
            weekdays=weekdays,
            zone_id=zone_id,
        )

        return iot_device_schedule_dto


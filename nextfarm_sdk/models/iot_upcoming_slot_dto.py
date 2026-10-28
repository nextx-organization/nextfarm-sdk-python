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






T = TypeVar("T", bound="IotUpcomingSlotDto")



@_attrs_define
class IotUpcomingSlotDto:
    

    anchor_schedule_id: UUID | Unset = UNSET
    date: datetime.date | Unset = UNSET
    device_id: UUID | Unset = UNSET
    device_name: None | str | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    exception_id: None | Unset | UUID = UNSET
    fired: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    run_once: bool | Unset = UNSET
    skipped: bool | Unset = UNSET
    time: str | Unset = UNSET
    valves: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        anchor_schedule_id: str | Unset = UNSET
        if not isinstance(self.anchor_schedule_id, Unset):
            anchor_schedule_id = str(self.anchor_schedule_id)

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        duration_seconds = self.duration_seconds

        exception_id: None | str | Unset
        if isinstance(self.exception_id, Unset):
            exception_id = UNSET
        elif isinstance(self.exception_id, UUID):
            exception_id = str(self.exception_id)
        else:
            exception_id = self.exception_id

        fired = self.fired

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        run_once = self.run_once

        skipped = self.skipped

        time = self.time

        valves: list[str] | None | Unset
        if isinstance(self.valves, Unset):
            valves = UNSET
        elif isinstance(self.valves, list):
            valves = self.valves


        else:
            valves = self.valves


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor_schedule_id is not UNSET:
            field_dict["anchor_schedule_id"] = anchor_schedule_id
        if date is not UNSET:
            field_dict["date"] = date
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if exception_id is not UNSET:
            field_dict["exception_id"] = exception_id
        if fired is not UNSET:
            field_dict["fired"] = fired
        if name is not UNSET:
            field_dict["name"] = name
        if run_once is not UNSET:
            field_dict["run_once"] = run_once
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if time is not UNSET:
            field_dict["time"] = time
        if valves is not UNSET:
            field_dict["valves"] = valves

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _anchor_schedule_id = d.pop("anchor_schedule_id", UNSET)
        anchor_schedule_id: UUID | Unset
        if isinstance(_anchor_schedule_id,  Unset):
            anchor_schedule_id = UNSET
        else:
            anchor_schedule_id = UUID(_anchor_schedule_id)




        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)




        _device_id = d.pop("device_id", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("device_name", UNSET))


        duration_seconds = d.pop("duration_seconds", UNSET)

        def _parse_exception_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exception_id_type_0 = UUID(data)



                return exception_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        exception_id = _parse_exception_id(d.pop("exception_id", UNSET))


        fired = d.pop("fired", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        run_once = d.pop("run_once", UNSET)

        skipped = d.pop("skipped", UNSET)

        time = d.pop("time", UNSET)

        def _parse_valves(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                valves_type_0 = cast(list[str], data)

                return valves_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        valves = _parse_valves(d.pop("valves", UNSET))


        iot_upcoming_slot_dto = cls(
            anchor_schedule_id=anchor_schedule_id,
            date=date,
            device_id=device_id,
            device_name=device_name,
            duration_seconds=duration_seconds,
            exception_id=exception_id,
            fired=fired,
            name=name,
            run_once=run_once,
            skipped=skipped,
            time=time,
            valves=valves,
        )

        return iot_upcoming_slot_dto


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






T = TypeVar("T", bound="IotIrrigationLogEntryDto")



@_attrs_define
class IotIrrigationLogEntryDto:
    

    cycle_at: datetime.datetime | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    duration_sec: int | Unset = UNSET
    fert_mask: int | Unset = UNSET
    fert_ml: list[int] | None | Unset = UNSET
    fert_sec: int | Unset = UNSET
    trigger: int | Unset = UNSET
    trigger_source: None | str | Unset = UNSET
    volume_l: float | None | Unset = UNSET
    zone_id: UUID | Unset = UNSET
    zone_mask: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cycle_at: str | Unset = UNSET
        if not isinstance(self.cycle_at, Unset):
            cycle_at = self.cycle_at.isoformat()

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        duration_sec = self.duration_sec

        fert_mask = self.fert_mask

        fert_ml: list[int] | None | Unset
        if isinstance(self.fert_ml, Unset):
            fert_ml = UNSET
        elif isinstance(self.fert_ml, list):
            fert_ml = self.fert_ml


        else:
            fert_ml = self.fert_ml

        fert_sec = self.fert_sec

        trigger = self.trigger

        trigger_source: None | str | Unset
        if isinstance(self.trigger_source, Unset):
            trigger_source = UNSET
        else:
            trigger_source = self.trigger_source

        volume_l: float | None | Unset
        if isinstance(self.volume_l, Unset):
            volume_l = UNSET
        else:
            volume_l = self.volume_l

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)

        zone_mask = self.zone_mask


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cycle_at is not UNSET:
            field_dict["cycle_at"] = cycle_at
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if duration_sec is not UNSET:
            field_dict["duration_sec"] = duration_sec
        if fert_mask is not UNSET:
            field_dict["fert_mask"] = fert_mask
        if fert_ml is not UNSET:
            field_dict["fert_ml"] = fert_ml
        if fert_sec is not UNSET:
            field_dict["fert_sec"] = fert_sec
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if trigger_source is not UNSET:
            field_dict["trigger_source"] = trigger_source
        if volume_l is not UNSET:
            field_dict["volume_l"] = volume_l
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if zone_mask is not UNSET:
            field_dict["zone_mask"] = zone_mask

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _cycle_at = d.pop("cycle_at", UNSET)
        cycle_at: datetime.datetime | Unset
        if isinstance(_cycle_at,  Unset):
            cycle_at = UNSET
        else:
            cycle_at = datetime.datetime.fromisoformat(_cycle_at)




        def _parse_device_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_code = _parse_device_code(d.pop("device_code", UNSET))


        _device_id = d.pop("device_id", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        duration_sec = d.pop("duration_sec", UNSET)

        fert_mask = d.pop("fert_mask", UNSET)

        def _parse_fert_ml(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fert_ml_type_0 = cast(list[int], data)

                return fert_ml_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        fert_ml = _parse_fert_ml(d.pop("fert_ml", UNSET))


        fert_sec = d.pop("fert_sec", UNSET)

        trigger = d.pop("trigger", UNSET)

        def _parse_trigger_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_source = _parse_trigger_source(d.pop("trigger_source", UNSET))


        def _parse_volume_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        volume_l = _parse_volume_l(d.pop("volume_l", UNSET))


        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        zone_mask = d.pop("zone_mask", UNSET)

        iot_irrigation_log_entry_dto = cls(
            cycle_at=cycle_at,
            device_code=device_code,
            device_id=device_id,
            duration_sec=duration_sec,
            fert_mask=fert_mask,
            fert_ml=fert_ml,
            fert_sec=fert_sec,
            trigger=trigger,
            trigger_source=trigger_source,
            volume_l=volume_l,
            zone_id=zone_id,
            zone_mask=zone_mask,
        )

        return iot_irrigation_log_entry_dto


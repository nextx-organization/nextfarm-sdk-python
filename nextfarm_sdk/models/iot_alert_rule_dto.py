from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotAlertRuleDto")



@_attrs_define
class IotAlertRuleDto:
    

    consecutive_breach_count: int | Unset = UNSET
    cooldown_hours: int | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    device_name: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_active: bool | Unset = UNSET
    sensor_type: None | str | Unset = UNSET
    threshold_max: float | None | Unset = UNSET
    threshold_min: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        consecutive_breach_count = self.consecutive_breach_count

        cooldown_hours = self.cooldown_hours

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_active = self.is_active

        sensor_type: None | str | Unset
        if isinstance(self.sensor_type, Unset):
            sensor_type = UNSET
        else:
            sensor_type = self.sensor_type

        threshold_max: float | None | Unset
        if isinstance(self.threshold_max, Unset):
            threshold_max = UNSET
        else:
            threshold_max = self.threshold_max

        threshold_min: float | None | Unset
        if isinstance(self.threshold_min, Unset):
            threshold_min = UNSET
        else:
            threshold_min = self.threshold_min


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if consecutive_breach_count is not UNSET:
            field_dict["consecutive_breach_count"] = consecutive_breach_count
        if cooldown_hours is not UNSET:
            field_dict["cooldown_hours"] = cooldown_hours
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if sensor_type is not UNSET:
            field_dict["sensor_type"] = sensor_type
        if threshold_max is not UNSET:
            field_dict["threshold_max"] = threshold_max
        if threshold_min is not UNSET:
            field_dict["threshold_min"] = threshold_min

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consecutive_breach_count = d.pop("consecutive_breach_count", UNSET)

        cooldown_hours = d.pop("cooldown_hours", UNSET)

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




        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("device_name", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_active = d.pop("is_active", UNSET)

        def _parse_sensor_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sensor_type = _parse_sensor_type(d.pop("sensor_type", UNSET))


        def _parse_threshold_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        threshold_max = _parse_threshold_max(d.pop("threshold_max", UNSET))


        def _parse_threshold_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        threshold_min = _parse_threshold_min(d.pop("threshold_min", UNSET))


        iot_alert_rule_dto = cls(
            consecutive_breach_count=consecutive_breach_count,
            cooldown_hours=cooldown_hours,
            device_code=device_code,
            device_id=device_id,
            device_name=device_name,
            id=id,
            is_active=is_active,
            sensor_type=sensor_type,
            threshold_max=threshold_max,
            threshold_min=threshold_min,
        )

        return iot_alert_rule_dto


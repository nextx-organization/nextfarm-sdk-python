from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotCreateAlertRuleRequest")



@_attrs_define
class IotCreateAlertRuleRequest:
    

    consecutive_breach_count: int | Unset = UNSET
    cooldown_hours: int | Unset = UNSET
    device_id: UUID | Unset = UNSET
    sensor_type: None | str | Unset = UNSET
    threshold_max: float | None | Unset = UNSET
    threshold_min: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        consecutive_breach_count = self.consecutive_breach_count

        cooldown_hours = self.cooldown_hours

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

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
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
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

        _device_id = d.pop("device_id", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




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


        iot_create_alert_rule_request = cls(
            consecutive_breach_count=consecutive_breach_count,
            cooldown_hours=cooldown_hours,
            device_id=device_id,
            sensor_type=sensor_type,
            threshold_max=threshold_max,
            threshold_min=threshold_min,
        )

        return iot_create_alert_rule_request


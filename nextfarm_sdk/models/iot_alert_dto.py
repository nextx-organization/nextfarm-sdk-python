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






T = TypeVar("T", bound="IotAlertDto")



@_attrs_define
class IotAlertDto:
    

    acknowledged_at: datetime.datetime | None | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    rule_id: UUID | Unset = UNSET
    sensor_type: None | str | Unset = UNSET
    severity: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    threshold: None | str | Unset = UNSET
    triggered_at: datetime.datetime | Unset = UNSET
    value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        elif isinstance(self.acknowledged_at, datetime.datetime):
            acknowledged_at = self.acknowledged_at.isoformat()
        else:
            acknowledged_at = self.acknowledged_at

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        rule_id: str | Unset = UNSET
        if not isinstance(self.rule_id, Unset):
            rule_id = str(self.rule_id)

        sensor_type: None | str | Unset
        if isinstance(self.sensor_type, Unset):
            sensor_type = UNSET
        else:
            sensor_type = self.sensor_type

        severity: None | str | Unset
        if isinstance(self.severity, Unset):
            severity = UNSET
        else:
            severity = self.severity

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        threshold: None | str | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        else:
            threshold = self.threshold

        triggered_at: str | Unset = UNSET
        if not isinstance(self.triggered_at, Unset):
            triggered_at = self.triggered_at.isoformat()

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if id is not UNSET:
            field_dict["id"] = id
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id
        if sensor_type is not UNSET:
            field_dict["sensor_type"] = sensor_type
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if triggered_at is not UNSET:
            field_dict["triggered_at"] = triggered_at
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_acknowledged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledged_at_type_0 = datetime.datetime.fromisoformat(data)



                return acknowledged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))


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




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)



                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))


        _rule_id = d.pop("rule_id", UNSET)
        rule_id: UUID | Unset
        if isinstance(_rule_id,  Unset):
            rule_id = UNSET
        else:
            rule_id = UUID(_rule_id)




        def _parse_sensor_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sensor_type = _parse_sensor_type(d.pop("sensor_type", UNSET))


        def _parse_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity = _parse_severity(d.pop("severity", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_threshold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))


        _triggered_at = d.pop("triggered_at", UNSET)
        triggered_at: datetime.datetime | Unset
        if isinstance(_triggered_at,  Unset):
            triggered_at = UNSET
        else:
            triggered_at = datetime.datetime.fromisoformat(_triggered_at)




        value = d.pop("value", UNSET)

        iot_alert_dto = cls(
            acknowledged_at=acknowledged_at,
            device_code=device_code,
            device_id=device_id,
            id=id,
            resolved_at=resolved_at,
            rule_id=rule_id,
            sensor_type=sensor_type,
            severity=severity,
            status=status,
            threshold=threshold,
            triggered_at=triggered_at,
            value=value,
        )

        return iot_alert_dto


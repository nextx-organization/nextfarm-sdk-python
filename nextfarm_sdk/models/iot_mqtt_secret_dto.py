from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotMqttSecretDto")



@_attrs_define
class IotMqttSecretDto:
    

    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    mqtt_secret: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        mqtt_secret: None | str | Unset
        if isinstance(self.mqtt_secret, Unset):
            mqtt_secret = UNSET
        else:
            mqtt_secret = self.mqtt_secret


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if mqtt_secret is not UNSET:
            field_dict["mqtt_secret"] = mqtt_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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




        def _parse_mqtt_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mqtt_secret = _parse_mqtt_secret(d.pop("mqtt_secret", UNSET))


        iot_mqtt_secret_dto = cls(
            device_code=device_code,
            device_id=device_id,
            mqtt_secret=mqtt_secret,
        )

        return iot_mqtt_secret_dto


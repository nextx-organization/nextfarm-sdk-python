from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotSendDeviceCommandRequest")



@_attrs_define
class IotSendDeviceCommandRequest:
    

    command_type: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    payload: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        command_type: None | str | Unset
        if isinstance(self.command_type, Unset):
            command_type = UNSET
        else:
            command_type = self.command_type

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if command_type is not UNSET:
            field_dict["command_type"] = command_type
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_command_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command_type = _parse_command_type(d.pop("command_type", UNSET))


        _device_id = d.pop("device_id", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))


        iot_send_device_command_request = cls(
            command_type=command_type,
            device_id=device_id,
            payload=payload,
        )

        return iot_send_device_command_request


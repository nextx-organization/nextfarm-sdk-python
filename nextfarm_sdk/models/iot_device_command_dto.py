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






T = TypeVar("T", bound="IotDeviceCommandDto")



@_attrs_define
class IotDeviceCommandDto:
    

    acknowledged_at: datetime.datetime | None | Unset = UNSET
    command_type: None | str | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    payload: None | str | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    sent_by_user_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        elif isinstance(self.acknowledged_at, datetime.datetime):
            acknowledged_at = self.acknowledged_at.isoformat()
        else:
            acknowledged_at = self.acknowledged_at

        command_type: None | str | Unset
        if isinstance(self.command_type, Unset):
            command_type = UNSET
        else:
            command_type = self.command_type

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

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        sent_by_user_id: str | Unset = UNSET
        if not isinstance(self.sent_by_user_id, Unset):
            sent_by_user_id = str(self.sent_by_user_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if command_type is not UNSET:
            field_dict["command_type"] = command_type
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if id is not UNSET:
            field_dict["id"] = id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if sent_by_user_id is not UNSET:
            field_dict["sent_by_user_id"] = sent_by_user_id
        if status is not UNSET:
            field_dict["status"] = status

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


        def _parse_command_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command_type = _parse_command_type(d.pop("command_type", UNSET))


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




        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))


        _sent_at = d.pop("sent_at", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at,  Unset):
            sent_at = UNSET
        else:
            sent_at = datetime.datetime.fromisoformat(_sent_at)




        _sent_by_user_id = d.pop("sent_by_user_id", UNSET)
        sent_by_user_id: UUID | Unset
        if isinstance(_sent_by_user_id,  Unset):
            sent_by_user_id = UNSET
        else:
            sent_by_user_id = UUID(_sent_by_user_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        iot_device_command_dto = cls(
            acknowledged_at=acknowledged_at,
            command_type=command_type,
            device_code=device_code,
            device_id=device_id,
            id=id,
            payload=payload,
            sent_at=sent_at,
            sent_by_user_id=sent_by_user_id,
            status=status,
        )

        return iot_device_command_dto


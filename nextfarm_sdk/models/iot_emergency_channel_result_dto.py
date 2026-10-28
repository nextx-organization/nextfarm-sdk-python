from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotEmergencyChannelResultDto")



@_attrs_define
class IotEmergencyChannelResultDto:
    

    command_id: None | Unset | UUID = UNSET
    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    error: None | str | Unset = UNSET
    error_code: None | str | Unset = UNSET
    family: None | str | Unset = UNSET
    idx: int | Unset = UNSET
    label: None | str | Unset = UNSET
    ok: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        command_id: None | str | Unset
        if isinstance(self.command_id, Unset):
            command_id = UNSET
        elif isinstance(self.command_id, UUID):
            command_id = str(self.command_id)
        else:
            command_id = self.command_id

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        idx = self.idx

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if command_id is not UNSET:
            field_dict["command_id"] = command_id
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if error is not UNSET:
            field_dict["error"] = error
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if family is not UNSET:
            field_dict["family"] = family
        if idx is not UNSET:
            field_dict["idx"] = idx
        if label is not UNSET:
            field_dict["label"] = label
        if ok is not UNSET:
            field_dict["ok"] = ok

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_command_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                command_id_type_0 = UUID(data)



                return command_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        command_id = _parse_command_id(d.pop("command_id", UNSET))


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




        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))


        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))


        idx = d.pop("idx", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        ok = d.pop("ok", UNSET)

        iot_emergency_channel_result_dto = cls(
            command_id=command_id,
            device_code=device_code,
            device_id=device_id,
            error=error,
            error_code=error_code,
            family=family,
            idx=idx,
            label=label,
            ok=ok,
        )

        return iot_emergency_channel_result_dto


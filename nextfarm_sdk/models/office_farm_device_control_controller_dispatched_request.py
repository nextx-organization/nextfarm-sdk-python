from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeFarmDeviceControlControllerDispatchedRequest")



@_attrs_define
class OfficeFarmDeviceControlControllerDispatchedRequest:
    

    iot_command_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        iot_command_id: None | str | Unset
        if isinstance(self.iot_command_id, Unset):
            iot_command_id = UNSET
        elif isinstance(self.iot_command_id, UUID):
            iot_command_id = str(self.iot_command_id)
        else:
            iot_command_id = self.iot_command_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if iot_command_id is not UNSET:
            field_dict["iotCommandId"] = iot_command_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_iot_command_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                iot_command_id_type_0 = UUID(data)



                return iot_command_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        iot_command_id = _parse_iot_command_id(d.pop("iotCommandId", UNSET))


        office_farm_device_control_controller_dispatched_request = cls(
            iot_command_id=iot_command_id,
        )

        return office_farm_device_control_controller_dispatched_request


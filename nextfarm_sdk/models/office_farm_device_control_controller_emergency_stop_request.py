from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeFarmDeviceControlControllerEmergencyStopRequest")



@_attrs_define
class OfficeFarmDeviceControlControllerEmergencyStopRequest:
    

    stopped: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        stopped = self.stopped


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if stopped is not UNSET:
            field_dict["stopped"] = stopped

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stopped = d.pop("stopped", UNSET)

        office_farm_device_control_controller_emergency_stop_request = cls(
            stopped=stopped,
        )

        return office_farm_device_control_controller_emergency_stop_request


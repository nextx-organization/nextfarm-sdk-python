from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotSaveDeviceDisplayPrefsRequest")



@_attrs_define
class IotSaveDeviceDisplayPrefsRequest:
    

    control_sensors: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        control_sensors: list[str] | None | Unset
        if isinstance(self.control_sensors, Unset):
            control_sensors = UNSET
        elif isinstance(self.control_sensors, list):
            control_sensors = self.control_sensors


        else:
            control_sensors = self.control_sensors


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if control_sensors is not UNSET:
            field_dict["control_sensors"] = control_sensors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_control_sensors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_sensors_type_0 = cast(list[str], data)

                return control_sensors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        control_sensors = _parse_control_sensors(d.pop("control_sensors", UNSET))


        iot_save_device_display_prefs_request = cls(
            control_sensors=control_sensors,
        )

        return iot_save_device_display_prefs_request


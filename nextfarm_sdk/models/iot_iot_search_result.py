from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.iot_spotlight_hit import IotSpotlightHit





T = TypeVar("T", bound="IotIotSearchResult")



@_attrs_define
class IotIotSearchResult:
    

    devices: list[IotSpotlightHit] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_spotlight_hit import IotSpotlightHit # noqa: PLC0415
        devices: list[dict[str, Any]] | None | Unset
        if isinstance(self.devices, Unset):
            devices = UNSET
        elif isinstance(self.devices, list):
            devices = []
            for devices_type_0_item_data in self.devices:
                devices_type_0_item = devices_type_0_item_data.to_dict()
                devices.append(devices_type_0_item)


        else:
            devices = self.devices


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_spotlight_hit import IotSpotlightHit # noqa: PLC0415
        d = dict(src_dict)
        def _parse_devices(data: object) -> list[IotSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                devices_type_0 = []
                _devices_type_0 = data
                for devices_type_0_item_data in (_devices_type_0):
                    devices_type_0_item = IotSpotlightHit.from_dict(devices_type_0_item_data)



                    devices_type_0.append(devices_type_0_item)

                return devices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IotSpotlightHit] | None | Unset, data)

        devices = _parse_devices(d.pop("devices", UNSET))


        iot_iot_search_result = cls(
            devices=devices,
        )

        return iot_iot_search_result


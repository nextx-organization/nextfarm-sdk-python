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






T = TypeVar("T", bound="IotResolveAlertsBulkRequest")



@_attrs_define
class IotResolveAlertsBulkRequest:
    

    device_ids: list[UUID] | None | Unset = UNSET
    note: None | str | Unset = UNSET
    sensor_type: None | str | Unset = UNSET
    triggered_before: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        device_ids: list[str] | None | Unset
        if isinstance(self.device_ids, Unset):
            device_ids = UNSET
        elif isinstance(self.device_ids, list):
            device_ids = []
            for device_ids_type_0_item_data in self.device_ids:
                device_ids_type_0_item = str(device_ids_type_0_item_data)
                device_ids.append(device_ids_type_0_item)


        else:
            device_ids = self.device_ids

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        sensor_type: None | str | Unset
        if isinstance(self.sensor_type, Unset):
            sensor_type = UNSET
        else:
            sensor_type = self.sensor_type

        triggered_before: str | Unset = UNSET
        if not isinstance(self.triggered_before, Unset):
            triggered_before = self.triggered_before.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if device_ids is not UNSET:
            field_dict["device_ids"] = device_ids
        if note is not UNSET:
            field_dict["note"] = note
        if sensor_type is not UNSET:
            field_dict["sensor_type"] = sensor_type
        if triggered_before is not UNSET:
            field_dict["triggered_before"] = triggered_before

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_device_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                device_ids_type_0 = []
                _device_ids_type_0 = data
                for device_ids_type_0_item_data in (_device_ids_type_0):
                    device_ids_type_0_item = UUID(device_ids_type_0_item_data)



                    device_ids_type_0.append(device_ids_type_0_item)

                return device_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        device_ids = _parse_device_ids(d.pop("device_ids", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_sensor_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sensor_type = _parse_sensor_type(d.pop("sensor_type", UNSET))


        _triggered_before = d.pop("triggered_before", UNSET)
        triggered_before: datetime.datetime | Unset
        if isinstance(_triggered_before,  Unset):
            triggered_before = UNSET
        else:
            triggered_before = datetime.datetime.fromisoformat(_triggered_before)




        iot_resolve_alerts_bulk_request = cls(
            device_ids=device_ids,
            note=note,
            sensor_type=sensor_type,
            triggered_before=triggered_before,
        )

        return iot_resolve_alerts_bulk_request


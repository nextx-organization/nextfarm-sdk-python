from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotRegisterDeviceRequest")



@_attrs_define
class IotRegisterDeviceRequest:
    

    customer_code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_type: None | str | Unset = UNSET
    location_lat: float | None | Unset = UNSET
    location_lng: float | None | Unset = UNSET
    mac_address: None | str | Unset = UNSET
    mcv_valve_variant: None | str | Unset = UNSET
    metadata_json: None | str | Unset = UNSET
    mqtt_topic_prefix: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    parcel_ids: list[UUID] | None | Unset = UNSET
    shared_in_zone: bool | Unset = UNSET
    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        customer_code: None | str | Unset
        if isinstance(self.customer_code, Unset):
            customer_code = UNSET
        else:
            customer_code = self.customer_code

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_type: None | str | Unset
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        else:
            device_type = self.device_type

        location_lat: float | None | Unset
        if isinstance(self.location_lat, Unset):
            location_lat = UNSET
        else:
            location_lat = self.location_lat

        location_lng: float | None | Unset
        if isinstance(self.location_lng, Unset):
            location_lng = UNSET
        else:
            location_lng = self.location_lng

        mac_address: None | str | Unset
        if isinstance(self.mac_address, Unset):
            mac_address = UNSET
        else:
            mac_address = self.mac_address

        mcv_valve_variant: None | str | Unset
        if isinstance(self.mcv_valve_variant, Unset):
            mcv_valve_variant = UNSET
        else:
            mcv_valve_variant = self.mcv_valve_variant

        metadata_json: None | str | Unset
        if isinstance(self.metadata_json, Unset):
            metadata_json = UNSET
        else:
            metadata_json = self.metadata_json

        mqtt_topic_prefix: None | str | Unset
        if isinstance(self.mqtt_topic_prefix, Unset):
            mqtt_topic_prefix = UNSET
        else:
            mqtt_topic_prefix = self.mqtt_topic_prefix

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parcel_ids: list[str] | None | Unset
        if isinstance(self.parcel_ids, Unset):
            parcel_ids = UNSET
        elif isinstance(self.parcel_ids, list):
            parcel_ids = []
            for parcel_ids_type_0_item_data in self.parcel_ids:
                parcel_ids_type_0_item = str(parcel_ids_type_0_item_data)
                parcel_ids.append(parcel_ids_type_0_item)


        else:
            parcel_ids = self.parcel_ids

        shared_in_zone = self.shared_in_zone

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if customer_code is not UNSET:
            field_dict["customer_code"] = customer_code
        if description is not UNSET:
            field_dict["description"] = description
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if location_lat is not UNSET:
            field_dict["location_lat"] = location_lat
        if location_lng is not UNSET:
            field_dict["location_lng"] = location_lng
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if mcv_valve_variant is not UNSET:
            field_dict["mcv_valve_variant"] = mcv_valve_variant
        if metadata_json is not UNSET:
            field_dict["metadata_json"] = metadata_json
        if mqtt_topic_prefix is not UNSET:
            field_dict["mqtt_topic_prefix"] = mqtt_topic_prefix
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_ids is not UNSET:
            field_dict["parcel_ids"] = parcel_ids
        if shared_in_zone is not UNSET:
            field_dict["shared_in_zone"] = shared_in_zone
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_customer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_code = _parse_customer_code(d.pop("customer_code", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_device_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_code = _parse_device_code(d.pop("device_code", UNSET))


        def _parse_device_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_type = _parse_device_type(d.pop("device_type", UNSET))


        def _parse_location_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        location_lat = _parse_location_lat(d.pop("location_lat", UNSET))


        def _parse_location_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        location_lng = _parse_location_lng(d.pop("location_lng", UNSET))


        def _parse_mac_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mac_address = _parse_mac_address(d.pop("mac_address", UNSET))


        def _parse_mcv_valve_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcv_valve_variant = _parse_mcv_valve_variant(d.pop("mcv_valve_variant", UNSET))


        def _parse_metadata_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_json = _parse_metadata_json(d.pop("metadata_json", UNSET))


        def _parse_mqtt_topic_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mqtt_topic_prefix = _parse_mqtt_topic_prefix(d.pop("mqtt_topic_prefix", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_parcel_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parcel_ids_type_0 = []
                _parcel_ids_type_0 = data
                for parcel_ids_type_0_item_data in (_parcel_ids_type_0):
                    parcel_ids_type_0_item = UUID(parcel_ids_type_0_item_data)



                    parcel_ids_type_0.append(parcel_ids_type_0_item)

                return parcel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        parcel_ids = _parse_parcel_ids(d.pop("parcel_ids", UNSET))


        shared_in_zone = d.pop("shared_in_zone", UNSET)

        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        iot_register_device_request = cls(
            customer_code=customer_code,
            description=description,
            device_code=device_code,
            device_type=device_type,
            location_lat=location_lat,
            location_lng=location_lng,
            mac_address=mac_address,
            mcv_valve_variant=mcv_valve_variant,
            metadata_json=metadata_json,
            mqtt_topic_prefix=mqtt_topic_prefix,
            name=name,
            parcel_ids=parcel_ids,
            shared_in_zone=shared_in_zone,
            zone_id=zone_id,
        )

        return iot_register_device_request


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






T = TypeVar("T", bound="IotDeviceDetailDto")



@_attrs_define
class IotDeviceDetailDto:
    

    created_at: datetime.datetime | Unset = UNSET
    customer_code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_type: None | str | Unset = UNSET
    dong_ho_nuoc: None | str | Unset = UNSET
    firmware_version: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    installed_at: datetime.date | None | Unset = UNSET
    is_online: bool | Unset = UNSET
    last_heartbeat: datetime.datetime | None | Unset = UNSET
    location_lat: float | None | Unset = UNSET
    location_lng: float | None | Unset = UNSET
    mac_address: None | str | Unset = UNSET
    manual_max_min: int | Unset = UNSET
    mcv_valve_variant: None | str | Unset = UNSET
    metadata_json: None | str | Unset = UNSET
    mqtt_topic_prefix: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    niche: None | str | Unset = UNSET
    parcel_ids: list[UUID] | None | Unset = UNSET
    provision_status: None | str | Unset = UNSET
    provisioned_at: datetime.datetime | None | Unset = UNSET
    scene_kind: None | str | Unset = UNSET
    shared_in_zone: bool | Unset = UNSET
    status: None | str | Unset = UNSET
    tran_thoi_luong: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

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

        dong_ho_nuoc: None | str | Unset
        if isinstance(self.dong_ho_nuoc, Unset):
            dong_ho_nuoc = UNSET
        else:
            dong_ho_nuoc = self.dong_ho_nuoc

        firmware_version: None | str | Unset
        if isinstance(self.firmware_version, Unset):
            firmware_version = UNSET
        else:
            firmware_version = self.firmware_version

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        installed_at: None | str | Unset
        if isinstance(self.installed_at, Unset):
            installed_at = UNSET
        elif isinstance(self.installed_at, datetime.date):
            installed_at = self.installed_at.isoformat()
        else:
            installed_at = self.installed_at

        is_online = self.is_online

        last_heartbeat: None | str | Unset
        if isinstance(self.last_heartbeat, Unset):
            last_heartbeat = UNSET
        elif isinstance(self.last_heartbeat, datetime.datetime):
            last_heartbeat = self.last_heartbeat.isoformat()
        else:
            last_heartbeat = self.last_heartbeat

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

        manual_max_min = self.manual_max_min

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

        niche: None | str | Unset
        if isinstance(self.niche, Unset):
            niche = UNSET
        else:
            niche = self.niche

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

        provision_status: None | str | Unset
        if isinstance(self.provision_status, Unset):
            provision_status = UNSET
        else:
            provision_status = self.provision_status

        provisioned_at: None | str | Unset
        if isinstance(self.provisioned_at, Unset):
            provisioned_at = UNSET
        elif isinstance(self.provisioned_at, datetime.datetime):
            provisioned_at = self.provisioned_at.isoformat()
        else:
            provisioned_at = self.provisioned_at

        scene_kind: None | str | Unset
        if isinstance(self.scene_kind, Unset):
            scene_kind = UNSET
        else:
            scene_kind = self.scene_kind

        shared_in_zone = self.shared_in_zone

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        tran_thoi_luong: None | str | Unset
        if isinstance(self.tran_thoi_luong, Unset):
            tran_thoi_luong = UNSET
        else:
            tran_thoi_luong = self.tran_thoi_luong

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if customer_code is not UNSET:
            field_dict["customer_code"] = customer_code
        if description is not UNSET:
            field_dict["description"] = description
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if dong_ho_nuoc is not UNSET:
            field_dict["dong_ho_nuoc"] = dong_ho_nuoc
        if firmware_version is not UNSET:
            field_dict["firmware_version"] = firmware_version
        if id is not UNSET:
            field_dict["id"] = id
        if installed_at is not UNSET:
            field_dict["installed_at"] = installed_at
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if last_heartbeat is not UNSET:
            field_dict["last_heartbeat"] = last_heartbeat
        if location_lat is not UNSET:
            field_dict["location_lat"] = location_lat
        if location_lng is not UNSET:
            field_dict["location_lng"] = location_lng
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if manual_max_min is not UNSET:
            field_dict["manual_max_min"] = manual_max_min
        if mcv_valve_variant is not UNSET:
            field_dict["mcv_valve_variant"] = mcv_valve_variant
        if metadata_json is not UNSET:
            field_dict["metadata_json"] = metadata_json
        if mqtt_topic_prefix is not UNSET:
            field_dict["mqtt_topic_prefix"] = mqtt_topic_prefix
        if name is not UNSET:
            field_dict["name"] = name
        if niche is not UNSET:
            field_dict["niche"] = niche
        if parcel_ids is not UNSET:
            field_dict["parcel_ids"] = parcel_ids
        if provision_status is not UNSET:
            field_dict["provision_status"] = provision_status
        if provisioned_at is not UNSET:
            field_dict["provisioned_at"] = provisioned_at
        if scene_kind is not UNSET:
            field_dict["scene_kind"] = scene_kind
        if shared_in_zone is not UNSET:
            field_dict["shared_in_zone"] = shared_in_zone
        if status is not UNSET:
            field_dict["status"] = status
        if tran_thoi_luong is not UNSET:
            field_dict["tran_thoi_luong"] = tran_thoi_luong
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




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


        def _parse_dong_ho_nuoc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dong_ho_nuoc = _parse_dong_ho_nuoc(d.pop("dong_ho_nuoc", UNSET))


        def _parse_firmware_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        firmware_version = _parse_firmware_version(d.pop("firmware_version", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_installed_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                installed_at_type_0 = datetime.date.fromisoformat(data)



                return installed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        installed_at = _parse_installed_at(d.pop("installed_at", UNSET))


        is_online = d.pop("is_online", UNSET)

        def _parse_last_heartbeat(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_heartbeat_type_0 = datetime.datetime.fromisoformat(data)



                return last_heartbeat_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_heartbeat = _parse_last_heartbeat(d.pop("last_heartbeat", UNSET))


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


        manual_max_min = d.pop("manual_max_min", UNSET)

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


        def _parse_niche(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        niche = _parse_niche(d.pop("niche", UNSET))


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


        def _parse_provision_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provision_status = _parse_provision_status(d.pop("provision_status", UNSET))


        def _parse_provisioned_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provisioned_at_type_0 = datetime.datetime.fromisoformat(data)



                return provisioned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        provisioned_at = _parse_provisioned_at(d.pop("provisioned_at", UNSET))


        def _parse_scene_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scene_kind = _parse_scene_kind(d.pop("scene_kind", UNSET))


        shared_in_zone = d.pop("shared_in_zone", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_tran_thoi_luong(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tran_thoi_luong = _parse_tran_thoi_luong(d.pop("tran_thoi_luong", UNSET))


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        iot_device_detail_dto = cls(
            created_at=created_at,
            customer_code=customer_code,
            description=description,
            device_code=device_code,
            device_type=device_type,
            dong_ho_nuoc=dong_ho_nuoc,
            firmware_version=firmware_version,
            id=id,
            installed_at=installed_at,
            is_online=is_online,
            last_heartbeat=last_heartbeat,
            location_lat=location_lat,
            location_lng=location_lng,
            mac_address=mac_address,
            manual_max_min=manual_max_min,
            mcv_valve_variant=mcv_valve_variant,
            metadata_json=metadata_json,
            mqtt_topic_prefix=mqtt_topic_prefix,
            name=name,
            niche=niche,
            parcel_ids=parcel_ids,
            provision_status=provision_status,
            provisioned_at=provisioned_at,
            scene_kind=scene_kind,
            shared_in_zone=shared_in_zone,
            status=status,
            tran_thoi_luong=tran_thoi_luong,
            updated_at=updated_at,
            zone_id=zone_id,
        )

        return iot_device_detail_dto


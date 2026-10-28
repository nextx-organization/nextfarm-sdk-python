from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotUpdateDeviceRequest")



@_attrs_define
class IotUpdateDeviceRequest:
    

    description: None | str | Unset = UNSET
    dong_ho_nuoc: None | str | Unset = UNSET
    firmware_version: None | str | Unset = UNSET
    mcv_valve_variant: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    niche: None | str | Unset = UNSET
    scene_kind: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        mcv_valve_variant: None | str | Unset
        if isinstance(self.mcv_valve_variant, Unset):
            mcv_valve_variant = UNSET
        else:
            mcv_valve_variant = self.mcv_valve_variant

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

        scene_kind: None | str | Unset
        if isinstance(self.scene_kind, Unset):
            scene_kind = UNSET
        else:
            scene_kind = self.scene_kind


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if dong_ho_nuoc is not UNSET:
            field_dict["dong_ho_nuoc"] = dong_ho_nuoc
        if firmware_version is not UNSET:
            field_dict["firmware_version"] = firmware_version
        if mcv_valve_variant is not UNSET:
            field_dict["mcv_valve_variant"] = mcv_valve_variant
        if name is not UNSET:
            field_dict["name"] = name
        if niche is not UNSET:
            field_dict["niche"] = niche
        if scene_kind is not UNSET:
            field_dict["scene_kind"] = scene_kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


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


        def _parse_mcv_valve_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcv_valve_variant = _parse_mcv_valve_variant(d.pop("mcv_valve_variant", UNSET))


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


        def _parse_scene_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scene_kind = _parse_scene_kind(d.pop("scene_kind", UNSET))


        iot_update_device_request = cls(
            description=description,
            dong_ho_nuoc=dong_ho_nuoc,
            firmware_version=firmware_version,
            mcv_valve_variant=mcv_valve_variant,
            name=name,
            niche=niche,
            scene_kind=scene_kind,
        )

        return iot_update_device_request


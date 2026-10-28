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






T = TypeVar("T", bound="GisCreateLayerRequest")



@_attrs_define
class GisCreateLayerRequest:
    

    captured_at: datetime.date | None | Unset = UNSET
    layer_type: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    style_config: None | str | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        captured_at: None | str | Unset
        if isinstance(self.captured_at, Unset):
            captured_at = UNSET
        elif isinstance(self.captured_at, datetime.date):
            captured_at = self.captured_at.isoformat()
        else:
            captured_at = self.captured_at

        layer_type: None | str | Unset
        if isinstance(self.layer_type, Unset):
            layer_type = UNSET
        else:
            layer_type = self.layer_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        style_config: None | str | Unset
        if isinstance(self.style_config, Unset):
            style_config = UNSET
        else:
            style_config = self.style_config

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if captured_at is not UNSET:
            field_dict["captured_at"] = captured_at
        if layer_type is not UNSET:
            field_dict["layer_type"] = layer_type
        if name is not UNSET:
            field_dict["name"] = name
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if style_config is not UNSET:
            field_dict["style_config"] = style_config
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_captured_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                captured_at_type_0 = datetime.date.fromisoformat(data)



                return captured_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        captured_at = _parse_captured_at(d.pop("captured_at", UNSET))


        def _parse_layer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layer_type = _parse_layer_type(d.pop("layer_type", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))


        def _parse_style_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        style_config = _parse_style_config(d.pop("style_config", UNSET))


        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)



                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zone_id", UNSET))


        gis_create_layer_request = cls(
            captured_at=captured_at,
            layer_type=layer_type,
            name=name,
            source_url=source_url,
            style_config=style_config,
            zone_id=zone_id,
        )

        return gis_create_layer_request


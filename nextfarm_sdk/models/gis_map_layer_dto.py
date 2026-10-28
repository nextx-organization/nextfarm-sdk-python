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






T = TypeVar("T", bound="GisMapLayerDto")



@_attrs_define
class GisMapLayerDto:
    

    captured_at: datetime.date | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    file_path: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    layer_type: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    ndvi_avg: float | None | Unset = UNSET
    ndvi_max: float | None | Unset = UNSET
    ndvi_min: float | None | Unset = UNSET
    source_url: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    style_config: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET
    zone_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        captured_at: None | str | Unset
        if isinstance(self.captured_at, Unset):
            captured_at = UNSET
        elif isinstance(self.captured_at, datetime.date):
            captured_at = self.captured_at.isoformat()
        else:
            captured_at = self.captured_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        file_path: None | str | Unset
        if isinstance(self.file_path, Unset):
            file_path = UNSET
        else:
            file_path = self.file_path

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        ndvi_avg: float | None | Unset
        if isinstance(self.ndvi_avg, Unset):
            ndvi_avg = UNSET
        else:
            ndvi_avg = self.ndvi_avg

        ndvi_max: float | None | Unset
        if isinstance(self.ndvi_max, Unset):
            ndvi_max = UNSET
        else:
            ndvi_max = self.ndvi_max

        ndvi_min: float | None | Unset
        if isinstance(self.ndvi_min, Unset):
            ndvi_min = UNSET
        else:
            ndvi_min = self.ndvi_min

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        style_config: None | str | Unset
        if isinstance(self.style_config, Unset):
            style_config = UNSET
        else:
            style_config = self.style_config

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id

        zone_name: None | str | Unset
        if isinstance(self.zone_name, Unset):
            zone_name = UNSET
        else:
            zone_name = self.zone_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if captured_at is not UNSET:
            field_dict["captured_at"] = captured_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if file_path is not UNSET:
            field_dict["file_path"] = file_path
        if id is not UNSET:
            field_dict["id"] = id
        if layer_type is not UNSET:
            field_dict["layer_type"] = layer_type
        if name is not UNSET:
            field_dict["name"] = name
        if ndvi_avg is not UNSET:
            field_dict["ndvi_avg"] = ndvi_avg
        if ndvi_max is not UNSET:
            field_dict["ndvi_max"] = ndvi_max
        if ndvi_min is not UNSET:
            field_dict["ndvi_min"] = ndvi_min
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if status is not UNSET:
            field_dict["status"] = status
        if style_config is not UNSET:
            field_dict["style_config"] = style_config
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if zone_name is not UNSET:
            field_dict["zone_name"] = zone_name

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


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_path = _parse_file_path(d.pop("file_path", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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


        def _parse_ndvi_avg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ndvi_avg = _parse_ndvi_avg(d.pop("ndvi_avg", UNSET))


        def _parse_ndvi_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ndvi_max = _parse_ndvi_max(d.pop("ndvi_max", UNSET))


        def _parse_ndvi_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ndvi_min = _parse_ndvi_min(d.pop("ndvi_min", UNSET))


        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_style_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        style_config = _parse_style_config(d.pop("style_config", UNSET))


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




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


        def _parse_zone_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_name = _parse_zone_name(d.pop("zone_name", UNSET))


        gis_map_layer_dto = cls(
            captured_at=captured_at,
            created_at=created_at,
            file_path=file_path,
            id=id,
            layer_type=layer_type,
            name=name,
            ndvi_avg=ndvi_avg,
            ndvi_max=ndvi_max,
            ndvi_min=ndvi_min,
            source_url=source_url,
            status=status,
            style_config=style_config,
            updated_at=updated_at,
            zone_id=zone_id,
            zone_name=zone_name,
        )

        return gis_map_layer_dto


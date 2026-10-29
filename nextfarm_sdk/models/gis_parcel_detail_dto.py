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

if TYPE_CHECKING:
  from ..models.gis_parcel_crop_type_dto import GisParcelCropTypeDto
  from ..models.gis_parcel_ndvi_reading_dto import GisParcelNdviReadingDto
  from ..models.gis_parcel_owner_dto import GisParcelOwnerDto
  from ..models.gis_parcel_zone_dto import GisParcelZoneDto





T = TypeVar("T", bound="GisParcelDetailDto")



@_attrs_define
class GisParcelDetailDto:
    

    area_ha: float | None | Unset = UNSET
    boundary_geo_json: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | Unset = UNSET
    crop_type: GisParcelCropTypeDto | Unset = UNSET
    id: UUID | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    ndvi_history: list[GisParcelNdviReadingDto] | None | Unset = UNSET
    owner: GisParcelOwnerDto | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    zone: GisParcelZoneDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_parcel_crop_type_dto import GisParcelCropTypeDto # noqa: PLC0415
        from ..models.gis_parcel_ndvi_reading_dto import GisParcelNdviReadingDto # noqa: PLC0415
        from ..models.gis_parcel_owner_dto import GisParcelOwnerDto # noqa: PLC0415
        from ..models.gis_parcel_zone_dto import GisParcelZoneDto # noqa: PLC0415
        area_ha: float | None | Unset
        if isinstance(self.area_ha, Unset):
            area_ha = UNSET
        else:
            area_ha = self.area_ha

        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        crop_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crop_type, Unset):
            crop_type = self.crop_type.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        ndvi_history: list[dict[str, Any]] | None | Unset
        if isinstance(self.ndvi_history, Unset):
            ndvi_history = UNSET
        elif isinstance(self.ndvi_history, list):
            ndvi_history = []
            for ndvi_history_type_0_item_data in self.ndvi_history:
                ndvi_history_type_0_item = ndvi_history_type_0_item_data.to_dict()
                ndvi_history.append(ndvi_history_type_0_item)


        else:
            ndvi_history = self.ndvi_history

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        zone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.zone, Unset):
            zone = self.zone.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if area_ha is not UNSET:
            field_dict["area_ha"] = area_ha
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if crop_type is not UNSET:
            field_dict["crop_type"] = crop_type
        if id is not UNSET:
            field_dict["id"] = id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if ndvi_history is not UNSET:
            field_dict["ndvi_history"] = ndvi_history
        if owner is not UNSET:
            field_dict["owner"] = owner
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_parcel_crop_type_dto import GisParcelCropTypeDto # noqa: PLC0415
        from ..models.gis_parcel_ndvi_reading_dto import GisParcelNdviReadingDto # noqa: PLC0415
        from ..models.gis_parcel_owner_dto import GisParcelOwnerDto # noqa: PLC0415
        from ..models.gis_parcel_zone_dto import GisParcelZoneDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_area_ha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area_ha = _parse_area_ha(d.pop("area_ha", UNSET))


        def _parse_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_geo_json = _parse_boundary_geo_json(d.pop("boundary_geo_json", UNSET))


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branch_id", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _crop_type = d.pop("crop_type", UNSET)
        crop_type: GisParcelCropTypeDto | Unset
        if isinstance(_crop_type,  Unset):
            crop_type = UNSET
        else:
            crop_type = GisParcelCropTypeDto.from_dict(_crop_type)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))


        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))


        def _parse_ndvi_history(data: object) -> list[GisParcelNdviReadingDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ndvi_history_type_0 = []
                _ndvi_history_type_0 = data
                for ndvi_history_type_0_item_data in (_ndvi_history_type_0):
                    ndvi_history_type_0_item = GisParcelNdviReadingDto.from_dict(ndvi_history_type_0_item_data)



                    ndvi_history_type_0.append(ndvi_history_type_0_item)

                return ndvi_history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisParcelNdviReadingDto] | None | Unset, data)

        ndvi_history = _parse_ndvi_history(d.pop("ndvi_history", UNSET))


        _owner = d.pop("owner", UNSET)
        owner: GisParcelOwnerDto | Unset
        if isinstance(_owner,  Unset):
            owner = UNSET
        else:
            owner = GisParcelOwnerDto.from_dict(_owner)




        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcel_code", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        _zone = d.pop("zone", UNSET)
        zone: GisParcelZoneDto | Unset
        if isinstance(_zone,  Unset):
            zone = UNSET
        else:
            zone = GisParcelZoneDto.from_dict(_zone)




        gis_parcel_detail_dto = cls(
            area_ha=area_ha,
            boundary_geo_json=boundary_geo_json,
            branch_id=branch_id,
            created_at=created_at,
            crop_type=crop_type,
            id=id,
            latitude=latitude,
            longitude=longitude,
            ndvi_history=ndvi_history,
            owner=owner,
            parcel_code=parcel_code,
            status=status,
            updated_at=updated_at,
            zone=zone,
        )

        return gis_parcel_detail_dto


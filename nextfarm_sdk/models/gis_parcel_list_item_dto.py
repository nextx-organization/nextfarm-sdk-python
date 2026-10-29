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
  from ..models.gis_parcel_active_season_dto import GisParcelActiveSeasonDto





T = TypeVar("T", bound="GisParcelListItemDto")



@_attrs_define
class GisParcelListItemDto:
    

    active_season_id: None | Unset | UUID = UNSET
    active_season_name: None | str | Unset = UNSET
    active_seasons: list[GisParcelActiveSeasonDto] | None | Unset = UNSET
    area_ha: float | None | Unset = UNSET
    boundary_geo_json: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | Unset = UNSET
    crop_type_id: None | Unset | UUID = UNSET
    crop_type_name: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    owner_id: None | Unset | UUID = UNSET
    owner_name: None | str | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    zone_id: UUID | Unset = UNSET
    zone_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_parcel_active_season_dto import GisParcelActiveSeasonDto # noqa: PLC0415
        active_season_id: None | str | Unset
        if isinstance(self.active_season_id, Unset):
            active_season_id = UNSET
        elif isinstance(self.active_season_id, UUID):
            active_season_id = str(self.active_season_id)
        else:
            active_season_id = self.active_season_id

        active_season_name: None | str | Unset
        if isinstance(self.active_season_name, Unset):
            active_season_name = UNSET
        else:
            active_season_name = self.active_season_name

        active_seasons: list[dict[str, Any]] | None | Unset
        if isinstance(self.active_seasons, Unset):
            active_seasons = UNSET
        elif isinstance(self.active_seasons, list):
            active_seasons = []
            for active_seasons_type_0_item_data in self.active_seasons:
                active_seasons_type_0_item = active_seasons_type_0_item_data.to_dict()
                active_seasons.append(active_seasons_type_0_item)


        else:
            active_seasons = self.active_seasons

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

        crop_type_id: None | str | Unset
        if isinstance(self.crop_type_id, Unset):
            crop_type_id = UNSET
        elif isinstance(self.crop_type_id, UUID):
            crop_type_id = str(self.crop_type_id)
        else:
            crop_type_id = self.crop_type_id

        crop_type_name: None | str | Unset
        if isinstance(self.crop_type_name, Unset):
            crop_type_name = UNSET
        else:
            crop_type_name = self.crop_type_name

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

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        elif isinstance(self.owner_id, UUID):
            owner_id = str(self.owner_id)
        else:
            owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

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

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)

        zone_name: None | str | Unset
        if isinstance(self.zone_name, Unset):
            zone_name = UNSET
        else:
            zone_name = self.zone_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active_season_id is not UNSET:
            field_dict["active_season_id"] = active_season_id
        if active_season_name is not UNSET:
            field_dict["active_season_name"] = active_season_name
        if active_seasons is not UNSET:
            field_dict["active_seasons"] = active_seasons
        if area_ha is not UNSET:
            field_dict["area_ha"] = area_ha
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if crop_type_name is not UNSET:
            field_dict["crop_type_name"] = crop_type_name
        if id is not UNSET:
            field_dict["id"] = id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if status is not UNSET:
            field_dict["status"] = status
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if zone_name is not UNSET:
            field_dict["zone_name"] = zone_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_parcel_active_season_dto import GisParcelActiveSeasonDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_active_season_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_season_id_type_0 = UUID(data)



                return active_season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        active_season_id = _parse_active_season_id(d.pop("active_season_id", UNSET))


        def _parse_active_season_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_season_name = _parse_active_season_name(d.pop("active_season_name", UNSET))


        def _parse_active_seasons(data: object) -> list[GisParcelActiveSeasonDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_seasons_type_0 = []
                _active_seasons_type_0 = data
                for active_seasons_type_0_item_data in (_active_seasons_type_0):
                    active_seasons_type_0_item = GisParcelActiveSeasonDto.from_dict(active_seasons_type_0_item_data)



                    active_seasons_type_0.append(active_seasons_type_0_item)

                return active_seasons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisParcelActiveSeasonDto] | None | Unset, data)

        active_seasons = _parse_active_seasons(d.pop("active_seasons", UNSET))


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




        def _parse_crop_type_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                crop_type_id_type_0 = UUID(data)



                return crop_type_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        crop_type_id = _parse_crop_type_id(d.pop("crop_type_id", UNSET))


        def _parse_crop_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_type_name = _parse_crop_type_name(d.pop("crop_type_name", UNSET))


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


        def _parse_owner_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_id_type_0 = UUID(data)



                return owner_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))


        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))


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


        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        def _parse_zone_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_name = _parse_zone_name(d.pop("zone_name", UNSET))


        gis_parcel_list_item_dto = cls(
            active_season_id=active_season_id,
            active_season_name=active_season_name,
            active_seasons=active_seasons,
            area_ha=area_ha,
            boundary_geo_json=boundary_geo_json,
            branch_id=branch_id,
            created_at=created_at,
            crop_type_id=crop_type_id,
            crop_type_name=crop_type_name,
            id=id,
            latitude=latitude,
            longitude=longitude,
            owner_id=owner_id,
            owner_name=owner_name,
            parcel_code=parcel_code,
            status=status,
            zone_id=zone_id,
            zone_name=zone_name,
        )

        return gis_parcel_list_item_dto


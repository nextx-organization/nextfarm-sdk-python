from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest





T = TypeVar("T", bound="HarvestUpdateOrganismRequest")



@_attrs_define
class HarvestUpdateOrganismRequest:
    

    code: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    life_stage_override: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    position_in_row: int | None | Unset = UNSET
    profile: HarvestOrganismProfileRequest | Unset = UNSET
    row_no: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        life_stage_override: None | str | Unset
        if isinstance(self.life_stage_override, Unset):
            life_stage_override = UNSET
        else:
            life_stage_override = self.life_stage_override

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        position_in_row: int | None | Unset
        if isinstance(self.position_in_row, Unset):
            position_in_row = UNSET
        else:
            position_in_row = self.position_in_row

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        row_no: int | None | Unset
        if isinstance(self.row_no, Unset):
            row_no = UNSET
        else:
            row_no = self.row_no


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if life_stage_override is not UNSET:
            field_dict["life_stage_override"] = life_stage_override
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if position_in_row is not UNSET:
            field_dict["position_in_row"] = position_in_row
        if profile is not UNSET:
            field_dict["profile"] = profile
        if row_no is not UNSET:
            field_dict["row_no"] = row_no

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))


        def _parse_life_stage_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        life_stage_override = _parse_life_stage_override(d.pop("life_stage_override", UNSET))


        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))


        def _parse_position_in_row(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_in_row = _parse_position_in_row(d.pop("position_in_row", UNSET))


        _profile = d.pop("profile", UNSET)
        profile: HarvestOrganismProfileRequest | Unset
        if isinstance(_profile,  Unset):
            profile = UNSET
        else:
            profile = HarvestOrganismProfileRequest.from_dict(_profile)




        def _parse_row_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_no = _parse_row_no(d.pop("row_no", UNSET))


        harvest_update_organism_request = cls(
            code=code,
            latitude=latitude,
            life_stage_override=life_stage_override,
            longitude=longitude,
            position_in_row=position_in_row,
            profile=profile,
            row_no=row_no,
        )

        return harvest_update_organism_request


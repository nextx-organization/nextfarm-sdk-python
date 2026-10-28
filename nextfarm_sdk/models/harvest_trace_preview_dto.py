from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestTracePreviewDto")



@_attrs_define
class HarvestTracePreviewDto:
    

    certification_expiry: datetime.date | None | Unset = UNSET
    certification_name: None | str | Unset = UNSET
    certification_number: None | str | Unset = UNSET
    has_season: bool | Unset = UNSET
    input_count: int | Unset = UNSET
    parcel_has_boundary: bool | Unset = UNSET
    season_name: None | str | Unset = UNSET
    stage_count: int | Unset = UNSET
    stages_with_photo: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        certification_expiry: None | str | Unset
        if isinstance(self.certification_expiry, Unset):
            certification_expiry = UNSET
        elif isinstance(self.certification_expiry, datetime.date):
            certification_expiry = self.certification_expiry.isoformat()
        else:
            certification_expiry = self.certification_expiry

        certification_name: None | str | Unset
        if isinstance(self.certification_name, Unset):
            certification_name = UNSET
        else:
            certification_name = self.certification_name

        certification_number: None | str | Unset
        if isinstance(self.certification_number, Unset):
            certification_number = UNSET
        else:
            certification_number = self.certification_number

        has_season = self.has_season

        input_count = self.input_count

        parcel_has_boundary = self.parcel_has_boundary

        season_name: None | str | Unset
        if isinstance(self.season_name, Unset):
            season_name = UNSET
        else:
            season_name = self.season_name

        stage_count = self.stage_count

        stages_with_photo = self.stages_with_photo


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if certification_expiry is not UNSET:
            field_dict["certification_expiry"] = certification_expiry
        if certification_name is not UNSET:
            field_dict["certification_name"] = certification_name
        if certification_number is not UNSET:
            field_dict["certification_number"] = certification_number
        if has_season is not UNSET:
            field_dict["has_season"] = has_season
        if input_count is not UNSET:
            field_dict["input_count"] = input_count
        if parcel_has_boundary is not UNSET:
            field_dict["parcel_has_boundary"] = parcel_has_boundary
        if season_name is not UNSET:
            field_dict["season_name"] = season_name
        if stage_count is not UNSET:
            field_dict["stage_count"] = stage_count
        if stages_with_photo is not UNSET:
            field_dict["stages_with_photo"] = stages_with_photo

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_certification_expiry(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certification_expiry_type_0 = datetime.date.fromisoformat(data)



                return certification_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        certification_expiry = _parse_certification_expiry(d.pop("certification_expiry", UNSET))


        def _parse_certification_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certification_name = _parse_certification_name(d.pop("certification_name", UNSET))


        def _parse_certification_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certification_number = _parse_certification_number(d.pop("certification_number", UNSET))


        has_season = d.pop("has_season", UNSET)

        input_count = d.pop("input_count", UNSET)

        parcel_has_boundary = d.pop("parcel_has_boundary", UNSET)

        def _parse_season_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        season_name = _parse_season_name(d.pop("season_name", UNSET))


        stage_count = d.pop("stage_count", UNSET)

        stages_with_photo = d.pop("stages_with_photo", UNSET)

        harvest_trace_preview_dto = cls(
            certification_expiry=certification_expiry,
            certification_name=certification_name,
            certification_number=certification_number,
            has_season=has_season,
            input_count=input_count,
            parcel_has_boundary=parcel_has_boundary,
            season_name=season_name,
            stage_count=stage_count,
            stages_with_photo=stages_with_photo,
        )

        return harvest_trace_preview_dto


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






T = TypeVar("T", bound="GisSeasonPeriodDto")



@_attrs_define
class GisSeasonPeriodDto:
    

    crop_name: None | str | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    missing_end_count: int | Unset = UNSET
    name: None | str | Unset = UNSET
    season_count: int | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    season_key: None | str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        crop_name: None | str | Unset
        if isinstance(self.crop_name, Unset):
            crop_name = UNSET
        else:
            crop_name = self.crop_name

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        missing_end_count = self.missing_end_count

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        season_count = self.season_count

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        season_key: None | str | Unset
        if isinstance(self.season_key, Unset):
            season_key = UNSET
        else:
            season_key = self.season_key

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_name is not UNSET:
            field_dict["crop_name"] = crop_name
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if missing_end_count is not UNSET:
            field_dict["missing_end_count"] = missing_end_count
        if name is not UNSET:
            field_dict["name"] = name
        if season_count is not UNSET:
            field_dict["season_count"] = season_count
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if season_key is not UNSET:
            field_dict["season_key"] = season_key
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_crop_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_name = _parse_crop_name(d.pop("crop_name", UNSET))


        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        missing_end_count = d.pop("missing_end_count", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        season_count = d.pop("season_count", UNSET)

        def _parse_season_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)



                return season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        season_id = _parse_season_id(d.pop("season_id", UNSET))


        def _parse_season_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        season_key = _parse_season_key(d.pop("season_key", UNSET))


        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        gis_season_period_dto = cls(
            crop_name=crop_name,
            end_date=end_date,
            missing_end_count=missing_end_count,
            name=name,
            season_count=season_count,
            season_id=season_id,
            season_key=season_key,
            start_date=start_date,
        )

        return gis_season_period_dto


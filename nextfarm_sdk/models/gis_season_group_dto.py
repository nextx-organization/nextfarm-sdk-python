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






T = TypeVar("T", bound="GisSeasonGroupDto")



@_attrs_define
class GisSeasonGroupDto:
    

    branch_ids: list[UUID] | None | Unset = UNSET
    crop_name: None | str | Unset = UNSET
    crop_type_id: UUID | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    key: None | str | Unset = UNSET
    missing_end_count: int | Unset = UNSET
    name: None | str | Unset = UNSET
    parcel_count: int | Unset = UNSET
    season_count: int | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    year: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        branch_ids: list[str] | None | Unset
        if isinstance(self.branch_ids, Unset):
            branch_ids = UNSET
        elif isinstance(self.branch_ids, list):
            branch_ids = []
            for branch_ids_type_0_item_data in self.branch_ids:
                branch_ids_type_0_item = str(branch_ids_type_0_item_data)
                branch_ids.append(branch_ids_type_0_item)


        else:
            branch_ids = self.branch_ids

        crop_name: None | str | Unset
        if isinstance(self.crop_name, Unset):
            crop_name = UNSET
        else:
            crop_name = self.crop_name

        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        missing_end_count = self.missing_end_count

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parcel_count = self.parcel_count

        season_count = self.season_count

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        year = self.year


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_ids is not UNSET:
            field_dict["branch_ids"] = branch_ids
        if crop_name is not UNSET:
            field_dict["crop_name"] = crop_name
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if key is not UNSET:
            field_dict["key"] = key
        if missing_end_count is not UNSET:
            field_dict["missing_end_count"] = missing_end_count
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_count is not UNSET:
            field_dict["parcel_count"] = parcel_count
        if season_count is not UNSET:
            field_dict["season_count"] = season_count
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_branch_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                branch_ids_type_0 = []
                _branch_ids_type_0 = data
                for branch_ids_type_0_item_data in (_branch_ids_type_0):
                    branch_ids_type_0_item = UUID(branch_ids_type_0_item_data)



                    branch_ids_type_0.append(branch_ids_type_0_item)

                return branch_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        branch_ids = _parse_branch_ids(d.pop("branch_ids", UNSET))


        def _parse_crop_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_name = _parse_crop_name(d.pop("crop_name", UNSET))


        _crop_type_id = d.pop("crop_type_id", UNSET)
        crop_type_id: UUID | Unset
        if isinstance(_crop_type_id,  Unset):
            crop_type_id = UNSET
        else:
            crop_type_id = UUID(_crop_type_id)




        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)



                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))


        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        missing_end_count = d.pop("missing_end_count", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        parcel_count = d.pop("parcel_count", UNSET)

        season_count = d.pop("season_count", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        year = d.pop("year", UNSET)

        gis_season_group_dto = cls(
            branch_ids=branch_ids,
            crop_name=crop_name,
            crop_type_id=crop_type_id,
            end_date=end_date,
            key=key,
            missing_end_count=missing_end_count,
            name=name,
            parcel_count=parcel_count,
            season_count=season_count,
            start_date=start_date,
            year=year,
        )

        return gis_season_group_dto


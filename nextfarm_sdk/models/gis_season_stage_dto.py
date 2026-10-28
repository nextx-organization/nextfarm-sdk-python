from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisSeasonStageDto")



@_attrs_define
class GisSeasonStageDto:
    

    day_offset: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    sort_order: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        day_offset: int | None | Unset
        if isinstance(self.day_offset, Unset):
            day_offset = UNSET
        else:
            day_offset = self.day_offset

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if day_offset is not UNSET:
            field_dict["day_offset"] = day_offset
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_day_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_offset = _parse_day_offset(d.pop("day_offset", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        sort_order = d.pop("sort_order", UNSET)

        gis_season_stage_dto = cls(
            day_offset=day_offset,
            id=id,
            name=name,
            sort_order=sort_order,
        )

        return gis_season_stage_dto


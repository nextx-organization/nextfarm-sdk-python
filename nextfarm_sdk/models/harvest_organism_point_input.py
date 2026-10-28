from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestOrganismPointInput")



@_attrs_define
class HarvestOrganismPointInput:
    

    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    position_in_row: int | None | Unset = UNSET
    row_no: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        position_in_row: int | None | Unset
        if isinstance(self.position_in_row, Unset):
            position_in_row = UNSET
        else:
            position_in_row = self.position_in_row

        row_no: int | None | Unset
        if isinstance(self.row_no, Unset):
            row_no = UNSET
        else:
            row_no = self.row_no


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if position_in_row is not UNSET:
            field_dict["position_in_row"] = position_in_row
        if row_no is not UNSET:
            field_dict["row_no"] = row_no

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        def _parse_position_in_row(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_in_row = _parse_position_in_row(d.pop("position_in_row", UNSET))


        def _parse_row_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_no = _parse_row_no(d.pop("row_no", UNSET))


        harvest_organism_point_input = cls(
            latitude=latitude,
            longitude=longitude,
            position_in_row=position_in_row,
            row_no=row_no,
        )

        return harvest_organism_point_input


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GisUpdateParcelBoundaryRequest")



@_attrs_define
class GisUpdateParcelBoundaryRequest:
    

    boundary_geo_json: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_geo_json = _parse_boundary_geo_json(d.pop("boundary_geo_json", UNSET))


        gis_update_parcel_boundary_request = cls(
            boundary_geo_json=boundary_geo_json,
        )

        return gis_update_parcel_boundary_request


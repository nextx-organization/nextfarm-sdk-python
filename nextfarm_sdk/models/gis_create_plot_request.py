from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisCreatePlotRequest")



@_attrs_define
class GisCreatePlotRequest:
    

    boundary_geo_json: None | str | Unset = UNSET
    crop_type_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    row_spacing_m: float | Unset = UNSET
    tree_spacing_m: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json

        crop_type_id: None | str | Unset
        if isinstance(self.crop_type_id, Unset):
            crop_type_id = UNSET
        elif isinstance(self.crop_type_id, UUID):
            crop_type_id = str(self.crop_type_id)
        else:
            crop_type_id = self.crop_type_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        row_spacing_m = self.row_spacing_m

        tree_spacing_m = self.tree_spacing_m


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if row_spacing_m is not UNSET:
            field_dict["row_spacing_m"] = row_spacing_m
        if tree_spacing_m is not UNSET:
            field_dict["tree_spacing_m"] = tree_spacing_m

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


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        row_spacing_m = d.pop("row_spacing_m", UNSET)

        tree_spacing_m = d.pop("tree_spacing_m", UNSET)

        gis_create_plot_request = cls(
            boundary_geo_json=boundary_geo_json,
            crop_type_id=crop_type_id,
            name=name,
            parcel_id=parcel_id,
            row_spacing_m=row_spacing_m,
            tree_spacing_m=tree_spacing_m,
        )

        return gis_create_plot_request


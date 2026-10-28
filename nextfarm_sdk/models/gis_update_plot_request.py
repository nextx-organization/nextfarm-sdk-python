from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisUpdatePlotRequest")



@_attrs_define
class GisUpdatePlotRequest:
    

    boundary_geo_json: None | str | Unset = UNSET
    crop_type_id: None | Unset | UUID = UNSET
    custom_trees_geo_json: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
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

        custom_trees_geo_json: None | str | Unset
        if isinstance(self.custom_trees_geo_json, Unset):
            custom_trees_geo_json = UNSET
        else:
            custom_trees_geo_json = self.custom_trees_geo_json

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        row_spacing_m = self.row_spacing_m

        tree_spacing_m = self.tree_spacing_m


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if custom_trees_geo_json is not UNSET:
            field_dict["custom_trees_geo_json"] = custom_trees_geo_json
        if name is not UNSET:
            field_dict["name"] = name
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


        def _parse_custom_trees_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_trees_geo_json = _parse_custom_trees_geo_json(d.pop("custom_trees_geo_json", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        row_spacing_m = d.pop("row_spacing_m", UNSET)

        tree_spacing_m = d.pop("tree_spacing_m", UNSET)

        gis_update_plot_request = cls(
            boundary_geo_json=boundary_geo_json,
            crop_type_id=crop_type_id,
            custom_trees_geo_json=custom_trees_geo_json,
            name=name,
            row_spacing_m=row_spacing_m,
            tree_spacing_m=tree_spacing_m,
        )

        return gis_update_plot_request


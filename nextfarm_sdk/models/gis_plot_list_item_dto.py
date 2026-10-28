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
  from ..models.gis_plot_crop_dto import GisPlotCropDto





T = TypeVar("T", bound="GisPlotListItemDto")



@_attrs_define
class GisPlotListItemDto:
    

    area_m2: float | Unset = UNSET
    boundary_geo_json: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    crop_category: None | str | Unset = UNSET
    crop_type_id: None | Unset | UUID = UNSET
    crop_type_name: None | str | Unset = UNSET
    crops: list[GisPlotCropDto] | None | Unset = UNSET
    custom_trees_geo_json: None | str | Unset = UNSET
    density_per1000_m2: float | Unset = UNSET
    estimated_tree_count: int | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    row_spacing_m: float | Unset = UNSET
    tree_spacing_m: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_plot_crop_dto import GisPlotCropDto # noqa: PLC0415
        area_m2 = self.area_m2

        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        crop_category: None | str | Unset
        if isinstance(self.crop_category, Unset):
            crop_category = UNSET
        else:
            crop_category = self.crop_category

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

        crops: list[dict[str, Any]] | None | Unset
        if isinstance(self.crops, Unset):
            crops = UNSET
        elif isinstance(self.crops, list):
            crops = []
            for crops_type_0_item_data in self.crops:
                crops_type_0_item = crops_type_0_item_data.to_dict()
                crops.append(crops_type_0_item)


        else:
            crops = self.crops

        custom_trees_geo_json: None | str | Unset
        if isinstance(self.custom_trees_geo_json, Unset):
            custom_trees_geo_json = UNSET
        else:
            custom_trees_geo_json = self.custom_trees_geo_json

        density_per1000_m2 = self.density_per1000_m2

        estimated_tree_count = self.estimated_tree_count

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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
        if area_m2 is not UNSET:
            field_dict["area_m2"] = area_m2
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if crop_category is not UNSET:
            field_dict["crop_category"] = crop_category
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if crop_type_name is not UNSET:
            field_dict["crop_type_name"] = crop_type_name
        if crops is not UNSET:
            field_dict["crops"] = crops
        if custom_trees_geo_json is not UNSET:
            field_dict["custom_trees_geo_json"] = custom_trees_geo_json
        if density_per1000_m2 is not UNSET:
            field_dict["density_per1000_m2"] = density_per1000_m2
        if estimated_tree_count is not UNSET:
            field_dict["estimated_tree_count"] = estimated_tree_count
        if id is not UNSET:
            field_dict["id"] = id
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
        from ..models.gis_plot_crop_dto import GisPlotCropDto # noqa: PLC0415
        d = dict(src_dict)
        area_m2 = d.pop("area_m2", UNSET)

        def _parse_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_geo_json = _parse_boundary_geo_json(d.pop("boundary_geo_json", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_crop_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_category = _parse_crop_category(d.pop("crop_category", UNSET))


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


        def _parse_crops(data: object) -> list[GisPlotCropDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                crops_type_0 = []
                _crops_type_0 = data
                for crops_type_0_item_data in (_crops_type_0):
                    crops_type_0_item = GisPlotCropDto.from_dict(crops_type_0_item_data)



                    crops_type_0.append(crops_type_0_item)

                return crops_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisPlotCropDto] | None | Unset, data)

        crops = _parse_crops(d.pop("crops", UNSET))


        def _parse_custom_trees_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_trees_geo_json = _parse_custom_trees_geo_json(d.pop("custom_trees_geo_json", UNSET))


        density_per1000_m2 = d.pop("density_per1000_m2", UNSET)

        estimated_tree_count = d.pop("estimated_tree_count", UNSET)

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


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        row_spacing_m = d.pop("row_spacing_m", UNSET)

        tree_spacing_m = d.pop("tree_spacing_m", UNSET)

        gis_plot_list_item_dto = cls(
            area_m2=area_m2,
            boundary_geo_json=boundary_geo_json,
            created_at=created_at,
            crop_category=crop_category,
            crop_type_id=crop_type_id,
            crop_type_name=crop_type_name,
            crops=crops,
            custom_trees_geo_json=custom_trees_geo_json,
            density_per1000_m2=density_per1000_m2,
            estimated_tree_count=estimated_tree_count,
            id=id,
            name=name,
            parcel_id=parcel_id,
            row_spacing_m=row_spacing_m,
            tree_spacing_m=tree_spacing_m,
        )

        return gis_plot_list_item_dto


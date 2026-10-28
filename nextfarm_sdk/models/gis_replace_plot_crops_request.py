from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_plot_crop_request import GisPlotCropRequest





T = TypeVar("T", bound="GisReplacePlotCropsRequest")



@_attrs_define
class GisReplacePlotCropsRequest:
    

    crops: list[GisPlotCropRequest] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_plot_crop_request import GisPlotCropRequest # noqa: PLC0415
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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crops is not UNSET:
            field_dict["crops"] = crops

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_plot_crop_request import GisPlotCropRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_crops(data: object) -> list[GisPlotCropRequest] | None | Unset:
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
                    crops_type_0_item = GisPlotCropRequest.from_dict(crops_type_0_item_data)



                    crops_type_0.append(crops_type_0_item)

                return crops_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisPlotCropRequest] | None | Unset, data)

        crops = _parse_crops(d.pop("crops", UNSET))


        gis_replace_plot_crops_request = cls(
            crops=crops,
        )

        return gis_replace_plot_crops_request


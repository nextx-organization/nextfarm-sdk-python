from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GisMapClusterDto")



@_attrs_define
class GisMapClusterDto:
    

    count: int | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        latitude = self.latitude

        longitude = self.longitude


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        gis_map_cluster_dto = cls(
            count=count,
            latitude=latitude,
            longitude=longitude,
        )

        return gis_map_cluster_dto


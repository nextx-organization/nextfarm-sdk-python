from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GisParcelNdviReadingDto")



@_attrs_define
class GisParcelNdviReadingDto:
    

    ndvi_value: float | Unset = UNSET
    recorded_at: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ndvi_value = self.ndvi_value

        recorded_at: str | Unset = UNSET
        if not isinstance(self.recorded_at, Unset):
            recorded_at = self.recorded_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ndvi_value is not UNSET:
            field_dict["ndvi_value"] = ndvi_value
        if recorded_at is not UNSET:
            field_dict["recorded_at"] = recorded_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ndvi_value = d.pop("ndvi_value", UNSET)

        _recorded_at = d.pop("recorded_at", UNSET)
        recorded_at: datetime.date | Unset
        if isinstance(_recorded_at,  Unset):
            recorded_at = UNSET
        else:
            recorded_at = datetime.date.fromisoformat(_recorded_at)




        gis_parcel_ndvi_reading_dto = cls(
            ndvi_value=ndvi_value,
            recorded_at=recorded_at,
        )

        return gis_parcel_ndvi_reading_dto


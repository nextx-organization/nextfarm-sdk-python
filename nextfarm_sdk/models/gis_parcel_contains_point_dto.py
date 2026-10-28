from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="GisParcelContainsPointDto")



@_attrs_define
class GisParcelContainsPointDto:
    

    inside: bool | Unset = UNSET
    parcel_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        inside = self.inside

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if inside is not UNSET:
            field_dict["inside"] = inside
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inside = d.pop("inside", UNSET)

        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        gis_parcel_contains_point_dto = cls(
            inside=inside,
            parcel_id=parcel_id,
        )

        return gis_parcel_contains_point_dto


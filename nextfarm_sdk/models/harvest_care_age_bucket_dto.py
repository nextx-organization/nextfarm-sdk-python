from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestCareAgeBucketDto")



@_attrs_define
class HarvestCareAgeBucketDto:
    

    age_years: int | None | Unset = UNSET
    trees: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        age_years: int | None | Unset
        if isinstance(self.age_years, Unset):
            age_years = UNSET
        else:
            age_years = self.age_years

        trees = self.trees


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if age_years is not UNSET:
            field_dict["age_years"] = age_years
        if trees is not UNSET:
            field_dict["trees"] = trees

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_age_years(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age_years = _parse_age_years(d.pop("age_years", UNSET))


        trees = d.pop("trees", UNSET)

        harvest_care_age_bucket_dto = cls(
            age_years=age_years,
            trees=trees,
        )

        return harvest_care_age_bucket_dto


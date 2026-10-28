from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GisCareDose")



@_attrs_define
class GisCareDose:
    

    age_from: int | Unset = UNSET
    age_to: int | None | Unset = UNSET
    quantity_per_tree: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        age_from = self.age_from

        age_to: int | None | Unset
        if isinstance(self.age_to, Unset):
            age_to = UNSET
        else:
            age_to = self.age_to

        quantity_per_tree = self.quantity_per_tree


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if age_from is not UNSET:
            field_dict["age_from"] = age_from
        if age_to is not UNSET:
            field_dict["age_to"] = age_to
        if quantity_per_tree is not UNSET:
            field_dict["quantity_per_tree"] = quantity_per_tree

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        age_from = d.pop("age_from", UNSET)

        def _parse_age_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age_to = _parse_age_to(d.pop("age_to", UNSET))


        quantity_per_tree = d.pop("quantity_per_tree", UNSET)

        gis_care_dose = cls(
            age_from=age_from,
            age_to=age_to,
            quantity_per_tree=quantity_per_tree,
        )

        return gis_care_dose


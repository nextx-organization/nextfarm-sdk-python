from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisPlotCropRequest")



@_attrs_define
class GisPlotCropRequest:
    

    crop_type_id: UUID | Unset = UNSET
    estimated_tree_count: int | None | Unset = UNSET
    note: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    row_spacing_m: float | None | Unset = UNSET
    tree_spacing_m: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

        estimated_tree_count: int | None | Unset
        if isinstance(self.estimated_tree_count, Unset):
            estimated_tree_count = UNSET
        else:
            estimated_tree_count = self.estimated_tree_count

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        row_spacing_m: float | None | Unset
        if isinstance(self.row_spacing_m, Unset):
            row_spacing_m = UNSET
        else:
            row_spacing_m = self.row_spacing_m

        tree_spacing_m: float | None | Unset
        if isinstance(self.tree_spacing_m, Unset):
            tree_spacing_m = UNSET
        else:
            tree_spacing_m = self.tree_spacing_m


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if estimated_tree_count is not UNSET:
            field_dict["estimated_tree_count"] = estimated_tree_count
        if note is not UNSET:
            field_dict["note"] = note
        if role is not UNSET:
            field_dict["role"] = role
        if row_spacing_m is not UNSET:
            field_dict["row_spacing_m"] = row_spacing_m
        if tree_spacing_m is not UNSET:
            field_dict["tree_spacing_m"] = tree_spacing_m

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _crop_type_id = d.pop("crop_type_id", UNSET)
        crop_type_id: UUID | Unset
        if isinstance(_crop_type_id,  Unset):
            crop_type_id = UNSET
        else:
            crop_type_id = UUID(_crop_type_id)




        def _parse_estimated_tree_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_tree_count = _parse_estimated_tree_count(d.pop("estimated_tree_count", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        def _parse_row_spacing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        row_spacing_m = _parse_row_spacing_m(d.pop("row_spacing_m", UNSET))


        def _parse_tree_spacing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tree_spacing_m = _parse_tree_spacing_m(d.pop("tree_spacing_m", UNSET))


        gis_plot_crop_request = cls(
            crop_type_id=crop_type_id,
            estimated_tree_count=estimated_tree_count,
            note=note,
            role=role,
            row_spacing_m=row_spacing_m,
            tree_spacing_m=tree_spacing_m,
        )

        return gis_plot_crop_request


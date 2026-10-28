from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeImportTargetColumnDto")



@_attrs_define
class OfficeImportTargetColumnDto:
    

    canonical: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    required: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        canonical: None | str | Unset
        if isinstance(self.canonical, Unset):
            canonical = UNSET
        else:
            canonical = self.canonical

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        required = self.required


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if label is not UNSET:
            field_dict["label"] = label
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_canonical(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        canonical = _parse_canonical(d.pop("canonical", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        required = d.pop("required", UNSET)

        office_import_target_column_dto = cls(
            canonical=canonical,
            label=label,
            required=required,
        )

        return office_import_target_column_dto


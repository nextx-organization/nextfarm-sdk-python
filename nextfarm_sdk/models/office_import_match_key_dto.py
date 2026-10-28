from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeImportMatchKeyDto")



@_attrs_define
class OfficeImportMatchKeyDto:
    

    label: None | str | Unset = UNSET
    label_key: None | str | Unset = UNSET
    value: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        label_key: None | str | Unset
        if isinstance(self.label_key, Unset):
            label_key = UNSET
        else:
            label_key = self.label_key

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if label is not UNSET:
            field_dict["label"] = label
        if label_key is not UNSET:
            field_dict["labelKey"] = label_key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_label_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_key = _parse_label_key(d.pop("labelKey", UNSET))


        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        office_import_match_key_dto = cls(
            label=label,
            label_key=label_key,
            value=value,
        )

        return office_import_match_key_dto


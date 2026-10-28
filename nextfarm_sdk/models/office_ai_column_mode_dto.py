from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAiColumnModeDto")



@_attrs_define
class OfficeAiColumnModeDto:
    

    label_key: None | str | Unset = UNSET
    mode: None | str | Unset = UNSET
    needs_options: bool | Unset = UNSET
    needs_range: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        label_key: None | str | Unset
        if isinstance(self.label_key, Unset):
            label_key = UNSET
        else:
            label_key = self.label_key

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        needs_options = self.needs_options

        needs_range = self.needs_range


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if label_key is not UNSET:
            field_dict["labelKey"] = label_key
        if mode is not UNSET:
            field_dict["mode"] = mode
        if needs_options is not UNSET:
            field_dict["needsOptions"] = needs_options
        if needs_range is not UNSET:
            field_dict["needsRange"] = needs_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_label_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_key = _parse_label_key(d.pop("labelKey", UNSET))


        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        needs_options = d.pop("needsOptions", UNSET)

        needs_range = d.pop("needsRange", UNSET)

        office_ai_column_mode_dto = cls(
            label_key=label_key,
            mode=mode,
            needs_options=needs_options,
            needs_range=needs_range,
        )

        return office_ai_column_mode_dto


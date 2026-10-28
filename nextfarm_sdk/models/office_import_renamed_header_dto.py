from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeImportRenamedHeaderDto")



@_attrs_define
class OfficeImportRenamedHeaderDto:
    

    column: int | Unset = UNSET
    name: None | str | Unset = UNSET
    original: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        column = self.column

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        original: None | str | Unset
        if isinstance(self.original, Unset):
            original = UNSET
        else:
            original = self.original

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if column is not UNSET:
            field_dict["column"] = column
        if name is not UNSET:
            field_dict["name"] = name
        if original is not UNSET:
            field_dict["original"] = original
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_original(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original = _parse_original(d.pop("original", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        office_import_renamed_header_dto = cls(
            column=column,
            name=name,
            original=original,
            reason=reason,
        )

        return office_import_renamed_header_dto


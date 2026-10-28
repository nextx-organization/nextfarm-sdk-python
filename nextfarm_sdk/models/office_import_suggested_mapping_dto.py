from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeImportSuggestedMappingDto")



@_attrs_define
class OfficeImportSuggestedMappingDto:
    

    column_name: None | str | Unset = UNSET
    field_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        column_name: None | str | Unset
        if isinstance(self.column_name, Unset):
            column_name = UNSET
        else:
            column_name = self.column_name

        field_key: None | str | Unset
        if isinstance(self.field_key, Unset):
            field_key = UNSET
        else:
            field_key = self.field_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if column_name is not UNSET:
            field_dict["columnName"] = column_name
        if field_key is not UNSET:
            field_dict["fieldKey"] = field_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_column_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        column_name = _parse_column_name(d.pop("columnName", UNSET))


        def _parse_field_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_key = _parse_field_key(d.pop("fieldKey", UNSET))


        office_import_suggested_mapping_dto = cls(
            column_name=column_name,
            field_key=field_key,
        )

        return office_import_suggested_mapping_dto


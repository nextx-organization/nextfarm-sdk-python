from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeImportPreviewErrorDto")



@_attrs_define
class OfficeImportPreviewErrorDto:
    

    column: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    row_number: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        column: None | str | Unset
        if isinstance(self.column, Unset):
            column = UNSET
        else:
            column = self.column

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        row_number = self.row_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if column is not UNSET:
            field_dict["column"] = column
        if message is not UNSET:
            field_dict["message"] = message
        if row_number is not UNSET:
            field_dict["rowNumber"] = row_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_column(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        column = _parse_column(d.pop("column", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        row_number = d.pop("rowNumber", UNSET)

        office_import_preview_error_dto = cls(
            column=column,
            message=message,
            row_number=row_number,
        )

        return office_import_preview_error_dto


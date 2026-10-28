from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_import_row_validation_dto_existing_values_type_0 import OfficeImportRowValidationDtoExistingValuesType0





T = TypeVar("T", bound="OfficeImportRowValidationDto")



@_attrs_define
class OfficeImportRowValidationDto:
    

    error_message: None | str | Unset = UNSET
    existing_values: None | OfficeImportRowValidationDtoExistingValuesType0 | Unset = UNSET
    is_duplicate: bool | Unset = UNSET
    is_valid: bool | Unset = UNSET
    row_number: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_import_row_validation_dto_existing_values_type_0 import OfficeImportRowValidationDtoExistingValuesType0 # noqa: PLC0415
        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        existing_values: dict[str, Any] | None | Unset
        if isinstance(self.existing_values, Unset):
            existing_values = UNSET
        elif isinstance(self.existing_values, OfficeImportRowValidationDtoExistingValuesType0):
            existing_values = self.existing_values.to_dict()
        else:
            existing_values = self.existing_values

        is_duplicate = self.is_duplicate

        is_valid = self.is_valid

        row_number = self.row_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if existing_values is not UNSET:
            field_dict["existingValues"] = existing_values
        if is_duplicate is not UNSET:
            field_dict["isDuplicate"] = is_duplicate
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if row_number is not UNSET:
            field_dict["rowNumber"] = row_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_import_row_validation_dto_existing_values_type_0 import OfficeImportRowValidationDtoExistingValuesType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))


        def _parse_existing_values(data: object) -> None | OfficeImportRowValidationDtoExistingValuesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                existing_values_type_0 = OfficeImportRowValidationDtoExistingValuesType0.from_dict(data)



                return existing_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeImportRowValidationDtoExistingValuesType0 | Unset, data)

        existing_values = _parse_existing_values(d.pop("existingValues", UNSET))


        is_duplicate = d.pop("isDuplicate", UNSET)

        is_valid = d.pop("isValid", UNSET)

        row_number = d.pop("rowNumber", UNSET)

        office_import_row_validation_dto = cls(
            error_message=error_message,
            existing_values=existing_values,
            is_duplicate=is_duplicate,
            is_valid=is_valid,
            row_number=row_number,
        )

        return office_import_row_validation_dto


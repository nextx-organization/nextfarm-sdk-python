from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_validate_import_row_input_data_type_0 import OfficeValidateImportRowInputDataType0





T = TypeVar("T", bound="OfficeValidateImportRowInput")



@_attrs_define
class OfficeValidateImportRowInput:
    

    data: None | OfficeValidateImportRowInputDataType0 | Unset = UNSET
    row_number: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_validate_import_row_input_data_type_0 import OfficeValidateImportRowInputDataType0 # noqa: PLC0415
        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, OfficeValidateImportRowInputDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        row_number = self.row_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if row_number is not UNSET:
            field_dict["rowNumber"] = row_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_validate_import_row_input_data_type_0 import OfficeValidateImportRowInputDataType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_data(data: object) -> None | OfficeValidateImportRowInputDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = OfficeValidateImportRowInputDataType0.from_dict(data)



                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeValidateImportRowInputDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        row_number = d.pop("rowNumber", UNSET)

        office_validate_import_row_input = cls(
            data=data,
            row_number=row_number,
        )

        return office_validate_import_row_input


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_import_validate_row_values_type_0 import GisImportValidateRowValuesType0





T = TypeVar("T", bound="GisImportValidateRow")



@_attrs_define
class GisImportValidateRow:
    

    row_number: int | Unset = UNSET
    values: GisImportValidateRowValuesType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_import_validate_row_values_type_0 import GisImportValidateRowValuesType0 # noqa: PLC0415
        row_number = self.row_number

        values: dict[str, Any] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, GisImportValidateRowValuesType0):
            values = self.values.to_dict()
        else:
            values = self.values


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if row_number is not UNSET:
            field_dict["row_number"] = row_number
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_import_validate_row_values_type_0 import GisImportValidateRowValuesType0 # noqa: PLC0415
        d = dict(src_dict)
        row_number = d.pop("row_number", UNSET)

        def _parse_values(data: object) -> GisImportValidateRowValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                values_type_0 = GisImportValidateRowValuesType0.from_dict(data)



                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GisImportValidateRowValuesType0 | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))


        gis_import_validate_row = cls(
            row_number=row_number,
            values=values,
        )

        return gis_import_validate_row


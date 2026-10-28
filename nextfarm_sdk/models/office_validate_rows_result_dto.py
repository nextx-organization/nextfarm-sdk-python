from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_import_row_validation_dto import OfficeImportRowValidationDto





T = TypeVar("T", bound="OfficeValidateRowsResultDto")



@_attrs_define
class OfficeValidateRowsResultDto:
    

    rows: list[OfficeImportRowValidationDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_import_row_validation_dto import OfficeImportRowValidationDto # noqa: PLC0415
        rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)


        else:
            rows = self.rows


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_import_row_validation_dto import OfficeImportRowValidationDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_rows(data: object) -> list[OfficeImportRowValidationDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in (_rows_type_0):
                    rows_type_0_item = OfficeImportRowValidationDto.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportRowValidationDto] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        office_validate_rows_result_dto = cls(
            rows=rows,
        )

        return office_validate_rows_result_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_validate_import_row_input import OfficeValidateImportRowInput





T = TypeVar("T", bound="OfficeValidateImportRowsRequest")



@_attrs_define
class OfficeValidateImportRowsRequest:
    

    headers: list[str] | None | Unset = UNSET
    match_key: None | str | Unset = UNSET
    rows: list[OfficeValidateImportRowInput] | None | Unset = UNSET
    upload_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_validate_import_row_input import OfficeValidateImportRowInput # noqa: PLC0415
        headers: list[str] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, list):
            headers = self.headers


        else:
            headers = self.headers

        match_key: None | str | Unset
        if isinstance(self.match_key, Unset):
            match_key = UNSET
        else:
            match_key = self.match_key

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

        upload_key: None | str | Unset
        if isinstance(self.upload_key, Unset):
            upload_key = UNSET
        else:
            upload_key = self.upload_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if headers is not UNSET:
            field_dict["headers"] = headers
        if match_key is not UNSET:
            field_dict["matchKey"] = match_key
        if rows is not UNSET:
            field_dict["rows"] = rows
        if upload_key is not UNSET:
            field_dict["uploadKey"] = upload_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_validate_import_row_input import OfficeValidateImportRowInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                headers_type_0 = cast(list[str], data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))


        def _parse_match_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        match_key = _parse_match_key(d.pop("matchKey", UNSET))


        def _parse_rows(data: object) -> list[OfficeValidateImportRowInput] | None | Unset:
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
                    rows_type_0_item = OfficeValidateImportRowInput.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeValidateImportRowInput] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        def _parse_upload_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_key = _parse_upload_key(d.pop("uploadKey", UNSET))


        office_validate_import_rows_request = cls(
            headers=headers,
            match_key=match_key,
            rows=rows,
            upload_key=upload_key,
        )

        return office_validate_import_rows_request


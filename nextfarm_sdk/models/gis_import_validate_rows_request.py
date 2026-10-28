from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_import_validate_row import GisImportValidateRow





T = TypeVar("T", bound="GisImportValidateRowsRequest")



@_attrs_define
class GisImportValidateRowsRequest:
    

    duplicate_strategy: None | str | Unset = UNSET
    headers: list[str] | None | Unset = UNSET
    import_type: None | str | Unset = UNSET
    match_key: None | str | Unset = UNSET
    rows: list[GisImportValidateRow] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_import_validate_row import GisImportValidateRow # noqa: PLC0415
        duplicate_strategy: None | str | Unset
        if isinstance(self.duplicate_strategy, Unset):
            duplicate_strategy = UNSET
        else:
            duplicate_strategy = self.duplicate_strategy

        headers: list[str] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, list):
            headers = self.headers


        else:
            headers = self.headers

        import_type: None | str | Unset
        if isinstance(self.import_type, Unset):
            import_type = UNSET
        else:
            import_type = self.import_type

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if duplicate_strategy is not UNSET:
            field_dict["duplicate_strategy"] = duplicate_strategy
        if headers is not UNSET:
            field_dict["headers"] = headers
        if import_type is not UNSET:
            field_dict["import_type"] = import_type
        if match_key is not UNSET:
            field_dict["match_key"] = match_key
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_import_validate_row import GisImportValidateRow # noqa: PLC0415
        d = dict(src_dict)
        def _parse_duplicate_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicate_strategy = _parse_duplicate_strategy(d.pop("duplicate_strategy", UNSET))


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


        def _parse_import_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_type = _parse_import_type(d.pop("import_type", UNSET))


        def _parse_match_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        match_key = _parse_match_key(d.pop("match_key", UNSET))


        def _parse_rows(data: object) -> list[GisImportValidateRow] | None | Unset:
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
                    rows_type_0_item = GisImportValidateRow.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisImportValidateRow] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        gis_import_validate_rows_request = cls(
            duplicate_strategy=duplicate_strategy,
            headers=headers,
            import_type=import_type,
            match_key=match_key,
            rows=rows,
        )

        return gis_import_validate_rows_request


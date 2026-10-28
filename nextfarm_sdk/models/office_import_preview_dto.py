from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_import_match_key_dto import OfficeImportMatchKeyDto
  from ..models.office_import_preview_error_dto import OfficeImportPreviewErrorDto
  from ..models.office_import_preview_row_dto import OfficeImportPreviewRowDto
  from ..models.office_import_renamed_header_dto import OfficeImportRenamedHeaderDto
  from ..models.office_import_suggested_mapping_dto import OfficeImportSuggestedMappingDto





T = TypeVar("T", bound="OfficeImportPreviewDto")



@_attrs_define
class OfficeImportPreviewDto:
    

    duplicate_rows: int | Unset = UNSET
    errors: list[OfficeImportPreviewErrorDto] | None | Unset = UNSET
    headers: list[str] | None | Unset = UNSET
    invalid_rows: int | Unset = UNSET
    match_keys: list[OfficeImportMatchKeyDto] | None | Unset = UNSET
    new_rows: int | Unset = UNSET
    renamed_headers: list[OfficeImportRenamedHeaderDto] | None | Unset = UNSET
    sample_rows: list[OfficeImportPreviewRowDto] | None | Unset = UNSET
    suggested_mapping: list[OfficeImportSuggestedMappingDto] | None | Unset = UNSET
    supports_column_mapping: bool | Unset = UNSET
    supports_duplicate_skip: bool | Unset = UNSET
    supports_duplicate_update: bool | Unset = UNSET
    total_rows: int | Unset = UNSET
    updatable_columns: list[str] | None | Unset = UNSET
    upload_key: None | str | Unset = UNSET
    valid_rows: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_import_match_key_dto import OfficeImportMatchKeyDto # noqa: PLC0415
        from ..models.office_import_preview_error_dto import OfficeImportPreviewErrorDto # noqa: PLC0415
        from ..models.office_import_preview_row_dto import OfficeImportPreviewRowDto # noqa: PLC0415
        from ..models.office_import_renamed_header_dto import OfficeImportRenamedHeaderDto # noqa: PLC0415
        from ..models.office_import_suggested_mapping_dto import OfficeImportSuggestedMappingDto # noqa: PLC0415
        duplicate_rows = self.duplicate_rows

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)


        else:
            errors = self.errors

        headers: list[str] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, list):
            headers = self.headers


        else:
            headers = self.headers

        invalid_rows = self.invalid_rows

        match_keys: list[dict[str, Any]] | None | Unset
        if isinstance(self.match_keys, Unset):
            match_keys = UNSET
        elif isinstance(self.match_keys, list):
            match_keys = []
            for match_keys_type_0_item_data in self.match_keys:
                match_keys_type_0_item = match_keys_type_0_item_data.to_dict()
                match_keys.append(match_keys_type_0_item)


        else:
            match_keys = self.match_keys

        new_rows = self.new_rows

        renamed_headers: list[dict[str, Any]] | None | Unset
        if isinstance(self.renamed_headers, Unset):
            renamed_headers = UNSET
        elif isinstance(self.renamed_headers, list):
            renamed_headers = []
            for renamed_headers_type_0_item_data in self.renamed_headers:
                renamed_headers_type_0_item = renamed_headers_type_0_item_data.to_dict()
                renamed_headers.append(renamed_headers_type_0_item)


        else:
            renamed_headers = self.renamed_headers

        sample_rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.sample_rows, Unset):
            sample_rows = UNSET
        elif isinstance(self.sample_rows, list):
            sample_rows = []
            for sample_rows_type_0_item_data in self.sample_rows:
                sample_rows_type_0_item = sample_rows_type_0_item_data.to_dict()
                sample_rows.append(sample_rows_type_0_item)


        else:
            sample_rows = self.sample_rows

        suggested_mapping: list[dict[str, Any]] | None | Unset
        if isinstance(self.suggested_mapping, Unset):
            suggested_mapping = UNSET
        elif isinstance(self.suggested_mapping, list):
            suggested_mapping = []
            for suggested_mapping_type_0_item_data in self.suggested_mapping:
                suggested_mapping_type_0_item = suggested_mapping_type_0_item_data.to_dict()
                suggested_mapping.append(suggested_mapping_type_0_item)


        else:
            suggested_mapping = self.suggested_mapping

        supports_column_mapping = self.supports_column_mapping

        supports_duplicate_skip = self.supports_duplicate_skip

        supports_duplicate_update = self.supports_duplicate_update

        total_rows = self.total_rows

        updatable_columns: list[str] | None | Unset
        if isinstance(self.updatable_columns, Unset):
            updatable_columns = UNSET
        elif isinstance(self.updatable_columns, list):
            updatable_columns = self.updatable_columns


        else:
            updatable_columns = self.updatable_columns

        upload_key: None | str | Unset
        if isinstance(self.upload_key, Unset):
            upload_key = UNSET
        else:
            upload_key = self.upload_key

        valid_rows = self.valid_rows


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if duplicate_rows is not UNSET:
            field_dict["duplicateRows"] = duplicate_rows
        if errors is not UNSET:
            field_dict["errors"] = errors
        if headers is not UNSET:
            field_dict["headers"] = headers
        if invalid_rows is not UNSET:
            field_dict["invalidRows"] = invalid_rows
        if match_keys is not UNSET:
            field_dict["matchKeys"] = match_keys
        if new_rows is not UNSET:
            field_dict["newRows"] = new_rows
        if renamed_headers is not UNSET:
            field_dict["renamedHeaders"] = renamed_headers
        if sample_rows is not UNSET:
            field_dict["sampleRows"] = sample_rows
        if suggested_mapping is not UNSET:
            field_dict["suggestedMapping"] = suggested_mapping
        if supports_column_mapping is not UNSET:
            field_dict["supportsColumnMapping"] = supports_column_mapping
        if supports_duplicate_skip is not UNSET:
            field_dict["supportsDuplicateSkip"] = supports_duplicate_skip
        if supports_duplicate_update is not UNSET:
            field_dict["supportsDuplicateUpdate"] = supports_duplicate_update
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if updatable_columns is not UNSET:
            field_dict["updatableColumns"] = updatable_columns
        if upload_key is not UNSET:
            field_dict["uploadKey"] = upload_key
        if valid_rows is not UNSET:
            field_dict["validRows"] = valid_rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_import_match_key_dto import OfficeImportMatchKeyDto # noqa: PLC0415
        from ..models.office_import_preview_error_dto import OfficeImportPreviewErrorDto # noqa: PLC0415
        from ..models.office_import_preview_row_dto import OfficeImportPreviewRowDto # noqa: PLC0415
        from ..models.office_import_renamed_header_dto import OfficeImportRenamedHeaderDto # noqa: PLC0415
        from ..models.office_import_suggested_mapping_dto import OfficeImportSuggestedMappingDto # noqa: PLC0415
        d = dict(src_dict)
        duplicate_rows = d.pop("duplicateRows", UNSET)

        def _parse_errors(data: object) -> list[OfficeImportPreviewErrorDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in (_errors_type_0):
                    errors_type_0_item = OfficeImportPreviewErrorDto.from_dict(errors_type_0_item_data)



                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportPreviewErrorDto] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))


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


        invalid_rows = d.pop("invalidRows", UNSET)

        def _parse_match_keys(data: object) -> list[OfficeImportMatchKeyDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                match_keys_type_0 = []
                _match_keys_type_0 = data
                for match_keys_type_0_item_data in (_match_keys_type_0):
                    match_keys_type_0_item = OfficeImportMatchKeyDto.from_dict(match_keys_type_0_item_data)



                    match_keys_type_0.append(match_keys_type_0_item)

                return match_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportMatchKeyDto] | None | Unset, data)

        match_keys = _parse_match_keys(d.pop("matchKeys", UNSET))


        new_rows = d.pop("newRows", UNSET)

        def _parse_renamed_headers(data: object) -> list[OfficeImportRenamedHeaderDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                renamed_headers_type_0 = []
                _renamed_headers_type_0 = data
                for renamed_headers_type_0_item_data in (_renamed_headers_type_0):
                    renamed_headers_type_0_item = OfficeImportRenamedHeaderDto.from_dict(renamed_headers_type_0_item_data)



                    renamed_headers_type_0.append(renamed_headers_type_0_item)

                return renamed_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportRenamedHeaderDto] | None | Unset, data)

        renamed_headers = _parse_renamed_headers(d.pop("renamedHeaders", UNSET))


        def _parse_sample_rows(data: object) -> list[OfficeImportPreviewRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sample_rows_type_0 = []
                _sample_rows_type_0 = data
                for sample_rows_type_0_item_data in (_sample_rows_type_0):
                    sample_rows_type_0_item = OfficeImportPreviewRowDto.from_dict(sample_rows_type_0_item_data)



                    sample_rows_type_0.append(sample_rows_type_0_item)

                return sample_rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportPreviewRowDto] | None | Unset, data)

        sample_rows = _parse_sample_rows(d.pop("sampleRows", UNSET))


        def _parse_suggested_mapping(data: object) -> list[OfficeImportSuggestedMappingDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                suggested_mapping_type_0 = []
                _suggested_mapping_type_0 = data
                for suggested_mapping_type_0_item_data in (_suggested_mapping_type_0):
                    suggested_mapping_type_0_item = OfficeImportSuggestedMappingDto.from_dict(suggested_mapping_type_0_item_data)



                    suggested_mapping_type_0.append(suggested_mapping_type_0_item)

                return suggested_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportSuggestedMappingDto] | None | Unset, data)

        suggested_mapping = _parse_suggested_mapping(d.pop("suggestedMapping", UNSET))


        supports_column_mapping = d.pop("supportsColumnMapping", UNSET)

        supports_duplicate_skip = d.pop("supportsDuplicateSkip", UNSET)

        supports_duplicate_update = d.pop("supportsDuplicateUpdate", UNSET)

        total_rows = d.pop("totalRows", UNSET)

        def _parse_updatable_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                updatable_columns_type_0 = cast(list[str], data)

                return updatable_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        updatable_columns = _parse_updatable_columns(d.pop("updatableColumns", UNSET))


        def _parse_upload_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_key = _parse_upload_key(d.pop("uploadKey", UNSET))


        valid_rows = d.pop("validRows", UNSET)

        office_import_preview_dto = cls(
            duplicate_rows=duplicate_rows,
            errors=errors,
            headers=headers,
            invalid_rows=invalid_rows,
            match_keys=match_keys,
            new_rows=new_rows,
            renamed_headers=renamed_headers,
            sample_rows=sample_rows,
            suggested_mapping=suggested_mapping,
            supports_column_mapping=supports_column_mapping,
            supports_duplicate_skip=supports_duplicate_skip,
            supports_duplicate_update=supports_duplicate_update,
            total_rows=total_rows,
            updatable_columns=updatable_columns,
            upload_key=upload_key,
            valid_rows=valid_rows,
        )

        return office_import_preview_dto


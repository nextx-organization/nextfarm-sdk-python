from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_confirm_import_request_column_mapping_type_0 import OfficeConfirmImportRequestColumnMappingType0
  from ..models.office_confirm_import_request_row_patches_type_0 import OfficeConfirmImportRequestRowPatchesType0





T = TypeVar("T", bound="OfficeConfirmImportRequest")



@_attrs_define
class OfficeConfirmImportRequest:
    

    column_mapping: None | OfficeConfirmImportRequestColumnMappingType0 | Unset = UNSET
    duplicate_strategy: None | str | Unset = UNSET
    match_key: None | str | Unset = UNSET
    options: Any | Unset = UNSET
    row_patches: None | OfficeConfirmImportRequestRowPatchesType0 | Unset = UNSET
    skip_empty_on_update: bool | None | Unset = UNSET
    skipped_row_numbers: list[int] | None | Unset = UNSET
    update_columns: list[str] | None | Unset = UNSET
    upload_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_confirm_import_request_column_mapping_type_0 import OfficeConfirmImportRequestColumnMappingType0 # noqa: PLC0415
        from ..models.office_confirm_import_request_row_patches_type_0 import OfficeConfirmImportRequestRowPatchesType0 # noqa: PLC0415
        column_mapping: dict[str, Any] | None | Unset
        if isinstance(self.column_mapping, Unset):
            column_mapping = UNSET
        elif isinstance(self.column_mapping, OfficeConfirmImportRequestColumnMappingType0):
            column_mapping = self.column_mapping.to_dict()
        else:
            column_mapping = self.column_mapping

        duplicate_strategy: None | str | Unset
        if isinstance(self.duplicate_strategy, Unset):
            duplicate_strategy = UNSET
        else:
            duplicate_strategy = self.duplicate_strategy

        match_key: None | str | Unset
        if isinstance(self.match_key, Unset):
            match_key = UNSET
        else:
            match_key = self.match_key

        options = self.options

        row_patches: dict[str, Any] | None | Unset
        if isinstance(self.row_patches, Unset):
            row_patches = UNSET
        elif isinstance(self.row_patches, OfficeConfirmImportRequestRowPatchesType0):
            row_patches = self.row_patches.to_dict()
        else:
            row_patches = self.row_patches

        skip_empty_on_update: bool | None | Unset
        if isinstance(self.skip_empty_on_update, Unset):
            skip_empty_on_update = UNSET
        else:
            skip_empty_on_update = self.skip_empty_on_update

        skipped_row_numbers: list[int] | None | Unset
        if isinstance(self.skipped_row_numbers, Unset):
            skipped_row_numbers = UNSET
        elif isinstance(self.skipped_row_numbers, list):
            skipped_row_numbers = self.skipped_row_numbers


        else:
            skipped_row_numbers = self.skipped_row_numbers

        update_columns: list[str] | None | Unset
        if isinstance(self.update_columns, Unset):
            update_columns = UNSET
        elif isinstance(self.update_columns, list):
            update_columns = self.update_columns


        else:
            update_columns = self.update_columns

        upload_key: None | str | Unset
        if isinstance(self.upload_key, Unset):
            upload_key = UNSET
        else:
            upload_key = self.upload_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if column_mapping is not UNSET:
            field_dict["columnMapping"] = column_mapping
        if duplicate_strategy is not UNSET:
            field_dict["duplicateStrategy"] = duplicate_strategy
        if match_key is not UNSET:
            field_dict["matchKey"] = match_key
        if options is not UNSET:
            field_dict["options"] = options
        if row_patches is not UNSET:
            field_dict["rowPatches"] = row_patches
        if skip_empty_on_update is not UNSET:
            field_dict["skipEmptyOnUpdate"] = skip_empty_on_update
        if skipped_row_numbers is not UNSET:
            field_dict["skippedRowNumbers"] = skipped_row_numbers
        if update_columns is not UNSET:
            field_dict["updateColumns"] = update_columns
        if upload_key is not UNSET:
            field_dict["uploadKey"] = upload_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_confirm_import_request_column_mapping_type_0 import OfficeConfirmImportRequestColumnMappingType0 # noqa: PLC0415
        from ..models.office_confirm_import_request_row_patches_type_0 import OfficeConfirmImportRequestRowPatchesType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_column_mapping(data: object) -> None | OfficeConfirmImportRequestColumnMappingType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                column_mapping_type_0 = OfficeConfirmImportRequestColumnMappingType0.from_dict(data)



                return column_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeConfirmImportRequestColumnMappingType0 | Unset, data)

        column_mapping = _parse_column_mapping(d.pop("columnMapping", UNSET))


        def _parse_duplicate_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicate_strategy = _parse_duplicate_strategy(d.pop("duplicateStrategy", UNSET))


        def _parse_match_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        match_key = _parse_match_key(d.pop("matchKey", UNSET))


        options = d.pop("options", UNSET)

        def _parse_row_patches(data: object) -> None | OfficeConfirmImportRequestRowPatchesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                row_patches_type_0 = OfficeConfirmImportRequestRowPatchesType0.from_dict(data)



                return row_patches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeConfirmImportRequestRowPatchesType0 | Unset, data)

        row_patches = _parse_row_patches(d.pop("rowPatches", UNSET))


        def _parse_skip_empty_on_update(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_empty_on_update = _parse_skip_empty_on_update(d.pop("skipEmptyOnUpdate", UNSET))


        def _parse_skipped_row_numbers(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skipped_row_numbers_type_0 = cast(list[int], data)

                return skipped_row_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        skipped_row_numbers = _parse_skipped_row_numbers(d.pop("skippedRowNumbers", UNSET))


        def _parse_update_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                update_columns_type_0 = cast(list[str], data)

                return update_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        update_columns = _parse_update_columns(d.pop("updateColumns", UNSET))


        def _parse_upload_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_key = _parse_upload_key(d.pop("uploadKey", UNSET))


        office_confirm_import_request = cls(
            column_mapping=column_mapping,
            duplicate_strategy=duplicate_strategy,
            match_key=match_key,
            options=options,
            row_patches=row_patches,
            skip_empty_on_update=skip_empty_on_update,
            skipped_row_numbers=skipped_row_numbers,
            update_columns=update_columns,
            upload_key=upload_key,
        )

        return office_confirm_import_request


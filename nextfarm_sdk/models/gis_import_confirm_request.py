from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_import_confirm_request_row_patches_type_0 import GisImportConfirmRequestRowPatchesType0





T = TypeVar("T", bound="GisImportConfirmRequest")



@_attrs_define
class GisImportConfirmRequest:
    

    duplicate_strategy: None | str | Unset = UNSET
    import_type: None | str | Unset = UNSET
    match_key: None | str | Unset = UNSET
    row_patches: GisImportConfirmRequestRowPatchesType0 | None | Unset = UNSET
    skipped_row_numbers: list[int] | None | Unset = UNSET
    upload_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_import_confirm_request_row_patches_type_0 import GisImportConfirmRequestRowPatchesType0 # noqa: PLC0415
        duplicate_strategy: None | str | Unset
        if isinstance(self.duplicate_strategy, Unset):
            duplicate_strategy = UNSET
        else:
            duplicate_strategy = self.duplicate_strategy

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

        row_patches: dict[str, Any] | None | Unset
        if isinstance(self.row_patches, Unset):
            row_patches = UNSET
        elif isinstance(self.row_patches, GisImportConfirmRequestRowPatchesType0):
            row_patches = self.row_patches.to_dict()
        else:
            row_patches = self.row_patches

        skipped_row_numbers: list[int] | None | Unset
        if isinstance(self.skipped_row_numbers, Unset):
            skipped_row_numbers = UNSET
        elif isinstance(self.skipped_row_numbers, list):
            skipped_row_numbers = self.skipped_row_numbers


        else:
            skipped_row_numbers = self.skipped_row_numbers

        upload_key: None | str | Unset
        if isinstance(self.upload_key, Unset):
            upload_key = UNSET
        else:
            upload_key = self.upload_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if duplicate_strategy is not UNSET:
            field_dict["duplicate_strategy"] = duplicate_strategy
        if import_type is not UNSET:
            field_dict["import_type"] = import_type
        if match_key is not UNSET:
            field_dict["match_key"] = match_key
        if row_patches is not UNSET:
            field_dict["row_patches"] = row_patches
        if skipped_row_numbers is not UNSET:
            field_dict["skipped_row_numbers"] = skipped_row_numbers
        if upload_key is not UNSET:
            field_dict["upload_key"] = upload_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_import_confirm_request_row_patches_type_0 import GisImportConfirmRequestRowPatchesType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_duplicate_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicate_strategy = _parse_duplicate_strategy(d.pop("duplicate_strategy", UNSET))


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


        def _parse_row_patches(data: object) -> GisImportConfirmRequestRowPatchesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                row_patches_type_0 = GisImportConfirmRequestRowPatchesType0.from_dict(data)



                return row_patches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GisImportConfirmRequestRowPatchesType0 | None | Unset, data)

        row_patches = _parse_row_patches(d.pop("row_patches", UNSET))


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

        skipped_row_numbers = _parse_skipped_row_numbers(d.pop("skipped_row_numbers", UNSET))


        def _parse_upload_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_key = _parse_upload_key(d.pop("upload_key", UNSET))


        gis_import_confirm_request = cls(
            duplicate_strategy=duplicate_strategy,
            import_type=import_type,
            match_key=match_key,
            row_patches=row_patches,
            skipped_row_numbers=skipped_row_numbers,
            upload_key=upload_key,
        )

        return gis_import_confirm_request


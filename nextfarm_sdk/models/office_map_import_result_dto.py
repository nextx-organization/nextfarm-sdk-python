from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_import_preview_dto import OfficeImportPreviewDto
  from ..models.office_import_target_column_dto import OfficeImportTargetColumnDto





T = TypeVar("T", bound="OfficeMapImportResultDto")



@_attrs_define
class OfficeMapImportResultDto:
    

    header_fingerprint: None | str | Unset = UNSET
    preview: OfficeImportPreviewDto | Unset = UNSET
    skipped_headers: list[str] | None | Unset = UNSET
    target_columns: list[OfficeImportTargetColumnDto] | None | Unset = UNSET
    unknown_headers: list[str] | None | Unset = UNSET
    unknown_targets: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_import_preview_dto import OfficeImportPreviewDto # noqa: PLC0415
        from ..models.office_import_target_column_dto import OfficeImportTargetColumnDto # noqa: PLC0415
        header_fingerprint: None | str | Unset
        if isinstance(self.header_fingerprint, Unset):
            header_fingerprint = UNSET
        else:
            header_fingerprint = self.header_fingerprint

        preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        skipped_headers: list[str] | None | Unset
        if isinstance(self.skipped_headers, Unset):
            skipped_headers = UNSET
        elif isinstance(self.skipped_headers, list):
            skipped_headers = self.skipped_headers


        else:
            skipped_headers = self.skipped_headers

        target_columns: list[dict[str, Any]] | None | Unset
        if isinstance(self.target_columns, Unset):
            target_columns = UNSET
        elif isinstance(self.target_columns, list):
            target_columns = []
            for target_columns_type_0_item_data in self.target_columns:
                target_columns_type_0_item = target_columns_type_0_item_data.to_dict()
                target_columns.append(target_columns_type_0_item)


        else:
            target_columns = self.target_columns

        unknown_headers: list[str] | None | Unset
        if isinstance(self.unknown_headers, Unset):
            unknown_headers = UNSET
        elif isinstance(self.unknown_headers, list):
            unknown_headers = self.unknown_headers


        else:
            unknown_headers = self.unknown_headers

        unknown_targets: list[str] | None | Unset
        if isinstance(self.unknown_targets, Unset):
            unknown_targets = UNSET
        elif isinstance(self.unknown_targets, list):
            unknown_targets = self.unknown_targets


        else:
            unknown_targets = self.unknown_targets


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if header_fingerprint is not UNSET:
            field_dict["headerFingerprint"] = header_fingerprint
        if preview is not UNSET:
            field_dict["preview"] = preview
        if skipped_headers is not UNSET:
            field_dict["skippedHeaders"] = skipped_headers
        if target_columns is not UNSET:
            field_dict["targetColumns"] = target_columns
        if unknown_headers is not UNSET:
            field_dict["unknownHeaders"] = unknown_headers
        if unknown_targets is not UNSET:
            field_dict["unknownTargets"] = unknown_targets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_import_preview_dto import OfficeImportPreviewDto # noqa: PLC0415
        from ..models.office_import_target_column_dto import OfficeImportTargetColumnDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_header_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_fingerprint = _parse_header_fingerprint(d.pop("headerFingerprint", UNSET))


        _preview = d.pop("preview", UNSET)
        preview: OfficeImportPreviewDto | Unset
        if isinstance(_preview,  Unset):
            preview = UNSET
        else:
            preview = OfficeImportPreviewDto.from_dict(_preview)




        def _parse_skipped_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skipped_headers_type_0 = cast(list[str], data)

                return skipped_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        skipped_headers = _parse_skipped_headers(d.pop("skippedHeaders", UNSET))


        def _parse_target_columns(data: object) -> list[OfficeImportTargetColumnDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                target_columns_type_0 = []
                _target_columns_type_0 = data
                for target_columns_type_0_item_data in (_target_columns_type_0):
                    target_columns_type_0_item = OfficeImportTargetColumnDto.from_dict(target_columns_type_0_item_data)



                    target_columns_type_0.append(target_columns_type_0_item)

                return target_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeImportTargetColumnDto] | None | Unset, data)

        target_columns = _parse_target_columns(d.pop("targetColumns", UNSET))


        def _parse_unknown_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unknown_headers_type_0 = cast(list[str], data)

                return unknown_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        unknown_headers = _parse_unknown_headers(d.pop("unknownHeaders", UNSET))


        def _parse_unknown_targets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unknown_targets_type_0 = cast(list[str], data)

                return unknown_targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        unknown_targets = _parse_unknown_targets(d.pop("unknownTargets", UNSET))


        office_map_import_result_dto = cls(
            header_fingerprint=header_fingerprint,
            preview=preview,
            skipped_headers=skipped_headers,
            target_columns=target_columns,
            unknown_headers=unknown_headers,
            unknown_targets=unknown_targets,
        )

        return office_map_import_result_dto


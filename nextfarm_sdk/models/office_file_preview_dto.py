from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_xlsx_sheet_preview import OfficeXlsxSheetPreview





T = TypeVar("T", bound="OfficeFilePreviewDto")



@_attrs_define
class OfficeFilePreviewDto:
    

    html: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    sheets: list[OfficeXlsxSheetPreview] | None | Unset = UNSET
    skipped_images: int | Unset = UNSET
    truncated: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_xlsx_sheet_preview import OfficeXlsxSheetPreview # noqa: PLC0415
        html: None | str | Unset
        if isinstance(self.html, Unset):
            html = UNSET
        else:
            html = self.html

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        sheets: list[dict[str, Any]] | None | Unset
        if isinstance(self.sheets, Unset):
            sheets = UNSET
        elif isinstance(self.sheets, list):
            sheets = []
            for sheets_type_0_item_data in self.sheets:
                sheets_type_0_item = sheets_type_0_item_data.to_dict()
                sheets.append(sheets_type_0_item)


        else:
            sheets = self.sheets

        skipped_images = self.skipped_images

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if html is not UNSET:
            field_dict["html"] = html
        if kind is not UNSET:
            field_dict["kind"] = kind
        if sheets is not UNSET:
            field_dict["sheets"] = sheets
        if skipped_images is not UNSET:
            field_dict["skippedImages"] = skipped_images
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_xlsx_sheet_preview import OfficeXlsxSheetPreview # noqa: PLC0415
        d = dict(src_dict)
        def _parse_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        html = _parse_html(d.pop("html", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_sheets(data: object) -> list[OfficeXlsxSheetPreview] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sheets_type_0 = []
                _sheets_type_0 = data
                for sheets_type_0_item_data in (_sheets_type_0):
                    sheets_type_0_item = OfficeXlsxSheetPreview.from_dict(sheets_type_0_item_data)



                    sheets_type_0.append(sheets_type_0_item)

                return sheets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeXlsxSheetPreview] | None | Unset, data)

        sheets = _parse_sheets(d.pop("sheets", UNSET))


        skipped_images = d.pop("skippedImages", UNSET)

        truncated = d.pop("truncated", UNSET)

        office_file_preview_dto = cls(
            html=html,
            kind=kind,
            sheets=sheets,
            skipped_images=skipped_images,
            truncated=truncated,
        )

        return office_file_preview_dto


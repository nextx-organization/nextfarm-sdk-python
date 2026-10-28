from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficePreviewPrintTemplateRequest")



@_attrs_define
class OfficePreviewPrintTemplateRequest:
    

    content_html: None | str | Unset = UNSET
    document_type: None | str | Unset = UNSET
    margin_mm: int | Unset = UNSET
    orientation: None | str | Unset = UNSET
    paper_size: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content_html: None | str | Unset
        if isinstance(self.content_html, Unset):
            content_html = UNSET
        else:
            content_html = self.content_html

        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        margin_mm = self.margin_mm

        orientation: None | str | Unset
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        paper_size: None | str | Unset
        if isinstance(self.paper_size, Unset):
            paper_size = UNSET
        else:
            paper_size = self.paper_size


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_html is not UNSET:
            field_dict["contentHtml"] = content_html
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if margin_mm is not UNSET:
            field_dict["marginMm"] = margin_mm
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if paper_size is not UNSET:
            field_dict["paperSize"] = paper_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_content_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_html = _parse_content_html(d.pop("contentHtml", UNSET))


        def _parse_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type = _parse_document_type(d.pop("documentType", UNSET))


        margin_mm = d.pop("marginMm", UNSET)

        def _parse_orientation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))


        def _parse_paper_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paper_size = _parse_paper_size(d.pop("paperSize", UNSET))


        office_preview_print_template_request = cls(
            content_html=content_html,
            document_type=document_type,
            margin_mm=margin_mm,
            orientation=orientation,
            paper_size=paper_size,
        )

        return office_preview_print_template_request


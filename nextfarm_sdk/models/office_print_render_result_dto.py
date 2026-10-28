from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficePrintRenderResultDto")



@_attrs_define
class OfficePrintRenderResultDto:
    

    document_type: None | str | Unset = UNSET
    html: None | str | Unset = UNSET
    margin_mm: int | Unset = UNSET
    orientation: None | str | Unset = UNSET
    paper_size: None | str | Unset = UNSET
    template_id: UUID | Unset = UNSET
    template_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        html: None | str | Unset
        if isinstance(self.html, Unset):
            html = UNSET
        else:
            html = self.html

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

        template_id: str | Unset = UNSET
        if not isinstance(self.template_id, Unset):
            template_id = str(self.template_id)

        template_name: None | str | Unset
        if isinstance(self.template_name, Unset):
            template_name = UNSET
        else:
            template_name = self.template_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if html is not UNSET:
            field_dict["html"] = html
        if margin_mm is not UNSET:
            field_dict["marginMm"] = margin_mm
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if paper_size is not UNSET:
            field_dict["paperSize"] = paper_size
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if template_name is not UNSET:
            field_dict["templateName"] = template_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type = _parse_document_type(d.pop("documentType", UNSET))


        def _parse_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        html = _parse_html(d.pop("html", UNSET))


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


        _template_id = d.pop("templateId", UNSET)
        template_id: UUID | Unset
        if isinstance(_template_id,  Unset):
            template_id = UNSET
        else:
            template_id = UUID(_template_id)




        def _parse_template_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_name = _parse_template_name(d.pop("templateName", UNSET))


        office_print_render_result_dto = cls(
            document_type=document_type,
            html=html,
            margin_mm=margin_mm,
            orientation=orientation,
            paper_size=paper_size,
            template_id=template_id,
            template_name=template_name,
        )

        return office_print_render_result_dto


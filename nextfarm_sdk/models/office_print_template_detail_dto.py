from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_print_template_dto import OfficePrintTemplateDto





T = TypeVar("T", bound="OfficePrintTemplateDetailDto")



@_attrs_define
class OfficePrintTemplateDetailDto:
    

    content_html: None | str | Unset = UNSET
    template: OfficePrintTemplateDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_print_template_dto import OfficePrintTemplateDto # noqa: PLC0415
        content_html: None | str | Unset
        if isinstance(self.content_html, Unset):
            content_html = UNSET
        else:
            content_html = self.content_html

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_html is not UNSET:
            field_dict["contentHtml"] = content_html
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_print_template_dto import OfficePrintTemplateDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_content_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_html = _parse_content_html(d.pop("contentHtml", UNSET))


        _template = d.pop("template", UNSET)
        template: OfficePrintTemplateDto | Unset
        if isinstance(_template,  Unset):
            template = UNSET
        else:
            template = OfficePrintTemplateDto.from_dict(_template)




        office_print_template_detail_dto = cls(
            content_html=content_html,
            template=template,
        )

        return office_print_template_detail_dto


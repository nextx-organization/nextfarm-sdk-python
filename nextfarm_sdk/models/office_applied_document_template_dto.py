from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAppliedDocumentTemplateDto")



@_attrs_define
class OfficeAppliedDocumentTemplateDto:
    

    page_id: UUID | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        page_id: str | Unset = UNSET
        if not isinstance(self.page_id, Unset):
            page_id = str(self.page_id)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if page_id is not UNSET:
            field_dict["pageId"] = page_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _page_id = d.pop("pageId", UNSET)
        page_id: UUID | Unset
        if isinstance(_page_id,  Unset):
            page_id = UNSET
        else:
            page_id = UUID(_page_id)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_applied_document_template_dto = cls(
            page_id=page_id,
            title=title,
        )

        return office_applied_document_template_dto


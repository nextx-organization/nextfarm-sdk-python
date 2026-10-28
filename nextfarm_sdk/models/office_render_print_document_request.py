from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeRenderPrintDocumentRequest")



@_attrs_define
class OfficeRenderPrintDocumentRequest:
    

    document_type: None | str | Unset = UNSET
    entity_id: UUID | Unset = UNSET
    template_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        elif isinstance(self.template_id, UUID):
            template_id = str(self.template_id)
        else:
            template_id = self.template_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id

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


        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        def _parse_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                template_id_type_0 = UUID(data)



                return template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        template_id = _parse_template_id(d.pop("templateId", UNSET))


        office_render_print_document_request = cls(
            document_type=document_type,
            entity_id=entity_id,
            template_id=template_id,
        )

        return office_render_print_document_request


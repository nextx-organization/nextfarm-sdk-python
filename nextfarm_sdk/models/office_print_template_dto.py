from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficePrintTemplateDto")



@_attrs_define
class OfficePrintTemplateDto:
    

    current_version_number: int | Unset = UNSET
    description: None | str | Unset = UNSET
    document_type: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    margin_mm: int | Unset = UNSET
    name: None | str | Unset = UNSET
    orientation: None | str | Unset = UNSET
    paper_size: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        current_version_number = self.current_version_number

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_active = self.is_active

        is_default = self.is_default

        margin_mm = self.margin_mm

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current_version_number is not UNSET:
            field_dict["currentVersionNumber"] = current_version_number
        if description is not UNSET:
            field_dict["description"] = description
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if margin_mm is not UNSET:
            field_dict["marginMm"] = margin_mm
        if name is not UNSET:
            field_dict["name"] = name
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if paper_size is not UNSET:
            field_dict["paperSize"] = paper_size
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_version_number = d.pop("currentVersionNumber", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type = _parse_document_type(d.pop("documentType", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_active = d.pop("isActive", UNSET)

        is_default = d.pop("isDefault", UNSET)

        margin_mm = d.pop("marginMm", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


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


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_print_template_dto = cls(
            current_version_number=current_version_number,
            description=description,
            document_type=document_type,
            id=id,
            is_active=is_active,
            is_default=is_default,
            margin_mm=margin_mm,
            name=name,
            orientation=orientation,
            paper_size=paper_size,
            updated_at=updated_at,
        )

        return office_print_template_dto


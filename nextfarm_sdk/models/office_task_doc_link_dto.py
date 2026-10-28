from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_task_doc_link_dto_node_type import check_office_task_doc_link_dto_node_type
from ..models.office_task_doc_link_dto_node_type import OfficeTaskDocLinkDtoNodeType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeTaskDocLinkDto")



@_attrs_define
class OfficeTaskDocLinkDto:
    

    breadcrumb: list[str] | None | Unset = UNSET
    can_view: bool | Unset = UNSET
    doc_node_id: UUID | Unset = UNSET
    doc_updated_at: datetime.datetime | None | Unset = UNSET
    doc_updated_by: None | Unset | UUID = UNSET
    icon: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_missing: bool | Unset = UNSET
    linked_at: datetime.datetime | Unset = UNSET
    linked_by: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    node_type: OfficeTaskDocLinkDtoNodeType | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        breadcrumb: list[str] | None | Unset
        if isinstance(self.breadcrumb, Unset):
            breadcrumb = UNSET
        elif isinstance(self.breadcrumb, list):
            breadcrumb = self.breadcrumb


        else:
            breadcrumb = self.breadcrumb

        can_view = self.can_view

        doc_node_id: str | Unset = UNSET
        if not isinstance(self.doc_node_id, Unset):
            doc_node_id = str(self.doc_node_id)

        doc_updated_at: None | str | Unset
        if isinstance(self.doc_updated_at, Unset):
            doc_updated_at = UNSET
        elif isinstance(self.doc_updated_at, datetime.datetime):
            doc_updated_at = self.doc_updated_at.isoformat()
        else:
            doc_updated_at = self.doc_updated_at

        doc_updated_by: None | str | Unset
        if isinstance(self.doc_updated_by, Unset):
            doc_updated_by = UNSET
        elif isinstance(self.doc_updated_by, UUID):
            doc_updated_by = str(self.doc_updated_by)
        else:
            doc_updated_by = self.doc_updated_by

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_missing = self.is_missing

        linked_at: str | Unset = UNSET
        if not isinstance(self.linked_at, Unset):
            linked_at = self.linked_at.isoformat()

        linked_by: str | Unset = UNSET
        if not isinstance(self.linked_by, Unset):
            linked_by = str(self.linked_by)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        node_type: str | Unset = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type


        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if breadcrumb is not UNSET:
            field_dict["breadcrumb"] = breadcrumb
        if can_view is not UNSET:
            field_dict["canView"] = can_view
        if doc_node_id is not UNSET:
            field_dict["docNodeId"] = doc_node_id
        if doc_updated_at is not UNSET:
            field_dict["docUpdatedAt"] = doc_updated_at
        if doc_updated_by is not UNSET:
            field_dict["docUpdatedBy"] = doc_updated_by
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if is_missing is not UNSET:
            field_dict["isMissing"] = is_missing
        if linked_at is not UNSET:
            field_dict["linkedAt"] = linked_at
        if linked_by is not UNSET:
            field_dict["linkedBy"] = linked_by
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_breadcrumb(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breadcrumb_type_0 = cast(list[str], data)

                return breadcrumb_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        breadcrumb = _parse_breadcrumb(d.pop("breadcrumb", UNSET))


        can_view = d.pop("canView", UNSET)

        _doc_node_id = d.pop("docNodeId", UNSET)
        doc_node_id: UUID | Unset
        if isinstance(_doc_node_id,  Unset):
            doc_node_id = UNSET
        else:
            doc_node_id = UUID(_doc_node_id)




        def _parse_doc_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                doc_updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return doc_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        doc_updated_at = _parse_doc_updated_at(d.pop("docUpdatedAt", UNSET))


        def _parse_doc_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                doc_updated_by_type_0 = UUID(data)



                return doc_updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        doc_updated_by = _parse_doc_updated_by(d.pop("docUpdatedBy", UNSET))


        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_missing = d.pop("isMissing", UNSET)

        _linked_at = d.pop("linkedAt", UNSET)
        linked_at: datetime.datetime | Unset
        if isinstance(_linked_at,  Unset):
            linked_at = UNSET
        else:
            linked_at = datetime.datetime.fromisoformat(_linked_at)




        _linked_by = d.pop("linkedBy", UNSET)
        linked_by: UUID | Unset
        if isinstance(_linked_by,  Unset):
            linked_by = UNSET
        else:
            linked_by = UUID(_linked_by)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _node_type = d.pop("nodeType", UNSET)
        node_type: OfficeTaskDocLinkDtoNodeType | Unset
        if isinstance(_node_type,  Unset):
            node_type = UNSET
        else:
            node_type = check_office_task_doc_link_dto_node_type(_node_type)




        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        office_task_doc_link_dto = cls(
            breadcrumb=breadcrumb,
            can_view=can_view,
            doc_node_id=doc_node_id,
            doc_updated_at=doc_updated_at,
            doc_updated_by=doc_updated_by,
            icon=icon,
            id=id,
            is_missing=is_missing,
            linked_at=linked_at,
            linked_by=linked_by,
            name=name,
            node_type=node_type,
            note=note,
        )

        return office_task_doc_link_dto


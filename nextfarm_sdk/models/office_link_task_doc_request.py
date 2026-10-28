from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeLinkTaskDocRequest")



@_attrs_define
class OfficeLinkTaskDocRequest:
    

    doc_node_id: UUID | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        doc_node_id: str | Unset = UNSET
        if not isinstance(self.doc_node_id, Unset):
            doc_node_id = str(self.doc_node_id)

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if doc_node_id is not UNSET:
            field_dict["docNodeId"] = doc_node_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _doc_node_id = d.pop("docNodeId", UNSET)
        doc_node_id: UUID | Unset
        if isinstance(_doc_node_id,  Unset):
            doc_node_id = UNSET
        else:
            doc_node_id = UUID(_doc_node_id)




        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        office_link_task_doc_request = cls(
            doc_node_id=doc_node_id,
            note=note,
        )

        return office_link_task_doc_request


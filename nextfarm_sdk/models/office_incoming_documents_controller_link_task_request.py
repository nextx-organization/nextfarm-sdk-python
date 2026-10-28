from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeIncomingDocumentsControllerLinkTaskRequest")



@_attrs_define
class OfficeIncomingDocumentsControllerLinkTaskRequest:
    

    task_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        task_id: str | Unset = UNSET
        if not isinstance(self.task_id, Unset):
            task_id = str(self.task_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if task_id is not UNSET:
            field_dict["taskId"] = task_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _task_id = d.pop("taskId", UNSET)
        task_id: UUID | Unset
        if isinstance(_task_id,  Unset):
            task_id = UNSET
        else:
            task_id = UUID(_task_id)




        office_incoming_documents_controller_link_task_request = cls(
            task_id=task_id,
        )

        return office_incoming_documents_controller_link_task_request


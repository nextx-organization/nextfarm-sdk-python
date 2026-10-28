from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskDependencyDto")



@_attrs_define
class OfficeTaskDependencyDto:
    

    depends_on_task_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    is_resolved: bool | Unset = UNSET
    status: None | str | Unset = UNSET
    task_id: UUID | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        depends_on_task_id: str | Unset = UNSET
        if not isinstance(self.depends_on_task_id, Unset):
            depends_on_task_id = str(self.depends_on_task_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_resolved = self.is_resolved

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        task_id: str | Unset = UNSET
        if not isinstance(self.task_id, Unset):
            task_id = str(self.task_id)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if depends_on_task_id is not UNSET:
            field_dict["dependsOnTaskId"] = depends_on_task_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_resolved is not UNSET:
            field_dict["isResolved"] = is_resolved
        if status is not UNSET:
            field_dict["status"] = status
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _depends_on_task_id = d.pop("dependsOnTaskId", UNSET)
        depends_on_task_id: UUID | Unset
        if isinstance(_depends_on_task_id,  Unset):
            depends_on_task_id = UNSET
        else:
            depends_on_task_id = UUID(_depends_on_task_id)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_resolved = d.pop("isResolved", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _task_id = d.pop("taskId", UNSET)
        task_id: UUID | Unset
        if isinstance(_task_id,  Unset):
            task_id = UNSET
        else:
            task_id = UUID(_task_id)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_task_dependency_dto = cls(
            depends_on_task_id=depends_on_task_id,
            id=id,
            is_resolved=is_resolved,
            status=status,
            task_id=task_id,
            title=title,
        )

        return office_task_dependency_dto


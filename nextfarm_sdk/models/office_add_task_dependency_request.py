from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeAddTaskDependencyRequest")



@_attrs_define
class OfficeAddTaskDependencyRequest:
    

    depends_on_task_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        depends_on_task_id: str | Unset = UNSET
        if not isinstance(self.depends_on_task_id, Unset):
            depends_on_task_id = str(self.depends_on_task_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if depends_on_task_id is not UNSET:
            field_dict["dependsOnTaskId"] = depends_on_task_id

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




        office_add_task_dependency_request = cls(
            depends_on_task_id=depends_on_task_id,
        )

        return office_add_task_dependency_request


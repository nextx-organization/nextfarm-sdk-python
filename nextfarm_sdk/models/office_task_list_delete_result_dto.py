from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeTaskListDeleteResultDto")



@_attrs_define
class OfficeTaskListDeleteResultDto:
    

    deleted_groups: int | Unset = UNSET
    deleted_tasks: int | Unset = UNSET
    mode: None | str | Unset = UNSET
    moved_groups: int | Unset = UNSET
    moved_tasks: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_groups = self.deleted_groups

        deleted_tasks = self.deleted_tasks

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        moved_groups = self.moved_groups

        moved_tasks = self.moved_tasks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_groups is not UNSET:
            field_dict["deletedGroups"] = deleted_groups
        if deleted_tasks is not UNSET:
            field_dict["deletedTasks"] = deleted_tasks
        if mode is not UNSET:
            field_dict["mode"] = mode
        if moved_groups is not UNSET:
            field_dict["movedGroups"] = moved_groups
        if moved_tasks is not UNSET:
            field_dict["movedTasks"] = moved_tasks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted_groups = d.pop("deletedGroups", UNSET)

        deleted_tasks = d.pop("deletedTasks", UNSET)

        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        moved_groups = d.pop("movedGroups", UNSET)

        moved_tasks = d.pop("movedTasks", UNSET)

        office_task_list_delete_result_dto = cls(
            deleted_groups=deleted_groups,
            deleted_tasks=deleted_tasks,
            mode=mode,
            moved_groups=moved_groups,
            moved_tasks=moved_tasks,
        )

        return office_task_list_delete_result_dto


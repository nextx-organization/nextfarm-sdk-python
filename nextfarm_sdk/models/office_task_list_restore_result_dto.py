from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskListRestoreResultDto")



@_attrs_define
class OfficeTaskListRestoreResultDto:
    

    group_id: None | Unset | UUID = UNSET
    restored_groups: int | Unset = UNSET
    restored_tasks: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        restored_groups = self.restored_groups

        restored_tasks = self.restored_tasks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if restored_groups is not UNSET:
            field_dict["restoredGroups"] = restored_groups
        if restored_tasks is not UNSET:
            field_dict["restoredTasks"] = restored_tasks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)



                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))


        restored_groups = d.pop("restoredGroups", UNSET)

        restored_tasks = d.pop("restoredTasks", UNSET)

        office_task_list_restore_result_dto = cls(
            group_id=group_id,
            restored_groups=restored_groups,
            restored_tasks=restored_tasks,
        )

        return office_task_list_restore_result_dto


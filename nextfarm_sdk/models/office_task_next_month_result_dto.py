from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_group_dto import OfficeTaskGroupDto
  from ..models.office_task_list_dto import OfficeTaskListDto





T = TypeVar("T", bound="OfficeTaskNextMonthResultDto")



@_attrs_define
class OfficeTaskNextMonthResultDto:
    

    groups: list[OfficeTaskGroupDto] | None | Unset = UNSET
    list_: OfficeTaskListDto | Unset = UNSET
    moved_tasks: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_group_dto import OfficeTaskGroupDto # noqa: PLC0415
        from ..models.office_task_list_dto import OfficeTaskListDto # noqa: PLC0415
        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)


        else:
            groups = self.groups

        list_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_, Unset):
            list_ = self.list_.to_dict()

        moved_tasks = self.moved_tasks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if groups is not UNSET:
            field_dict["groups"] = groups
        if list_ is not UNSET:
            field_dict["list"] = list_
        if moved_tasks is not UNSET:
            field_dict["movedTasks"] = moved_tasks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_group_dto import OfficeTaskGroupDto # noqa: PLC0415
        from ..models.office_task_list_dto import OfficeTaskListDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_groups(data: object) -> list[OfficeTaskGroupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in (_groups_type_0):
                    groups_type_0_item = OfficeTaskGroupDto.from_dict(groups_type_0_item_data)



                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskGroupDto] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        _list_ = d.pop("list", UNSET)
        list_: OfficeTaskListDto | Unset
        if isinstance(_list_,  Unset):
            list_ = UNSET
        else:
            list_ = OfficeTaskListDto.from_dict(_list_)




        moved_tasks = d.pop("movedTasks", UNSET)

        office_task_next_month_result_dto = cls(
            groups=groups,
            list_=list_,
            moved_tasks=moved_tasks,
        )

        return office_task_next_month_result_dto


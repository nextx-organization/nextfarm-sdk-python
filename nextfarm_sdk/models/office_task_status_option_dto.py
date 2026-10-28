from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskStatusOptionDto")



@_attrs_define
class OfficeTaskStatusOptionDto:
    

    category: None | str | Unset = UNSET
    color_tag: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    sort_order: int | Unset = UNSET
    task_count: int | Unset = UNSET
    task_list_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        color_tag: None | str | Unset
        if isinstance(self.color_tag, Unset):
            color_tag = UNSET
        else:
            color_tag = self.color_tag

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sort_order = self.sort_order

        task_count = self.task_count

        task_list_id: str | Unset = UNSET
        if not isinstance(self.task_list_id, Unset):
            task_list_id = str(self.task_list_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if color_tag is not UNSET:
            field_dict["colorTag"] = color_tag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if task_count is not UNSET:
            field_dict["taskCount"] = task_count
        if task_list_id is not UNSET:
            field_dict["taskListId"] = task_list_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_color_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_tag = _parse_color_tag(d.pop("colorTag", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        task_count = d.pop("taskCount", UNSET)

        _task_list_id = d.pop("taskListId", UNSET)
        task_list_id: UUID | Unset
        if isinstance(_task_list_id,  Unset):
            task_list_id = UNSET
        else:
            task_list_id = UUID(_task_list_id)




        office_task_status_option_dto = cls(
            category=category,
            color_tag=color_tag,
            id=id,
            name=name,
            sort_order=sort_order,
            task_count=task_count,
            task_list_id=task_list_id,
        )

        return office_task_status_option_dto


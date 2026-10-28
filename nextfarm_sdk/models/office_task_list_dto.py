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






T = TypeVar("T", bound="OfficeTaskListDto")



@_attrs_define
class OfficeTaskListDto:
    

    color_tag: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    done_count: int | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    group_id: None | Unset | UUID = UNSET
    health: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_pinned: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_activity_at: datetime.datetime | None | Unset = UNSET
    lead_user_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    open_count: int | Unset = UNSET
    overdue_count: int | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    pin_sort_order: int | None | Unset = UNSET
    sort_order: int | Unset = UNSET
    task_count: int | Unset = UNSET
    unassigned_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        color_tag: None | str | Unset
        if isinstance(self.color_tag, Unset):
            color_tag = UNSET
        else:
            color_tag = self.color_tag

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        done_count = self.done_count

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        health: None | str | Unset
        if isinstance(self.health, Unset):
            health = UNSET
        else:
            health = self.health

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_archived = self.is_archived

        is_pinned = self.is_pinned

        is_template = self.is_template

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        elif isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        lead_user_id: None | str | Unset
        if isinstance(self.lead_user_id, Unset):
            lead_user_id = UNSET
        elif isinstance(self.lead_user_id, UUID):
            lead_user_id = str(self.lead_user_id)
        else:
            lead_user_id = self.lead_user_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        open_count = self.open_count

        overdue_count = self.overdue_count

        owner_id: str | Unset = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = str(self.owner_id)

        pin_sort_order: int | None | Unset
        if isinstance(self.pin_sort_order, Unset):
            pin_sort_order = UNSET
        else:
            pin_sort_order = self.pin_sort_order

        sort_order = self.sort_order

        task_count = self.task_count

        unassigned_count = self.unassigned_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color_tag is not UNSET:
            field_dict["colorTag"] = color_tag
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if done_count is not UNSET:
            field_dict["doneCount"] = done_count
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if health is not UNSET:
            field_dict["health"] = health
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if is_template is not UNSET:
            field_dict["isTemplate"] = is_template
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if lead_user_id is not UNSET:
            field_dict["leadUserId"] = lead_user_id
        if name is not UNSET:
            field_dict["name"] = name
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if overdue_count is not UNSET:
            field_dict["overdueCount"] = overdue_count
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if pin_sort_order is not UNSET:
            field_dict["pinSortOrder"] = pin_sort_order
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if task_count is not UNSET:
            field_dict["taskCount"] = task_count
        if unassigned_count is not UNSET:
            field_dict["unassignedCount"] = unassigned_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_color_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_tag = _parse_color_tag(d.pop("colorTag", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        done_count = d.pop("doneCount", UNSET)

        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)



                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("dueAt", UNSET))


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


        def _parse_health(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        health = _parse_health(d.pop("health", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_archived = d.pop("isArchived", UNSET)

        is_pinned = d.pop("isPinned", UNSET)

        is_template = d.pop("isTemplate", UNSET)

        def _parse_last_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt", UNSET))


        def _parse_lead_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lead_user_id_type_0 = UUID(data)



                return lead_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        lead_user_id = _parse_lead_user_id(d.pop("leadUserId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        open_count = d.pop("openCount", UNSET)

        overdue_count = d.pop("overdueCount", UNSET)

        _owner_id = d.pop("ownerId", UNSET)
        owner_id: UUID | Unset
        if isinstance(_owner_id,  Unset):
            owner_id = UNSET
        else:
            owner_id = UUID(_owner_id)




        def _parse_pin_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pin_sort_order = _parse_pin_sort_order(d.pop("pinSortOrder", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        task_count = d.pop("taskCount", UNSET)

        unassigned_count = d.pop("unassignedCount", UNSET)

        office_task_list_dto = cls(
            color_tag=color_tag,
            created_at=created_at,
            done_count=done_count,
            due_at=due_at,
            group_id=group_id,
            health=health,
            id=id,
            is_archived=is_archived,
            is_pinned=is_pinned,
            is_template=is_template,
            last_activity_at=last_activity_at,
            lead_user_id=lead_user_id,
            name=name,
            open_count=open_count,
            overdue_count=overdue_count,
            owner_id=owner_id,
            pin_sort_order=pin_sort_order,
            sort_order=sort_order,
            task_count=task_count,
            unassigned_count=unassigned_count,
        )

        return office_task_list_dto


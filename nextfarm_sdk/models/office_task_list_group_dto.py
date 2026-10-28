from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskListGroupDto")



@_attrs_define
class OfficeTaskListGroupDto:
    

    department_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    is_archived: bool | Unset = UNSET
    kind: None | str | Unset = UNSET
    lead_user_id: None | Unset | UUID = UNSET
    list_count: int | Unset = UNSET
    member_ids: list[UUID] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    sort_order: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_archived = self.is_archived

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        lead_user_id: None | str | Unset
        if isinstance(self.lead_user_id, Unset):
            lead_user_id = UNSET
        elif isinstance(self.lead_user_id, UUID):
            lead_user_id = str(self.lead_user_id)
        else:
            lead_user_id = self.lead_user_id

        list_count = self.list_count

        member_ids: list[str] | None | Unset
        if isinstance(self.member_ids, Unset):
            member_ids = UNSET
        elif isinstance(self.member_ids, list):
            member_ids = []
            for member_ids_type_0_item_data in self.member_ids:
                member_ids_type_0_item = str(member_ids_type_0_item_data)
                member_ids.append(member_ids_type_0_item)


        else:
            member_ids = self.member_ids

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if kind is not UNSET:
            field_dict["kind"] = kind
        if lead_user_id is not UNSET:
            field_dict["leadUserId"] = lead_user_id
        if list_count is not UNSET:
            field_dict["listCount"] = list_count
        if member_ids is not UNSET:
            field_dict["memberIds"] = member_ids
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)



                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("departmentId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_archived = d.pop("isArchived", UNSET)

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


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


        list_count = d.pop("listCount", UNSET)

        def _parse_member_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_ids_type_0 = []
                _member_ids_type_0 = data
                for member_ids_type_0_item_data in (_member_ids_type_0):
                    member_ids_type_0_item = UUID(member_ids_type_0_item_data)



                    member_ids_type_0.append(member_ids_type_0_item)

                return member_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        member_ids = _parse_member_ids(d.pop("memberIds", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)



                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        office_task_list_group_dto = cls(
            department_id=department_id,
            id=id,
            is_archived=is_archived,
            kind=kind,
            lead_user_id=lead_user_id,
            list_count=list_count,
            member_ids=member_ids,
            name=name,
            parent_id=parent_id,
            sort_order=sort_order,
        )

        return office_task_list_group_dto


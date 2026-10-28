from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeOfficeDepartmentDto")



@_attrs_define
class OfficeOfficeDepartmentDto:
    

    display_order: int | Unset = UNSET
    id: UUID | Unset = UNSET
    member_count: int | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_order = self.display_order

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        member_count = self.member_count

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if id is not UNSET:
            field_dict["id"] = id
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_order = d.pop("displayOrder", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        member_count = d.pop("memberCount", UNSET)

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


        office_office_department_dto = cls(
            display_order=display_order,
            id=id,
            member_count=member_count,
            name=name,
            parent_id=parent_id,
        )

        return office_office_department_dto


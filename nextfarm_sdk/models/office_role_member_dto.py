from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeRoleMemberDto")



@_attrs_define
class OfficeRoleMemberDto:
    

    id: UUID | Unset = UNSET
    member_id: UUID | Unset = UNSET
    member_type: None | str | Unset = UNSET
    role_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        member_id: str | Unset = UNSET
        if not isinstance(self.member_id, Unset):
            member_id = str(self.member_id)

        member_type: None | str | Unset
        if isinstance(self.member_type, Unset):
            member_type = UNSET
        else:
            member_type = self.member_type

        role_id: str | Unset = UNSET
        if not isinstance(self.role_id, Unset):
            role_id = str(self.role_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if member_type is not UNSET:
            field_dict["memberType"] = member_type
        if role_id is not UNSET:
            field_dict["roleId"] = role_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _member_id = d.pop("memberId", UNSET)
        member_id: UUID | Unset
        if isinstance(_member_id,  Unset):
            member_id = UNSET
        else:
            member_id = UUID(_member_id)




        def _parse_member_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_type = _parse_member_type(d.pop("memberType", UNSET))


        _role_id = d.pop("roleId", UNSET)
        role_id: UUID | Unset
        if isinstance(_role_id,  Unset):
            role_id = UNSET
        else:
            role_id = UUID(_role_id)




        office_role_member_dto = cls(
            id=id,
            member_id=member_id,
            member_type=member_type,
            role_id=role_id,
        )

        return office_role_member_dto


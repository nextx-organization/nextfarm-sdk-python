from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_add_member_request_member_type import check_office_add_member_request_member_type
from ..models.office_add_member_request_member_type import OfficeAddMemberRequestMemberType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAddMemberRequest")



@_attrs_define
class OfficeAddMemberRequest:
    

    member_id: UUID | Unset = UNSET
    member_type: OfficeAddMemberRequestMemberType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        member_id: str | Unset = UNSET
        if not isinstance(self.member_id, Unset):
            member_id = str(self.member_id)

        member_type: str | Unset = UNSET
        if not isinstance(self.member_type, Unset):
            member_type = self.member_type



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if member_type is not UNSET:
            field_dict["memberType"] = member_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _member_id = d.pop("memberId", UNSET)
        member_id: UUID | Unset
        if isinstance(_member_id,  Unset):
            member_id = UNSET
        else:
            member_id = UUID(_member_id)




        _member_type = d.pop("memberType", UNSET)
        member_type: OfficeAddMemberRequestMemberType | Unset
        if isinstance(_member_type,  Unset):
            member_type = UNSET
        else:
            member_type = check_office_add_member_request_member_type(_member_type)




        office_add_member_request = cls(
            member_id=member_id,
            member_type=member_type,
        )

        return office_add_member_request


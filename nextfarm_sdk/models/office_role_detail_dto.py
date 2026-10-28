from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_role_grant_dto import OfficeRoleGrantDto
  from ..models.office_role_member_dto import OfficeRoleMemberDto





T = TypeVar("T", bound="OfficeRoleDetailDto")



@_attrs_define
class OfficeRoleDetailDto:
    

    app_id: UUID | Unset = UNSET
    grants: list[OfficeRoleGrantDto] | None | Unset = UNSET
    id: UUID | Unset = UNSET
    is_admin: bool | Unset = UNSET
    members: list[OfficeRoleMemberDto] | None | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_role_grant_dto import OfficeRoleGrantDto # noqa: PLC0415
        from ..models.office_role_member_dto import OfficeRoleMemberDto # noqa: PLC0415
        app_id: str | Unset = UNSET
        if not isinstance(self.app_id, Unset):
            app_id = str(self.app_id)

        grants: list[dict[str, Any]] | None | Unset
        if isinstance(self.grants, Unset):
            grants = UNSET
        elif isinstance(self.grants, list):
            grants = []
            for grants_type_0_item_data in self.grants:
                grants_type_0_item = grants_type_0_item_data.to_dict()
                grants.append(grants_type_0_item)


        else:
            grants = self.grants

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_admin = self.is_admin

        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)


        else:
            members = self.members

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if grants is not UNSET:
            field_dict["grants"] = grants
        if id is not UNSET:
            field_dict["id"] = id
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_role_grant_dto import OfficeRoleGrantDto # noqa: PLC0415
        from ..models.office_role_member_dto import OfficeRoleMemberDto # noqa: PLC0415
        d = dict(src_dict)
        _app_id = d.pop("appId", UNSET)
        app_id: UUID | Unset
        if isinstance(_app_id,  Unset):
            app_id = UNSET
        else:
            app_id = UUID(_app_id)




        def _parse_grants(data: object) -> list[OfficeRoleGrantDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                grants_type_0 = []
                _grants_type_0 = data
                for grants_type_0_item_data in (_grants_type_0):
                    grants_type_0_item = OfficeRoleGrantDto.from_dict(grants_type_0_item_data)



                    grants_type_0.append(grants_type_0_item)

                return grants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRoleGrantDto] | None | Unset, data)

        grants = _parse_grants(d.pop("grants", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_admin = d.pop("isAdmin", UNSET)

        def _parse_members(data: object) -> list[OfficeRoleMemberDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in (_members_type_0):
                    members_type_0_item = OfficeRoleMemberDto.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRoleMemberDto] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_role_detail_dto = cls(
            app_id=app_id,
            grants=grants,
            id=id,
            is_admin=is_admin,
            members=members,
            name=name,
        )

        return office_role_detail_dto


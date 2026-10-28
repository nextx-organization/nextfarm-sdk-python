from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeRoleDto")



@_attrs_define
class OfficeRoleDto:
    

    app_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    is_admin: bool | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        app_id: str | Unset = UNSET
        if not isinstance(self.app_id, Unset):
            app_id = str(self.app_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_admin = self.is_admin

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
        if id is not UNSET:
            field_dict["id"] = id
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _app_id = d.pop("appId", UNSET)
        app_id: UUID | Unset
        if isinstance(_app_id,  Unset):
            app_id = UNSET
        else:
            app_id = UUID(_app_id)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_admin = d.pop("isAdmin", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_role_dto = cls(
            app_id=app_id,
            id=id,
            is_admin=is_admin,
            name=name,
        )

        return office_role_dto


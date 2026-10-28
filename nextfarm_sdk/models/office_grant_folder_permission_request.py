from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_grant_folder_permission_request_permission_level import check_office_grant_folder_permission_request_permission_level
from ..models.office_grant_folder_permission_request_permission_level import OfficeGrantFolderPermissionRequestPermissionLevel
from ..models.office_grant_folder_permission_request_principal_type import check_office_grant_folder_permission_request_principal_type
from ..models.office_grant_folder_permission_request_principal_type import OfficeGrantFolderPermissionRequestPrincipalType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeGrantFolderPermissionRequest")



@_attrs_define
class OfficeGrantFolderPermissionRequest:
    

    permission_level: OfficeGrantFolderPermissionRequestPermissionLevel | Unset = UNSET
    principal_id: None | str | Unset = UNSET
    principal_type: OfficeGrantFolderPermissionRequestPrincipalType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        permission_level: str | Unset = UNSET
        if not isinstance(self.permission_level, Unset):
            permission_level = self.permission_level


        principal_id: None | str | Unset
        if isinstance(self.principal_id, Unset):
            principal_id = UNSET
        else:
            principal_id = self.principal_id

        principal_type: str | Unset = UNSET
        if not isinstance(self.principal_type, Unset):
            principal_type = self.principal_type



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if permission_level is not UNSET:
            field_dict["permissionLevel"] = permission_level
        if principal_id is not UNSET:
            field_dict["principalId"] = principal_id
        if principal_type is not UNSET:
            field_dict["principalType"] = principal_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _permission_level = d.pop("permissionLevel", UNSET)
        permission_level: OfficeGrantFolderPermissionRequestPermissionLevel | Unset
        if isinstance(_permission_level,  Unset):
            permission_level = UNSET
        else:
            permission_level = check_office_grant_folder_permission_request_permission_level(_permission_level)




        def _parse_principal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_id = _parse_principal_id(d.pop("principalId", UNSET))


        _principal_type = d.pop("principalType", UNSET)
        principal_type: OfficeGrantFolderPermissionRequestPrincipalType | Unset
        if isinstance(_principal_type,  Unset):
            principal_type = UNSET
        else:
            principal_type = check_office_grant_folder_permission_request_principal_type(_principal_type)




        office_grant_folder_permission_request = cls(
            permission_level=permission_level,
            principal_id=principal_id,
            principal_type=principal_type,
        )

        return office_grant_folder_permission_request


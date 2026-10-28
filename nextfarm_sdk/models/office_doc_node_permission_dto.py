from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_doc_node_permission_dto_grant_kind import check_office_doc_node_permission_dto_grant_kind
from ..models.office_doc_node_permission_dto_grant_kind import OfficeDocNodePermissionDtoGrantKind
from ..models.office_doc_node_permission_dto_permission_level import check_office_doc_node_permission_dto_permission_level
from ..models.office_doc_node_permission_dto_permission_level import OfficeDocNodePermissionDtoPermissionLevel
from ..models.office_doc_node_permission_dto_principal_type import check_office_doc_node_permission_dto_principal_type
from ..models.office_doc_node_permission_dto_principal_type import OfficeDocNodePermissionDtoPrincipalType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeDocNodePermissionDto")



@_attrs_define
class OfficeDocNodePermissionDto:
    

    grant_kind: OfficeDocNodePermissionDtoGrantKind | Unset = UNSET
    id: UUID | Unset = UNSET
    inherited_from_name: None | str | Unset = UNSET
    inherited_from_node_id: UUID | Unset = UNSET
    node_id: UUID | Unset = UNSET
    permission_level: OfficeDocNodePermissionDtoPermissionLevel | Unset = UNSET
    principal_id: None | str | Unset = UNSET
    principal_type: OfficeDocNodePermissionDtoPrincipalType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        grant_kind: str | Unset = UNSET
        if not isinstance(self.grant_kind, Unset):
            grant_kind = self.grant_kind


        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        inherited_from_name: None | str | Unset
        if isinstance(self.inherited_from_name, Unset):
            inherited_from_name = UNSET
        else:
            inherited_from_name = self.inherited_from_name

        inherited_from_node_id: str | Unset = UNSET
        if not isinstance(self.inherited_from_node_id, Unset):
            inherited_from_node_id = str(self.inherited_from_node_id)

        node_id: str | Unset = UNSET
        if not isinstance(self.node_id, Unset):
            node_id = str(self.node_id)

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
        if grant_kind is not UNSET:
            field_dict["grantKind"] = grant_kind
        if id is not UNSET:
            field_dict["id"] = id
        if inherited_from_name is not UNSET:
            field_dict["inheritedFromName"] = inherited_from_name
        if inherited_from_node_id is not UNSET:
            field_dict["inheritedFromNodeId"] = inherited_from_node_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
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
        _grant_kind = d.pop("grantKind", UNSET)
        grant_kind: OfficeDocNodePermissionDtoGrantKind | Unset
        if isinstance(_grant_kind,  Unset):
            grant_kind = UNSET
        else:
            grant_kind = check_office_doc_node_permission_dto_grant_kind(_grant_kind)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_inherited_from_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inherited_from_name = _parse_inherited_from_name(d.pop("inheritedFromName", UNSET))


        _inherited_from_node_id = d.pop("inheritedFromNodeId", UNSET)
        inherited_from_node_id: UUID | Unset
        if isinstance(_inherited_from_node_id,  Unset):
            inherited_from_node_id = UNSET
        else:
            inherited_from_node_id = UUID(_inherited_from_node_id)




        _node_id = d.pop("nodeId", UNSET)
        node_id: UUID | Unset
        if isinstance(_node_id,  Unset):
            node_id = UNSET
        else:
            node_id = UUID(_node_id)




        _permission_level = d.pop("permissionLevel", UNSET)
        permission_level: OfficeDocNodePermissionDtoPermissionLevel | Unset
        if isinstance(_permission_level,  Unset):
            permission_level = UNSET
        else:
            permission_level = check_office_doc_node_permission_dto_permission_level(_permission_level)




        def _parse_principal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_id = _parse_principal_id(d.pop("principalId", UNSET))


        _principal_type = d.pop("principalType", UNSET)
        principal_type: OfficeDocNodePermissionDtoPrincipalType | Unset
        if isinstance(_principal_type,  Unset):
            principal_type = UNSET
        else:
            principal_type = check_office_doc_node_permission_dto_principal_type(_principal_type)




        office_doc_node_permission_dto = cls(
            grant_kind=grant_kind,
            id=id,
            inherited_from_name=inherited_from_name,
            inherited_from_node_id=inherited_from_node_id,
            node_id=node_id,
            permission_level=permission_level,
            principal_id=principal_id,
            principal_type=principal_type,
        )

        return office_doc_node_permission_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_doc_node_dto_display_mode import check_office_doc_node_dto_display_mode
from ..models.office_doc_node_dto_display_mode import OfficeDocNodeDtoDisplayMode
from ..models.office_doc_node_dto_my_permission import check_office_doc_node_dto_my_permission
from ..models.office_doc_node_dto_my_permission import OfficeDocNodeDtoMyPermission
from ..models.office_doc_node_dto_node_type import check_office_doc_node_dto_node_type
from ..models.office_doc_node_dto_node_type import OfficeDocNodeDtoNodeType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeDocNodeDto")



@_attrs_define
class OfficeDocNodeDto:
    

    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    depth: int | Unset = UNSET
    display_mode: OfficeDocNodeDtoDisplayMode | Unset = UNSET
    has_children: bool | Unset = UNSET
    icon: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_restricted: bool | Unset = UNSET
    my_permission: OfficeDocNodeDtoMyPermission | Unset = UNSET
    name: None | str | Unset = UNSET
    node_type: OfficeDocNodeDtoNodeType | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    ref_id: None | Unset | UUID = UNSET
    target_id: None | Unset | UUID = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        depth = self.depth

        display_mode: str | Unset = UNSET
        if not isinstance(self.display_mode, Unset):
            display_mode = self.display_mode


        has_children = self.has_children

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_restricted = self.is_restricted

        my_permission: str | Unset = UNSET
        if not isinstance(self.my_permission, Unset):
            my_permission = self.my_permission


        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        node_type: str | Unset = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type


        owner_id: str | Unset = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = str(self.owner_id)

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        ref_id: None | str | Unset
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        elif isinstance(self.ref_id, UUID):
            ref_id = str(self.ref_id)
        else:
            ref_id = self.ref_id

        target_id: None | str | Unset
        if isinstance(self.target_id, Unset):
            target_id = UNSET
        elif isinstance(self.target_id, UUID):
            target_id = str(self.target_id)
        else:
            target_id = self.target_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if depth is not UNSET:
            field_dict["depth"] = depth
        if display_mode is not UNSET:
            field_dict["displayMode"] = display_mode
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if my_permission is not UNSET:
            field_dict["myPermission"] = my_permission
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if ref_id is not UNSET:
            field_dict["refId"] = ref_id
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _created_by = d.pop("createdBy", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)




        depth = d.pop("depth", UNSET)

        _display_mode = d.pop("displayMode", UNSET)
        display_mode: OfficeDocNodeDtoDisplayMode | Unset
        if isinstance(_display_mode,  Unset):
            display_mode = UNSET
        else:
            display_mode = check_office_doc_node_dto_display_mode(_display_mode)




        has_children = d.pop("hasChildren", UNSET)

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_restricted = d.pop("isRestricted", UNSET)

        _my_permission = d.pop("myPermission", UNSET)
        my_permission: OfficeDocNodeDtoMyPermission | Unset
        if isinstance(_my_permission,  Unset):
            my_permission = UNSET
        else:
            my_permission = check_office_doc_node_dto_my_permission(_my_permission)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _node_type = d.pop("nodeType", UNSET)
        node_type: OfficeDocNodeDtoNodeType | Unset
        if isinstance(_node_type,  Unset):
            node_type = UNSET
        else:
            node_type = check_office_doc_node_dto_node_type(_node_type)




        _owner_id = d.pop("ownerId", UNSET)
        owner_id: UUID | Unset
        if isinstance(_owner_id,  Unset):
            owner_id = UNSET
        else:
            owner_id = UUID(_owner_id)




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


        def _parse_ref_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ref_id_type_0 = UUID(data)



                return ref_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        ref_id = _parse_ref_id(d.pop("refId", UNSET))


        def _parse_target_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_id_type_0 = UUID(data)



                return target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        target_id = _parse_target_id(d.pop("targetId", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_doc_node_dto = cls(
            created_at=created_at,
            created_by=created_by,
            depth=depth,
            display_mode=display_mode,
            has_children=has_children,
            icon=icon,
            id=id,
            is_restricted=is_restricted,
            my_permission=my_permission,
            name=name,
            node_type=node_type,
            owner_id=owner_id,
            parent_id=parent_id,
            ref_id=ref_id,
            target_id=target_id,
            updated_at=updated_at,
        )

        return office_doc_node_dto


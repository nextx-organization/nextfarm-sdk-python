from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_create_doc_node_request_display_mode import check_office_create_doc_node_request_display_mode
from ..models.office_create_doc_node_request_display_mode import OfficeCreateDocNodeRequestDisplayMode
from ..models.office_create_doc_node_request_node_type import check_office_create_doc_node_request_node_type
from ..models.office_create_doc_node_request_node_type import OfficeCreateDocNodeRequestNodeType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCreateDocNodeRequest")



@_attrs_define
class OfficeCreateDocNodeRequest:
    

    display_mode: OfficeCreateDocNodeRequestDisplayMode | Unset = UNSET
    icon: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    node_type: OfficeCreateDocNodeRequestNodeType | Unset = UNSET
    owner_id: None | Unset | UUID = UNSET
    parent_id: None | Unset | UUID = UNSET
    ref_id: None | Unset | UUID = UNSET
    target_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_mode: str | Unset = UNSET
        if not isinstance(self.display_mode, Unset):
            display_mode = self.display_mode


        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        node_type: str | Unset = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type


        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        elif isinstance(self.owner_id, UUID):
            owner_id = str(self.owner_id)
        else:
            owner_id = self.owner_id

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if display_mode is not UNSET:
            field_dict["displayMode"] = display_mode
        if icon is not UNSET:
            field_dict["icon"] = icon
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _display_mode = d.pop("displayMode", UNSET)
        display_mode: OfficeCreateDocNodeRequestDisplayMode | Unset
        if isinstance(_display_mode,  Unset):
            display_mode = UNSET
        else:
            display_mode = check_office_create_doc_node_request_display_mode(_display_mode)




        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _node_type = d.pop("nodeType", UNSET)
        node_type: OfficeCreateDocNodeRequestNodeType | Unset
        if isinstance(_node_type,  Unset):
            node_type = UNSET
        else:
            node_type = check_office_create_doc_node_request_node_type(_node_type)




        def _parse_owner_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_id_type_0 = UUID(data)



                return owner_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))


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


        office_create_doc_node_request = cls(
            display_mode=display_mode,
            icon=icon,
            name=name,
            node_type=node_type,
            owner_id=owner_id,
            parent_id=parent_id,
            ref_id=ref_id,
            target_id=target_id,
        )

        return office_create_doc_node_request


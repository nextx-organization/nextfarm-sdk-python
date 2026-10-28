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
  from ..models.office_org_member_dto import OfficeOrgMemberDto





T = TypeVar("T", bound="OfficeOrgUnitNodeDto")



@_attrs_define
class OfficeOrgUnitNodeDto:
    

    children: list[OfficeOrgUnitNodeDto] | None | Unset = UNSET
    display_order: int | Unset = UNSET
    heads: list[OfficeOrgMemberDto] | None | Unset = UNSET
    heads_derived: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    members: list[OfficeOrgMemberDto] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_org_member_dto import OfficeOrgMemberDto # noqa: PLC0415
        children: list[dict[str, Any]] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)


        else:
            children = self.children

        display_order = self.display_order

        heads: list[dict[str, Any]] | None | Unset
        if isinstance(self.heads, Unset):
            heads = UNSET
        elif isinstance(self.heads, list):
            heads = []
            for heads_type_0_item_data in self.heads:
                heads_type_0_item = heads_type_0_item_data.to_dict()
                heads.append(heads_type_0_item)


        else:
            heads = self.heads

        heads_derived = self.heads_derived

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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
        if children is not UNSET:
            field_dict["children"] = children
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if heads is not UNSET:
            field_dict["heads"] = heads
        if heads_derived is not UNSET:
            field_dict["headsDerived"] = heads_derived
        if id is not UNSET:
            field_dict["id"] = id
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_org_member_dto import OfficeOrgMemberDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_children(data: object) -> list[OfficeOrgUnitNodeDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in (_children_type_0):
                    children_type_0_item = OfficeOrgUnitNodeDto.from_dict(children_type_0_item_data)



                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOrgUnitNodeDto] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))


        display_order = d.pop("displayOrder", UNSET)

        def _parse_heads(data: object) -> list[OfficeOrgMemberDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                heads_type_0 = []
                _heads_type_0 = data
                for heads_type_0_item_data in (_heads_type_0):
                    heads_type_0_item = OfficeOrgMemberDto.from_dict(heads_type_0_item_data)



                    heads_type_0.append(heads_type_0_item)

                return heads_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOrgMemberDto] | None | Unset, data)

        heads = _parse_heads(d.pop("heads", UNSET))


        heads_derived = d.pop("headsDerived", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_members(data: object) -> list[OfficeOrgMemberDto] | None | Unset:
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
                    members_type_0_item = OfficeOrgMemberDto.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOrgMemberDto] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


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


        office_org_unit_node_dto = cls(
            children=children,
            display_order=display_order,
            heads=heads,
            heads_derived=heads_derived,
            id=id,
            members=members,
            name=name,
            parent_id=parent_id,
        )

        return office_org_unit_node_dto


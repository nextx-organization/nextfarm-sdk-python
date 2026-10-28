from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeObjectiveTreeNodeDto")



@_attrs_define
class OfficeObjectiveTreeNodeDto:
    

    branch_id: None | Unset | UUID = UNSET
    children: list[OfficeObjectiveTreeNodeDto] | None | Unset = UNSET
    children_progress: int | None | Unset = UNSET
    department_id: None | Unset | UUID = UNSET
    depth: int | Unset = UNSET
    id: UUID | Unset = UNSET
    is_at_risk: bool | Unset = UNSET
    key_result_count: int | Unset = UNSET
    level: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    pace_status: None | str | Unset = UNSET
    parent_objective_id: None | Unset | UUID = UNSET
    progress: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

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

        children_progress: int | None | Unset
        if isinstance(self.children_progress, Unset):
            children_progress = UNSET
        else:
            children_progress = self.children_progress

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        depth = self.depth

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_at_risk = self.is_at_risk

        key_result_count = self.key_result_count

        level: None | str | Unset
        if isinstance(self.level, Unset):
            level = UNSET
        else:
            level = self.level

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        owner_id: str | Unset = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = str(self.owner_id)

        pace_status: None | str | Unset
        if isinstance(self.pace_status, Unset):
            pace_status = UNSET
        else:
            pace_status = self.pace_status

        parent_objective_id: None | str | Unset
        if isinstance(self.parent_objective_id, Unset):
            parent_objective_id = UNSET
        elif isinstance(self.parent_objective_id, UUID):
            parent_objective_id = str(self.parent_objective_id)
        else:
            parent_objective_id = self.parent_objective_id

        progress = self.progress


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if children is not UNSET:
            field_dict["children"] = children
        if children_progress is not UNSET:
            field_dict["childrenProgress"] = children_progress
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if depth is not UNSET:
            field_dict["depth"] = depth
        if id is not UNSET:
            field_dict["id"] = id
        if is_at_risk is not UNSET:
            field_dict["isAtRisk"] = is_at_risk
        if key_result_count is not UNSET:
            field_dict["keyResultCount"] = key_result_count
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if pace_status is not UNSET:
            field_dict["paceStatus"] = pace_status
        if parent_objective_id is not UNSET:
            field_dict["parentObjectiveId"] = parent_objective_id
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


        def _parse_children(data: object) -> list[OfficeObjectiveTreeNodeDto] | None | Unset:
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
                    children_type_0_item = OfficeObjectiveTreeNodeDto.from_dict(children_type_0_item_data)



                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeObjectiveTreeNodeDto] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))


        def _parse_children_progress(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        children_progress = _parse_children_progress(d.pop("childrenProgress", UNSET))


        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)



                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("departmentId", UNSET))


        depth = d.pop("depth", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_at_risk = d.pop("isAtRisk", UNSET)

        key_result_count = d.pop("keyResultCount", UNSET)

        def _parse_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level = _parse_level(d.pop("level", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _owner_id = d.pop("ownerId", UNSET)
        owner_id: UUID | Unset
        if isinstance(_owner_id,  Unset):
            owner_id = UNSET
        else:
            owner_id = UUID(_owner_id)




        def _parse_pace_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pace_status = _parse_pace_status(d.pop("paceStatus", UNSET))


        def _parse_parent_objective_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_objective_id_type_0 = UUID(data)



                return parent_objective_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_objective_id = _parse_parent_objective_id(d.pop("parentObjectiveId", UNSET))


        progress = d.pop("progress", UNSET)

        office_objective_tree_node_dto = cls(
            branch_id=branch_id,
            children=children,
            children_progress=children_progress,
            department_id=department_id,
            depth=depth,
            id=id,
            is_at_risk=is_at_risk,
            key_result_count=key_result_count,
            level=level,
            name=name,
            owner_id=owner_id,
            pace_status=pace_status,
            parent_objective_id=parent_objective_id,
            progress=progress,
        )

        return office_objective_tree_node_dto


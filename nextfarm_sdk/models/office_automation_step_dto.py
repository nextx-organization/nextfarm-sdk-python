from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAutomationStepDto")



@_attrs_define
class OfficeAutomationStepDto:
    

    action_type: None | str | Unset = UNSET
    branch_index: int | None | Unset = UNSET
    branch_label: None | str | Unset = UNSET
    condition_config: None | str | Unset = UNSET
    config: None | str | Unset = UNSET
    false_next_step_id: None | Unset | UUID = UNSET
    group_id: None | Unset | UUID = UNSET
    group_kind: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    loop_automation_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    next_step_id: None | Unset | UUID = UNSET
    order: int | Unset = UNSET
    split_ratio: int | None | Unset = UNSET
    step_type: None | str | Unset = UNSET
    true_next_step_id: None | Unset | UUID = UNSET
    wait_config: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action_type: None | str | Unset
        if isinstance(self.action_type, Unset):
            action_type = UNSET
        else:
            action_type = self.action_type

        branch_index: int | None | Unset
        if isinstance(self.branch_index, Unset):
            branch_index = UNSET
        else:
            branch_index = self.branch_index

        branch_label: None | str | Unset
        if isinstance(self.branch_label, Unset):
            branch_label = UNSET
        else:
            branch_label = self.branch_label

        condition_config: None | str | Unset
        if isinstance(self.condition_config, Unset):
            condition_config = UNSET
        else:
            condition_config = self.condition_config

        config: None | str | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        else:
            config = self.config

        false_next_step_id: None | str | Unset
        if isinstance(self.false_next_step_id, Unset):
            false_next_step_id = UNSET
        elif isinstance(self.false_next_step_id, UUID):
            false_next_step_id = str(self.false_next_step_id)
        else:
            false_next_step_id = self.false_next_step_id

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        group_kind: None | str | Unset
        if isinstance(self.group_kind, Unset):
            group_kind = UNSET
        else:
            group_kind = self.group_kind

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        loop_automation_id: None | str | Unset
        if isinstance(self.loop_automation_id, Unset):
            loop_automation_id = UNSET
        elif isinstance(self.loop_automation_id, UUID):
            loop_automation_id = str(self.loop_automation_id)
        else:
            loop_automation_id = self.loop_automation_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        next_step_id: None | str | Unset
        if isinstance(self.next_step_id, Unset):
            next_step_id = UNSET
        elif isinstance(self.next_step_id, UUID):
            next_step_id = str(self.next_step_id)
        else:
            next_step_id = self.next_step_id

        order = self.order

        split_ratio: int | None | Unset
        if isinstance(self.split_ratio, Unset):
            split_ratio = UNSET
        else:
            split_ratio = self.split_ratio

        step_type: None | str | Unset
        if isinstance(self.step_type, Unset):
            step_type = UNSET
        else:
            step_type = self.step_type

        true_next_step_id: None | str | Unset
        if isinstance(self.true_next_step_id, Unset):
            true_next_step_id = UNSET
        elif isinstance(self.true_next_step_id, UUID):
            true_next_step_id = str(self.true_next_step_id)
        else:
            true_next_step_id = self.true_next_step_id

        wait_config: None | str | Unset
        if isinstance(self.wait_config, Unset):
            wait_config = UNSET
        else:
            wait_config = self.wait_config


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if branch_index is not UNSET:
            field_dict["branchIndex"] = branch_index
        if branch_label is not UNSET:
            field_dict["branchLabel"] = branch_label
        if condition_config is not UNSET:
            field_dict["conditionConfig"] = condition_config
        if config is not UNSET:
            field_dict["config"] = config
        if false_next_step_id is not UNSET:
            field_dict["falseNextStepId"] = false_next_step_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_kind is not UNSET:
            field_dict["groupKind"] = group_kind
        if id is not UNSET:
            field_dict["id"] = id
        if loop_automation_id is not UNSET:
            field_dict["loopAutomationId"] = loop_automation_id
        if name is not UNSET:
            field_dict["name"] = name
        if next_step_id is not UNSET:
            field_dict["nextStepId"] = next_step_id
        if order is not UNSET:
            field_dict["order"] = order
        if split_ratio is not UNSET:
            field_dict["splitRatio"] = split_ratio
        if step_type is not UNSET:
            field_dict["stepType"] = step_type
        if true_next_step_id is not UNSET:
            field_dict["trueNextStepId"] = true_next_step_id
        if wait_config is not UNSET:
            field_dict["waitConfig"] = wait_config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_action_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_type = _parse_action_type(d.pop("actionType", UNSET))


        def _parse_branch_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        branch_index = _parse_branch_index(d.pop("branchIndex", UNSET))


        def _parse_branch_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_label = _parse_branch_label(d.pop("branchLabel", UNSET))


        def _parse_condition_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition_config = _parse_condition_config(d.pop("conditionConfig", UNSET))


        def _parse_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config = _parse_config(d.pop("config", UNSET))


        def _parse_false_next_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                false_next_step_id_type_0 = UUID(data)



                return false_next_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        false_next_step_id = _parse_false_next_step_id(d.pop("falseNextStepId", UNSET))


        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)



                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))


        def _parse_group_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_kind = _parse_group_kind(d.pop("groupKind", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_loop_automation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                loop_automation_id_type_0 = UUID(data)



                return loop_automation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        loop_automation_id = _parse_loop_automation_id(d.pop("loopAutomationId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_next_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_step_id_type_0 = UUID(data)



                return next_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        next_step_id = _parse_next_step_id(d.pop("nextStepId", UNSET))


        order = d.pop("order", UNSET)

        def _parse_split_ratio(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        split_ratio = _parse_split_ratio(d.pop("splitRatio", UNSET))


        def _parse_step_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_type = _parse_step_type(d.pop("stepType", UNSET))


        def _parse_true_next_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                true_next_step_id_type_0 = UUID(data)



                return true_next_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        true_next_step_id = _parse_true_next_step_id(d.pop("trueNextStepId", UNSET))


        def _parse_wait_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wait_config = _parse_wait_config(d.pop("waitConfig", UNSET))


        office_automation_step_dto = cls(
            action_type=action_type,
            branch_index=branch_index,
            branch_label=branch_label,
            condition_config=condition_config,
            config=config,
            false_next_step_id=false_next_step_id,
            group_id=group_id,
            group_kind=group_kind,
            id=id,
            loop_automation_id=loop_automation_id,
            name=name,
            next_step_id=next_step_id,
            order=order,
            split_ratio=split_ratio,
            step_type=step_type,
            true_next_step_id=true_next_step_id,
            wait_config=wait_config,
        )

        return office_automation_step_dto


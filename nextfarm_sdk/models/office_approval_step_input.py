from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_approval_step_condition_input import OfficeApprovalStepConditionInput





T = TypeVar("T", bound="OfficeApprovalStepInput")



@_attrs_define
class OfficeApprovalStepInput:
    

    approver_mode: None | str | Unset = UNSET
    condition: OfficeApprovalStepConditionInput | Unset = UNSET
    due_hours: int | None | Unset = UNSET
    escalate_on_overdue: bool | Unset = UNSET
    join_mode: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    rule: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_approval_step_condition_input import OfficeApprovalStepConditionInput # noqa: PLC0415
        approver_mode: None | str | Unset
        if isinstance(self.approver_mode, Unset):
            approver_mode = UNSET
        else:
            approver_mode = self.approver_mode

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        due_hours: int | None | Unset
        if isinstance(self.due_hours, Unset):
            due_hours = UNSET
        else:
            due_hours = self.due_hours

        escalate_on_overdue = self.escalate_on_overdue

        join_mode: None | str | Unset
        if isinstance(self.join_mode, Unset):
            join_mode = UNSET
        else:
            join_mode = self.join_mode

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        rule: None | str | Unset
        if isinstance(self.rule, Unset):
            rule = UNSET
        else:
            rule = self.rule


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approver_mode is not UNSET:
            field_dict["approverMode"] = approver_mode
        if condition is not UNSET:
            field_dict["condition"] = condition
        if due_hours is not UNSET:
            field_dict["dueHours"] = due_hours
        if escalate_on_overdue is not UNSET:
            field_dict["escalateOnOverdue"] = escalate_on_overdue
        if join_mode is not UNSET:
            field_dict["joinMode"] = join_mode
        if name is not UNSET:
            field_dict["name"] = name
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_approval_step_condition_input import OfficeApprovalStepConditionInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_approver_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approver_mode = _parse_approver_mode(d.pop("approverMode", UNSET))


        _condition = d.pop("condition", UNSET)
        condition: OfficeApprovalStepConditionInput | Unset
        if isinstance(_condition,  Unset):
            condition = UNSET
        else:
            condition = OfficeApprovalStepConditionInput.from_dict(_condition)




        def _parse_due_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        due_hours = _parse_due_hours(d.pop("dueHours", UNSET))


        escalate_on_overdue = d.pop("escalateOnOverdue", UNSET)

        def _parse_join_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        join_mode = _parse_join_mode(d.pop("joinMode", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rule = _parse_rule(d.pop("rule", UNSET))


        office_approval_step_input = cls(
            approver_mode=approver_mode,
            condition=condition,
            due_hours=due_hours,
            escalate_on_overdue=escalate_on_overdue,
            join_mode=join_mode,
            name=name,
            rule=rule,
        )

        return office_approval_step_input


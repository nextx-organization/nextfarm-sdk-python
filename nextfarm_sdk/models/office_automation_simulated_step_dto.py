from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeAutomationSimulatedStepDto")



@_attrs_define
class OfficeAutomationSimulatedStepDto:
    

    action_type: None | str | Unset = UNSET
    at: datetime.datetime | Unset = UNSET
    detail: None | str | Unset = UNSET
    order: int | Unset = UNSET
    outcome: None | str | Unset = UNSET
    step_id: UUID | Unset = UNSET
    step_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action_type: None | str | Unset
        if isinstance(self.action_type, Unset):
            action_type = UNSET
        else:
            action_type = self.action_type

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        order = self.order

        outcome: None | str | Unset
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        else:
            outcome = self.outcome

        step_id: str | Unset = UNSET
        if not isinstance(self.step_id, Unset):
            step_id = str(self.step_id)

        step_type: None | str | Unset
        if isinstance(self.step_type, Unset):
            step_type = UNSET
        else:
            step_type = self.step_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if at is not UNSET:
            field_dict["at"] = at
        if detail is not UNSET:
            field_dict["detail"] = detail
        if order is not UNSET:
            field_dict["order"] = order
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if step_id is not UNSET:
            field_dict["stepId"] = step_id
        if step_type is not UNSET:
            field_dict["stepType"] = step_type

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


        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at,  Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)




        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        order = d.pop("order", UNSET)

        def _parse_outcome(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outcome = _parse_outcome(d.pop("outcome", UNSET))


        _step_id = d.pop("stepId", UNSET)
        step_id: UUID | Unset
        if isinstance(_step_id,  Unset):
            step_id = UNSET
        else:
            step_id = UUID(_step_id)




        def _parse_step_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_type = _parse_step_type(d.pop("stepType", UNSET))


        office_automation_simulated_step_dto = cls(
            action_type=action_type,
            at=at,
            detail=detail,
            order=order,
            outcome=outcome,
            step_id=step_id,
            step_type=step_type,
        )

        return office_automation_simulated_step_dto


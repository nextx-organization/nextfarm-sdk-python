from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.office_automation_simulated_step_dto import OfficeAutomationSimulatedStepDto





T = TypeVar("T", bound="OfficeAutomationSimulationDto")



@_attrs_define
class OfficeAutomationSimulationDto:
    

    end_reason: None | str | Unset = UNSET
    ended_at: datetime.datetime | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    steps: list[OfficeAutomationSimulatedStepDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automation_simulated_step_dto import OfficeAutomationSimulatedStepDto # noqa: PLC0415
        end_reason: None | str | Unset
        if isinstance(self.end_reason, Unset):
            end_reason = UNSET
        else:
            end_reason = self.end_reason

        ended_at: str | Unset = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        steps: list[dict[str, Any]] | None | Unset
        if isinstance(self.steps, Unset):
            steps = UNSET
        elif isinstance(self.steps, list):
            steps = []
            for steps_type_0_item_data in self.steps:
                steps_type_0_item = steps_type_0_item_data.to_dict()
                steps.append(steps_type_0_item)


        else:
            steps = self.steps


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if end_reason is not UNSET:
            field_dict["endReason"] = end_reason
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automation_simulated_step_dto import OfficeAutomationSimulatedStepDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_end_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_reason = _parse_end_reason(d.pop("endReason", UNSET))


        _ended_at = d.pop("endedAt", UNSET)
        ended_at: datetime.datetime | Unset
        if isinstance(_ended_at,  Unset):
            ended_at = UNSET
        else:
            ended_at = datetime.datetime.fromisoformat(_ended_at)




        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        def _parse_steps(data: object) -> list[OfficeAutomationSimulatedStepDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                steps_type_0 = []
                _steps_type_0 = data
                for steps_type_0_item_data in (_steps_type_0):
                    steps_type_0_item = OfficeAutomationSimulatedStepDto.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAutomationSimulatedStepDto] | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))


        office_automation_simulation_dto = cls(
            end_reason=end_reason,
            ended_at=ended_at,
            started_at=started_at,
            steps=steps,
        )

        return office_automation_simulation_dto


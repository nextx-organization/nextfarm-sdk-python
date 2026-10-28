from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.iot_setup_step_dto import IotSetupStepDto





T = TypeVar("T", bound="IotSetupProgressResult")



@_attrs_define
class IotSetupProgressResult:
    

    completed: int | Unset = UNSET
    steps: list[IotSetupStepDto] | None | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_setup_step_dto import IotSetupStepDto # noqa: PLC0415
        completed = self.completed

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

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if completed is not UNSET:
            field_dict["completed"] = completed
        if steps is not UNSET:
            field_dict["steps"] = steps
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_setup_step_dto import IotSetupStepDto # noqa: PLC0415
        d = dict(src_dict)
        completed = d.pop("completed", UNSET)

        def _parse_steps(data: object) -> list[IotSetupStepDto] | None | Unset:
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
                    steps_type_0_item = IotSetupStepDto.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IotSetupStepDto] | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))


        total = d.pop("total", UNSET)

        iot_setup_progress_result = cls(
            completed=completed,
            steps=steps,
            total=total,
        )

        return iot_setup_progress_result


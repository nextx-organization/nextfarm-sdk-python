from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAutomationsControllerReorderStepsRequest")



@_attrs_define
class OfficeAutomationsControllerReorderStepsRequest:
    

    step_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        step_ids: list[str] | None | Unset
        if isinstance(self.step_ids, Unset):
            step_ids = UNSET
        elif isinstance(self.step_ids, list):
            step_ids = []
            for step_ids_type_0_item_data in self.step_ids:
                step_ids_type_0_item = str(step_ids_type_0_item_data)
                step_ids.append(step_ids_type_0_item)


        else:
            step_ids = self.step_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if step_ids is not UNSET:
            field_dict["stepIds"] = step_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_step_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                step_ids_type_0 = []
                _step_ids_type_0 = data
                for step_ids_type_0_item_data in (_step_ids_type_0):
                    step_ids_type_0_item = UUID(step_ids_type_0_item_data)



                    step_ids_type_0.append(step_ids_type_0_item)

                return step_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        step_ids = _parse_step_ids(d.pop("stepIds", UNSET))


        office_automations_controller_reorder_steps_request = cls(
            step_ids=step_ids,
        )

        return office_automations_controller_reorder_steps_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAutomationsControllerSimulateAutomationRequest")



@_attrs_define
class OfficeAutomationsControllerSimulateAutomationRequest:
    

    record_id: None | Unset | UUID = UNSET
    trigger_data: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        record_id: None | str | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        elif isinstance(self.record_id, UUID):
            record_id = str(self.record_id)
        else:
            record_id = self.record_id

        trigger_data = self.trigger_data


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if trigger_data is not UNSET:
            field_dict["triggerData"] = trigger_data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_record_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_id_type_0 = UUID(data)



                return record_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        record_id = _parse_record_id(d.pop("recordId", UNSET))


        trigger_data = d.pop("triggerData", UNSET)

        office_automations_controller_simulate_automation_request = cls(
            record_id=record_id,
            trigger_data=trigger_data,
        )

        return office_automations_controller_simulate_automation_request


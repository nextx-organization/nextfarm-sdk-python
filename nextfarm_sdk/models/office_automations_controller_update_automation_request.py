from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAutomationsControllerUpdateAutomationRequest")



@_attrs_define
class OfficeAutomationsControllerUpdateAutomationRequest:
    

    description: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    trigger_config: Any | Unset = UNSET
    trigger_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        trigger_config = self.trigger_config

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if trigger_config is not UNSET:
            field_dict["triggerConfig"] = trigger_config
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        trigger_config = d.pop("triggerConfig", UNSET)

        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("triggerType", UNSET))


        office_automations_controller_update_automation_request = cls(
            description=description,
            name=name,
            source=source,
            trigger_config=trigger_config,
            trigger_type=trigger_type,
        )

        return office_automations_controller_update_automation_request


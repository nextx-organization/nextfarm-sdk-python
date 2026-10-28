from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_automation_draft_step import OfficeAutomationDraftStep





T = TypeVar("T", bound="OfficeAutomationsControllerCreateAutomationRequest")



@_attrs_define
class OfficeAutomationsControllerCreateAutomationRequest:
    

    description: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    steps: list[OfficeAutomationDraftStep] | None | Unset = UNSET
    trigger_config: None | str | Unset = UNSET
    trigger_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automation_draft_step import OfficeAutomationDraftStep # noqa: PLC0415
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

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

        trigger_config: None | str | Unset
        if isinstance(self.trigger_config, Unset):
            trigger_config = UNSET
        else:
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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if steps is not UNSET:
            field_dict["steps"] = steps
        if trigger_config is not UNSET:
            field_dict["triggerConfig"] = trigger_config
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automation_draft_step import OfficeAutomationDraftStep # noqa: PLC0415
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


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


        def _parse_steps(data: object) -> list[OfficeAutomationDraftStep] | None | Unset:
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
                    steps_type_0_item = OfficeAutomationDraftStep.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAutomationDraftStep] | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))


        def _parse_trigger_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_config = _parse_trigger_config(d.pop("triggerConfig", UNSET))


        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("triggerType", UNSET))


        office_automations_controller_create_automation_request = cls(
            description=description,
            enabled=enabled,
            name=name,
            source=source,
            steps=steps,
            trigger_config=trigger_config,
            trigger_type=trigger_type,
        )

        return office_automations_controller_create_automation_request


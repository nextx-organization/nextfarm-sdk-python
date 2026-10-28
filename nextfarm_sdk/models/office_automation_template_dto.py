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

if TYPE_CHECKING:
  from ..models.office_automation_template_step_summary_dto import OfficeAutomationTemplateStepSummaryDto





T = TypeVar("T", bound="OfficeAutomationTemplateDto")



@_attrs_define
class OfficeAutomationTemplateDto:
    

    created_at: datetime.datetime | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    source_automation_id: None | Unset | UUID = UNSET
    step_count: int | Unset = UNSET
    steps: list[OfficeAutomationTemplateStepSummaryDto] | None | Unset = UNSET
    trigger_config: None | str | Unset = UNSET
    trigger_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automation_template_step_summary_dto import OfficeAutomationTemplateStepSummaryDto # noqa: PLC0415
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source_automation_id: None | str | Unset
        if isinstance(self.source_automation_id, Unset):
            source_automation_id = UNSET
        elif isinstance(self.source_automation_id, UUID):
            source_automation_id = str(self.source_automation_id)
        else:
            source_automation_id = self.source_automation_id

        step_count = self.step_count

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if source_automation_id is not UNSET:
            field_dict["sourceAutomationId"] = source_automation_id
        if step_count is not UNSET:
            field_dict["stepCount"] = step_count
        if steps is not UNSET:
            field_dict["steps"] = steps
        if trigger_config is not UNSET:
            field_dict["triggerConfig"] = trigger_config
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automation_template_step_summary_dto import OfficeAutomationTemplateStepSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)



                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_source_automation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_automation_id_type_0 = UUID(data)



                return source_automation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_automation_id = _parse_source_automation_id(d.pop("sourceAutomationId", UNSET))


        step_count = d.pop("stepCount", UNSET)

        def _parse_steps(data: object) -> list[OfficeAutomationTemplateStepSummaryDto] | None | Unset:
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
                    steps_type_0_item = OfficeAutomationTemplateStepSummaryDto.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAutomationTemplateStepSummaryDto] | None | Unset, data)

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


        office_automation_template_dto = cls(
            created_at=created_at,
            created_by=created_by,
            description=description,
            id=id,
            name=name,
            source_automation_id=source_automation_id,
            step_count=step_count,
            steps=steps,
            trigger_config=trigger_config,
            trigger_type=trigger_type,
        )

        return office_automation_template_dto


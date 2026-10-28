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
  from ..models.office_automation_step_dto import OfficeAutomationStepDto





T = TypeVar("T", bound="OfficeAutomationDto")



@_attrs_define
class OfficeAutomationDto:
    

    created_by: None | Unset | UUID = UNSET
    created_by_id: None | Unset | UUID = UNSET
    created_by_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    failed7d: int | Unset = UNSET
    graph_version: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    last_run_at: datetime.datetime | None | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_automation_id: None | Unset | UUID = UNSET
    parent_step_id: None | Unset | UUID = UNSET
    runs7d: int | Unset = UNSET
    source: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    step_action_types: list[str] | None | Unset = UNSET
    step_count: int | Unset = UNSET
    steps: list[OfficeAutomationStepDto] | None | Unset = UNSET
    trigger_config: None | str | Unset = UNSET
    trigger_type: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automation_step_dto import OfficeAutomationStepDto # noqa: PLC0415
        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        created_by_id: None | str | Unset
        if isinstance(self.created_by_id, Unset):
            created_by_id = UNSET
        elif isinstance(self.created_by_id, UUID):
            created_by_id = str(self.created_by_id)
        else:
            created_by_id = self.created_by_id

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        failed7d = self.failed7d

        graph_version: int | None | Unset
        if isinstance(self.graph_version, Unset):
            graph_version = UNSET
        else:
            graph_version = self.graph_version

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_run_at: None | str | Unset
        if isinstance(self.last_run_at, Unset):
            last_run_at = UNSET
        elif isinstance(self.last_run_at, datetime.datetime):
            last_run_at = self.last_run_at.isoformat()
        else:
            last_run_at = self.last_run_at

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_automation_id: None | str | Unset
        if isinstance(self.parent_automation_id, Unset):
            parent_automation_id = UNSET
        elif isinstance(self.parent_automation_id, UUID):
            parent_automation_id = str(self.parent_automation_id)
        else:
            parent_automation_id = self.parent_automation_id

        parent_step_id: None | str | Unset
        if isinstance(self.parent_step_id, Unset):
            parent_step_id = UNSET
        elif isinstance(self.parent_step_id, UUID):
            parent_step_id = str(self.parent_step_id)
        else:
            parent_step_id = self.parent_step_id

        runs7d = self.runs7d

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        step_action_types: list[str] | None | Unset
        if isinstance(self.step_action_types, Unset):
            step_action_types = UNSET
        elif isinstance(self.step_action_types, list):
            step_action_types = self.step_action_types


        else:
            step_action_types = self.step_action_types

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

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_id is not UNSET:
            field_dict["createdById"] = created_by_id
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if description is not UNSET:
            field_dict["description"] = description
        if failed7d is not UNSET:
            field_dict["failed7d"] = failed7d
        if graph_version is not UNSET:
            field_dict["graphVersion"] = graph_version
        if id is not UNSET:
            field_dict["id"] = id
        if last_run_at is not UNSET:
            field_dict["lastRunAt"] = last_run_at
        if name is not UNSET:
            field_dict["name"] = name
        if parent_automation_id is not UNSET:
            field_dict["parentAutomationId"] = parent_automation_id
        if parent_step_id is not UNSET:
            field_dict["parentStepId"] = parent_step_id
        if runs7d is not UNSET:
            field_dict["runs7d"] = runs7d
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if step_action_types is not UNSET:
            field_dict["stepActionTypes"] = step_action_types
        if step_count is not UNSET:
            field_dict["stepCount"] = step_count
        if steps is not UNSET:
            field_dict["steps"] = steps
        if trigger_config is not UNSET:
            field_dict["triggerConfig"] = trigger_config
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automation_step_dto import OfficeAutomationStepDto # noqa: PLC0415
        d = dict(src_dict)
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


        def _parse_created_by_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_id_type_0 = UUID(data)



                return created_by_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_id = _parse_created_by_id(d.pop("createdById", UNSET))


        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("createdByName", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        failed7d = d.pop("failed7d", UNSET)

        def _parse_graph_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        graph_version = _parse_graph_version(d.pop("graphVersion", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_last_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_at = _parse_last_run_at(d.pop("lastRunAt", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_parent_automation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_automation_id_type_0 = UUID(data)



                return parent_automation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_automation_id = _parse_parent_automation_id(d.pop("parentAutomationId", UNSET))


        def _parse_parent_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_step_id_type_0 = UUID(data)



                return parent_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_step_id = _parse_parent_step_id(d.pop("parentStepId", UNSET))


        runs7d = d.pop("runs7d", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_step_action_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                step_action_types_type_0 = cast(list[str], data)

                return step_action_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        step_action_types = _parse_step_action_types(d.pop("stepActionTypes", UNSET))


        step_count = d.pop("stepCount", UNSET)

        def _parse_steps(data: object) -> list[OfficeAutomationStepDto] | None | Unset:
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
                    steps_type_0_item = OfficeAutomationStepDto.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAutomationStepDto] | None | Unset, data)

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


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        office_automation_dto = cls(
            created_by=created_by,
            created_by_id=created_by_id,
            created_by_name=created_by_name,
            description=description,
            failed7d=failed7d,
            graph_version=graph_version,
            id=id,
            last_run_at=last_run_at,
            name=name,
            parent_automation_id=parent_automation_id,
            parent_step_id=parent_step_id,
            runs7d=runs7d,
            source=source,
            status=status,
            step_action_types=step_action_types,
            step_count=step_count,
            steps=steps,
            trigger_config=trigger_config,
            trigger_type=trigger_type,
            updated_at=updated_at,
        )

        return office_automation_dto


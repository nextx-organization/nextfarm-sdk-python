from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAutomationSuggestionDto")



@_attrs_define
class OfficeAutomationSuggestionDto:
    

    action_type: None | str | Unset = UNSET
    event_type: None | str | Unset = UNSET
    evidence_count: int | Unset = UNSET
    evidence_days: int | Unset = UNSET
    existing_automation_id: None | Unset | UUID = UNSET
    existing_automation_name: None | str | Unset = UNSET
    existing_failed: int | Unset = UNSET
    existing_runs: int | Unset = UNSET
    existing_status: None | str | Unset = UNSET
    field_id: None | str | Unset = UNSET
    field_name: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    offset_days: int | None | Unset = UNSET
    service: None | str | Unset = UNSET
    table_id: None | Unset | UUID = UNSET
    table_name: None | str | Unset = UNSET
    trigger_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action_type: None | str | Unset
        if isinstance(self.action_type, Unset):
            action_type = UNSET
        else:
            action_type = self.action_type

        event_type: None | str | Unset
        if isinstance(self.event_type, Unset):
            event_type = UNSET
        else:
            event_type = self.event_type

        evidence_count = self.evidence_count

        evidence_days = self.evidence_days

        existing_automation_id: None | str | Unset
        if isinstance(self.existing_automation_id, Unset):
            existing_automation_id = UNSET
        elif isinstance(self.existing_automation_id, UUID):
            existing_automation_id = str(self.existing_automation_id)
        else:
            existing_automation_id = self.existing_automation_id

        existing_automation_name: None | str | Unset
        if isinstance(self.existing_automation_name, Unset):
            existing_automation_name = UNSET
        else:
            existing_automation_name = self.existing_automation_name

        existing_failed = self.existing_failed

        existing_runs = self.existing_runs

        existing_status: None | str | Unset
        if isinstance(self.existing_status, Unset):
            existing_status = UNSET
        else:
            existing_status = self.existing_status

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        field_name: None | str | Unset
        if isinstance(self.field_name, Unset):
            field_name = UNSET
        else:
            field_name = self.field_name

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        offset_days: int | None | Unset
        if isinstance(self.offset_days, Unset):
            offset_days = UNSET
        else:
            offset_days = self.offset_days

        service: None | str | Unset
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service

        table_id: None | str | Unset
        if isinstance(self.table_id, Unset):
            table_id = UNSET
        elif isinstance(self.table_id, UUID):
            table_id = str(self.table_id)
        else:
            table_id = self.table_id

        table_name: None | str | Unset
        if isinstance(self.table_name, Unset):
            table_name = UNSET
        else:
            table_name = self.table_name

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if evidence_count is not UNSET:
            field_dict["evidenceCount"] = evidence_count
        if evidence_days is not UNSET:
            field_dict["evidenceDays"] = evidence_days
        if existing_automation_id is not UNSET:
            field_dict["existingAutomationId"] = existing_automation_id
        if existing_automation_name is not UNSET:
            field_dict["existingAutomationName"] = existing_automation_name
        if existing_failed is not UNSET:
            field_dict["existingFailed"] = existing_failed
        if existing_runs is not UNSET:
            field_dict["existingRuns"] = existing_runs
        if existing_status is not UNSET:
            field_dict["existingStatus"] = existing_status
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if offset_days is not UNSET:
            field_dict["offsetDays"] = offset_days
        if service is not UNSET:
            field_dict["service"] = service
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type

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


        def _parse_event_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_type = _parse_event_type(d.pop("eventType", UNSET))


        evidence_count = d.pop("evidenceCount", UNSET)

        evidence_days = d.pop("evidenceDays", UNSET)

        def _parse_existing_automation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                existing_automation_id_type_0 = UUID(data)



                return existing_automation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        existing_automation_id = _parse_existing_automation_id(d.pop("existingAutomationId", UNSET))


        def _parse_existing_automation_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        existing_automation_name = _parse_existing_automation_name(d.pop("existingAutomationName", UNSET))


        existing_failed = d.pop("existingFailed", UNSET)

        existing_runs = d.pop("existingRuns", UNSET)

        def _parse_existing_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        existing_status = _parse_existing_status(d.pop("existingStatus", UNSET))


        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("fieldId", UNSET))


        def _parse_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_name = _parse_field_name(d.pop("fieldName", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_offset_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        offset_days = _parse_offset_days(d.pop("offsetDays", UNSET))


        def _parse_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service = _parse_service(d.pop("service", UNSET))


        def _parse_table_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                table_id_type_0 = UUID(data)



                return table_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        table_id = _parse_table_id(d.pop("tableId", UNSET))


        def _parse_table_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table_name = _parse_table_name(d.pop("tableName", UNSET))


        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("triggerType", UNSET))


        office_automation_suggestion_dto = cls(
            action_type=action_type,
            event_type=event_type,
            evidence_count=evidence_count,
            evidence_days=evidence_days,
            existing_automation_id=existing_automation_id,
            existing_automation_name=existing_automation_name,
            existing_failed=existing_failed,
            existing_runs=existing_runs,
            existing_status=existing_status,
            field_id=field_id,
            field_name=field_name,
            kind=kind,
            offset_days=offset_days,
            service=service,
            table_id=table_id,
            table_name=table_name,
            trigger_type=trigger_type,
        )

        return office_automation_suggestion_dto


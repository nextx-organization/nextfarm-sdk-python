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






T = TypeVar("T", bound="OfficeAutomationRunDto")



@_attrs_define
class OfficeAutomationRunDto:
    

    automation_id: UUID | Unset = UNSET
    automation_name: None | str | Unset = UNSET
    ended_at: datetime.datetime | Unset = UNSET
    enrollment_id: UUID | Unset = UNSET
    failed: int | Unset = UNSET
    result: None | str | Unset = UNSET
    skipped: int | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    status: None | str | Unset = UNSET
    steps: int | Unset = UNSET
    subject_id: None | Unset | UUID = UNSET
    subject_name: None | str | Unset = UNSET
    succeeded: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        automation_id: str | Unset = UNSET
        if not isinstance(self.automation_id, Unset):
            automation_id = str(self.automation_id)

        automation_name: None | str | Unset
        if isinstance(self.automation_name, Unset):
            automation_name = UNSET
        else:
            automation_name = self.automation_name

        ended_at: str | Unset = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        enrollment_id: str | Unset = UNSET
        if not isinstance(self.enrollment_id, Unset):
            enrollment_id = str(self.enrollment_id)

        failed = self.failed

        result: None | str | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        skipped = self.skipped

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        steps = self.steps

        subject_id: None | str | Unset
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        elif isinstance(self.subject_id, UUID):
            subject_id = str(self.subject_id)
        else:
            subject_id = self.subject_id

        subject_name: None | str | Unset
        if isinstance(self.subject_name, Unset):
            subject_name = UNSET
        else:
            subject_name = self.subject_name

        succeeded = self.succeeded


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if automation_id is not UNSET:
            field_dict["automationId"] = automation_id
        if automation_name is not UNSET:
            field_dict["automationName"] = automation_name
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if enrollment_id is not UNSET:
            field_dict["enrollmentId"] = enrollment_id
        if failed is not UNSET:
            field_dict["failed"] = failed
        if result is not UNSET:
            field_dict["result"] = result
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if steps is not UNSET:
            field_dict["steps"] = steps
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if subject_name is not UNSET:
            field_dict["subjectName"] = subject_name
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _automation_id = d.pop("automationId", UNSET)
        automation_id: UUID | Unset
        if isinstance(_automation_id,  Unset):
            automation_id = UNSET
        else:
            automation_id = UUID(_automation_id)




        def _parse_automation_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        automation_name = _parse_automation_name(d.pop("automationName", UNSET))


        _ended_at = d.pop("endedAt", UNSET)
        ended_at: datetime.datetime | Unset
        if isinstance(_ended_at,  Unset):
            ended_at = UNSET
        else:
            ended_at = datetime.datetime.fromisoformat(_ended_at)




        _enrollment_id = d.pop("enrollmentId", UNSET)
        enrollment_id: UUID | Unset
        if isinstance(_enrollment_id,  Unset):
            enrollment_id = UNSET
        else:
            enrollment_id = UUID(_enrollment_id)




        failed = d.pop("failed", UNSET)

        def _parse_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result = _parse_result(d.pop("result", UNSET))


        skipped = d.pop("skipped", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        steps = d.pop("steps", UNSET)

        def _parse_subject_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_id_type_0 = UUID(data)



                return subject_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subject_id = _parse_subject_id(d.pop("subjectId", UNSET))


        def _parse_subject_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_name = _parse_subject_name(d.pop("subjectName", UNSET))


        succeeded = d.pop("succeeded", UNSET)

        office_automation_run_dto = cls(
            automation_id=automation_id,
            automation_name=automation_name,
            ended_at=ended_at,
            enrollment_id=enrollment_id,
            failed=failed,
            result=result,
            skipped=skipped,
            started_at=started_at,
            status=status,
            steps=steps,
            subject_id=subject_id,
            subject_name=subject_name,
            succeeded=succeeded,
        )

        return office_automation_run_dto


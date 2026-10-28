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






T = TypeVar("T", bound="OfficeAutomationRunLogDto")



@_attrs_define
class OfficeAutomationRunLogDto:
    

    automation_id: UUID | Unset = UNSET
    detail: None | str | Unset = UNSET
    detail_key: None | str | Unset = UNSET
    enrollment_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    result: None | str | Unset = UNSET
    run_at: datetime.datetime | Unset = UNSET
    step_id: None | Unset | UUID = UNSET
    subject_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        automation_id: str | Unset = UNSET
        if not isinstance(self.automation_id, Unset):
            automation_id = str(self.automation_id)

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        detail_key: None | str | Unset
        if isinstance(self.detail_key, Unset):
            detail_key = UNSET
        else:
            detail_key = self.detail_key

        enrollment_id: None | str | Unset
        if isinstance(self.enrollment_id, Unset):
            enrollment_id = UNSET
        elif isinstance(self.enrollment_id, UUID):
            enrollment_id = str(self.enrollment_id)
        else:
            enrollment_id = self.enrollment_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        result: None | str | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        run_at: str | Unset = UNSET
        if not isinstance(self.run_at, Unset):
            run_at = self.run_at.isoformat()

        step_id: None | str | Unset
        if isinstance(self.step_id, Unset):
            step_id = UNSET
        elif isinstance(self.step_id, UUID):
            step_id = str(self.step_id)
        else:
            step_id = self.step_id

        subject_id: None | str | Unset
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        elif isinstance(self.subject_id, UUID):
            subject_id = str(self.subject_id)
        else:
            subject_id = self.subject_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if automation_id is not UNSET:
            field_dict["automationId"] = automation_id
        if detail is not UNSET:
            field_dict["detail"] = detail
        if detail_key is not UNSET:
            field_dict["detailKey"] = detail_key
        if enrollment_id is not UNSET:
            field_dict["enrollmentId"] = enrollment_id
        if id is not UNSET:
            field_dict["id"] = id
        if result is not UNSET:
            field_dict["result"] = result
        if run_at is not UNSET:
            field_dict["runAt"] = run_at
        if step_id is not UNSET:
            field_dict["stepId"] = step_id
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id

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




        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        def _parse_detail_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail_key = _parse_detail_key(d.pop("detailKey", UNSET))


        def _parse_enrollment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrollment_id_type_0 = UUID(data)



                return enrollment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        enrollment_id = _parse_enrollment_id(d.pop("enrollmentId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result = _parse_result(d.pop("result", UNSET))


        _run_at = d.pop("runAt", UNSET)
        run_at: datetime.datetime | Unset
        if isinstance(_run_at,  Unset):
            run_at = UNSET
        else:
            run_at = datetime.datetime.fromisoformat(_run_at)




        def _parse_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                step_id_type_0 = UUID(data)



                return step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        step_id = _parse_step_id(d.pop("stepId", UNSET))


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


        office_automation_run_log_dto = cls(
            automation_id=automation_id,
            detail=detail,
            detail_key=detail_key,
            enrollment_id=enrollment_id,
            id=id,
            result=result,
            run_at=run_at,
            step_id=step_id,
            subject_id=subject_id,
        )

        return office_automation_run_log_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChangeTaskStatusRequest")



@_attrs_define
class OfficeChangeTaskStatusRequest:
    

    result_note: None | str | Unset = UNSET
    reviewer_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    task_status_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        result_note: None | str | Unset
        if isinstance(self.result_note, Unset):
            result_note = UNSET
        else:
            result_note = self.result_note

        reviewer_id: None | str | Unset
        if isinstance(self.reviewer_id, Unset):
            reviewer_id = UNSET
        elif isinstance(self.reviewer_id, UUID):
            reviewer_id = str(self.reviewer_id)
        else:
            reviewer_id = self.reviewer_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        task_status_id: None | str | Unset
        if isinstance(self.task_status_id, Unset):
            task_status_id = UNSET
        elif isinstance(self.task_status_id, UUID):
            task_status_id = str(self.task_status_id)
        else:
            task_status_id = self.task_status_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if result_note is not UNSET:
            field_dict["resultNote"] = result_note
        if reviewer_id is not UNSET:
            field_dict["reviewerId"] = reviewer_id
        if status is not UNSET:
            field_dict["status"] = status
        if task_status_id is not UNSET:
            field_dict["taskStatusId"] = task_status_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_result_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_note = _parse_result_note(d.pop("resultNote", UNSET))


        def _parse_reviewer_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewer_id_type_0 = UUID(data)



                return reviewer_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reviewer_id = _parse_reviewer_id(d.pop("reviewerId", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_task_status_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_status_id_type_0 = UUID(data)



                return task_status_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        task_status_id = _parse_task_status_id(d.pop("taskStatusId", UNSET))


        office_change_task_status_request = cls(
            result_note=result_note,
            reviewer_id=reviewer_id,
            status=status,
            task_status_id=task_status_id,
        )

        return office_change_task_status_request


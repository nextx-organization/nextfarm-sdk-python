from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskBulkErrorDto")



@_attrs_define
class OfficeTaskBulkErrorDto:
    

    code: None | str | Unset = UNSET
    task_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        task_id: str | Unset = UNSET
        if not isinstance(self.task_id, Unset):
            task_id = str(self.task_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if task_id is not UNSET:
            field_dict["taskId"] = task_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        _task_id = d.pop("taskId", UNSET)
        task_id: UUID | Unset
        if isinstance(_task_id,  Unset):
            task_id = UNSET
        else:
            task_id = UUID(_task_id)




        office_task_bulk_error_dto = cls(
            code=code,
            task_id=task_id,
        )

        return office_task_bulk_error_dto


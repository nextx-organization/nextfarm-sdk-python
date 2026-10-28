from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeBulkApprovalItemDto")



@_attrs_define
class OfficeBulkApprovalItemDto:
    

    error_key: None | str | Unset = UNSET
    succeeded: bool | Unset = UNSET
    task_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error_key: None | str | Unset
        if isinstance(self.error_key, Unset):
            error_key = UNSET
        else:
            error_key = self.error_key

        succeeded = self.succeeded

        task_id: str | Unset = UNSET
        if not isinstance(self.task_id, Unset):
            task_id = str(self.task_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if error_key is not UNSET:
            field_dict["errorKey"] = error_key
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded
        if task_id is not UNSET:
            field_dict["taskId"] = task_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_error_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_key = _parse_error_key(d.pop("errorKey", UNSET))


        succeeded = d.pop("succeeded", UNSET)

        _task_id = d.pop("taskId", UNSET)
        task_id: UUID | Unset
        if isinstance(_task_id,  Unset):
            task_id = UNSET
        else:
            task_id = UUID(_task_id)




        office_bulk_approval_item_dto = cls(
            error_key=error_key,
            succeeded=succeeded,
            task_id=task_id,
        )

        return office_bulk_approval_item_dto


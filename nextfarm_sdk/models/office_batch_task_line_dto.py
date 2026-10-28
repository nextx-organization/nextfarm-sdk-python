from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeBatchTaskLineDto")



@_attrs_define
class OfficeBatchTaskLineDto:
    

    error_code: None | str | Unset = UNSET
    index: int | Unset = UNSET
    task_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        index = self.index

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        elif isinstance(self.task_id, UUID):
            task_id = str(self.task_id)
        else:
            task_id = self.task_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if index is not UNSET:
            field_dict["index"] = index
        if task_id is not UNSET:
            field_dict["taskId"] = task_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))


        index = d.pop("index", UNSET)

        def _parse_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_id_type_0 = UUID(data)



                return task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        task_id = _parse_task_id(d.pop("taskId", UNSET))


        office_batch_task_line_dto = cls(
            error_code=error_code,
            index=index,
            task_id=task_id,
        )

        return office_batch_task_line_dto


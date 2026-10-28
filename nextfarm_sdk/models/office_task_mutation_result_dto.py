from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_task_warning_dto import OfficeTaskWarningDto





T = TypeVar("T", bound="OfficeTaskMutationResultDto")



@_attrs_define
class OfficeTaskMutationResultDto:
    

    replayed: bool | Unset = UNSET
    task_id: UUID | Unset = UNSET
    warning: OfficeTaskWarningDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_warning_dto import OfficeTaskWarningDto # noqa: PLC0415
        replayed = self.replayed

        task_id: str | Unset = UNSET
        if not isinstance(self.task_id, Unset):
            task_id = str(self.task_id)

        warning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.warning, Unset):
            warning = self.warning.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if replayed is not UNSET:
            field_dict["replayed"] = replayed
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_warning_dto import OfficeTaskWarningDto # noqa: PLC0415
        d = dict(src_dict)
        replayed = d.pop("replayed", UNSET)

        _task_id = d.pop("taskId", UNSET)
        task_id: UUID | Unset
        if isinstance(_task_id,  Unset):
            task_id = UNSET
        else:
            task_id = UUID(_task_id)




        _warning = d.pop("warning", UNSET)
        warning: OfficeTaskWarningDto | Unset
        if isinstance(_warning,  Unset):
            warning = UNSET
        else:
            warning = OfficeTaskWarningDto.from_dict(_warning)




        office_task_mutation_result_dto = cls(
            replayed=replayed,
            task_id=task_id,
            warning=warning,
        )

        return office_task_mutation_result_dto


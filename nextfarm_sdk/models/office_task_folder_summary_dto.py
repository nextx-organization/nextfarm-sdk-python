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
  from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto





T = TypeVar("T", bound="OfficeTaskFolderSummaryDto")



@_attrs_define
class OfficeTaskFolderSummaryDto:
    

    counts: OfficeTaskSummaryCountsDto | Unset = UNSET
    id: UUID | Unset = UNSET
    list_count: int | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto # noqa: PLC0415
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        list_count = self.list_count

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if counts is not UNSET:
            field_dict["counts"] = counts
        if id is not UNSET:
            field_dict["id"] = id
        if list_count is not UNSET:
            field_dict["listCount"] = list_count
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto # noqa: PLC0415
        d = dict(src_dict)
        _counts = d.pop("counts", UNSET)
        counts: OfficeTaskSummaryCountsDto | Unset
        if isinstance(_counts,  Unset):
            counts = UNSET
        else:
            counts = OfficeTaskSummaryCountsDto.from_dict(_counts)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        list_count = d.pop("listCount", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_task_folder_summary_dto = cls(
            counts=counts,
            id=id,
            list_count=list_count,
            name=name,
        )

        return office_task_folder_summary_dto


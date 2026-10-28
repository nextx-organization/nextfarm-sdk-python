from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto





T = TypeVar("T", bound="OfficeTaskUnfiledSummaryDto")



@_attrs_define
class OfficeTaskUnfiledSummaryDto:
    

    counts: OfficeTaskSummaryCountsDto | Unset = UNSET
    list_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto # noqa: PLC0415
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        list_count = self.list_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if counts is not UNSET:
            field_dict["counts"] = counts
        if list_count is not UNSET:
            field_dict["listCount"] = list_count

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




        list_count = d.pop("listCount", UNSET)

        office_task_unfiled_summary_dto = cls(
            counts=counts,
            list_count=list_count,
        )

        return office_task_unfiled_summary_dto


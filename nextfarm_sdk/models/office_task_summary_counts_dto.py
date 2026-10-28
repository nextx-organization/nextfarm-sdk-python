from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeTaskSummaryCountsDto")



@_attrs_define
class OfficeTaskSummaryCountsDto:
    

    done7d: int | Unset = UNSET
    in_progress: int | Unset = UNSET
    open_: int | Unset = UNSET
    overdue: int | Unset = UNSET
    pending_review: int | Unset = UNSET
    todo: int | Unset = UNSET
    unassigned: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        done7d = self.done7d

        in_progress = self.in_progress

        open_ = self.open_

        overdue = self.overdue

        pending_review = self.pending_review

        todo = self.todo

        unassigned = self.unassigned


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if done7d is not UNSET:
            field_dict["done7d"] = done7d
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if open_ is not UNSET:
            field_dict["open"] = open_
        if overdue is not UNSET:
            field_dict["overdue"] = overdue
        if pending_review is not UNSET:
            field_dict["pendingReview"] = pending_review
        if todo is not UNSET:
            field_dict["todo"] = todo
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done7d = d.pop("done7d", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        open_ = d.pop("open", UNSET)

        overdue = d.pop("overdue", UNSET)

        pending_review = d.pop("pendingReview", UNSET)

        todo = d.pop("todo", UNSET)

        unassigned = d.pop("unassigned", UNSET)

        office_task_summary_counts_dto = cls(
            done7d=done7d,
            in_progress=in_progress,
            open_=open_,
            overdue=overdue,
            pending_review=pending_review,
            todo=todo,
            unassigned=unassigned,
        )

        return office_task_summary_counts_dto


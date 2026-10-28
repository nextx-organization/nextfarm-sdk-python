from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeTaskQuickCountsDto")



@_attrs_define
class OfficeTaskQuickCountsDto:
    

    due_this_week: int | Unset = UNSET
    mine: int | Unset = UNSET
    no_due: int | Unset = UNSET
    overdue: int | Unset = UNSET
    pending_review: int | Unset = UNSET
    stale: int | Unset = UNSET
    stale_days: int | Unset = UNSET
    total: int | Unset = UNSET
    unassigned: int | Unset = UNSET
    week_start: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        due_this_week = self.due_this_week

        mine = self.mine

        no_due = self.no_due

        overdue = self.overdue

        pending_review = self.pending_review

        stale = self.stale

        stale_days = self.stale_days

        total = self.total

        unassigned = self.unassigned

        week_start: str | Unset = UNSET
        if not isinstance(self.week_start, Unset):
            week_start = self.week_start.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if due_this_week is not UNSET:
            field_dict["dueThisWeek"] = due_this_week
        if mine is not UNSET:
            field_dict["mine"] = mine
        if no_due is not UNSET:
            field_dict["noDue"] = no_due
        if overdue is not UNSET:
            field_dict["overdue"] = overdue
        if pending_review is not UNSET:
            field_dict["pendingReview"] = pending_review
        if stale is not UNSET:
            field_dict["stale"] = stale
        if stale_days is not UNSET:
            field_dict["staleDays"] = stale_days
        if total is not UNSET:
            field_dict["total"] = total
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned
        if week_start is not UNSET:
            field_dict["weekStart"] = week_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        due_this_week = d.pop("dueThisWeek", UNSET)

        mine = d.pop("mine", UNSET)

        no_due = d.pop("noDue", UNSET)

        overdue = d.pop("overdue", UNSET)

        pending_review = d.pop("pendingReview", UNSET)

        stale = d.pop("stale", UNSET)

        stale_days = d.pop("staleDays", UNSET)

        total = d.pop("total", UNSET)

        unassigned = d.pop("unassigned", UNSET)

        _week_start = d.pop("weekStart", UNSET)
        week_start: datetime.date | Unset
        if isinstance(_week_start,  Unset):
            week_start = UNSET
        else:
            week_start = datetime.date.fromisoformat(_week_start)




        office_task_quick_counts_dto = cls(
            due_this_week=due_this_week,
            mine=mine,
            no_due=no_due,
            overdue=overdue,
            pending_review=pending_review,
            stale=stale,
            stale_days=stale_days,
            total=total,
            unassigned=unassigned,
            week_start=week_start,
        )

        return office_task_quick_counts_dto


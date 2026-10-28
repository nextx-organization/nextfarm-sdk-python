from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_nav_open_counts_dto import OfficeTaskNavOpenCountsDto





T = TypeVar("T", bound="OfficeTaskNavCountsDto")



@_attrs_define
class OfficeTaskNavCountsDto:
    

    all_: int | Unset = UNSET
    assigned: int | Unset = UNSET
    completed: int | Unset = UNSET
    created: int | Unset = UNSET
    open_count: OfficeTaskNavOpenCountsDto | Unset = UNSET
    unassigned: int | Unset = UNSET
    unlisted: int | Unset = UNSET
    watching: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_nav_open_counts_dto import OfficeTaskNavOpenCountsDto # noqa: PLC0415
        all_ = self.all_

        assigned = self.assigned

        completed = self.completed

        created = self.created

        open_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.open_count, Unset):
            open_count = self.open_count.to_dict()

        unassigned = self.unassigned

        unlisted = self.unlisted

        watching = self.watching


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if all_ is not UNSET:
            field_dict["all"] = all_
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if completed is not UNSET:
            field_dict["completed"] = completed
        if created is not UNSET:
            field_dict["created"] = created
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned
        if unlisted is not UNSET:
            field_dict["unlisted"] = unlisted
        if watching is not UNSET:
            field_dict["watching"] = watching

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_nav_open_counts_dto import OfficeTaskNavOpenCountsDto # noqa: PLC0415
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        assigned = d.pop("assigned", UNSET)

        completed = d.pop("completed", UNSET)

        created = d.pop("created", UNSET)

        _open_count = d.pop("openCount", UNSET)
        open_count: OfficeTaskNavOpenCountsDto | Unset
        if isinstance(_open_count,  Unset):
            open_count = UNSET
        else:
            open_count = OfficeTaskNavOpenCountsDto.from_dict(_open_count)




        unassigned = d.pop("unassigned", UNSET)

        unlisted = d.pop("unlisted", UNSET)

        watching = d.pop("watching", UNSET)

        office_task_nav_counts_dto = cls(
            all_=all_,
            assigned=assigned,
            completed=completed,
            created=created,
            open_count=open_count,
            unassigned=unassigned,
            unlisted=unlisted,
            watching=watching,
        )

        return office_task_nav_counts_dto


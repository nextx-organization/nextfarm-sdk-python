from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskTeamMemberSummaryDto")



@_attrs_define
class OfficeTaskTeamMemberSummaryDto:
    

    done7d: int | Unset = UNSET
    in_progress: int | Unset = UNSET
    open_: int | Unset = UNSET
    overdue: int | Unset = UNSET
    parent_open: int | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        done7d = self.done7d

        in_progress = self.in_progress

        open_ = self.open_

        overdue = self.overdue

        parent_open = self.parent_open

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


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
        if parent_open is not UNSET:
            field_dict["parentOpen"] = parent_open
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done7d = d.pop("done7d", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        open_ = d.pop("open", UNSET)

        overdue = d.pop("overdue", UNSET)

        parent_open = d.pop("parentOpen", UNSET)

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_task_team_member_summary_dto = cls(
            done7d=done7d,
            in_progress=in_progress,
            open_=open_,
            overdue=overdue,
            parent_open=parent_open,
            user_id=user_id,
        )

        return office_task_team_member_summary_dto


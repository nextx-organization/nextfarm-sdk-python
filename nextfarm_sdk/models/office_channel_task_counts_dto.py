from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeChannelTaskCountsDto")



@_attrs_define
class OfficeChannelTaskCountsDto:
    

    done: int | Unset = UNSET
    mine: int | Unset = UNSET
    open_: int | Unset = UNSET
    overdue: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        done = self.done

        mine = self.mine

        open_ = self.open_

        overdue = self.overdue


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if done is not UNSET:
            field_dict["done"] = done
        if mine is not UNSET:
            field_dict["mine"] = mine
        if open_ is not UNSET:
            field_dict["open"] = open_
        if overdue is not UNSET:
            field_dict["overdue"] = overdue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done = d.pop("done", UNSET)

        mine = d.pop("mine", UNSET)

        open_ = d.pop("open", UNSET)

        overdue = d.pop("overdue", UNSET)

        office_channel_task_counts_dto = cls(
            done=done,
            mine=mine,
            open_=open_,
            overdue=overdue,
        )

        return office_channel_task_counts_dto


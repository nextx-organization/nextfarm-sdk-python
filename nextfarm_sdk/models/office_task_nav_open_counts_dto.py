from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeTaskNavOpenCountsDto")



@_attrs_define
class OfficeTaskNavOpenCountsDto:
    

    all_: int | Unset = UNSET
    assigned: int | Unset = UNSET
    created: int | Unset = UNSET
    unlisted: int | Unset = UNSET
    watching: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        assigned = self.assigned

        created = self.created

        unlisted = self.unlisted

        watching = self.watching


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if all_ is not UNSET:
            field_dict["all"] = all_
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if created is not UNSET:
            field_dict["created"] = created
        if unlisted is not UNSET:
            field_dict["unlisted"] = unlisted
        if watching is not UNSET:
            field_dict["watching"] = watching

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        assigned = d.pop("assigned", UNSET)

        created = d.pop("created", UNSET)

        unlisted = d.pop("unlisted", UNSET)

        watching = d.pop("watching", UNSET)

        office_task_nav_open_counts_dto = cls(
            all_=all_,
            assigned=assigned,
            created=created,
            unlisted=unlisted,
            watching=watching,
        )

        return office_task_nav_open_counts_dto


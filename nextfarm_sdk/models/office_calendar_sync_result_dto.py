from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeCalendarSyncResultDto")



@_attrs_define
class OfficeCalendarSyncResultDto:
    

    created: int | Unset = UNSET
    deleted: int | Unset = UNSET
    pulled: int | Unset = UNSET
    pushed: int | Unset = UNSET
    updated: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created = self.created

        deleted = self.deleted

        pulled = self.pulled

        pushed = self.pushed

        updated = self.updated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created is not UNSET:
            field_dict["created"] = created
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if pulled is not UNSET:
            field_dict["pulled"] = pulled
        if pushed is not UNSET:
            field_dict["pushed"] = pushed
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        deleted = d.pop("deleted", UNSET)

        pulled = d.pop("pulled", UNSET)

        pushed = d.pop("pushed", UNSET)

        updated = d.pop("updated", UNSET)

        office_calendar_sync_result_dto = cls(
            created=created,
            deleted=deleted,
            pulled=pulled,
            pushed=pushed,
            updated=updated,
        )

        return office_calendar_sync_result_dto


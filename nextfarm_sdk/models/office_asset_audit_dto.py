from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeAssetAuditDto")



@_attrs_define
class OfficeAssetAuditDto:
    

    completed_at: datetime.datetime | None | Unset = UNSET
    confirmed_count: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    due_date: datetime.date | Unset = UNSET
    id: UUID | Unset = UNSET
    item_count: int | Unset = UNSET
    mismatch_count: int | Unset = UNSET
    name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    scope: None | str | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        confirmed_count = self.confirmed_count

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        item_count = self.item_count

        mismatch_count = self.mismatch_count

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if confirmed_count is not UNSET:
            field_dict["confirmedCount"] = confirmed_count
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if id is not UNSET:
            field_dict["id"] = id
        if item_count is not UNSET:
            field_dict["itemCount"] = item_count
        if mismatch_count is not UNSET:
            field_dict["mismatchCount"] = mismatch_count
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if opened_at is not UNSET:
            field_dict["openedAt"] = opened_at
        if scope is not UNSET:
            field_dict["scope"] = scope
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        confirmed_count = d.pop("confirmedCount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.date | Unset
        if isinstance(_due_date,  Unset):
            due_date = UNSET
        else:
            due_date = datetime.date.fromisoformat(_due_date)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        item_count = d.pop("itemCount", UNSET)

        mismatch_count = d.pop("mismatchCount", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_opened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)



                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        opened_at = _parse_opened_at(d.pop("openedAt", UNSET))


        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_asset_audit_dto = cls(
            completed_at=completed_at,
            confirmed_count=confirmed_count,
            created_at=created_at,
            due_date=due_date,
            id=id,
            item_count=item_count,
            mismatch_count=mismatch_count,
            name=name,
            note=note,
            opened_at=opened_at,
            scope=scope,
            status=status,
        )

        return office_asset_audit_dto


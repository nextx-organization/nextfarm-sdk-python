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






T = TypeVar("T", bound="OfficeTaskSavedFilterDto")



@_attrs_define
class OfficeTaskSavedFilterDto:
    

    id: UUID | Unset = UNSET
    is_mine: bool | Unset = UNSET
    is_shared: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    payload: None | str | Unset = UNSET
    sort_order: int | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_mine = self.is_mine

        is_shared = self.is_shared

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        owner_id: str | Unset = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = str(self.owner_id)

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

        sort_order = self.sort_order

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_mine is not UNSET:
            field_dict["isMine"] = is_mine
        if is_shared is not UNSET:
            field_dict["isShared"] = is_shared
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_mine = d.pop("isMine", UNSET)

        is_shared = d.pop("isShared", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _owner_id = d.pop("ownerId", UNSET)
        owner_id: UUID | Unset
        if isinstance(_owner_id,  Unset):
            owner_id = UNSET
        else:
            owner_id = UUID(_owner_id)




        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_task_saved_filter_dto = cls(
            id=id,
            is_mine=is_mine,
            is_shared=is_shared,
            name=name,
            owner_id=owner_id,
            payload=payload,
            sort_order=sort_order,
            updated_at=updated_at,
        )

        return office_task_saved_filter_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCalendarDto")



@_attrs_define
class OfficeCalendarDto:
    

    color: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_mine: bool | Unset = UNSET
    is_subscribed: bool | Unset = UNSET
    is_visible: bool | Unset = UNSET
    kind: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_id: None | Unset | UUID = UNSET
    owner_name: None | str | Unset = UNSET
    role: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_mine = self.is_mine

        is_subscribed = self.is_subscribed

        is_visible = self.is_visible

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        elif isinstance(self.owner_id, UUID):
            owner_id = str(self.owner_id)
        else:
            owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_mine is not UNSET:
            field_dict["isMine"] = is_mine
        if is_subscribed is not UNSET:
            field_dict["isSubscribed"] = is_subscribed
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_mine = d.pop("isMine", UNSET)

        is_subscribed = d.pop("isSubscribed", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_owner_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_id_type_0 = UUID(data)



                return owner_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))


        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("ownerName", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        office_calendar_dto = cls(
            color=color,
            description=description,
            id=id,
            is_mine=is_mine,
            is_subscribed=is_subscribed,
            is_visible=is_visible,
            kind=kind,
            name=name,
            owner_id=owner_id,
            owner_name=owner_name,
            role=role,
        )

        return office_calendar_dto


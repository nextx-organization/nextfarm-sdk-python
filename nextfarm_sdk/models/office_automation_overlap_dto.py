from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAutomationOverlapDto")



@_attrs_define
class OfficeAutomationOverlapDto:
    

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    shared_actions: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        shared_actions: list[str] | None | Unset
        if isinstance(self.shared_actions, Unset):
            shared_actions = UNSET
        elif isinstance(self.shared_actions, list):
            shared_actions = self.shared_actions


        else:
            shared_actions = self.shared_actions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if shared_actions is not UNSET:
            field_dict["sharedActions"] = shared_actions

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




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_shared_actions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shared_actions_type_0 = cast(list[str], data)

                return shared_actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        shared_actions = _parse_shared_actions(d.pop("sharedActions", UNSET))


        office_automation_overlap_dto = cls(
            id=id,
            name=name,
            shared_actions=shared_actions,
        )

        return office_automation_overlap_dto


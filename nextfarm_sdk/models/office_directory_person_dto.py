from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeDirectoryPersonDto")



@_attrs_define
class OfficeDirectoryPersonDto:
    

    full_name: None | str | Unset = UNSET
    user_id: UUID | Unset = UNSET
    workplace: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        workplace: None | str | Unset
        if isinstance(self.workplace, Unset):
            workplace = UNSET
        else:
            workplace = self.workplace


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if workplace is not UNSET:
            field_dict["workplace"] = workplace

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        def _parse_workplace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workplace = _parse_workplace(d.pop("workplace", UNSET))


        office_directory_person_dto = cls(
            full_name=full_name,
            user_id=user_id,
            workplace=workplace,
        )

        return office_directory_person_dto


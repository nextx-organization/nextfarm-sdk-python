from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeIpAllowlistEntryDto")



@_attrs_define
class OfficeIpAllowlistEntryDto:
    

    cidr: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_active: bool | Unset = UNSET
    label: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cidr: None | str | Unset
        if isinstance(self.cidr, Unset):
            cidr = UNSET
        else:
            cidr = self.cidr

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_active = self.is_active

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cidr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cidr = _parse_cidr(d.pop("cidr", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_active = d.pop("isActive", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        office_ip_allowlist_entry_dto = cls(
            cidr=cidr,
            id=id,
            is_active=is_active,
            label=label,
        )

        return office_ip_allowlist_entry_dto


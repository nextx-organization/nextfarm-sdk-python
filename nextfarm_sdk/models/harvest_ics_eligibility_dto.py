from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestIcsEligibilityDto")



@_attrs_define
class HarvestIcsEligibilityDto:
    

    eligible: bool | Unset = UNSET
    farmer_id: UUID | Unset = UNSET
    group_id: UUID | Unset = UNSET
    group_name: None | str | Unset = UNSET
    member_status: None | str | Unset = UNSET
    scheme: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        eligible = self.eligible

        farmer_id: str | Unset = UNSET
        if not isinstance(self.farmer_id, Unset):
            farmer_id = str(self.farmer_id)

        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        member_status: None | str | Unset
        if isinstance(self.member_status, Unset):
            member_status = UNSET
        else:
            member_status = self.member_status

        scheme: None | str | Unset
        if isinstance(self.scheme, Unset):
            scheme = UNSET
        else:
            scheme = self.scheme


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if farmer_id is not UNSET:
            field_dict["farmer_id"] = farmer_id
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if member_status is not UNSET:
            field_dict["member_status"] = member_status
        if scheme is not UNSET:
            field_dict["scheme"] = scheme

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eligible = d.pop("eligible", UNSET)

        _farmer_id = d.pop("farmer_id", UNSET)
        farmer_id: UUID | Unset
        if isinstance(_farmer_id,  Unset):
            farmer_id = UNSET
        else:
            farmer_id = UUID(_farmer_id)




        _group_id = d.pop("group_id", UNSET)
        group_id: UUID | Unset
        if isinstance(_group_id,  Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)




        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("group_name", UNSET))


        def _parse_member_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_status = _parse_member_status(d.pop("member_status", UNSET))


        def _parse_scheme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme = _parse_scheme(d.pop("scheme", UNSET))


        harvest_ics_eligibility_dto = cls(
            eligible=eligible,
            farmer_id=farmer_id,
            group_id=group_id,
            group_name=group_name,
            member_status=member_status,
            scheme=scheme,
        )

        return harvest_ics_eligibility_dto


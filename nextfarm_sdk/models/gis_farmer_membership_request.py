from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisFarmerMembershipRequest")



@_attrs_define
class GisFarmerMembershipRequest:
    

    cooperative_name: None | str | Unset = UNSET
    group_id: None | Unset | UUID = UNSET
    member_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cooperative_name: None | str | Unset
        if isinstance(self.cooperative_name, Unset):
            cooperative_name = UNSET
        else:
            cooperative_name = self.cooperative_name

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        member_type: None | str | Unset
        if isinstance(self.member_type, Unset):
            member_type = UNSET
        else:
            member_type = self.member_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cooperative_name is not UNSET:
            field_dict["cooperative_name"] = cooperative_name
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if member_type is not UNSET:
            field_dict["member_type"] = member_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cooperative_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cooperative_name = _parse_cooperative_name(d.pop("cooperative_name", UNSET))


        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)



                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))


        def _parse_member_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_type = _parse_member_type(d.pop("member_type", UNSET))


        gis_farmer_membership_request = cls(
            cooperative_name=cooperative_name,
            group_id=group_id,
            member_type=member_type,
        )

        return gis_farmer_membership_request


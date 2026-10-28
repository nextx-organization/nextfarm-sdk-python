from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_cert_member_input import HarvestCertMemberInput





T = TypeVar("T", bound="HarvestCertMembersRequest")



@_attrs_define
class HarvestCertMembersRequest:
    

    members: list[HarvestCertMemberInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_cert_member_input import HarvestCertMemberInput # noqa: PLC0415
        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)


        else:
            members = self.members


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_cert_member_input import HarvestCertMemberInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_members(data: object) -> list[HarvestCertMemberInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in (_members_type_0):
                    members_type_0_item = HarvestCertMemberInput.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestCertMemberInput] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


        harvest_cert_members_request = cls(
            members=members,
        )

        return harvest_cert_members_request


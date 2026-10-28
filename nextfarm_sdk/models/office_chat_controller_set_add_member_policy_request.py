from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerSetAddMemberPolicyRequest")



@_attrs_define
class OfficeChatControllerSetAddMemberPolicyRequest:
    

    policy: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        policy: None | str | Unset
        if isinstance(self.policy, Unset):
            policy = UNSET
        else:
            policy = self.policy


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy = _parse_policy(d.pop("policy", UNSET))


        office_chat_controller_set_add_member_policy_request = cls(
            policy=policy,
        )

        return office_chat_controller_set_add_member_policy_request


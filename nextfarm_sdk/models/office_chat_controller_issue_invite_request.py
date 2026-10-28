from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerIssueInviteRequest")



@_attrs_define
class OfficeChatControllerIssueInviteRequest:
    

    audience: None | str | Unset = UNSET
    expires_in_days: int | None | Unset = UNSET
    label: None | str | Unset = UNSET
    max_uses: int | None | Unset = UNSET
    replace_existing: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        audience: None | str | Unset
        if isinstance(self.audience, Unset):
            audience = UNSET
        else:
            audience = self.audience

        expires_in_days: int | None | Unset
        if isinstance(self.expires_in_days, Unset):
            expires_in_days = UNSET
        else:
            expires_in_days = self.expires_in_days

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        max_uses: int | None | Unset
        if isinstance(self.max_uses, Unset):
            max_uses = UNSET
        else:
            max_uses = self.max_uses

        replace_existing = self.replace_existing


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if audience is not UNSET:
            field_dict["audience"] = audience
        if expires_in_days is not UNSET:
            field_dict["expiresInDays"] = expires_in_days
        if label is not UNSET:
            field_dict["label"] = label
        if max_uses is not UNSET:
            field_dict["maxUses"] = max_uses
        if replace_existing is not UNSET:
            field_dict["replaceExisting"] = replace_existing

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_audience(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audience = _parse_audience(d.pop("audience", UNSET))


        def _parse_expires_in_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_in_days = _parse_expires_in_days(d.pop("expiresInDays", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_max_uses(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_uses = _parse_max_uses(d.pop("maxUses", UNSET))


        replace_existing = d.pop("replaceExisting", UNSET)

        office_chat_controller_issue_invite_request = cls(
            audience=audience,
            expires_in_days=expires_in_days,
            label=label,
            max_uses=max_uses,
            replace_existing=replace_existing,
        )

        return office_chat_controller_issue_invite_request


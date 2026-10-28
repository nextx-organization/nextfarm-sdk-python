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






T = TypeVar("T", bound="OfficeContactInviteDto")



@_attrs_define
class OfficeContactInviteDto:
    

    expires_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    owner_user_id: UUID | Unset = UNSET
    token: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    use_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        owner_user_id: str | Unset = UNSET
        if not isinstance(self.owner_user_id, Unset):
            owner_user_id = str(self.owner_user_id)

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        use_count = self.use_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if owner_user_id is not UNSET:
            field_dict["ownerUserId"] = owner_user_id
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url
        if use_count is not UNSET:
            field_dict["useCount"] = use_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _owner_user_id = d.pop("ownerUserId", UNSET)
        owner_user_id: UUID | Unset
        if isinstance(_owner_user_id,  Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = UUID(_owner_user_id)




        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        use_count = d.pop("useCount", UNSET)

        office_contact_invite_dto = cls(
            expires_at=expires_at,
            id=id,
            owner_user_id=owner_user_id,
            token=token,
            url=url,
            use_count=use_count,
        )

        return office_contact_invite_dto


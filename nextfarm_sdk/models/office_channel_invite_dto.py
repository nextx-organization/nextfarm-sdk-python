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






T = TypeVar("T", bound="OfficeChannelInviteDto")



@_attrs_define
class OfficeChannelInviteDto:
    

    audience: None | str | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    label: None | str | Unset = UNSET
    max_uses: int | None | Unset = UNSET
    token: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    use_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        audience: None | str | Unset
        if isinstance(self.audience, Unset):
            audience = UNSET
        else:
            audience = self.audience

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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
        if audience is not UNSET:
            field_dict["audience"] = audience
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if max_uses is not UNSET:
            field_dict["maxUses"] = max_uses
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
        def _parse_audience(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audience = _parse_audience(d.pop("audience", UNSET))


        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _created_by = d.pop("createdBy", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)




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

        office_channel_invite_dto = cls(
            audience=audience,
            channel_id=channel_id,
            created_at=created_at,
            created_by=created_by,
            expires_at=expires_at,
            id=id,
            label=label,
            max_uses=max_uses,
            token=token,
            url=url,
            use_count=use_count,
        )

        return office_channel_invite_dto


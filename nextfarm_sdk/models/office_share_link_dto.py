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






T = TypeVar("T", bound="OfficeShareLinkDto")



@_attrs_define
class OfficeShareLinkDto:
    

    allow_download: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    last_viewed_at: datetime.datetime | None | Unset = UNSET
    requires_password: bool | Unset = UNSET
    revoked_at: datetime.datetime | None | Unset = UNSET
    target_id: UUID | Unset = UNSET
    target_type: None | str | Unset = UNSET
    token: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    view_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allow_download = self.allow_download

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

        last_viewed_at: None | str | Unset
        if isinstance(self.last_viewed_at, Unset):
            last_viewed_at = UNSET
        elif isinstance(self.last_viewed_at, datetime.datetime):
            last_viewed_at = self.last_viewed_at.isoformat()
        else:
            last_viewed_at = self.last_viewed_at

        requires_password = self.requires_password

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        target_id: str | Unset = UNSET
        if not isinstance(self.target_id, Unset):
            target_id = str(self.target_id)

        target_type: None | str | Unset
        if isinstance(self.target_type, Unset):
            target_type = UNSET
        else:
            target_type = self.target_type

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

        view_count = self.view_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allow_download is not UNSET:
            field_dict["allowDownload"] = allow_download
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if last_viewed_at is not UNSET:
            field_dict["lastViewedAt"] = last_viewed_at
        if requires_password is not UNSET:
            field_dict["requiresPassword"] = requires_password
        if revoked_at is not UNSET:
            field_dict["revokedAt"] = revoked_at
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_download = d.pop("allowDownload", UNSET)

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




        def _parse_last_viewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_viewed_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_viewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_viewed_at = _parse_last_viewed_at(d.pop("lastViewedAt", UNSET))


        requires_password = d.pop("requiresPassword", UNSET)

        def _parse_revoked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)



                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revokedAt", UNSET))


        _target_id = d.pop("targetId", UNSET)
        target_id: UUID | Unset
        if isinstance(_target_id,  Unset):
            target_id = UNSET
        else:
            target_id = UUID(_target_id)




        def _parse_target_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_type = _parse_target_type(d.pop("targetType", UNSET))


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


        view_count = d.pop("viewCount", UNSET)

        office_share_link_dto = cls(
            allow_download=allow_download,
            created_at=created_at,
            created_by=created_by,
            expires_at=expires_at,
            id=id,
            last_viewed_at=last_viewed_at,
            requires_password=requires_password,
            revoked_at=revoked_at,
            target_id=target_id,
            target_type=target_type,
            token=token,
            url=url,
            view_count=view_count,
        )

        return office_share_link_dto


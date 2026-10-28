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






T = TypeVar("T", bound="GisCreateSyncTokenResult")



@_attrs_define
class GisCreateSyncTokenResult:
    

    expires_at: datetime.datetime | Unset = UNSET
    token: None | str | Unset = UNSET
    ttl_seconds: int | Unset = UNSET
    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        ttl_seconds = self.ttl_seconds

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if token is not UNSET:
            field_dict["token"] = token
        if ttl_seconds is not UNSET:
            field_dict["ttl_seconds"] = ttl_seconds
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))


        ttl_seconds = d.pop("ttl_seconds", UNSET)

        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        gis_create_sync_token_result = cls(
            expires_at=expires_at,
            token=token,
            ttl_seconds=ttl_seconds,
            zone_id=zone_id,
        )

        return gis_create_sync_token_result


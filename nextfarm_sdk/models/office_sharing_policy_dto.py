from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeSharingPolicyDto")



@_attrs_define
class OfficeSharingPolicyDto:
    

    allow_download: bool | Unset = UNSET
    allow_external_sharing: bool | Unset = UNSET
    link_expiry_days: int | None | Unset = UNSET
    require_password: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allow_download = self.allow_download

        allow_external_sharing = self.allow_external_sharing

        link_expiry_days: int | None | Unset
        if isinstance(self.link_expiry_days, Unset):
            link_expiry_days = UNSET
        else:
            link_expiry_days = self.link_expiry_days

        require_password = self.require_password


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allow_download is not UNSET:
            field_dict["allowDownload"] = allow_download
        if allow_external_sharing is not UNSET:
            field_dict["allowExternalSharing"] = allow_external_sharing
        if link_expiry_days is not UNSET:
            field_dict["linkExpiryDays"] = link_expiry_days
        if require_password is not UNSET:
            field_dict["requirePassword"] = require_password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_download = d.pop("allowDownload", UNSET)

        allow_external_sharing = d.pop("allowExternalSharing", UNSET)

        def _parse_link_expiry_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        link_expiry_days = _parse_link_expiry_days(d.pop("linkExpiryDays", UNSET))


        require_password = d.pop("requirePassword", UNSET)

        office_sharing_policy_dto = cls(
            allow_download=allow_download,
            allow_external_sharing=allow_external_sharing,
            link_expiry_days=link_expiry_days,
            require_password=require_password,
        )

        return office_sharing_policy_dto


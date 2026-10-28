from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeShareLinksControllerCreateRequest")



@_attrs_define
class OfficeShareLinksControllerCreateRequest:
    

    allow_download: bool | Unset = UNSET
    expiry_days: int | None | Unset = UNSET
    password: None | str | Unset = UNSET
    target_id: UUID | Unset = UNSET
    target_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allow_download = self.allow_download

        expiry_days: int | None | Unset
        if isinstance(self.expiry_days, Unset):
            expiry_days = UNSET
        else:
            expiry_days = self.expiry_days

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        target_id: str | Unset = UNSET
        if not isinstance(self.target_id, Unset):
            target_id = str(self.target_id)

        target_type: None | str | Unset
        if isinstance(self.target_type, Unset):
            target_type = UNSET
        else:
            target_type = self.target_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allow_download is not UNSET:
            field_dict["allowDownload"] = allow_download
        if expiry_days is not UNSET:
            field_dict["expiryDays"] = expiry_days
        if password is not UNSET:
            field_dict["password"] = password
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if target_type is not UNSET:
            field_dict["targetType"] = target_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_download = d.pop("allowDownload", UNSET)

        def _parse_expiry_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expiry_days = _parse_expiry_days(d.pop("expiryDays", UNSET))


        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))


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


        office_share_links_controller_create_request = cls(
            allow_download=allow_download,
            expiry_days=expiry_days,
            password=password,
            target_id=target_id,
            target_type=target_type,
        )

        return office_share_links_controller_create_request


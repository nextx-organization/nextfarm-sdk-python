from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeResolvedMemberEmailDto")



@_attrs_define
class OfficeResolvedMemberEmailDto:
    

    avatar_url: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    job_title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if email is not UNSET:
            field_dict["email"] = email
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))


        office_resolved_member_email_dto = cls(
            avatar_url=avatar_url,
            email=email,
            full_name=full_name,
            id=id,
            job_title=job_title,
        )

        return office_resolved_member_email_dto


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






T = TypeVar("T", bound="OfficeOrgMemberDto")



@_attrs_define
class OfficeOrgMemberDto:
    

    avatar_url: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    branch_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    employee_code: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    joined_at: datetime.datetime | None | Unset = UNSET
    manager_user_id: None | Unset | UUID = UNSET
    phone: None | str | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        employee_code: None | str | Unset
        if isinstance(self.employee_code, Unset):
            employee_code = UNSET
        else:
            employee_code = self.employee_code

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        joined_at: None | str | Unset
        if isinstance(self.joined_at, Unset):
            joined_at = UNSET
        elif isinstance(self.joined_at, datetime.datetime):
            joined_at = self.joined_at.isoformat()
        else:
            joined_at = self.joined_at

        manager_user_id: None | str | Unset
        if isinstance(self.manager_user_id, Unset):
            manager_user_id = UNSET
        elif isinstance(self.manager_user_id, UUID):
            manager_user_id = str(self.manager_user_id)
        else:
            manager_user_id = self.manager_user_id

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if email is not UNSET:
            field_dict["email"] = email
        if employee_code is not UNSET:
            field_dict["employeeCode"] = employee_code
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if joined_at is not UNSET:
            field_dict["joinedAt"] = joined_at
        if manager_user_id is not UNSET:
            field_dict["managerUserId"] = manager_user_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if user_id is not UNSET:
            field_dict["userId"] = user_id

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


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_employee_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_code = _parse_employee_code(d.pop("employeeCode", UNSET))


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))


        def _parse_joined_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                joined_at_type_0 = datetime.datetime.fromisoformat(data)



                return joined_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        joined_at = _parse_joined_at(d.pop("joinedAt", UNSET))


        def _parse_manager_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manager_user_id_type_0 = UUID(data)



                return manager_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        manager_user_id = _parse_manager_user_id(d.pop("managerUserId", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_org_member_dto = cls(
            avatar_url=avatar_url,
            branch_id=branch_id,
            branch_name=branch_name,
            email=email,
            employee_code=employee_code,
            full_name=full_name,
            job_title=job_title,
            joined_at=joined_at,
            manager_user_id=manager_user_id,
            phone=phone,
            user_id=user_id,
        )

        return office_org_member_dto


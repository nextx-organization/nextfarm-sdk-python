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






T = TypeVar("T", bound="OfficeFarmDeviceRuleApprovalDto")



@_attrs_define
class OfficeFarmDeviceRuleApprovalDto:
    

    approved: bool | Unset = UNSET
    approved_at: datetime.datetime | None | Unset = UNSET
    approved_by: None | Unset | UUID = UNSET
    automation_id: UUID | Unset = UNSET
    can_approve: bool | Unset = UNSET
    valid: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        approved = self.approved

        approved_at: None | str | Unset
        if isinstance(self.approved_at, Unset):
            approved_at = UNSET
        elif isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        approved_by: None | str | Unset
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        elif isinstance(self.approved_by, UUID):
            approved_by = str(self.approved_by)
        else:
            approved_by = self.approved_by

        automation_id: str | Unset = UNSET
        if not isinstance(self.automation_id, Unset):
            automation_id = str(self.automation_id)

        can_approve = self.can_approve

        valid = self.valid


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approved is not UNSET:
            field_dict["approved"] = approved
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if automation_id is not UNSET:
            field_dict["automationId"] = automation_id
        if can_approve is not UNSET:
            field_dict["canApprove"] = can_approve
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approved = d.pop("approved", UNSET)

        def _parse_approved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)



                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approved_at = _parse_approved_at(d.pop("approvedAt", UNSET))


        def _parse_approved_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_type_0 = UUID(data)



                return approved_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        approved_by = _parse_approved_by(d.pop("approvedBy", UNSET))


        _automation_id = d.pop("automationId", UNSET)
        automation_id: UUID | Unset
        if isinstance(_automation_id,  Unset):
            automation_id = UNSET
        else:
            automation_id = UUID(_automation_id)




        can_approve = d.pop("canApprove", UNSET)

        valid = d.pop("valid", UNSET)

        office_farm_device_rule_approval_dto = cls(
            approved=approved,
            approved_at=approved_at,
            approved_by=approved_by,
            automation_id=automation_id,
            can_approve=can_approve,
            valid=valid,
        )

        return office_farm_device_rule_approval_dto


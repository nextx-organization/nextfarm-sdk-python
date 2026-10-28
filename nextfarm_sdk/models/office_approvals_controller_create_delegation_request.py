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






T = TypeVar("T", bound="OfficeApprovalsControllerCreateDelegationRequest")



@_attrs_define
class OfficeApprovalsControllerCreateDelegationRequest:
    

    delegate_id: UUID | Unset = UNSET
    from_at: datetime.datetime | Unset = UNSET
    reason: None | str | Unset = UNSET
    to_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        delegate_id: str | Unset = UNSET
        if not isinstance(self.delegate_id, Unset):
            delegate_id = str(self.delegate_id)

        from_at: str | Unset = UNSET
        if not isinstance(self.from_at, Unset):
            from_at = self.from_at.isoformat()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        to_at: str | Unset = UNSET
        if not isinstance(self.to_at, Unset):
            to_at = self.to_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if delegate_id is not UNSET:
            field_dict["delegateId"] = delegate_id
        if from_at is not UNSET:
            field_dict["fromAt"] = from_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if to_at is not UNSET:
            field_dict["toAt"] = to_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _delegate_id = d.pop("delegateId", UNSET)
        delegate_id: UUID | Unset
        if isinstance(_delegate_id,  Unset):
            delegate_id = UNSET
        else:
            delegate_id = UUID(_delegate_id)




        _from_at = d.pop("fromAt", UNSET)
        from_at: datetime.datetime | Unset
        if isinstance(_from_at,  Unset):
            from_at = UNSET
        else:
            from_at = datetime.datetime.fromisoformat(_from_at)




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        _to_at = d.pop("toAt", UNSET)
        to_at: datetime.datetime | Unset
        if isinstance(_to_at,  Unset):
            to_at = UNSET
        else:
            to_at = datetime.datetime.fromisoformat(_to_at)




        office_approvals_controller_create_delegation_request = cls(
            delegate_id=delegate_id,
            from_at=from_at,
            reason=reason,
            to_at=to_at,
        )

        return office_approvals_controller_create_delegation_request


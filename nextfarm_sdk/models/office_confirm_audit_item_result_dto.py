from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeConfirmAuditItemResultDto")



@_attrs_define
class OfficeConfirmAuditItemResultDto:
    

    discrepancy_approval_instance_id: None | Unset | UUID = UNSET
    discrepancy_approval_raised: bool | Unset = UNSET
    discrepancy_blocked_reason_key: None | str | Unset = UNSET
    is_matched: bool | Unset = UNSET
    item_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        discrepancy_approval_instance_id: None | str | Unset
        if isinstance(self.discrepancy_approval_instance_id, Unset):
            discrepancy_approval_instance_id = UNSET
        elif isinstance(self.discrepancy_approval_instance_id, UUID):
            discrepancy_approval_instance_id = str(self.discrepancy_approval_instance_id)
        else:
            discrepancy_approval_instance_id = self.discrepancy_approval_instance_id

        discrepancy_approval_raised = self.discrepancy_approval_raised

        discrepancy_blocked_reason_key: None | str | Unset
        if isinstance(self.discrepancy_blocked_reason_key, Unset):
            discrepancy_blocked_reason_key = UNSET
        else:
            discrepancy_blocked_reason_key = self.discrepancy_blocked_reason_key

        is_matched = self.is_matched

        item_id: str | Unset = UNSET
        if not isinstance(self.item_id, Unset):
            item_id = str(self.item_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if discrepancy_approval_instance_id is not UNSET:
            field_dict["discrepancyApprovalInstanceId"] = discrepancy_approval_instance_id
        if discrepancy_approval_raised is not UNSET:
            field_dict["discrepancyApprovalRaised"] = discrepancy_approval_raised
        if discrepancy_blocked_reason_key is not UNSET:
            field_dict["discrepancyBlockedReasonKey"] = discrepancy_blocked_reason_key
        if is_matched is not UNSET:
            field_dict["isMatched"] = is_matched
        if item_id is not UNSET:
            field_dict["itemId"] = item_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_discrepancy_approval_instance_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discrepancy_approval_instance_id_type_0 = UUID(data)



                return discrepancy_approval_instance_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        discrepancy_approval_instance_id = _parse_discrepancy_approval_instance_id(d.pop("discrepancyApprovalInstanceId", UNSET))


        discrepancy_approval_raised = d.pop("discrepancyApprovalRaised", UNSET)

        def _parse_discrepancy_blocked_reason_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discrepancy_blocked_reason_key = _parse_discrepancy_blocked_reason_key(d.pop("discrepancyBlockedReasonKey", UNSET))


        is_matched = d.pop("isMatched", UNSET)

        _item_id = d.pop("itemId", UNSET)
        item_id: UUID | Unset
        if isinstance(_item_id,  Unset):
            item_id = UNSET
        else:
            item_id = UUID(_item_id)




        office_confirm_audit_item_result_dto = cls(
            discrepancy_approval_instance_id=discrepancy_approval_instance_id,
            discrepancy_approval_raised=discrepancy_approval_raised,
            discrepancy_blocked_reason_key=discrepancy_blocked_reason_key,
            is_matched=is_matched,
            item_id=item_id,
        )

        return office_confirm_audit_item_result_dto


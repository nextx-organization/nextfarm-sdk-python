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






T = TypeVar("T", bound="OfficeAssetAuditItemDto")



@_attrs_define
class OfficeAssetAuditItemDto:
    

    actual_condition: None | str | Unset = UNSET
    asset_code: None | str | Unset = UNSET
    asset_id: UUID | Unset = UNSET
    asset_name: None | str | Unset = UNSET
    audit_id: UUID | Unset = UNSET
    confirmed_at: datetime.datetime | None | Unset = UNSET
    confirmed_by: None | Unset | UUID = UNSET
    discrepancy_approval_instance_id: None | Unset | UUID = UNSET
    expected_holder_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    is_matched: bool | None | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        actual_condition: None | str | Unset
        if isinstance(self.actual_condition, Unset):
            actual_condition = UNSET
        else:
            actual_condition = self.actual_condition

        asset_code: None | str | Unset
        if isinstance(self.asset_code, Unset):
            asset_code = UNSET
        else:
            asset_code = self.asset_code

        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        asset_name: None | str | Unset
        if isinstance(self.asset_name, Unset):
            asset_name = UNSET
        else:
            asset_name = self.asset_name

        audit_id: str | Unset = UNSET
        if not isinstance(self.audit_id, Unset):
            audit_id = str(self.audit_id)

        confirmed_at: None | str | Unset
        if isinstance(self.confirmed_at, Unset):
            confirmed_at = UNSET
        elif isinstance(self.confirmed_at, datetime.datetime):
            confirmed_at = self.confirmed_at.isoformat()
        else:
            confirmed_at = self.confirmed_at

        confirmed_by: None | str | Unset
        if isinstance(self.confirmed_by, Unset):
            confirmed_by = UNSET
        elif isinstance(self.confirmed_by, UUID):
            confirmed_by = str(self.confirmed_by)
        else:
            confirmed_by = self.confirmed_by

        discrepancy_approval_instance_id: None | str | Unset
        if isinstance(self.discrepancy_approval_instance_id, Unset):
            discrepancy_approval_instance_id = UNSET
        elif isinstance(self.discrepancy_approval_instance_id, UUID):
            discrepancy_approval_instance_id = str(self.discrepancy_approval_instance_id)
        else:
            discrepancy_approval_instance_id = self.discrepancy_approval_instance_id

        expected_holder_id: None | str | Unset
        if isinstance(self.expected_holder_id, Unset):
            expected_holder_id = UNSET
        elif isinstance(self.expected_holder_id, UUID):
            expected_holder_id = str(self.expected_holder_id)
        else:
            expected_holder_id = self.expected_holder_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_matched: bool | None | Unset
        if isinstance(self.is_matched, Unset):
            is_matched = UNSET
        else:
            is_matched = self.is_matched

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actual_condition is not UNSET:
            field_dict["actualCondition"] = actual_condition
        if asset_code is not UNSET:
            field_dict["assetCode"] = asset_code
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id
        if confirmed_at is not UNSET:
            field_dict["confirmedAt"] = confirmed_at
        if confirmed_by is not UNSET:
            field_dict["confirmedBy"] = confirmed_by
        if discrepancy_approval_instance_id is not UNSET:
            field_dict["discrepancyApprovalInstanceId"] = discrepancy_approval_instance_id
        if expected_holder_id is not UNSET:
            field_dict["expectedHolderId"] = expected_holder_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_matched is not UNSET:
            field_dict["isMatched"] = is_matched
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_actual_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_condition = _parse_actual_condition(d.pop("actualCondition", UNSET))


        def _parse_asset_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_code = _parse_asset_code(d.pop("assetCode", UNSET))


        _asset_id = d.pop("assetId", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id,  Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)




        def _parse_asset_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_name = _parse_asset_name(d.pop("assetName", UNSET))


        _audit_id = d.pop("auditId", UNSET)
        audit_id: UUID | Unset
        if isinstance(_audit_id,  Unset):
            audit_id = UNSET
        else:
            audit_id = UUID(_audit_id)




        def _parse_confirmed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmed_at_type_0 = datetime.datetime.fromisoformat(data)



                return confirmed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmedAt", UNSET))


        def _parse_confirmed_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmed_by_type_0 = UUID(data)



                return confirmed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        confirmed_by = _parse_confirmed_by(d.pop("confirmedBy", UNSET))


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


        def _parse_expected_holder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_holder_id_type_0 = UUID(data)



                return expected_holder_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        expected_holder_id = _parse_expected_holder_id(d.pop("expectedHolderId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_is_matched(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_matched = _parse_is_matched(d.pop("isMatched", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        office_asset_audit_item_dto = cls(
            actual_condition=actual_condition,
            asset_code=asset_code,
            asset_id=asset_id,
            asset_name=asset_name,
            audit_id=audit_id,
            confirmed_at=confirmed_at,
            confirmed_by=confirmed_by,
            discrepancy_approval_instance_id=discrepancy_approval_instance_id,
            expected_holder_id=expected_holder_id,
            id=id,
            is_matched=is_matched,
            note=note,
        )

        return office_asset_audit_item_dto


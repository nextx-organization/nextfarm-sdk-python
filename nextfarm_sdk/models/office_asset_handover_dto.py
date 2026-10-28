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






T = TypeVar("T", bound="OfficeAssetHandoverDto")



@_attrs_define
class OfficeAssetHandoverDto:
    

    approval_instance_id: None | Unset | UUID = UNSET
    asset_code: None | str | Unset = UNSET
    asset_id: UUID | Unset = UNSET
    asset_name: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    condition: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    from_user_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    note: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    to_user_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        approval_instance_id: None | str | Unset
        if isinstance(self.approval_instance_id, Unset):
            approval_instance_id = UNSET
        elif isinstance(self.approval_instance_id, UUID):
            approval_instance_id = str(self.approval_instance_id)
        else:
            approval_instance_id = self.approval_instance_id

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

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        condition: None | str | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        from_user_id: None | str | Unset
        if isinstance(self.from_user_id, Unset):
            from_user_id = UNSET
        elif isinstance(self.from_user_id, UUID):
            from_user_id = str(self.from_user_id)
        else:
            from_user_id = self.from_user_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        to_user_id: None | str | Unset
        if isinstance(self.to_user_id, Unset):
            to_user_id = UNSET
        elif isinstance(self.to_user_id, UUID):
            to_user_id = str(self.to_user_id)
        else:
            to_user_id = self.to_user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approval_instance_id is not UNSET:
            field_dict["approvalInstanceId"] = approval_instance_id
        if asset_code is not UNSET:
            field_dict["assetCode"] = asset_code
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if condition is not UNSET:
            field_dict["condition"] = condition
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if from_user_id is not UNSET:
            field_dict["fromUserId"] = from_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if status is not UNSET:
            field_dict["status"] = status
        if to_user_id is not UNSET:
            field_dict["toUserId"] = to_user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_approval_instance_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approval_instance_id_type_0 = UUID(data)



                return approval_instance_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        approval_instance_id = _parse_approval_instance_id(d.pop("approvalInstanceId", UNSET))


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


        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        def _parse_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_from_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_user_id_type_0 = UUID(data)



                return from_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        from_user_id = _parse_from_user_id(d.pop("fromUserId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_to_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_user_id_type_0 = UUID(data)



                return to_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        to_user_id = _parse_to_user_id(d.pop("toUserId", UNSET))


        office_asset_handover_dto = cls(
            approval_instance_id=approval_instance_id,
            asset_code=asset_code,
            asset_id=asset_id,
            asset_name=asset_name,
            completed_at=completed_at,
            condition=condition,
            created_at=created_at,
            from_user_id=from_user_id,
            id=id,
            note=note,
            status=status,
            to_user_id=to_user_id,
        )

        return office_asset_handover_dto


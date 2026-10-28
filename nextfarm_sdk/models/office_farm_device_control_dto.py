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






T = TypeVar("T", bound="OfficeFarmDeviceControlDto")



@_attrs_define
class OfficeFarmDeviceControlDto:
    

    approver_ids: list[UUID] | None | Unset = UNSET
    automation_id: UUID | Unset = UNSET
    can_decide: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    decided_at: datetime.datetime | None | Unset = UNSET
    decided_by: None | Unset | UUID = UNSET
    device_id: UUID | Unset = UNSET
    device_label: None | str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    family: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    idx: int | Unset = UNSET
    iot_command_id: None | Unset | UUID = UNSET
    note: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    value: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        approver_ids: list[str] | None | Unset
        if isinstance(self.approver_ids, Unset):
            approver_ids = UNSET
        elif isinstance(self.approver_ids, list):
            approver_ids = []
            for approver_ids_type_0_item_data in self.approver_ids:
                approver_ids_type_0_item = str(approver_ids_type_0_item_data)
                approver_ids.append(approver_ids_type_0_item)


        else:
            approver_ids = self.approver_ids

        automation_id: str | Unset = UNSET
        if not isinstance(self.automation_id, Unset):
            automation_id = str(self.automation_id)

        can_decide = self.can_decide

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        decided_at: None | str | Unset
        if isinstance(self.decided_at, Unset):
            decided_at = UNSET
        elif isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        decided_by: None | str | Unset
        if isinstance(self.decided_by, Unset):
            decided_by = UNSET
        elif isinstance(self.decided_by, UUID):
            decided_by = str(self.decided_by)
        else:
            decided_by = self.decided_by

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        device_label: None | str | Unset
        if isinstance(self.device_label, Unset):
            device_label = UNSET
        else:
            device_label = self.device_label

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        idx = self.idx

        iot_command_id: None | str | Unset
        if isinstance(self.iot_command_id, Unset):
            iot_command_id = UNSET
        elif isinstance(self.iot_command_id, UUID):
            iot_command_id = str(self.iot_command_id)
        else:
            iot_command_id = self.iot_command_id

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approver_ids is not UNSET:
            field_dict["approverIds"] = approver_ids
        if automation_id is not UNSET:
            field_dict["automationId"] = automation_id
        if can_decide is not UNSET:
            field_dict["canDecide"] = can_decide
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if decided_at is not UNSET:
            field_dict["decidedAt"] = decided_at
        if decided_by is not UNSET:
            field_dict["decidedBy"] = decided_by
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_label is not UNSET:
            field_dict["deviceLabel"] = device_label
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if family is not UNSET:
            field_dict["family"] = family
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if iot_command_id is not UNSET:
            field_dict["iotCommandId"] = iot_command_id
        if note is not UNSET:
            field_dict["note"] = note
        if reason is not UNSET:
            field_dict["reason"] = reason
        if status is not UNSET:
            field_dict["status"] = status
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_approver_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                approver_ids_type_0 = []
                _approver_ids_type_0 = data
                for approver_ids_type_0_item_data in (_approver_ids_type_0):
                    approver_ids_type_0_item = UUID(approver_ids_type_0_item_data)



                    approver_ids_type_0.append(approver_ids_type_0_item)

                return approver_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        approver_ids = _parse_approver_ids(d.pop("approverIds", UNSET))


        _automation_id = d.pop("automationId", UNSET)
        automation_id: UUID | Unset
        if isinstance(_automation_id,  Unset):
            automation_id = UNSET
        else:
            automation_id = UUID(_automation_id)




        can_decide = d.pop("canDecide", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_decided_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_at_type_0 = datetime.datetime.fromisoformat(data)



                return decided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        decided_at = _parse_decided_at(d.pop("decidedAt", UNSET))


        def _parse_decided_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_by_type_0 = UUID(data)



                return decided_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        decided_by = _parse_decided_by(d.pop("decidedBy", UNSET))


        _device_id = d.pop("deviceId", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        def _parse_device_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_label = _parse_device_label(d.pop("deviceLabel", UNSET))


        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        idx = d.pop("idx", UNSET)

        def _parse_iot_command_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                iot_command_id_type_0 = UUID(data)



                return iot_command_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        iot_command_id = _parse_iot_command_id(d.pop("iotCommandId", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        value = d.pop("value", UNSET)

        office_farm_device_control_dto = cls(
            approver_ids=approver_ids,
            automation_id=automation_id,
            can_decide=can_decide,
            created_at=created_at,
            decided_at=decided_at,
            decided_by=decided_by,
            device_id=device_id,
            device_label=device_label,
            expires_at=expires_at,
            family=family,
            id=id,
            idx=idx,
            iot_command_id=iot_command_id,
            note=note,
            reason=reason,
            status=status,
            value=value,
        )

        return office_farm_device_control_dto


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






T = TypeVar("T", bound="OfficeActivityLogDto")



@_attrs_define
class OfficeActivityLogDto:
    

    action: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    event_status: None | str | Unset = UNSET
    event_type: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    new_values: None | str | Unset = UNSET
    old_values: None | str | Unset = UNSET
    resource_id: None | Unset | UUID = UNSET
    resource_type: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        event_status: None | str | Unset
        if isinstance(self.event_status, Unset):
            event_status = UNSET
        else:
            event_status = self.event_status

        event_type: None | str | Unset
        if isinstance(self.event_type, Unset):
            event_type = UNSET
        else:
            event_type = self.event_type

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        new_values: None | str | Unset
        if isinstance(self.new_values, Unset):
            new_values = UNSET
        else:
            new_values = self.new_values

        old_values: None | str | Unset
        if isinstance(self.old_values, Unset):
            old_values = UNSET
        else:
            old_values = self.old_values

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        elif isinstance(self.resource_id, UUID):
            resource_id = str(self.resource_id)
        else:
            resource_id = self.resource_id

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if event_status is not UNSET:
            field_dict["eventStatus"] = event_status
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if new_values is not UNSET:
            field_dict["newValues"] = new_values
        if old_values is not UNSET:
            field_dict["oldValues"] = old_values
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_event_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_status = _parse_event_status(d.pop("eventStatus", UNSET))


        def _parse_event_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_type = _parse_event_type(d.pop("eventType", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_new_values(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_values = _parse_new_values(d.pop("newValues", UNSET))


        def _parse_old_values(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_values = _parse_old_values(d.pop("oldValues", UNSET))


        def _parse_resource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_id_type_0 = UUID(data)



                return resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))


        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resourceType", UNSET))


        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)



                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


        office_activity_log_dto = cls(
            action=action,
            created_at=created_at,
            event_status=event_status,
            event_type=event_type,
            id=id,
            new_values=new_values,
            old_values=old_values,
            resource_id=resource_id,
            resource_type=resource_type,
            user_id=user_id,
        )

        return office_activity_log_dto


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






T = TypeVar("T", bound="OfficeSendMessageResultDto")



@_attrs_define
class OfficeSendMessageResultDto:
    

    created_at: datetime.datetime | Unset = UNSET
    deduplicated: bool | Unset = UNSET
    message_id: UUID | Unset = UNSET
    registered_attachments: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deduplicated = self.deduplicated

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        registered_attachments = self.registered_attachments


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if deduplicated is not UNSET:
            field_dict["deduplicated"] = deduplicated
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if registered_attachments is not UNSET:
            field_dict["registeredAttachments"] = registered_attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        deduplicated = d.pop("deduplicated", UNSET)

        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        registered_attachments = d.pop("registeredAttachments", UNSET)

        office_send_message_result_dto = cls(
            created_at=created_at,
            deduplicated=deduplicated,
            message_id=message_id,
            registered_attachments=registered_attachments,
        )

        return office_send_message_result_dto


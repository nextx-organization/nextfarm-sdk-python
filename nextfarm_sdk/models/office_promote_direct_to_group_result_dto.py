from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficePromoteDirectToGroupResultDto")



@_attrs_define
class OfficePromoteDirectToGroupResultDto:
    

    channel_id: UUID | Unset = UNSET
    sync_truncated: bool | Unset = UNSET
    synced_message_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        sync_truncated = self.sync_truncated

        synced_message_count = self.synced_message_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if sync_truncated is not UNSET:
            field_dict["syncTruncated"] = sync_truncated
        if synced_message_count is not UNSET:
            field_dict["syncedMessageCount"] = synced_message_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        sync_truncated = d.pop("syncTruncated", UNSET)

        synced_message_count = d.pop("syncedMessageCount", UNSET)

        office_promote_direct_to_group_result_dto = cls(
            channel_id=channel_id,
            sync_truncated=sync_truncated,
            synced_message_count=synced_message_count,
        )

        return office_promote_direct_to_group_result_dto


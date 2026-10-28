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






T = TypeVar("T", bound="OfficeCallRecordingItemDto")



@_attrs_define
class OfficeCallRecordingItemDto:
    

    call_id: UUID | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    duration_seconds: int | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    playback_url: None | str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    started_by: None | Unset | UUID = UNSET
    state: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        call_id: str | Unset = UNSET
        if not isinstance(self.call_id, Unset):
            call_id = str(self.call_id)

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        duration_seconds: int | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        playback_url: None | str | Unset
        if isinstance(self.playback_url, Unset):
            playback_url = UNSET
        else:
            playback_url = self.playback_url

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        started_by: None | str | Unset
        if isinstance(self.started_by, Unset):
            started_by = UNSET
        elif isinstance(self.started_by, UUID):
            started_by = str(self.started_by)
        else:
            started_by = self.started_by

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if call_id is not UNSET:
            field_dict["callId"] = call_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if playback_url is not UNSET:
            field_dict["playbackUrl"] = playback_url
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if started_by is not UNSET:
            field_dict["startedBy"] = started_by
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _call_id = d.pop("callId", UNSET)
        call_id: UUID | Unset
        if isinstance(_call_id,  Unset):
            call_id = UNSET
        else:
            call_id = UUID(_call_id)




        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("durationSeconds", UNSET))


        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)



                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))


        def _parse_playback_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        playback_url = _parse_playback_url(d.pop("playbackUrl", UNSET))


        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        def _parse_started_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_by_type_0 = UUID(data)



                return started_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        started_by = _parse_started_by(d.pop("startedBy", UNSET))


        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        office_call_recording_item_dto = cls(
            call_id=call_id,
            channel_id=channel_id,
            duration_seconds=duration_seconds,
            ended_at=ended_at,
            playback_url=playback_url,
            started_at=started_at,
            started_by=started_by,
            state=state,
        )

        return office_call_recording_item_dto


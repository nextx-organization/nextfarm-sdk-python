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






T = TypeVar("T", bound="OfficeCallDto")



@_attrs_define
class OfficeCallDto:
    

    answered_at: datetime.datetime | None | Unset = UNSET
    callee_ids: list[UUID] | None | Unset = UNSET
    caller_id: UUID | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    end_reason: None | str | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    id: UUID | Unset = UNSET
    kind: None | str | Unset = UNSET
    recording_started_at: datetime.datetime | None | Unset = UNSET
    recording_started_by: None | Unset | UUID = UNSET
    recording_state: None | str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        answered_at: None | str | Unset
        if isinstance(self.answered_at, Unset):
            answered_at = UNSET
        elif isinstance(self.answered_at, datetime.datetime):
            answered_at = self.answered_at.isoformat()
        else:
            answered_at = self.answered_at

        callee_ids: list[str] | None | Unset
        if isinstance(self.callee_ids, Unset):
            callee_ids = UNSET
        elif isinstance(self.callee_ids, list):
            callee_ids = []
            for callee_ids_type_0_item_data in self.callee_ids:
                callee_ids_type_0_item = str(callee_ids_type_0_item_data)
                callee_ids.append(callee_ids_type_0_item)


        else:
            callee_ids = self.callee_ids

        caller_id: str | Unset = UNSET
        if not isinstance(self.caller_id, Unset):
            caller_id = str(self.caller_id)

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        end_reason: None | str | Unset
        if isinstance(self.end_reason, Unset):
            end_reason = UNSET
        else:
            end_reason = self.end_reason

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        recording_started_at: None | str | Unset
        if isinstance(self.recording_started_at, Unset):
            recording_started_at = UNSET
        elif isinstance(self.recording_started_at, datetime.datetime):
            recording_started_at = self.recording_started_at.isoformat()
        else:
            recording_started_at = self.recording_started_at

        recording_started_by: None | str | Unset
        if isinstance(self.recording_started_by, Unset):
            recording_started_by = UNSET
        elif isinstance(self.recording_started_by, UUID):
            recording_started_by = str(self.recording_started_by)
        else:
            recording_started_by = self.recording_started_by

        recording_state: None | str | Unset
        if isinstance(self.recording_state, Unset):
            recording_state = UNSET
        else:
            recording_state = self.recording_state

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if answered_at is not UNSET:
            field_dict["answeredAt"] = answered_at
        if callee_ids is not UNSET:
            field_dict["calleeIds"] = callee_ids
        if caller_id is not UNSET:
            field_dict["callerId"] = caller_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if end_reason is not UNSET:
            field_dict["endReason"] = end_reason
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if recording_started_at is not UNSET:
            field_dict["recordingStartedAt"] = recording_started_at
        if recording_started_by is not UNSET:
            field_dict["recordingStartedBy"] = recording_started_by
        if recording_state is not UNSET:
            field_dict["recordingState"] = recording_state
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_answered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                answered_at_type_0 = datetime.datetime.fromisoformat(data)



                return answered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        answered_at = _parse_answered_at(d.pop("answeredAt", UNSET))


        def _parse_callee_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                callee_ids_type_0 = []
                _callee_ids_type_0 = data
                for callee_ids_type_0_item_data in (_callee_ids_type_0):
                    callee_ids_type_0_item = UUID(callee_ids_type_0_item_data)



                    callee_ids_type_0.append(callee_ids_type_0_item)

                return callee_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        callee_ids = _parse_callee_ids(d.pop("calleeIds", UNSET))


        _caller_id = d.pop("callerId", UNSET)
        caller_id: UUID | Unset
        if isinstance(_caller_id,  Unset):
            caller_id = UNSET
        else:
            caller_id = UUID(_caller_id)




        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_end_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_reason = _parse_end_reason(d.pop("endReason", UNSET))


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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_recording_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recording_started_at_type_0 = datetime.datetime.fromisoformat(data)



                return recording_started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        recording_started_at = _parse_recording_started_at(d.pop("recordingStartedAt", UNSET))


        def _parse_recording_started_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recording_started_by_type_0 = UUID(data)



                return recording_started_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        recording_started_by = _parse_recording_started_by(d.pop("recordingStartedBy", UNSET))


        def _parse_recording_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recording_state = _parse_recording_state(d.pop("recordingState", UNSET))


        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_call_dto = cls(
            answered_at=answered_at,
            callee_ids=callee_ids,
            caller_id=caller_id,
            channel_id=channel_id,
            end_reason=end_reason,
            ended_at=ended_at,
            id=id,
            kind=kind,
            recording_started_at=recording_started_at,
            recording_started_by=recording_started_by,
            recording_state=recording_state,
            started_at=started_at,
            status=status,
        )

        return office_call_dto


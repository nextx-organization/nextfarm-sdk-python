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

if TYPE_CHECKING:
  from ..models.office_meeting_action_item_dto import OfficeMeetingActionItemDto





T = TypeVar("T", bound="OfficeMeetingMinuteDto")



@_attrs_define
class OfficeMeetingMinuteDto:
    

    action_items: list[OfficeMeetingActionItemDto] | None | Unset = UNSET
    artifacts_fetched_at: datetime.datetime | None | Unset = UNSET
    decisions: None | str | Unset = UNSET
    event_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    recorded_by: UUID | Unset = UNSET
    recording_url: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    transcript_text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_meeting_action_item_dto import OfficeMeetingActionItemDto # noqa: PLC0415
        action_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.action_items, Unset):
            action_items = UNSET
        elif isinstance(self.action_items, list):
            action_items = []
            for action_items_type_0_item_data in self.action_items:
                action_items_type_0_item = action_items_type_0_item_data.to_dict()
                action_items.append(action_items_type_0_item)


        else:
            action_items = self.action_items

        artifacts_fetched_at: None | str | Unset
        if isinstance(self.artifacts_fetched_at, Unset):
            artifacts_fetched_at = UNSET
        elif isinstance(self.artifacts_fetched_at, datetime.datetime):
            artifacts_fetched_at = self.artifacts_fetched_at.isoformat()
        else:
            artifacts_fetched_at = self.artifacts_fetched_at

        decisions: None | str | Unset
        if isinstance(self.decisions, Unset):
            decisions = UNSET
        else:
            decisions = self.decisions

        event_id: str | Unset = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        recorded_by: str | Unset = UNSET
        if not isinstance(self.recorded_by, Unset):
            recorded_by = str(self.recorded_by)

        recording_url: None | str | Unset
        if isinstance(self.recording_url, Unset):
            recording_url = UNSET
        else:
            recording_url = self.recording_url

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        transcript_text: None | str | Unset
        if isinstance(self.transcript_text, Unset):
            transcript_text = UNSET
        else:
            transcript_text = self.transcript_text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action_items is not UNSET:
            field_dict["actionItems"] = action_items
        if artifacts_fetched_at is not UNSET:
            field_dict["artifactsFetchedAt"] = artifacts_fetched_at
        if decisions is not UNSET:
            field_dict["decisions"] = decisions
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if id is not UNSET:
            field_dict["id"] = id
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if recorded_by is not UNSET:
            field_dict["recordedBy"] = recorded_by
        if recording_url is not UNSET:
            field_dict["recordingUrl"] = recording_url
        if summary is not UNSET:
            field_dict["summary"] = summary
        if transcript_text is not UNSET:
            field_dict["transcriptText"] = transcript_text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_meeting_action_item_dto import OfficeMeetingActionItemDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_action_items(data: object) -> list[OfficeMeetingActionItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                action_items_type_0 = []
                _action_items_type_0 = data
                for action_items_type_0_item_data in (_action_items_type_0):
                    action_items_type_0_item = OfficeMeetingActionItemDto.from_dict(action_items_type_0_item_data)



                    action_items_type_0.append(action_items_type_0_item)

                return action_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeMeetingActionItemDto] | None | Unset, data)

        action_items = _parse_action_items(d.pop("actionItems", UNSET))


        def _parse_artifacts_fetched_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                artifacts_fetched_at_type_0 = datetime.datetime.fromisoformat(data)



                return artifacts_fetched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        artifacts_fetched_at = _parse_artifacts_fetched_at(d.pop("artifactsFetchedAt", UNSET))


        def _parse_decisions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decisions = _parse_decisions(d.pop("decisions", UNSET))


        _event_id = d.pop("eventId", UNSET)
        event_id: UUID | Unset
        if isinstance(_event_id,  Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)



                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))


        _recorded_by = d.pop("recordedBy", UNSET)
        recorded_by: UUID | Unset
        if isinstance(_recorded_by,  Unset):
            recorded_by = UNSET
        else:
            recorded_by = UUID(_recorded_by)




        def _parse_recording_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recording_url = _parse_recording_url(d.pop("recordingUrl", UNSET))


        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_transcript_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcript_text = _parse_transcript_text(d.pop("transcriptText", UNSET))


        office_meeting_minute_dto = cls(
            action_items=action_items,
            artifacts_fetched_at=artifacts_fetched_at,
            decisions=decisions,
            event_id=event_id,
            id=id,
            published_at=published_at,
            recorded_by=recorded_by,
            recording_url=recording_url,
            summary=summary,
            transcript_text=transcript_text,
        )

        return office_meeting_minute_dto


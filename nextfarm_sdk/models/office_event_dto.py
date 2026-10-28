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
  from ..models.office_event_attendee_dto import OfficeEventAttendeeDto
  from ..models.office_event_reminder_dto import OfficeEventReminderDto
  from ..models.office_event_room_dto import OfficeEventRoomDto
  from ..models.office_event_time_proposal_dto import OfficeEventTimeProposalDto





T = TypeVar("T", bound="OfficeEventDto")



@_attrs_define
class OfficeEventDto:
    

    all_day: bool | Unset = UNSET
    attendees: list[OfficeEventAttendeeDto] | None | Unset = UNSET
    calendar_id: UUID | Unset = UNSET
    chat_channel_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    event_type: None | str | Unset = UNSET
    from_personal_calendar: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    location: None | str | Unset = UNSET
    meeting_provider: None | str | Unset = UNSET
    meeting_removal_pending: bool | Unset = UNSET
    meeting_url: None | str | Unset = UNSET
    organizer_id: UUID | Unset = UNSET
    push_error_key: None | str | Unset = UNSET
    push_pending: bool | Unset = UNSET
    recurrence_rule: None | str | Unset = UNSET
    remind_before_minutes: int | None | Unset = UNSET
    reminders: list[OfficeEventReminderDto] | None | Unset = UNSET
    rooms: list[OfficeEventRoomDto] | None | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    status: None | str | Unset = UNSET
    synced_with_google: bool | Unset = UNSET
    time_proposals: list[OfficeEventTimeProposalDto] | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_event_attendee_dto import OfficeEventAttendeeDto # noqa: PLC0415
        from ..models.office_event_reminder_dto import OfficeEventReminderDto # noqa: PLC0415
        from ..models.office_event_room_dto import OfficeEventRoomDto # noqa: PLC0415
        from ..models.office_event_time_proposal_dto import OfficeEventTimeProposalDto # noqa: PLC0415
        all_day = self.all_day

        attendees: list[dict[str, Any]] | None | Unset
        if isinstance(self.attendees, Unset):
            attendees = UNSET
        elif isinstance(self.attendees, list):
            attendees = []
            for attendees_type_0_item_data in self.attendees:
                attendees_type_0_item = attendees_type_0_item_data.to_dict()
                attendees.append(attendees_type_0_item)


        else:
            attendees = self.attendees

        calendar_id: str | Unset = UNSET
        if not isinstance(self.calendar_id, Unset):
            calendar_id = str(self.calendar_id)

        chat_channel_id: None | str | Unset
        if isinstance(self.chat_channel_id, Unset):
            chat_channel_id = UNSET
        elif isinstance(self.chat_channel_id, UUID):
            chat_channel_id = str(self.chat_channel_id)
        else:
            chat_channel_id = self.chat_channel_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        event_type: None | str | Unset
        if isinstance(self.event_type, Unset):
            event_type = UNSET
        else:
            event_type = self.event_type

        from_personal_calendar = self.from_personal_calendar

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        meeting_provider: None | str | Unset
        if isinstance(self.meeting_provider, Unset):
            meeting_provider = UNSET
        else:
            meeting_provider = self.meeting_provider

        meeting_removal_pending = self.meeting_removal_pending

        meeting_url: None | str | Unset
        if isinstance(self.meeting_url, Unset):
            meeting_url = UNSET
        else:
            meeting_url = self.meeting_url

        organizer_id: str | Unset = UNSET
        if not isinstance(self.organizer_id, Unset):
            organizer_id = str(self.organizer_id)

        push_error_key: None | str | Unset
        if isinstance(self.push_error_key, Unset):
            push_error_key = UNSET
        else:
            push_error_key = self.push_error_key

        push_pending = self.push_pending

        recurrence_rule: None | str | Unset
        if isinstance(self.recurrence_rule, Unset):
            recurrence_rule = UNSET
        else:
            recurrence_rule = self.recurrence_rule

        remind_before_minutes: int | None | Unset
        if isinstance(self.remind_before_minutes, Unset):
            remind_before_minutes = UNSET
        else:
            remind_before_minutes = self.remind_before_minutes

        reminders: list[dict[str, Any]] | None | Unset
        if isinstance(self.reminders, Unset):
            reminders = UNSET
        elif isinstance(self.reminders, list):
            reminders = []
            for reminders_type_0_item_data in self.reminders:
                reminders_type_0_item = reminders_type_0_item_data.to_dict()
                reminders.append(reminders_type_0_item)


        else:
            reminders = self.reminders

        rooms: list[dict[str, Any]] | None | Unset
        if isinstance(self.rooms, Unset):
            rooms = UNSET
        elif isinstance(self.rooms, list):
            rooms = []
            for rooms_type_0_item_data in self.rooms:
                rooms_type_0_item = rooms_type_0_item_data.to_dict()
                rooms.append(rooms_type_0_item)


        else:
            rooms = self.rooms

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        synced_with_google = self.synced_with_google

        time_proposals: list[dict[str, Any]] | None | Unset
        if isinstance(self.time_proposals, Unset):
            time_proposals = UNSET
        elif isinstance(self.time_proposals, list):
            time_proposals = []
            for time_proposals_type_0_item_data in self.time_proposals:
                time_proposals_type_0_item = time_proposals_type_0_item_data.to_dict()
                time_proposals.append(time_proposals_type_0_item)


        else:
            time_proposals = self.time_proposals

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if all_day is not UNSET:
            field_dict["allDay"] = all_day
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if calendar_id is not UNSET:
            field_dict["calendarId"] = calendar_id
        if chat_channel_id is not UNSET:
            field_dict["chatChannelId"] = chat_channel_id
        if description is not UNSET:
            field_dict["description"] = description
        if end_at is not UNSET:
            field_dict["endAt"] = end_at
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if from_personal_calendar is not UNSET:
            field_dict["fromPersonalCalendar"] = from_personal_calendar
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if meeting_provider is not UNSET:
            field_dict["meetingProvider"] = meeting_provider
        if meeting_removal_pending is not UNSET:
            field_dict["meetingRemovalPending"] = meeting_removal_pending
        if meeting_url is not UNSET:
            field_dict["meetingUrl"] = meeting_url
        if organizer_id is not UNSET:
            field_dict["organizerId"] = organizer_id
        if push_error_key is not UNSET:
            field_dict["pushErrorKey"] = push_error_key
        if push_pending is not UNSET:
            field_dict["pushPending"] = push_pending
        if recurrence_rule is not UNSET:
            field_dict["recurrenceRule"] = recurrence_rule
        if remind_before_minutes is not UNSET:
            field_dict["remindBeforeMinutes"] = remind_before_minutes
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if status is not UNSET:
            field_dict["status"] = status
        if synced_with_google is not UNSET:
            field_dict["syncedWithGoogle"] = synced_with_google
        if time_proposals is not UNSET:
            field_dict["timeProposals"] = time_proposals
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_event_attendee_dto import OfficeEventAttendeeDto # noqa: PLC0415
        from ..models.office_event_reminder_dto import OfficeEventReminderDto # noqa: PLC0415
        from ..models.office_event_room_dto import OfficeEventRoomDto # noqa: PLC0415
        from ..models.office_event_time_proposal_dto import OfficeEventTimeProposalDto # noqa: PLC0415
        d = dict(src_dict)
        all_day = d.pop("allDay", UNSET)

        def _parse_attendees(data: object) -> list[OfficeEventAttendeeDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attendees_type_0 = []
                _attendees_type_0 = data
                for attendees_type_0_item_data in (_attendees_type_0):
                    attendees_type_0_item = OfficeEventAttendeeDto.from_dict(attendees_type_0_item_data)



                    attendees_type_0.append(attendees_type_0_item)

                return attendees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeEventAttendeeDto] | None | Unset, data)

        attendees = _parse_attendees(d.pop("attendees", UNSET))


        _calendar_id = d.pop("calendarId", UNSET)
        calendar_id: UUID | Unset
        if isinstance(_calendar_id,  Unset):
            calendar_id = UNSET
        else:
            calendar_id = UUID(_calendar_id)




        def _parse_chat_channel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chat_channel_id_type_0 = UUID(data)



                return chat_channel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        chat_channel_id = _parse_chat_channel_id(d.pop("chatChannelId", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _end_at = d.pop("endAt", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at,  Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)




        def _parse_event_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_type = _parse_event_type(d.pop("eventType", UNSET))


        from_personal_calendar = d.pop("fromPersonalCalendar", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_meeting_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meeting_provider = _parse_meeting_provider(d.pop("meetingProvider", UNSET))


        meeting_removal_pending = d.pop("meetingRemovalPending", UNSET)

        def _parse_meeting_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meeting_url = _parse_meeting_url(d.pop("meetingUrl", UNSET))


        _organizer_id = d.pop("organizerId", UNSET)
        organizer_id: UUID | Unset
        if isinstance(_organizer_id,  Unset):
            organizer_id = UNSET
        else:
            organizer_id = UUID(_organizer_id)




        def _parse_push_error_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        push_error_key = _parse_push_error_key(d.pop("pushErrorKey", UNSET))


        push_pending = d.pop("pushPending", UNSET)

        def _parse_recurrence_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recurrence_rule = _parse_recurrence_rule(d.pop("recurrenceRule", UNSET))


        def _parse_remind_before_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remind_before_minutes = _parse_remind_before_minutes(d.pop("remindBeforeMinutes", UNSET))


        def _parse_reminders(data: object) -> list[OfficeEventReminderDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reminders_type_0 = []
                _reminders_type_0 = data
                for reminders_type_0_item_data in (_reminders_type_0):
                    reminders_type_0_item = OfficeEventReminderDto.from_dict(reminders_type_0_item_data)



                    reminders_type_0.append(reminders_type_0_item)

                return reminders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeEventReminderDto] | None | Unset, data)

        reminders = _parse_reminders(d.pop("reminders", UNSET))


        def _parse_rooms(data: object) -> list[OfficeEventRoomDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rooms_type_0 = []
                _rooms_type_0 = data
                for rooms_type_0_item_data in (_rooms_type_0):
                    rooms_type_0_item = OfficeEventRoomDto.from_dict(rooms_type_0_item_data)



                    rooms_type_0.append(rooms_type_0_item)

                return rooms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeEventRoomDto] | None | Unset, data)

        rooms = _parse_rooms(d.pop("rooms", UNSET))


        _start_at = d.pop("startAt", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at,  Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        synced_with_google = d.pop("syncedWithGoogle", UNSET)

        def _parse_time_proposals(data: object) -> list[OfficeEventTimeProposalDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                time_proposals_type_0 = []
                _time_proposals_type_0 = data
                for time_proposals_type_0_item_data in (_time_proposals_type_0):
                    time_proposals_type_0_item = OfficeEventTimeProposalDto.from_dict(time_proposals_type_0_item_data)



                    time_proposals_type_0.append(time_proposals_type_0_item)

                return time_proposals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeEventTimeProposalDto] | None | Unset, data)

        time_proposals = _parse_time_proposals(d.pop("timeProposals", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_event_dto = cls(
            all_day=all_day,
            attendees=attendees,
            calendar_id=calendar_id,
            chat_channel_id=chat_channel_id,
            description=description,
            end_at=end_at,
            event_type=event_type,
            from_personal_calendar=from_personal_calendar,
            id=id,
            location=location,
            meeting_provider=meeting_provider,
            meeting_removal_pending=meeting_removal_pending,
            meeting_url=meeting_url,
            organizer_id=organizer_id,
            push_error_key=push_error_key,
            push_pending=push_pending,
            recurrence_rule=recurrence_rule,
            remind_before_minutes=remind_before_minutes,
            reminders=reminders,
            rooms=rooms,
            start_at=start_at,
            status=status,
            synced_with_google=synced_with_google,
            time_proposals=time_proposals,
            title=title,
        )

        return office_event_dto


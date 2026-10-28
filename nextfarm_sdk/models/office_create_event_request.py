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






T = TypeVar("T", bound="OfficeCreateEventRequest")



@_attrs_define
class OfficeCreateEventRequest:
    

    all_day: bool | Unset = UNSET
    attendee_user_ids: list[UUID] | None | Unset = UNSET
    calendar_id: None | Unset | UUID = UNSET
    chat_channel_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    event_type: None | str | Unset = UNSET
    guest_emails: list[str] | None | Unset = UNSET
    location: None | str | Unset = UNSET
    meeting_provider: None | str | Unset = UNSET
    recurrence_rule: None | str | Unset = UNSET
    remind_before_minutes: int | None | Unset = UNSET
    room_ids: list[UUID] | None | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    title: None | str | Unset = UNSET
    with_google_meet: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        all_day = self.all_day

        attendee_user_ids: list[str] | None | Unset
        if isinstance(self.attendee_user_ids, Unset):
            attendee_user_ids = UNSET
        elif isinstance(self.attendee_user_ids, list):
            attendee_user_ids = []
            for attendee_user_ids_type_0_item_data in self.attendee_user_ids:
                attendee_user_ids_type_0_item = str(attendee_user_ids_type_0_item_data)
                attendee_user_ids.append(attendee_user_ids_type_0_item)


        else:
            attendee_user_ids = self.attendee_user_ids

        calendar_id: None | str | Unset
        if isinstance(self.calendar_id, Unset):
            calendar_id = UNSET
        elif isinstance(self.calendar_id, UUID):
            calendar_id = str(self.calendar_id)
        else:
            calendar_id = self.calendar_id

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

        guest_emails: list[str] | None | Unset
        if isinstance(self.guest_emails, Unset):
            guest_emails = UNSET
        elif isinstance(self.guest_emails, list):
            guest_emails = self.guest_emails


        else:
            guest_emails = self.guest_emails

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

        room_ids: list[str] | None | Unset
        if isinstance(self.room_ids, Unset):
            room_ids = UNSET
        elif isinstance(self.room_ids, list):
            room_ids = []
            for room_ids_type_0_item_data in self.room_ids:
                room_ids_type_0_item = str(room_ids_type_0_item_data)
                room_ids.append(room_ids_type_0_item)


        else:
            room_ids = self.room_ids

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        with_google_meet = self.with_google_meet


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if all_day is not UNSET:
            field_dict["allDay"] = all_day
        if attendee_user_ids is not UNSET:
            field_dict["attendeeUserIds"] = attendee_user_ids
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
        if guest_emails is not UNSET:
            field_dict["guestEmails"] = guest_emails
        if location is not UNSET:
            field_dict["location"] = location
        if meeting_provider is not UNSET:
            field_dict["meetingProvider"] = meeting_provider
        if recurrence_rule is not UNSET:
            field_dict["recurrenceRule"] = recurrence_rule
        if remind_before_minutes is not UNSET:
            field_dict["remindBeforeMinutes"] = remind_before_minutes
        if room_ids is not UNSET:
            field_dict["roomIds"] = room_ids
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if title is not UNSET:
            field_dict["title"] = title
        if with_google_meet is not UNSET:
            field_dict["withGoogleMeet"] = with_google_meet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_day = d.pop("allDay", UNSET)

        def _parse_attendee_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attendee_user_ids_type_0 = []
                _attendee_user_ids_type_0 = data
                for attendee_user_ids_type_0_item_data in (_attendee_user_ids_type_0):
                    attendee_user_ids_type_0_item = UUID(attendee_user_ids_type_0_item_data)



                    attendee_user_ids_type_0.append(attendee_user_ids_type_0_item)

                return attendee_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        attendee_user_ids = _parse_attendee_user_ids(d.pop("attendeeUserIds", UNSET))


        def _parse_calendar_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                calendar_id_type_0 = UUID(data)



                return calendar_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        calendar_id = _parse_calendar_id(d.pop("calendarId", UNSET))


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


        def _parse_guest_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guest_emails_type_0 = cast(list[str], data)

                return guest_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guest_emails = _parse_guest_emails(d.pop("guestEmails", UNSET))


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


        def _parse_room_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                room_ids_type_0 = []
                _room_ids_type_0 = data
                for room_ids_type_0_item_data in (_room_ids_type_0):
                    room_ids_type_0_item = UUID(room_ids_type_0_item_data)



                    room_ids_type_0.append(room_ids_type_0_item)

                return room_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        room_ids = _parse_room_ids(d.pop("roomIds", UNSET))


        _start_at = d.pop("startAt", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at,  Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        with_google_meet = d.pop("withGoogleMeet", UNSET)

        office_create_event_request = cls(
            all_day=all_day,
            attendee_user_ids=attendee_user_ids,
            calendar_id=calendar_id,
            chat_channel_id=chat_channel_id,
            description=description,
            end_at=end_at,
            event_type=event_type,
            guest_emails=guest_emails,
            location=location,
            meeting_provider=meeting_provider,
            recurrence_rule=recurrence_rule,
            remind_before_minutes=remind_before_minutes,
            room_ids=room_ids,
            start_at=start_at,
            title=title,
            with_google_meet=with_google_meet,
        )

        return office_create_event_request


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






T = TypeVar("T", bound="OfficeCalendarEntryDto")



@_attrs_define
class OfficeCalendarEntryDto:
    

    all_day: bool | Unset = UNSET
    attendee_count: int | Unset = UNSET
    calendar_color: None | str | Unset = UNSET
    calendar_id: UUID | Unset = UNSET
    content_visible: bool | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    event_id: UUID | Unset = UNSET
    event_type: None | str | Unset = UNSET
    from_personal_calendar: bool | Unset = UNSET
    id: None | str | Unset = UNSET
    is_recurring: bool | Unset = UNSET
    meeting_url: None | str | Unset = UNSET
    my_response: None | str | Unset = UNSET
    occurrence_start: datetime.datetime | None | Unset = UNSET
    organizer_id: UUID | Unset = UNSET
    room_names: list[str] | None | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    status: None | str | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        all_day = self.all_day

        attendee_count = self.attendee_count

        calendar_color: None | str | Unset
        if isinstance(self.calendar_color, Unset):
            calendar_color = UNSET
        else:
            calendar_color = self.calendar_color

        calendar_id: str | Unset = UNSET
        if not isinstance(self.calendar_id, Unset):
            calendar_id = str(self.calendar_id)

        content_visible = self.content_visible

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        event_id: str | Unset = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        event_type: None | str | Unset
        if isinstance(self.event_type, Unset):
            event_type = UNSET
        else:
            event_type = self.event_type

        from_personal_calendar = self.from_personal_calendar

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        is_recurring = self.is_recurring

        meeting_url: None | str | Unset
        if isinstance(self.meeting_url, Unset):
            meeting_url = UNSET
        else:
            meeting_url = self.meeting_url

        my_response: None | str | Unset
        if isinstance(self.my_response, Unset):
            my_response = UNSET
        else:
            my_response = self.my_response

        occurrence_start: None | str | Unset
        if isinstance(self.occurrence_start, Unset):
            occurrence_start = UNSET
        elif isinstance(self.occurrence_start, datetime.datetime):
            occurrence_start = self.occurrence_start.isoformat()
        else:
            occurrence_start = self.occurrence_start

        organizer_id: str | Unset = UNSET
        if not isinstance(self.organizer_id, Unset):
            organizer_id = str(self.organizer_id)

        room_names: list[str] | None | Unset
        if isinstance(self.room_names, Unset):
            room_names = UNSET
        elif isinstance(self.room_names, list):
            room_names = self.room_names


        else:
            room_names = self.room_names

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

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
        if attendee_count is not UNSET:
            field_dict["attendeeCount"] = attendee_count
        if calendar_color is not UNSET:
            field_dict["calendarColor"] = calendar_color
        if calendar_id is not UNSET:
            field_dict["calendarId"] = calendar_id
        if content_visible is not UNSET:
            field_dict["contentVisible"] = content_visible
        if end_at is not UNSET:
            field_dict["endAt"] = end_at
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if from_personal_calendar is not UNSET:
            field_dict["fromPersonalCalendar"] = from_personal_calendar
        if id is not UNSET:
            field_dict["id"] = id
        if is_recurring is not UNSET:
            field_dict["isRecurring"] = is_recurring
        if meeting_url is not UNSET:
            field_dict["meetingUrl"] = meeting_url
        if my_response is not UNSET:
            field_dict["myResponse"] = my_response
        if occurrence_start is not UNSET:
            field_dict["occurrenceStart"] = occurrence_start
        if organizer_id is not UNSET:
            field_dict["organizerId"] = organizer_id
        if room_names is not UNSET:
            field_dict["roomNames"] = room_names
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_day = d.pop("allDay", UNSET)

        attendee_count = d.pop("attendeeCount", UNSET)

        def _parse_calendar_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        calendar_color = _parse_calendar_color(d.pop("calendarColor", UNSET))


        _calendar_id = d.pop("calendarId", UNSET)
        calendar_id: UUID | Unset
        if isinstance(_calendar_id,  Unset):
            calendar_id = UNSET
        else:
            calendar_id = UUID(_calendar_id)




        content_visible = d.pop("contentVisible", UNSET)

        _end_at = d.pop("endAt", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at,  Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)




        _event_id = d.pop("eventId", UNSET)
        event_id: UUID | Unset
        if isinstance(_event_id,  Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)




        def _parse_event_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_type = _parse_event_type(d.pop("eventType", UNSET))


        from_personal_calendar = d.pop("fromPersonalCalendar", UNSET)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        is_recurring = d.pop("isRecurring", UNSET)

        def _parse_meeting_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meeting_url = _parse_meeting_url(d.pop("meetingUrl", UNSET))


        def _parse_my_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        my_response = _parse_my_response(d.pop("myResponse", UNSET))


        def _parse_occurrence_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                occurrence_start_type_0 = datetime.datetime.fromisoformat(data)



                return occurrence_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        occurrence_start = _parse_occurrence_start(d.pop("occurrenceStart", UNSET))


        _organizer_id = d.pop("organizerId", UNSET)
        organizer_id: UUID | Unset
        if isinstance(_organizer_id,  Unset):
            organizer_id = UNSET
        else:
            organizer_id = UUID(_organizer_id)




        def _parse_room_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                room_names_type_0 = cast(list[str], data)

                return room_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        room_names = _parse_room_names(d.pop("roomNames", UNSET))


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


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_calendar_entry_dto = cls(
            all_day=all_day,
            attendee_count=attendee_count,
            calendar_color=calendar_color,
            calendar_id=calendar_id,
            content_visible=content_visible,
            end_at=end_at,
            event_id=event_id,
            event_type=event_type,
            from_personal_calendar=from_personal_calendar,
            id=id,
            is_recurring=is_recurring,
            meeting_url=meeting_url,
            my_response=my_response,
            occurrence_start=occurrence_start,
            organizer_id=organizer_id,
            room_names=room_names,
            start_at=start_at,
            status=status,
            title=title,
        )

        return office_calendar_entry_dto


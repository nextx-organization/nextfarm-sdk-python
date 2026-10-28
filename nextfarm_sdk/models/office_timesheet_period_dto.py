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






T = TypeVar("T", bound="OfficeTimesheetPeriodDto")



@_attrs_define
class OfficeTimesheetPeriodDto:
    

    created_at: datetime.datetime | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    id: UUID | Unset = UNSET
    review_note: None | str | Unset = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    reviewed_by: None | Unset | UUID = UNSET
    start_date: datetime.date | Unset = UNSET
    status: None | str | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    submitted_by: None | Unset | UUID = UNSET
    total_hours: float | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        review_note: None | str | Unset
        if isinstance(self.review_note, Unset):
            review_note = UNSET
        else:
            review_note = self.review_note

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

        reviewed_by: None | str | Unset
        if isinstance(self.reviewed_by, Unset):
            reviewed_by = UNSET
        elif isinstance(self.reviewed_by, UUID):
            reviewed_by = str(self.reviewed_by)
        else:
            reviewed_by = self.reviewed_by

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        submitted_by: None | str | Unset
        if isinstance(self.submitted_by, Unset):
            submitted_by = UNSET
        elif isinstance(self.submitted_by, UUID):
            submitted_by = str(self.submitted_by)
        else:
            submitted_by = self.submitted_by

        total_hours = self.total_hours

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if id is not UNSET:
            field_dict["id"] = id
        if review_note is not UNSET:
            field_dict["reviewNote"] = review_note
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at
        if reviewed_by is not UNSET:
            field_dict["reviewedBy"] = reviewed_by
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if status is not UNSET:
            field_dict["status"] = status
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if total_hours is not UNSET:
            field_dict["totalHours"] = total_hours
        if user_id is not UNSET:
            field_dict["userId"] = user_id

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




        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_review_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_note = _parse_review_note(d.pop("reviewNote", UNSET))


        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = datetime.datetime.fromisoformat(data)



                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewedAt", UNSET))


        def _parse_reviewed_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_by_type_0 = UUID(data)



                return reviewed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reviewed_by = _parse_reviewed_by(d.pop("reviewedBy", UNSET))


        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = datetime.datetime.fromisoformat(data)



                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submittedAt", UNSET))


        def _parse_submitted_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_by_type_0 = UUID(data)



                return submitted_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        submitted_by = _parse_submitted_by(d.pop("submittedBy", UNSET))


        total_hours = d.pop("totalHours", UNSET)

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_timesheet_period_dto = cls(
            created_at=created_at,
            end_date=end_date,
            id=id,
            review_note=review_note,
            reviewed_at=reviewed_at,
            reviewed_by=reviewed_by,
            start_date=start_date,
            status=status,
            submitted_at=submitted_at,
            submitted_by=submitted_by,
            total_hours=total_hours,
            user_id=user_id,
        )

        return office_timesheet_period_dto


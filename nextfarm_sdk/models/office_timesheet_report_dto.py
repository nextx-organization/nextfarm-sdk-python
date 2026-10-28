from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.office_timesheet_user_total_dto import OfficeTimesheetUserTotalDto





T = TypeVar("T", bound="OfficeTimesheetReportDto")



@_attrs_define
class OfficeTimesheetReportDto:
    

    by_user: list[OfficeTimesheetUserTotalDto] | None | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    to: datetime.date | Unset = UNSET
    total_hours: float | Unset = UNSET
    working_days: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_timesheet_user_total_dto import OfficeTimesheetUserTotalDto # noqa: PLC0415
        by_user: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_user, Unset):
            by_user = UNSET
        elif isinstance(self.by_user, list):
            by_user = []
            for by_user_type_0_item_data in self.by_user:
                by_user_type_0_item = by_user_type_0_item_data.to_dict()
                by_user.append(by_user_type_0_item)


        else:
            by_user = self.by_user

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        total_hours = self.total_hours

        working_days = self.working_days


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if by_user is not UNSET:
            field_dict["byUser"] = by_user
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if total_hours is not UNSET:
            field_dict["totalHours"] = total_hours
        if working_days is not UNSET:
            field_dict["workingDays"] = working_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_timesheet_user_total_dto import OfficeTimesheetUserTotalDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_by_user(data: object) -> list[OfficeTimesheetUserTotalDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_user_type_0 = []
                _by_user_type_0 = data
                for by_user_type_0_item_data in (_by_user_type_0):
                    by_user_type_0_item = OfficeTimesheetUserTotalDto.from_dict(by_user_type_0_item_data)



                    by_user_type_0.append(by_user_type_0_item)

                return by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTimesheetUserTotalDto] | None | Unset, data)

        by_user = _parse_by_user(d.pop("byUser", UNSET))


        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        total_hours = d.pop("totalHours", UNSET)

        working_days = d.pop("workingDays", UNSET)

        office_timesheet_report_dto = cls(
            by_user=by_user,
            from_=from_,
            to=to,
            total_hours=total_hours,
            working_days=working_days,
        )

        return office_timesheet_report_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeUpdateReviewCycleRequest")



@_attrs_define
class OfficeUpdateReviewCycleRequest:
    

    description: None | str | Unset = UNSET
    due_date: datetime.datetime | Unset = UNSET
    name: None | str | Unset = UNSET
    period_end: datetime.datetime | Unset = UNSET
    period_start: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        period_end: str | Unset = UNSET
        if not isinstance(self.period_end, Unset):
            period_end = self.period_end.isoformat()

        period_start: str | Unset = UNSET
        if not isinstance(self.period_start, Unset):
            period_start = self.period_start.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if name is not UNSET:
            field_dict["name"] = name
        if period_end is not UNSET:
            field_dict["periodEnd"] = period_end
        if period_start is not UNSET:
            field_dict["periodStart"] = period_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.datetime | Unset
        if isinstance(_due_date,  Unset):
            due_date = UNSET
        else:
            due_date = datetime.datetime.fromisoformat(_due_date)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _period_end = d.pop("periodEnd", UNSET)
        period_end: datetime.datetime | Unset
        if isinstance(_period_end,  Unset):
            period_end = UNSET
        else:
            period_end = datetime.datetime.fromisoformat(_period_end)




        _period_start = d.pop("periodStart", UNSET)
        period_start: datetime.datetime | Unset
        if isinstance(_period_start,  Unset):
            period_start = UNSET
        else:
            period_start = datetime.datetime.fromisoformat(_period_start)




        office_update_review_cycle_request = cls(
            description=description,
            due_date=due_date,
            name=name,
            period_end=period_end,
            period_start=period_start,
        )

        return office_update_review_cycle_request


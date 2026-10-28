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






T = TypeVar("T", bound="HarvestIcsFindingRequest")



@_attrs_define
class HarvestIcsFindingRequest:
    

    description: None | str | Unset = UNSET
    due_on: datetime.date | None | Unset = UNSET
    member_id: UUID | Unset = UNSET
    severity: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_on: None | str | Unset
        if isinstance(self.due_on, Unset):
            due_on = UNSET
        elif isinstance(self.due_on, datetime.date):
            due_on = self.due_on.isoformat()
        else:
            due_on = self.due_on

        member_id: str | Unset = UNSET
        if not isinstance(self.member_id, Unset):
            member_id = str(self.member_id)

        severity: None | str | Unset
        if isinstance(self.severity, Unset):
            severity = UNSET
        else:
            severity = self.severity


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if severity is not UNSET:
            field_dict["severity"] = severity

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


        def _parse_due_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_on_type_0 = datetime.date.fromisoformat(data)



                return due_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        due_on = _parse_due_on(d.pop("due_on", UNSET))


        _member_id = d.pop("member_id", UNSET)
        member_id: UUID | Unset
        if isinstance(_member_id,  Unset):
            member_id = UNSET
        else:
            member_id = UUID(_member_id)




        def _parse_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity = _parse_severity(d.pop("severity", UNSET))


        harvest_ics_finding_request = cls(
            description=description,
            due_on=due_on,
            member_id=member_id,
            severity=severity,
        )

        return harvest_ics_finding_request


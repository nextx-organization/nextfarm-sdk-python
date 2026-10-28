from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestIcsFindingActionRequest")



@_attrs_define
class HarvestIcsFindingActionRequest:
    

    action: None | str | Unset = UNSET
    corrective_action: None | str | Unset = UNSET
    due_on: datetime.date | None | Unset = UNSET
    note: None | str | Unset = UNSET
    sanction: None | str | Unset = UNSET
    suspend_until: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        corrective_action: None | str | Unset
        if isinstance(self.corrective_action, Unset):
            corrective_action = UNSET
        else:
            corrective_action = self.corrective_action

        due_on: None | str | Unset
        if isinstance(self.due_on, Unset):
            due_on = UNSET
        elif isinstance(self.due_on, datetime.date):
            due_on = self.due_on.isoformat()
        else:
            due_on = self.due_on

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        sanction: None | str | Unset
        if isinstance(self.sanction, Unset):
            sanction = UNSET
        else:
            sanction = self.sanction

        suspend_until: None | str | Unset
        if isinstance(self.suspend_until, Unset):
            suspend_until = UNSET
        elif isinstance(self.suspend_until, datetime.date):
            suspend_until = self.suspend_until.isoformat()
        else:
            suspend_until = self.suspend_until


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if corrective_action is not UNSET:
            field_dict["corrective_action"] = corrective_action
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if note is not UNSET:
            field_dict["note"] = note
        if sanction is not UNSET:
            field_dict["sanction"] = sanction
        if suspend_until is not UNSET:
            field_dict["suspend_until"] = suspend_until

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


        def _parse_corrective_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corrective_action = _parse_corrective_action(d.pop("corrective_action", UNSET))


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


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_sanction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sanction = _parse_sanction(d.pop("sanction", UNSET))


        def _parse_suspend_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspend_until_type_0 = datetime.date.fromisoformat(data)



                return suspend_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        suspend_until = _parse_suspend_until(d.pop("suspend_until", UNSET))


        harvest_ics_finding_action_request = cls(
            action=action,
            corrective_action=corrective_action,
            due_on=due_on,
            note=note,
            sanction=sanction,
            suspend_until=suspend_until,
        )

        return harvest_ics_finding_action_request


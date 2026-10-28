from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_reminder_input import OfficeReminderInput





T = TypeVar("T", bound="OfficeSetEventRemindersRequest")



@_attrs_define
class OfficeSetEventRemindersRequest:
    

    reminders: list[OfficeReminderInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_reminder_input import OfficeReminderInput # noqa: PLC0415
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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if reminders is not UNSET:
            field_dict["reminders"] = reminders

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_reminder_input import OfficeReminderInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_reminders(data: object) -> list[OfficeReminderInput] | None | Unset:
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
                    reminders_type_0_item = OfficeReminderInput.from_dict(reminders_type_0_item_data)



                    reminders_type_0.append(reminders_type_0_item)

                return reminders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeReminderInput] | None | Unset, data)

        reminders = _parse_reminders(d.pop("reminders", UNSET))


        office_set_event_reminders_request = cls(
            reminders=reminders,
        )

        return office_set_event_reminders_request


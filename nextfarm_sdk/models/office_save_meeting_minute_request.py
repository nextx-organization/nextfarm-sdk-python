from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_action_item_input import OfficeActionItemInput





T = TypeVar("T", bound="OfficeSaveMeetingMinuteRequest")



@_attrs_define
class OfficeSaveMeetingMinuteRequest:
    

    action_items: list[OfficeActionItemInput] | None | Unset = UNSET
    decisions: None | str | Unset = UNSET
    event_id: UUID | Unset = UNSET
    summary: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_action_item_input import OfficeActionItemInput # noqa: PLC0415
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

        decisions: None | str | Unset
        if isinstance(self.decisions, Unset):
            decisions = UNSET
        else:
            decisions = self.decisions

        event_id: str | Unset = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action_items is not UNSET:
            field_dict["actionItems"] = action_items
        if decisions is not UNSET:
            field_dict["decisions"] = decisions
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_action_item_input import OfficeActionItemInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_action_items(data: object) -> list[OfficeActionItemInput] | None | Unset:
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
                    action_items_type_0_item = OfficeActionItemInput.from_dict(action_items_type_0_item_data)



                    action_items_type_0.append(action_items_type_0_item)

                return action_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeActionItemInput] | None | Unset, data)

        action_items = _parse_action_items(d.pop("actionItems", UNSET))


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




        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        office_save_meeting_minute_request = cls(
            action_items=action_items,
            decisions=decisions,
            event_id=event_id,
            summary=summary,
        )

        return office_save_meeting_minute_request


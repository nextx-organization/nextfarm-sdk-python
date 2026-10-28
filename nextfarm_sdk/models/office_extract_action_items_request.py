from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeExtractActionItemsRequest")



@_attrs_define
class OfficeExtractActionItemsRequest:
    

    action_item_ids: list[UUID] | None | Unset = UNSET
    event_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action_item_ids: list[str] | None | Unset
        if isinstance(self.action_item_ids, Unset):
            action_item_ids = UNSET
        elif isinstance(self.action_item_ids, list):
            action_item_ids = []
            for action_item_ids_type_0_item_data in self.action_item_ids:
                action_item_ids_type_0_item = str(action_item_ids_type_0_item_data)
                action_item_ids.append(action_item_ids_type_0_item)


        else:
            action_item_ids = self.action_item_ids

        event_id: str | Unset = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action_item_ids is not UNSET:
            field_dict["actionItemIds"] = action_item_ids
        if event_id is not UNSET:
            field_dict["eventId"] = event_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_action_item_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                action_item_ids_type_0 = []
                _action_item_ids_type_0 = data
                for action_item_ids_type_0_item_data in (_action_item_ids_type_0):
                    action_item_ids_type_0_item = UUID(action_item_ids_type_0_item_data)



                    action_item_ids_type_0.append(action_item_ids_type_0_item)

                return action_item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        action_item_ids = _parse_action_item_ids(d.pop("actionItemIds", UNSET))


        _event_id = d.pop("eventId", UNSET)
        event_id: UUID | Unset
        if isinstance(_event_id,  Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)




        office_extract_action_items_request = cls(
            action_item_ids=action_item_ids,
            event_id=event_id,
        )

        return office_extract_action_items_request


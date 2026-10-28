from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeMessageToWorkItemResultDto")



@_attrs_define
class OfficeMessageToWorkItemResultDto:
    

    card_message_id: None | Unset | UUID = UNSET
    entity_id: UUID | Unset = UNSET
    subtask_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        card_message_id: None | str | Unset
        if isinstance(self.card_message_id, Unset):
            card_message_id = UNSET
        elif isinstance(self.card_message_id, UUID):
            card_message_id = str(self.card_message_id)
        else:
            card_message_id = self.card_message_id

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        subtask_ids: list[str] | None | Unset
        if isinstance(self.subtask_ids, Unset):
            subtask_ids = UNSET
        elif isinstance(self.subtask_ids, list):
            subtask_ids = []
            for subtask_ids_type_0_item_data in self.subtask_ids:
                subtask_ids_type_0_item = str(subtask_ids_type_0_item_data)
                subtask_ids.append(subtask_ids_type_0_item)


        else:
            subtask_ids = self.subtask_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if card_message_id is not UNSET:
            field_dict["cardMessageId"] = card_message_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if subtask_ids is not UNSET:
            field_dict["subtaskIds"] = subtask_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_card_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                card_message_id_type_0 = UUID(data)



                return card_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        card_message_id = _parse_card_message_id(d.pop("cardMessageId", UNSET))


        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        def _parse_subtask_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtask_ids_type_0 = []
                _subtask_ids_type_0 = data
                for subtask_ids_type_0_item_data in (_subtask_ids_type_0):
                    subtask_ids_type_0_item = UUID(subtask_ids_type_0_item_data)



                    subtask_ids_type_0.append(subtask_ids_type_0_item)

                return subtask_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        subtask_ids = _parse_subtask_ids(d.pop("subtaskIds", UNSET))


        office_message_to_work_item_result_dto = cls(
            card_message_id=card_message_id,
            entity_id=entity_id,
            subtask_ids=subtask_ids,
        )

        return office_message_to_work_item_result_dto


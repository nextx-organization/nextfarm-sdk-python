from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeActionCardDto")



@_attrs_define
class OfficeActionCardDto:
    

    available_actions: list[str] | None | Unset = UNSET
    card_type: None | str | Unset = UNSET
    entity_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    message_id: UUID | Unset = UNSET
    payload: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        available_actions: list[str] | None | Unset
        if isinstance(self.available_actions, Unset):
            available_actions = UNSET
        elif isinstance(self.available_actions, list):
            available_actions = self.available_actions


        else:
            available_actions = self.available_actions

        card_type: None | str | Unset
        if isinstance(self.card_type, Unset):
            card_type = UNSET
        else:
            card_type = self.card_type

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

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
        if available_actions is not UNSET:
            field_dict["availableActions"] = available_actions
        if card_type is not UNSET:
            field_dict["cardType"] = card_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if id is not UNSET:
            field_dict["id"] = id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_available_actions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                available_actions_type_0 = cast(list[str], data)

                return available_actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        available_actions = _parse_available_actions(d.pop("availableActions", UNSET))


        def _parse_card_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_type = _parse_card_type(d.pop("cardType", UNSET))


        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))


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


        office_action_card_dto = cls(
            available_actions=available_actions,
            card_type=card_type,
            entity_id=entity_id,
            id=id,
            message_id=message_id,
            payload=payload,
            status=status,
            title=title,
        )

        return office_action_card_dto


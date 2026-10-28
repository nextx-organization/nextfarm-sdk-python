from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerCreatePollRequest")



@_attrs_define
class OfficeChatControllerCreatePollRequest:
    

    allow_multiple: bool | Unset = UNSET
    client_message_id: None | str | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    options: list[str] | None | Unset = UNSET
    question: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allow_multiple = self.allow_multiple

        client_message_id: None | str | Unset
        if isinstance(self.client_message_id, Unset):
            client_message_id = UNSET
        else:
            client_message_id = self.client_message_id

        is_anonymous = self.is_anonymous

        options: list[str] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options


        else:
            options = self.options

        question: None | str | Unset
        if isinstance(self.question, Unset):
            question = UNSET
        else:
            question = self.question


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allow_multiple is not UNSET:
            field_dict["allowMultiple"] = allow_multiple
        if client_message_id is not UNSET:
            field_dict["clientMessageId"] = client_message_id
        if is_anonymous is not UNSET:
            field_dict["isAnonymous"] = is_anonymous
        if options is not UNSET:
            field_dict["options"] = options
        if question is not UNSET:
            field_dict["question"] = question

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_multiple = d.pop("allowMultiple", UNSET)

        def _parse_client_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_message_id = _parse_client_message_id(d.pop("clientMessageId", UNSET))


        is_anonymous = d.pop("isAnonymous", UNSET)

        def _parse_options(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(list[str], data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        def _parse_question(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        question = _parse_question(d.pop("question", UNSET))


        office_chat_controller_create_poll_request = cls(
            allow_multiple=allow_multiple,
            client_message_id=client_message_id,
            is_anonymous=is_anonymous,
            options=options,
            question=question,
        )

        return office_chat_controller_create_poll_request


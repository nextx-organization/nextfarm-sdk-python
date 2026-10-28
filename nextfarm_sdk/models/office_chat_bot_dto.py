from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatBotDto")



@_attrs_define
class OfficeChatBotDto:
    

    bot_id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    reply_mode: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        bot_id: str | Unset = UNSET
        if not isinstance(self.bot_id, Unset):
            bot_id = str(self.bot_id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        is_active = self.is_active

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        reply_mode: None | str | Unset
        if isinstance(self.reply_mode, Unset):
            reply_mode = UNSET
        else:
            reply_mode = self.reply_mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if code is not UNSET:
            field_dict["code"] = code
        if icon is not UNSET:
            field_dict["icon"] = icon
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if name is not UNSET:
            field_dict["name"] = name
        if reply_mode is not UNSET:
            field_dict["replyMode"] = reply_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _bot_id = d.pop("botId", UNSET)
        bot_id: UUID | Unset
        if isinstance(_bot_id,  Unset):
            bot_id = UNSET
        else:
            bot_id = UUID(_bot_id)




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))


        is_active = d.pop("isActive", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_reply_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_mode = _parse_reply_mode(d.pop("replyMode", UNSET))


        office_chat_bot_dto = cls(
            bot_id=bot_id,
            code=code,
            icon=icon,
            is_active=is_active,
            name=name,
            reply_mode=reply_mode,
        )

        return office_chat_bot_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerMyChannelSettingsRequest")



@_attrs_define
class OfficeChatControllerMyChannelSettingsRequest:
    

    auto_translate_to: None | str | Unset = UNSET
    is_flagged: bool | None | Unset = UNSET
    mute_all_mentions: bool | None | Unset = UNSET
    nickname: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auto_translate_to: None | str | Unset
        if isinstance(self.auto_translate_to, Unset):
            auto_translate_to = UNSET
        else:
            auto_translate_to = self.auto_translate_to

        is_flagged: bool | None | Unset
        if isinstance(self.is_flagged, Unset):
            is_flagged = UNSET
        else:
            is_flagged = self.is_flagged

        mute_all_mentions: bool | None | Unset
        if isinstance(self.mute_all_mentions, Unset):
            mute_all_mentions = UNSET
        else:
            mute_all_mentions = self.mute_all_mentions

        nickname: None | str | Unset
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if auto_translate_to is not UNSET:
            field_dict["autoTranslateTo"] = auto_translate_to
        if is_flagged is not UNSET:
            field_dict["isFlagged"] = is_flagged
        if mute_all_mentions is not UNSET:
            field_dict["muteAllMentions"] = mute_all_mentions
        if nickname is not UNSET:
            field_dict["nickname"] = nickname

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_auto_translate_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_translate_to = _parse_auto_translate_to(d.pop("autoTranslateTo", UNSET))


        def _parse_is_flagged(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_flagged = _parse_is_flagged(d.pop("isFlagged", UNSET))


        def _parse_mute_all_mentions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mute_all_mentions = _parse_mute_all_mentions(d.pop("muteAllMentions", UNSET))


        def _parse_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))


        office_chat_controller_my_channel_settings_request = cls(
            auto_translate_to=auto_translate_to,
            is_flagged=is_flagged,
            mute_all_mentions=mute_all_mentions,
            nickname=nickname,
        )

        return office_chat_controller_my_channel_settings_request


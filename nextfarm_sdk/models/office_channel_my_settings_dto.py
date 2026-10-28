from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeChannelMySettingsDto")



@_attrs_define
class OfficeChannelMySettingsDto:
    

    auto_translate_to: None | str | Unset = UNSET
    hidden_at: datetime.datetime | None | Unset = UNSET
    history_cleared_at: datetime.datetime | None | Unset = UNSET
    is_archived_for_me: bool | Unset = UNSET
    is_flagged: bool | Unset = UNSET
    mute_all_mentions: bool | Unset = UNSET
    nickname: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auto_translate_to: None | str | Unset
        if isinstance(self.auto_translate_to, Unset):
            auto_translate_to = UNSET
        else:
            auto_translate_to = self.auto_translate_to

        hidden_at: None | str | Unset
        if isinstance(self.hidden_at, Unset):
            hidden_at = UNSET
        elif isinstance(self.hidden_at, datetime.datetime):
            hidden_at = self.hidden_at.isoformat()
        else:
            hidden_at = self.hidden_at

        history_cleared_at: None | str | Unset
        if isinstance(self.history_cleared_at, Unset):
            history_cleared_at = UNSET
        elif isinstance(self.history_cleared_at, datetime.datetime):
            history_cleared_at = self.history_cleared_at.isoformat()
        else:
            history_cleared_at = self.history_cleared_at

        is_archived_for_me = self.is_archived_for_me

        is_flagged = self.is_flagged

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
        if hidden_at is not UNSET:
            field_dict["hiddenAt"] = hidden_at
        if history_cleared_at is not UNSET:
            field_dict["historyClearedAt"] = history_cleared_at
        if is_archived_for_me is not UNSET:
            field_dict["isArchivedForMe"] = is_archived_for_me
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


        def _parse_hidden_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hidden_at_type_0 = datetime.datetime.fromisoformat(data)



                return hidden_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        hidden_at = _parse_hidden_at(d.pop("hiddenAt", UNSET))


        def _parse_history_cleared_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                history_cleared_at_type_0 = datetime.datetime.fromisoformat(data)



                return history_cleared_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        history_cleared_at = _parse_history_cleared_at(d.pop("historyClearedAt", UNSET))


        is_archived_for_me = d.pop("isArchivedForMe", UNSET)

        is_flagged = d.pop("isFlagged", UNSET)

        mute_all_mentions = d.pop("muteAllMentions", UNSET)

        def _parse_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))


        office_channel_my_settings_dto = cls(
            auto_translate_to=auto_translate_to,
            hidden_at=hidden_at,
            history_cleared_at=history_cleared_at,
            is_archived_for_me=is_archived_for_me,
            is_flagged=is_flagged,
            mute_all_mentions=mute_all_mentions,
            nickname=nickname,
        )

        return office_channel_my_settings_dto


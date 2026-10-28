from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeChatControllerNotificationLevelRequest")



@_attrs_define
class OfficeChatControllerNotificationLevelRequest:
    

    level: None | str | Unset = UNSET
    muted_until: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        level: None | str | Unset
        if isinstance(self.level, Unset):
            level = UNSET
        else:
            level = self.level

        muted_until: None | str | Unset
        if isinstance(self.muted_until, Unset):
            muted_until = UNSET
        elif isinstance(self.muted_until, datetime.datetime):
            muted_until = self.muted_until.isoformat()
        else:
            muted_until = self.muted_until


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if level is not UNSET:
            field_dict["level"] = level
        if muted_until is not UNSET:
            field_dict["mutedUntil"] = muted_until

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level = _parse_level(d.pop("level", UNSET))


        def _parse_muted_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                muted_until_type_0 = datetime.datetime.fromisoformat(data)



                return muted_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        muted_until = _parse_muted_until(d.pop("mutedUntil", UNSET))


        office_chat_controller_notification_level_request = cls(
            level=level,
            muted_until=muted_until,
        )

        return office_chat_controller_notification_level_request


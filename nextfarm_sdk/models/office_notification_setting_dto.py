from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeNotificationSettingDto")



@_attrs_define
class OfficeNotificationSettingDto:
    

    in_app: bool | Unset = UNSET
    notification_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        in_app = self.in_app

        notification_type: None | str | Unset
        if isinstance(self.notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = self.notification_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if in_app is not UNSET:
            field_dict["inApp"] = in_app
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_app = d.pop("inApp", UNSET)

        def _parse_notification_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_type = _parse_notification_type(d.pop("notificationType", UNSET))


        office_notification_setting_dto = cls(
            in_app=in_app,
            notification_type=notification_type,
        )

        return office_notification_setting_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IotSetAlertRuleActiveRequest")



@_attrs_define
class IotSetAlertRuleActiveRequest:
    

    is_active: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_active = self.is_active


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_active = d.pop("is_active", UNSET)

        iot_set_alert_rule_active_request = cls(
            is_active=is_active,
        )

        return iot_set_alert_rule_active_request


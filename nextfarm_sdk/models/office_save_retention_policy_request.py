from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeSaveRetentionPolicyRequest")



@_attrs_define
class OfficeSaveRetentionPolicyRequest:
    

    is_enabled: bool | Unset = UNSET
    retention_days: int | Unset = UNSET
    target: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        retention_days = self.retention_days

        target: None | str | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        def _parse_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target = _parse_target(d.pop("target", UNSET))


        office_save_retention_policy_request = cls(
            is_enabled=is_enabled,
            retention_days=retention_days,
            target=target,
        )

        return office_save_retention_policy_request


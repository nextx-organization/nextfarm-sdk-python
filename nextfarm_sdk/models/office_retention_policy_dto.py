from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeRetentionPolicyDto")



@_attrs_define
class OfficeRetentionPolicyDto:
    

    is_enabled: bool | Unset = UNSET
    last_deleted_count: int | Unset = UNSET
    last_run_at: datetime.datetime | None | Unset = UNSET
    max_days: int | Unset = UNSET
    retention_days: int | Unset = UNSET
    target: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        last_deleted_count = self.last_deleted_count

        last_run_at: None | str | Unset
        if isinstance(self.last_run_at, Unset):
            last_run_at = UNSET
        elif isinstance(self.last_run_at, datetime.datetime):
            last_run_at = self.last_run_at.isoformat()
        else:
            last_run_at = self.last_run_at

        max_days = self.max_days

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
        if last_deleted_count is not UNSET:
            field_dict["lastDeletedCount"] = last_deleted_count
        if last_run_at is not UNSET:
            field_dict["lastRunAt"] = last_run_at
        if max_days is not UNSET:
            field_dict["maxDays"] = max_days
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        last_deleted_count = d.pop("lastDeletedCount", UNSET)

        def _parse_last_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_at = _parse_last_run_at(d.pop("lastRunAt", UNSET))


        max_days = d.pop("maxDays", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        def _parse_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target = _parse_target(d.pop("target", UNSET))


        office_retention_policy_dto = cls(
            is_enabled=is_enabled,
            last_deleted_count=last_deleted_count,
            last_run_at=last_run_at,
            max_days=max_days,
            retention_days=retention_days,
            target=target,
        )

        return office_retention_policy_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeQuotaStatusDto")



@_attrs_define
class OfficeQuotaStatusDto:
    

    has_override: bool | Unset = UNSET
    is_exhausted: bool | Unset = UNSET
    is_measured: bool | Unset = UNSET
    is_near_limit: bool | Unset = UNSET
    key: None | str | Unset = UNSET
    limit: int | Unset = UNSET
    used: int | None | Unset = UNSET
    used_percent: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        has_override = self.has_override

        is_exhausted = self.is_exhausted

        is_measured = self.is_measured

        is_near_limit = self.is_near_limit

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        limit = self.limit

        used: int | None | Unset
        if isinstance(self.used, Unset):
            used = UNSET
        else:
            used = self.used

        used_percent: int | None | Unset
        if isinstance(self.used_percent, Unset):
            used_percent = UNSET
        else:
            used_percent = self.used_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if has_override is not UNSET:
            field_dict["hasOverride"] = has_override
        if is_exhausted is not UNSET:
            field_dict["isExhausted"] = is_exhausted
        if is_measured is not UNSET:
            field_dict["isMeasured"] = is_measured
        if is_near_limit is not UNSET:
            field_dict["isNearLimit"] = is_near_limit
        if key is not UNSET:
            field_dict["key"] = key
        if limit is not UNSET:
            field_dict["limit"] = limit
        if used is not UNSET:
            field_dict["used"] = used
        if used_percent is not UNSET:
            field_dict["usedPercent"] = used_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_override = d.pop("hasOverride", UNSET)

        is_exhausted = d.pop("isExhausted", UNSET)

        is_measured = d.pop("isMeasured", UNSET)

        is_near_limit = d.pop("isNearLimit", UNSET)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        limit = d.pop("limit", UNSET)

        def _parse_used(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used = _parse_used(d.pop("used", UNSET))


        def _parse_used_percent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_percent = _parse_used_percent(d.pop("usedPercent", UNSET))


        office_quota_status_dto = cls(
            has_override=has_override,
            is_exhausted=is_exhausted,
            is_measured=is_measured,
            is_near_limit=is_near_limit,
            key=key,
            limit=limit,
            used=used,
            used_percent=used_percent,
        )

        return office_quota_status_dto


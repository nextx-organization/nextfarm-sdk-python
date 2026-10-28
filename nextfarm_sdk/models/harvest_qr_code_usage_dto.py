from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="HarvestQrCodeUsageDto")



@_attrs_define
class HarvestQrCodeUsageDto:
    

    limit: int | Unset = UNSET
    remaining: int | Unset = UNSET
    used: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        remaining = self.remaining

        used = self.used


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        remaining = d.pop("remaining", UNSET)

        used = d.pop("used", UNSET)

        harvest_qr_code_usage_dto = cls(
            limit=limit,
            remaining=remaining,
            used=used,
        )

        return harvest_qr_code_usage_dto


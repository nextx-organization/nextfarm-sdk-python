from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAutomationQuotaDto")



@_attrs_define
class OfficeAutomationQuotaDto:
    

    limit: int | Unset = UNSET
    month: None | str | Unset = UNSET
    percent: float | Unset = UNSET
    used: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        month: None | str | Unset
        if isinstance(self.month, Unset):
            month = UNSET
        else:
            month = self.month

        percent = self.percent

        used = self.used


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if month is not UNSET:
            field_dict["month"] = month
        if percent is not UNSET:
            field_dict["percent"] = percent
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        def _parse_month(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        month = _parse_month(d.pop("month", UNSET))


        percent = d.pop("percent", UNSET)

        used = d.pop("used", UNSET)

        office_automation_quota_dto = cls(
            limit=limit,
            month=month,
            percent=percent,
            used=used,
        )

        return office_automation_quota_dto


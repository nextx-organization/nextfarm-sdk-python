from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeUpdateJobScheduleRequest")



@_attrs_define
class OfficeUpdateJobScheduleRequest:
    

    cron: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cron: None | str | Unset
        if isinstance(self.cron, Unset):
            cron = UNSET
        else:
            cron = self.cron

        enabled = self.enabled


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cron is not UNSET:
            field_dict["cron"] = cron
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cron(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cron = _parse_cron(d.pop("cron", UNSET))


        enabled = d.pop("enabled", UNSET)

        office_update_job_schedule_request = cls(
            cron=cron,
            enabled=enabled,
        )

        return office_update_job_schedule_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="IotIrrigationSummaryDto")



@_attrs_define
class IotIrrigationSummaryDto:
    

    command_count: int | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    success_command_count: int | Unset = UNSET
    success_rate: float | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    total_volume_l: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        command_count = self.command_count

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        success_command_count = self.success_command_count

        success_rate = self.success_rate

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        total_volume_l = self.total_volume_l


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if command_count is not UNSET:
            field_dict["command_count"] = command_count
        if from_ is not UNSET:
            field_dict["from"] = from_
        if success_command_count is not UNSET:
            field_dict["success_command_count"] = success_command_count
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate
        if to is not UNSET:
            field_dict["to"] = to
        if total_volume_l is not UNSET:
            field_dict["total_volume_l"] = total_volume_l

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command_count = d.pop("command_count", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.datetime.fromisoformat(_from_)




        success_command_count = d.pop("success_command_count", UNSET)

        success_rate = d.pop("success_rate", UNSET)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.datetime.fromisoformat(_to)




        total_volume_l = d.pop("total_volume_l", UNSET)

        iot_irrigation_summary_dto = cls(
            command_count=command_count,
            from_=from_,
            success_command_count=success_command_count,
            success_rate=success_rate,
            to=to,
            total_volume_l=total_volume_l,
        )

        return iot_irrigation_summary_dto


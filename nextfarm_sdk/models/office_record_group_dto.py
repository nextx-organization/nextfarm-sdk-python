from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeRecordGroupDto")



@_attrs_define
class OfficeRecordGroupDto:
    

    count: int | Unset = UNSET
    value: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        value = d.pop("value", UNSET)

        office_record_group_dto = cls(
            count=count,
            value=value,
        )

        return office_record_group_dto


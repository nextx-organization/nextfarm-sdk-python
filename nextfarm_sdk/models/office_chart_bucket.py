from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChartBucket")



@_attrs_define
class OfficeChartBucket:
    

    count: int | Unset = UNSET
    group_key: None | str | Unset = UNSET
    value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        group_key: None | str | Unset
        if isinstance(self.group_key, Unset):
            group_key = UNSET
        else:
            group_key = self.group_key

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if group_key is not UNSET:
            field_dict["groupKey"] = group_key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_group_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_key = _parse_group_key(d.pop("groupKey", UNSET))


        value = d.pop("value", UNSET)

        office_chart_bucket = cls(
            count=count,
            group_key=group_key,
            value=value,
        )

        return office_chart_bucket


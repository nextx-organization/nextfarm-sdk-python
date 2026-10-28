from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeColumnAggregateDto")



@_attrs_define
class OfficeColumnAggregateDto:
    

    average: float | None | Unset = UNSET
    count: int | Unset = UNSET
    field_id: None | str | Unset = UNSET
    max_: float | None | Unset = UNSET
    min_: float | None | Unset = UNSET
    numeric_count: int | Unset = UNSET
    sum_: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        average: float | None | Unset
        if isinstance(self.average, Unset):
            average = UNSET
        else:
            average = self.average

        count = self.count

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        max_: float | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        min_: float | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        numeric_count = self.numeric_count

        sum_ = self.sum_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if average is not UNSET:
            field_dict["average"] = average
        if count is not UNSET:
            field_dict["count"] = count
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if numeric_count is not UNSET:
            field_dict["numericCount"] = numeric_count
        if sum_ is not UNSET:
            field_dict["sum"] = sum_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_average(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average = _parse_average(d.pop("average", UNSET))


        count = d.pop("count", UNSET)

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("fieldId", UNSET))


        def _parse_max_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))


        def _parse_min_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))


        numeric_count = d.pop("numericCount", UNSET)

        sum_ = d.pop("sum", UNSET)

        office_column_aggregate_dto = cls(
            average=average,
            count=count,
            field_id=field_id,
            max_=max_,
            min_=min_,
            numeric_count=numeric_count,
            sum_=sum_,
        )

        return office_column_aggregate_dto


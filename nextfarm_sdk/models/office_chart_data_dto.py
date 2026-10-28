from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_chart_bucket import OfficeChartBucket





T = TypeVar("T", bound="OfficeChartDataDto")



@_attrs_define
class OfficeChartDataDto:
    

    aggregation: None | str | Unset = UNSET
    buckets: list[OfficeChartBucket] | None | Unset = UNSET
    group_field: None | str | Unset = UNSET
    value_field: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chart_bucket import OfficeChartBucket # noqa: PLC0415
        aggregation: None | str | Unset
        if isinstance(self.aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = self.aggregation

        buckets: list[dict[str, Any]] | None | Unset
        if isinstance(self.buckets, Unset):
            buckets = UNSET
        elif isinstance(self.buckets, list):
            buckets = []
            for buckets_type_0_item_data in self.buckets:
                buckets_type_0_item = buckets_type_0_item_data.to_dict()
                buckets.append(buckets_type_0_item)


        else:
            buckets = self.buckets

        group_field: None | str | Unset
        if isinstance(self.group_field, Unset):
            group_field = UNSET
        else:
            group_field = self.group_field

        value_field: None | str | Unset
        if isinstance(self.value_field, Unset):
            value_field = UNSET
        else:
            value_field = self.value_field


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if group_field is not UNSET:
            field_dict["groupField"] = group_field
        if value_field is not UNSET:
            field_dict["valueField"] = value_field

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chart_bucket import OfficeChartBucket # noqa: PLC0415
        d = dict(src_dict)
        def _parse_aggregation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aggregation = _parse_aggregation(d.pop("aggregation", UNSET))


        def _parse_buckets(data: object) -> list[OfficeChartBucket] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                buckets_type_0 = []
                _buckets_type_0 = data
                for buckets_type_0_item_data in (_buckets_type_0):
                    buckets_type_0_item = OfficeChartBucket.from_dict(buckets_type_0_item_data)



                    buckets_type_0.append(buckets_type_0_item)

                return buckets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChartBucket] | None | Unset, data)

        buckets = _parse_buckets(d.pop("buckets", UNSET))


        def _parse_group_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_field = _parse_group_field(d.pop("groupField", UNSET))


        def _parse_value_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_field = _parse_value_field(d.pop("valueField", UNSET))


        office_chart_data_dto = cls(
            aggregation=aggregation,
            buckets=buckets,
            group_field=group_field,
            value_field=value_field,
        )

        return office_chart_data_dto


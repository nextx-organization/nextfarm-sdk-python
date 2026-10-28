from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_dashboard_series_value_dto import OfficeDashboardSeriesValueDto





T = TypeVar("T", bound="OfficeDashboardGroupDto")



@_attrs_define
class OfficeDashboardGroupDto:
    

    count: int | Unset = UNSET
    key: None | str | Unset = UNSET
    series: list[OfficeDashboardSeriesValueDto] | None | Unset = UNSET
    value: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_series_value_dto import OfficeDashboardSeriesValueDto # noqa: PLC0415
        count = self.count

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        series: list[dict[str, Any]] | None | Unset
        if isinstance(self.series, Unset):
            series = UNSET
        elif isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)


        else:
            series = self.series

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if key is not UNSET:
            field_dict["key"] = key
        if series is not UNSET:
            field_dict["series"] = series
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_series_value_dto import OfficeDashboardSeriesValueDto # noqa: PLC0415
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_series(data: object) -> list[OfficeDashboardSeriesValueDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in (_series_type_0):
                    series_type_0_item = OfficeDashboardSeriesValueDto.from_dict(series_type_0_item_data)



                    series_type_0.append(series_type_0_item)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardSeriesValueDto] | None | Unset, data)

        series = _parse_series(d.pop("series", UNSET))


        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        office_dashboard_group_dto = cls(
            count=count,
            key=key,
            series=series,
            value=value,
        )

        return office_dashboard_group_dto


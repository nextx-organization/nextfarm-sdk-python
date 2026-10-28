from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_dashboard_bucket_dto import OfficeDashboardBucketDto
  from ..models.office_dashboard_compare_period_dto import OfficeDashboardComparePeriodDto
  from ..models.office_dashboard_group_dto import OfficeDashboardGroupDto
  from ..models.office_dashboard_table_row_dto import OfficeDashboardTableRowDto





T = TypeVar("T", bound="OfficeDashboardWidgetDataDto")



@_attrs_define
class OfficeDashboardWidgetDataDto:
    

    buckets: list[OfficeDashboardBucketDto] | None | Unset = UNSET
    compare_period: OfficeDashboardComparePeriodDto | Unset = UNSET
    count: int | Unset = UNSET
    delta_percent: float | None | Unset = UNSET
    groups: list[OfficeDashboardGroupDto] | None | Unset = UNSET
    previous_value: float | None | Unset = UNSET
    rows: list[OfficeDashboardTableRowDto] | None | Unset = UNSET
    series_keys: list[str] | None | Unset = UNSET
    target: float | None | Unset = UNSET
    truncated: bool | Unset = UNSET
    type_: None | str | Unset = UNSET
    unavailable: None | str | Unset = UNSET
    value: float | None | Unset = UNSET
    widget_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_bucket_dto import OfficeDashboardBucketDto # noqa: PLC0415
        from ..models.office_dashboard_compare_period_dto import OfficeDashboardComparePeriodDto # noqa: PLC0415
        from ..models.office_dashboard_group_dto import OfficeDashboardGroupDto # noqa: PLC0415
        from ..models.office_dashboard_table_row_dto import OfficeDashboardTableRowDto # noqa: PLC0415
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

        compare_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compare_period, Unset):
            compare_period = self.compare_period.to_dict()

        count = self.count

        delta_percent: float | None | Unset
        if isinstance(self.delta_percent, Unset):
            delta_percent = UNSET
        else:
            delta_percent = self.delta_percent

        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)


        else:
            groups = self.groups

        previous_value: float | None | Unset
        if isinstance(self.previous_value, Unset):
            previous_value = UNSET
        else:
            previous_value = self.previous_value

        rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)


        else:
            rows = self.rows

        series_keys: list[str] | None | Unset
        if isinstance(self.series_keys, Unset):
            series_keys = UNSET
        elif isinstance(self.series_keys, list):
            series_keys = self.series_keys


        else:
            series_keys = self.series_keys

        target: float | None | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        truncated = self.truncated

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        unavailable: None | str | Unset
        if isinstance(self.unavailable, Unset):
            unavailable = UNSET
        else:
            unavailable = self.unavailable

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        widget_id: None | str | Unset
        if isinstance(self.widget_id, Unset):
            widget_id = UNSET
        else:
            widget_id = self.widget_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if compare_period is not UNSET:
            field_dict["comparePeriod"] = compare_period
        if count is not UNSET:
            field_dict["count"] = count
        if delta_percent is not UNSET:
            field_dict["deltaPercent"] = delta_percent
        if groups is not UNSET:
            field_dict["groups"] = groups
        if previous_value is not UNSET:
            field_dict["previousValue"] = previous_value
        if rows is not UNSET:
            field_dict["rows"] = rows
        if series_keys is not UNSET:
            field_dict["seriesKeys"] = series_keys
        if target is not UNSET:
            field_dict["target"] = target
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable
        if value is not UNSET:
            field_dict["value"] = value
        if widget_id is not UNSET:
            field_dict["widgetId"] = widget_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_bucket_dto import OfficeDashboardBucketDto # noqa: PLC0415
        from ..models.office_dashboard_compare_period_dto import OfficeDashboardComparePeriodDto # noqa: PLC0415
        from ..models.office_dashboard_group_dto import OfficeDashboardGroupDto # noqa: PLC0415
        from ..models.office_dashboard_table_row_dto import OfficeDashboardTableRowDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_buckets(data: object) -> list[OfficeDashboardBucketDto] | None | Unset:
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
                    buckets_type_0_item = OfficeDashboardBucketDto.from_dict(buckets_type_0_item_data)



                    buckets_type_0.append(buckets_type_0_item)

                return buckets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardBucketDto] | None | Unset, data)

        buckets = _parse_buckets(d.pop("buckets", UNSET))


        _compare_period = d.pop("comparePeriod", UNSET)
        compare_period: OfficeDashboardComparePeriodDto | Unset
        if isinstance(_compare_period,  Unset):
            compare_period = UNSET
        else:
            compare_period = OfficeDashboardComparePeriodDto.from_dict(_compare_period)




        count = d.pop("count", UNSET)

        def _parse_delta_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        delta_percent = _parse_delta_percent(d.pop("deltaPercent", UNSET))


        def _parse_groups(data: object) -> list[OfficeDashboardGroupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in (_groups_type_0):
                    groups_type_0_item = OfficeDashboardGroupDto.from_dict(groups_type_0_item_data)



                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardGroupDto] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        def _parse_previous_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        previous_value = _parse_previous_value(d.pop("previousValue", UNSET))


        def _parse_rows(data: object) -> list[OfficeDashboardTableRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in (_rows_type_0):
                    rows_type_0_item = OfficeDashboardTableRowDto.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardTableRowDto] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        def _parse_series_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_keys_type_0 = cast(list[str], data)

                return series_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        series_keys = _parse_series_keys(d.pop("seriesKeys", UNSET))


        def _parse_target(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target = _parse_target(d.pop("target", UNSET))


        truncated = d.pop("truncated", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_unavailable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unavailable = _parse_unavailable(d.pop("unavailable", UNSET))


        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        def _parse_widget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        widget_id = _parse_widget_id(d.pop("widgetId", UNSET))


        office_dashboard_widget_data_dto = cls(
            buckets=buckets,
            compare_period=compare_period,
            count=count,
            delta_percent=delta_percent,
            groups=groups,
            previous_value=previous_value,
            rows=rows,
            series_keys=series_keys,
            target=target,
            truncated=truncated,
            type_=type_,
            unavailable=unavailable,
            value=value,
            widget_id=widget_id,
        )

        return office_dashboard_widget_data_dto


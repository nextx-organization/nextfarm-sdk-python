from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_dashboard_widget_format import OfficeDashboardWidgetFormat
  from ..models.office_record_filter import OfficeRecordFilter





T = TypeVar("T", bound="OfficeDashboardWidget")



@_attrs_define
class OfficeDashboardWidget:
    

    aggregation: None | str | Unset = UNSET
    columns: list[str] | None | Unset = UNSET
    compare: None | str | Unset = UNSET
    date_field: None | str | Unset = UNSET
    date_grouping: None | str | Unset = UNSET
    filter_: OfficeRecordFilter | Unset = UNSET
    format_: OfficeDashboardWidgetFormat | Unset = UNSET
    group_field: None | str | Unset = UNSET
    h: int | Unset = UNSET
    id: None | str | Unset = UNSET
    limit: int | None | Unset = UNSET
    orientation: None | str | Unset = UNSET
    series_field: None | str | Unset = UNSET
    sort: None | str | Unset = UNSET
    stacked: bool | None | Unset = UNSET
    table_id: UUID | Unset = UNSET
    target: float | None | Unset = UNSET
    text: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    value_field: None | str | Unset = UNSET
    w: int | Unset = UNSET
    x: int | Unset = UNSET
    y: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_widget_format import OfficeDashboardWidgetFormat # noqa: PLC0415
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        aggregation: None | str | Unset
        if isinstance(self.aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = self.aggregation

        columns: list[str] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = self.columns


        else:
            columns = self.columns

        compare: None | str | Unset
        if isinstance(self.compare, Unset):
            compare = UNSET
        else:
            compare = self.compare

        date_field: None | str | Unset
        if isinstance(self.date_field, Unset):
            date_field = UNSET
        else:
            date_field = self.date_field

        date_grouping: None | str | Unset
        if isinstance(self.date_grouping, Unset):
            date_grouping = UNSET
        else:
            date_grouping = self.date_grouping

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        format_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        group_field: None | str | Unset
        if isinstance(self.group_field, Unset):
            group_field = UNSET
        else:
            group_field = self.group_field

        h = self.h

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        orientation: None | str | Unset
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        series_field: None | str | Unset
        if isinstance(self.series_field, Unset):
            series_field = UNSET
        else:
            series_field = self.series_field

        sort: None | str | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        else:
            sort = self.sort

        stacked: bool | None | Unset
        if isinstance(self.stacked, Unset):
            stacked = UNSET
        else:
            stacked = self.stacked

        table_id: str | Unset = UNSET
        if not isinstance(self.table_id, Unset):
            table_id = str(self.table_id)

        target: float | None | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        value_field: None | str | Unset
        if isinstance(self.value_field, Unset):
            value_field = UNSET
        else:
            value_field = self.value_field

        w = self.w

        x = self.x

        y = self.y


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if columns is not UNSET:
            field_dict["columns"] = columns
        if compare is not UNSET:
            field_dict["compare"] = compare
        if date_field is not UNSET:
            field_dict["dateField"] = date_field
        if date_grouping is not UNSET:
            field_dict["dateGrouping"] = date_grouping
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if format_ is not UNSET:
            field_dict["format"] = format_
        if group_field is not UNSET:
            field_dict["groupField"] = group_field
        if h is not UNSET:
            field_dict["h"] = h
        if id is not UNSET:
            field_dict["id"] = id
        if limit is not UNSET:
            field_dict["limit"] = limit
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if series_field is not UNSET:
            field_dict["seriesField"] = series_field
        if sort is not UNSET:
            field_dict["sort"] = sort
        if stacked is not UNSET:
            field_dict["stacked"] = stacked
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if target is not UNSET:
            field_dict["target"] = target
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value_field is not UNSET:
            field_dict["valueField"] = value_field
        if w is not UNSET:
            field_dict["w"] = w
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_widget_format import OfficeDashboardWidgetFormat # noqa: PLC0415
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        d = dict(src_dict)
        def _parse_aggregation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aggregation = _parse_aggregation(d.pop("aggregation", UNSET))


        def _parse_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = cast(list[str], data)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))


        def _parse_compare(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compare = _parse_compare(d.pop("compare", UNSET))


        def _parse_date_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_field = _parse_date_field(d.pop("dateField", UNSET))


        def _parse_date_grouping(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_grouping = _parse_date_grouping(d.pop("dateGrouping", UNSET))


        _filter_ = d.pop("filter", UNSET)
        filter_: OfficeRecordFilter | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = OfficeRecordFilter.from_dict(_filter_)




        _format_ = d.pop("format", UNSET)
        format_: OfficeDashboardWidgetFormat | Unset
        if isinstance(_format_,  Unset):
            format_ = UNSET
        else:
            format_ = OfficeDashboardWidgetFormat.from_dict(_format_)




        def _parse_group_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_field = _parse_group_field(d.pop("groupField", UNSET))


        h = d.pop("h", UNSET)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))


        def _parse_orientation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))


        def _parse_series_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series_field = _parse_series_field(d.pop("seriesField", UNSET))


        def _parse_sort(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))


        def _parse_stacked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        stacked = _parse_stacked(d.pop("stacked", UNSET))


        _table_id = d.pop("tableId", UNSET)
        table_id: UUID | Unset
        if isinstance(_table_id,  Unset):
            table_id = UNSET
        else:
            table_id = UUID(_table_id)




        def _parse_target(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target = _parse_target(d.pop("target", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_value_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_field = _parse_value_field(d.pop("valueField", UNSET))


        w = d.pop("w", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        office_dashboard_widget = cls(
            aggregation=aggregation,
            columns=columns,
            compare=compare,
            date_field=date_field,
            date_grouping=date_grouping,
            filter_=filter_,
            format_=format_,
            group_field=group_field,
            h=h,
            id=id,
            limit=limit,
            orientation=orientation,
            series_field=series_field,
            sort=sort,
            stacked=stacked,
            table_id=table_id,
            target=target,
            text=text,
            title=title,
            type_=type_,
            value_field=value_field,
            w=w,
            x=x,
            y=y,
        )

        return office_dashboard_widget


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.report_block_result_totals_type_0 import ReportBlockResultTotalsType0
  from ..models.report_kpi_value import ReportKpiValue
  from ..models.report_measure_meta import ReportMeasureMeta
  from ..models.report_report_row import ReportReportRow





T = TypeVar("T", bound="ReportBlockResult")



@_attrs_define
class ReportBlockResult:
    

    chart: None | str | Unset = UNSET
    dataset: None | str | Unset = UNSET
    drill: None | str | Unset = UNSET
    group_by: list[str] | None | Unset = UNSET
    has_sample: bool | Unset = UNSET
    hidden: bool | Unset = UNSET
    id: None | str | Unset = UNSET
    kpis: list[ReportKpiValue] | None | Unset = UNSET
    measures: list[ReportMeasureMeta] | None | Unset = UNSET
    reason_code: None | str | Unset = UNSET
    rows: list[ReportReportRow] | None | Unset = UNSET
    source: None | str | Unset = UNSET
    span: int | Unset = UNSET
    status: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    totals: None | ReportBlockResultTotalsType0 | Unset = UNSET
    truncated: bool | Unset = UNSET
    type_: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_block_result_totals_type_0 import ReportBlockResultTotalsType0 # noqa: PLC0415
        from ..models.report_kpi_value import ReportKpiValue # noqa: PLC0415
        from ..models.report_measure_meta import ReportMeasureMeta # noqa: PLC0415
        from ..models.report_report_row import ReportReportRow # noqa: PLC0415
        chart: None | str | Unset
        if isinstance(self.chart, Unset):
            chart = UNSET
        else:
            chart = self.chart

        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        drill: None | str | Unset
        if isinstance(self.drill, Unset):
            drill = UNSET
        else:
            drill = self.drill

        group_by: list[str] | None | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        elif isinstance(self.group_by, list):
            group_by = self.group_by


        else:
            group_by = self.group_by

        has_sample = self.has_sample

        hidden = self.hidden

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        kpis: list[dict[str, Any]] | None | Unset
        if isinstance(self.kpis, Unset):
            kpis = UNSET
        elif isinstance(self.kpis, list):
            kpis = []
            for kpis_type_0_item_data in self.kpis:
                kpis_type_0_item = kpis_type_0_item_data.to_dict()
                kpis.append(kpis_type_0_item)


        else:
            kpis = self.kpis

        measures: list[dict[str, Any]] | None | Unset
        if isinstance(self.measures, Unset):
            measures = UNSET
        elif isinstance(self.measures, list):
            measures = []
            for measures_type_0_item_data in self.measures:
                measures_type_0_item = measures_type_0_item_data.to_dict()
                measures.append(measures_type_0_item)


        else:
            measures = self.measures

        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

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

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        span = self.span

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        totals: dict[str, Any] | None | Unset
        if isinstance(self.totals, Unset):
            totals = UNSET
        elif isinstance(self.totals, ReportBlockResultTotalsType0):
            totals = self.totals.to_dict()
        else:
            totals = self.totals

        truncated = self.truncated

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if chart is not UNSET:
            field_dict["chart"] = chart
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if drill is not UNSET:
            field_dict["drill"] = drill
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by
        if has_sample is not UNSET:
            field_dict["hasSample"] = has_sample
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if id is not UNSET:
            field_dict["id"] = id
        if kpis is not UNSET:
            field_dict["kpis"] = kpis
        if measures is not UNSET:
            field_dict["measures"] = measures
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if rows is not UNSET:
            field_dict["rows"] = rows
        if source is not UNSET:
            field_dict["source"] = source
        if span is not UNSET:
            field_dict["span"] = span
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if totals is not UNSET:
            field_dict["totals"] = totals
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_block_result_totals_type_0 import ReportBlockResultTotalsType0 # noqa: PLC0415
        from ..models.report_kpi_value import ReportKpiValue # noqa: PLC0415
        from ..models.report_measure_meta import ReportMeasureMeta # noqa: PLC0415
        from ..models.report_report_row import ReportReportRow # noqa: PLC0415
        d = dict(src_dict)
        def _parse_chart(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chart = _parse_chart(d.pop("chart", UNSET))


        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("dataset", UNSET))


        def _parse_drill(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drill = _parse_drill(d.pop("drill", UNSET))


        def _parse_group_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_by_type_0 = cast(list[str], data)

                return group_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_by = _parse_group_by(d.pop("groupBy", UNSET))


        has_sample = d.pop("hasSample", UNSET)

        hidden = d.pop("hidden", UNSET)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_kpis(data: object) -> list[ReportKpiValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kpis_type_0 = []
                _kpis_type_0 = data
                for kpis_type_0_item_data in (_kpis_type_0):
                    kpis_type_0_item = ReportKpiValue.from_dict(kpis_type_0_item_data)



                    kpis_type_0.append(kpis_type_0_item)

                return kpis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportKpiValue] | None | Unset, data)

        kpis = _parse_kpis(d.pop("kpis", UNSET))


        def _parse_measures(data: object) -> list[ReportMeasureMeta] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                measures_type_0 = []
                _measures_type_0 = data
                for measures_type_0_item_data in (_measures_type_0):
                    measures_type_0_item = ReportMeasureMeta.from_dict(measures_type_0_item_data)



                    measures_type_0.append(measures_type_0_item)

                return measures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportMeasureMeta] | None | Unset, data)

        measures = _parse_measures(d.pop("measures", UNSET))


        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reasonCode", UNSET))


        def _parse_rows(data: object) -> list[ReportReportRow] | None | Unset:
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
                    rows_type_0_item = ReportReportRow.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportReportRow] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        span = d.pop("span", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_totals(data: object) -> None | ReportBlockResultTotalsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                totals_type_0 = ReportBlockResultTotalsType0.from_dict(data)



                return totals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportBlockResultTotalsType0 | Unset, data)

        totals = _parse_totals(d.pop("totals", UNSET))


        truncated = d.pop("truncated", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        report_block_result = cls(
            chart=chart,
            dataset=dataset,
            drill=drill,
            group_by=group_by,
            has_sample=has_sample,
            hidden=hidden,
            id=id,
            kpis=kpis,
            measures=measures,
            reason_code=reason_code,
            rows=rows,
            source=source,
            span=span,
            status=status,
            title=title,
            totals=totals,
            truncated=truncated,
            type_=type_,
            updated_at=updated_at,
        )

        return report_block_result


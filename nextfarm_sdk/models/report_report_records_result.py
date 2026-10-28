from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.report_report_records_result_labels_type_0 import ReportReportRecordsResultLabelsType0
  from ..models.report_report_records_result_totals_type_0 import ReportReportRecordsResultTotalsType0
  from ..models.report_report_row import ReportReportRow





T = TypeVar("T", bound="ReportReportRecordsResult")



@_attrs_define
class ReportReportRecordsResult:
    

    dataset: None | str | Unset = UNSET
    labels: None | ReportReportRecordsResultLabelsType0 | Unset = UNSET
    reason_code: None | str | Unset = UNSET
    record_count: int | Unset = UNSET
    rows: list[ReportReportRow] | None | Unset = UNSET
    source: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    totals: None | ReportReportRecordsResultTotalsType0 | Unset = UNSET
    truncated: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_report_records_result_labels_type_0 import ReportReportRecordsResultLabelsType0 # noqa: PLC0415
        from ..models.report_report_records_result_totals_type_0 import ReportReportRecordsResultTotalsType0 # noqa: PLC0415
        from ..models.report_report_row import ReportReportRow # noqa: PLC0415
        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        labels: dict[str, Any] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, ReportReportRecordsResultLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        record_count = self.record_count

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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        totals: dict[str, Any] | None | Unset
        if isinstance(self.totals, Unset):
            totals = UNSET
        elif isinstance(self.totals, ReportReportRecordsResultTotalsType0):
            totals = self.totals.to_dict()
        else:
            totals = self.totals

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if labels is not UNSET:
            field_dict["labels"] = labels
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if record_count is not UNSET:
            field_dict["recordCount"] = record_count
        if rows is not UNSET:
            field_dict["rows"] = rows
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if totals is not UNSET:
            field_dict["totals"] = totals
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_report_records_result_labels_type_0 import ReportReportRecordsResultLabelsType0 # noqa: PLC0415
        from ..models.report_report_records_result_totals_type_0 import ReportReportRecordsResultTotalsType0 # noqa: PLC0415
        from ..models.report_report_row import ReportReportRow # noqa: PLC0415
        d = dict(src_dict)
        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("dataset", UNSET))


        def _parse_labels(data: object) -> None | ReportReportRecordsResultLabelsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = ReportReportRecordsResultLabelsType0.from_dict(data)



                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportReportRecordsResultLabelsType0 | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))


        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reasonCode", UNSET))


        record_count = d.pop("recordCount", UNSET)

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


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_totals(data: object) -> None | ReportReportRecordsResultTotalsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                totals_type_0 = ReportReportRecordsResultTotalsType0.from_dict(data)



                return totals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportReportRecordsResultTotalsType0 | Unset, data)

        totals = _parse_totals(d.pop("totals", UNSET))


        truncated = d.pop("truncated", UNSET)

        report_report_records_result = cls(
            dataset=dataset,
            labels=labels,
            reason_code=reason_code,
            record_count=record_count,
            rows=rows,
            source=source,
            status=status,
            totals=totals,
            truncated=truncated,
        )

        return report_report_records_result


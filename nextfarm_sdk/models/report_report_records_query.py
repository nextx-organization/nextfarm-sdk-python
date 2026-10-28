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
  from ..models.report_report_records_query_filters_type_0 import ReportReportRecordsQueryFiltersType0





T = TypeVar("T", bound="ReportReportRecordsQuery")



@_attrs_define
class ReportReportRecordsQuery:
    

    dataset: None | str | Unset = UNSET
    filters: None | ReportReportRecordsQueryFiltersType0 | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    include_sample: bool | Unset = UNSET
    limit: int | Unset = UNSET
    source: None | str | Unset = UNSET
    to: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_report_records_query_filters_type_0 import ReportReportRecordsQueryFiltersType0 # noqa: PLC0415
        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ReportReportRecordsQueryFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        include_sample = self.include_sample

        limit = self.limit

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if filters is not UNSET:
            field_dict["filters"] = filters
        if from_ is not UNSET:
            field_dict["from"] = from_
        if include_sample is not UNSET:
            field_dict["includeSample"] = include_sample
        if limit is not UNSET:
            field_dict["limit"] = limit
        if source is not UNSET:
            field_dict["source"] = source
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_report_records_query_filters_type_0 import ReportReportRecordsQueryFiltersType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("dataset", UNSET))


        def _parse_filters(data: object) -> None | ReportReportRecordsQueryFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ReportReportRecordsQueryFiltersType0.from_dict(data)



                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportReportRecordsQueryFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))


        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        include_sample = d.pop("includeSample", UNSET)

        limit = d.pop("limit", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        report_report_records_query = cls(
            dataset=dataset,
            filters=filters,
            from_=from_,
            include_sample=include_sample,
            limit=limit,
            source=source,
            to=to,
        )

        return report_report_records_query


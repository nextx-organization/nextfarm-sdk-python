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
  from ..models.report_run_report_query_filters_type_0 import ReportRunReportQueryFiltersType0





T = TypeVar("T", bound="ReportRunReportQuery")



@_attrs_define
class ReportRunReportQuery:
    

    code: None | str | Unset = UNSET
    compare: None | str | Unset = UNSET
    filters: None | ReportRunReportQueryFiltersType0 | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    grain: None | str | Unset = UNSET
    include_sample: bool | Unset = UNSET
    to: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_run_report_query_filters_type_0 import ReportRunReportQueryFiltersType0 # noqa: PLC0415
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        compare: None | str | Unset
        if isinstance(self.compare, Unset):
            compare = UNSET
        else:
            compare = self.compare

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ReportRunReportQueryFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        grain: None | str | Unset
        if isinstance(self.grain, Unset):
            grain = UNSET
        else:
            grain = self.grain

        include_sample = self.include_sample

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if compare is not UNSET:
            field_dict["compare"] = compare
        if filters is not UNSET:
            field_dict["filters"] = filters
        if from_ is not UNSET:
            field_dict["from"] = from_
        if grain is not UNSET:
            field_dict["grain"] = grain
        if include_sample is not UNSET:
            field_dict["includeSample"] = include_sample
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_run_report_query_filters_type_0 import ReportRunReportQueryFiltersType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_compare(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compare = _parse_compare(d.pop("compare", UNSET))


        def _parse_filters(data: object) -> None | ReportRunReportQueryFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ReportRunReportQueryFiltersType0.from_dict(data)



                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportRunReportQueryFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))


        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        def _parse_grain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grain = _parse_grain(d.pop("grain", UNSET))


        include_sample = d.pop("includeSample", UNSET)

        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        report_run_report_query = cls(
            code=code,
            compare=compare,
            filters=filters,
            from_=from_,
            grain=grain,
            include_sample=include_sample,
            to=to,
        )

        return report_run_report_query


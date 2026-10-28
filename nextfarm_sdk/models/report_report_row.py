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
  from ..models.report_report_row_dims_type_0 import ReportReportRowDimsType0
  from ..models.report_report_row_values_type_0 import ReportReportRowValuesType0





T = TypeVar("T", bound="ReportReportRow")



@_attrs_define
class ReportReportRow:
    

    date: datetime.date | None | Unset = UNSET
    dims: None | ReportReportRowDimsType0 | Unset = UNSET
    id: None | str | Unset = UNSET
    values: None | ReportReportRowValuesType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_report_row_dims_type_0 import ReportReportRowDimsType0 # noqa: PLC0415
        from ..models.report_report_row_values_type_0 import ReportReportRowValuesType0 # noqa: PLC0415
        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        dims: dict[str, Any] | None | Unset
        if isinstance(self.dims, Unset):
            dims = UNSET
        elif isinstance(self.dims, ReportReportRowDimsType0):
            dims = self.dims.to_dict()
        else:
            dims = self.dims

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        values: dict[str, Any] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, ReportReportRowValuesType0):
            values = self.values.to_dict()
        else:
            values = self.values


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if dims is not UNSET:
            field_dict["dims"] = dims
        if id is not UNSET:
            field_dict["id"] = id
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_report_row_dims_type_0 import ReportReportRowDimsType0 # noqa: PLC0415
        from ..models.report_report_row_values_type_0 import ReportReportRowValuesType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.date.fromisoformat(data)



                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        def _parse_dims(data: object) -> None | ReportReportRowDimsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dims_type_0 = ReportReportRowDimsType0.from_dict(data)



                return dims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportReportRowDimsType0 | Unset, data)

        dims = _parse_dims(d.pop("dims", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_values(data: object) -> None | ReportReportRowValuesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                values_type_0 = ReportReportRowValuesType0.from_dict(data)



                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportReportRowValuesType0 | Unset, data)

        values = _parse_values(d.pop("values", UNSET))


        report_report_row = cls(
            date=date,
            dims=dims,
            id=id,
            values=values,
        )

        return report_report_row


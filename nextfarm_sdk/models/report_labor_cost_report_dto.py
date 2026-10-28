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
  from ..models.report_labor_cost_freshness import ReportLaborCostFreshness
  from ..models.report_labor_cost_row_dto import ReportLaborCostRowDto
  from ..models.report_labor_cost_totals_dto import ReportLaborCostTotalsDto





T = TypeVar("T", bound="ReportLaborCostReportDto")



@_attrs_define
class ReportLaborCostReportDto:
    

    freshness: ReportLaborCostFreshness | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    rows: list[ReportLaborCostRowDto] | None | Unset = UNSET
    to: datetime.date | Unset = UNSET
    totals: ReportLaborCostTotalsDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_labor_cost_freshness import ReportLaborCostFreshness # noqa: PLC0415
        from ..models.report_labor_cost_row_dto import ReportLaborCostRowDto # noqa: PLC0415
        from ..models.report_labor_cost_totals_dto import ReportLaborCostTotalsDto # noqa: PLC0415
        freshness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.freshness, Unset):
            freshness = self.freshness.to_dict()

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

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

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if freshness is not UNSET:
            field_dict["freshness"] = freshness
        if from_ is not UNSET:
            field_dict["from"] = from_
        if rows is not UNSET:
            field_dict["rows"] = rows
        if to is not UNSET:
            field_dict["to"] = to
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_labor_cost_freshness import ReportLaborCostFreshness # noqa: PLC0415
        from ..models.report_labor_cost_row_dto import ReportLaborCostRowDto # noqa: PLC0415
        from ..models.report_labor_cost_totals_dto import ReportLaborCostTotalsDto # noqa: PLC0415
        d = dict(src_dict)
        _freshness = d.pop("freshness", UNSET)
        freshness: ReportLaborCostFreshness | Unset
        if isinstance(_freshness,  Unset):
            freshness = UNSET
        else:
            freshness = ReportLaborCostFreshness.from_dict(_freshness)




        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        def _parse_rows(data: object) -> list[ReportLaborCostRowDto] | None | Unset:
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
                    rows_type_0_item = ReportLaborCostRowDto.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportLaborCostRowDto] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        _totals = d.pop("totals", UNSET)
        totals: ReportLaborCostTotalsDto | Unset
        if isinstance(_totals,  Unset):
            totals = UNSET
        else:
            totals = ReportLaborCostTotalsDto.from_dict(_totals)




        report_labor_cost_report_dto = cls(
            freshness=freshness,
            from_=from_,
            rows=rows,
            to=to,
            totals=totals,
        )

        return report_labor_cost_report_dto


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
  from ..models.report_block_result import ReportBlockResult
  from ..models.report_report_period import ReportReportPeriod
  from ..models.report_report_result_labels_type_0 import ReportReportResultLabelsType0





T = TypeVar("T", bound="ReportReportResult")



@_attrs_define
class ReportReportResult:
    

    as_of: datetime.datetime | Unset = UNSET
    blocks: list[ReportBlockResult] | None | Unset = UNSET
    code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    has_sample: bool | Unset = UNSET
    hidden: list[str] | None | Unset = UNSET
    labels: None | ReportReportResultLabelsType0 | Unset = UNSET
    period: ReportReportPeriod | Unset = UNSET
    summary_focus: list[str] | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_block_result import ReportBlockResult # noqa: PLC0415
        from ..models.report_report_period import ReportReportPeriod # noqa: PLC0415
        from ..models.report_report_result_labels_type_0 import ReportReportResultLabelsType0 # noqa: PLC0415
        as_of: str | Unset = UNSET
        if not isinstance(self.as_of, Unset):
            as_of = self.as_of.isoformat()

        blocks: list[dict[str, Any]] | None | Unset
        if isinstance(self.blocks, Unset):
            blocks = UNSET
        elif isinstance(self.blocks, list):
            blocks = []
            for blocks_type_0_item_data in self.blocks:
                blocks_type_0_item = blocks_type_0_item_data.to_dict()
                blocks.append(blocks_type_0_item)


        else:
            blocks = self.blocks

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        has_sample = self.has_sample

        hidden: list[str] | None | Unset
        if isinstance(self.hidden, Unset):
            hidden = UNSET
        elif isinstance(self.hidden, list):
            hidden = self.hidden


        else:
            hidden = self.hidden

        labels: dict[str, Any] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, ReportReportResultLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        summary_focus: list[str] | None | Unset
        if isinstance(self.summary_focus, Unset):
            summary_focus = UNSET
        elif isinstance(self.summary_focus, list):
            summary_focus = self.summary_focus


        else:
            summary_focus = self.summary_focus

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if group is not UNSET:
            field_dict["group"] = group
        if has_sample is not UNSET:
            field_dict["hasSample"] = has_sample
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if labels is not UNSET:
            field_dict["labels"] = labels
        if period is not UNSET:
            field_dict["period"] = period
        if summary_focus is not UNSET:
            field_dict["summaryFocus"] = summary_focus
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_block_result import ReportBlockResult # noqa: PLC0415
        from ..models.report_report_period import ReportReportPeriod # noqa: PLC0415
        from ..models.report_report_result_labels_type_0 import ReportReportResultLabelsType0 # noqa: PLC0415
        d = dict(src_dict)
        _as_of = d.pop("asOf", UNSET)
        as_of: datetime.datetime | Unset
        if isinstance(_as_of,  Unset):
            as_of = UNSET
        else:
            as_of = datetime.datetime.fromisoformat(_as_of)




        def _parse_blocks(data: object) -> list[ReportBlockResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocks_type_0 = []
                _blocks_type_0 = data
                for blocks_type_0_item_data in (_blocks_type_0):
                    blocks_type_0_item = ReportBlockResult.from_dict(blocks_type_0_item_data)



                    blocks_type_0.append(blocks_type_0_item)

                return blocks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportBlockResult] | None | Unset, data)

        blocks = _parse_blocks(d.pop("blocks", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        has_sample = d.pop("hasSample", UNSET)

        def _parse_hidden(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hidden_type_0 = cast(list[str], data)

                return hidden_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        hidden = _parse_hidden(d.pop("hidden", UNSET))


        def _parse_labels(data: object) -> None | ReportReportResultLabelsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = ReportReportResultLabelsType0.from_dict(data)



                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportReportResultLabelsType0 | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))


        _period = d.pop("period", UNSET)
        period: ReportReportPeriod | Unset
        if isinstance(_period,  Unset):
            period = UNSET
        else:
            period = ReportReportPeriod.from_dict(_period)




        def _parse_summary_focus(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                summary_focus_type_0 = cast(list[str], data)

                return summary_focus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        summary_focus = _parse_summary_focus(d.pop("summaryFocus", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        report_report_result = cls(
            as_of=as_of,
            blocks=blocks,
            code=code,
            description=description,
            group=group,
            has_sample=has_sample,
            hidden=hidden,
            labels=labels,
            period=period,
            summary_focus=summary_focus,
            title=title,
        )

        return report_report_result


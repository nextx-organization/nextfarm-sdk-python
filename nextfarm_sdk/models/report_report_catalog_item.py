from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReportReportCatalogItem")



@_attrs_define
class ReportReportCatalogItem:
    

    accessible: bool | Unset = UNSET
    blocks: int | Unset = UNSET
    chart: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    visible_blocks: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        accessible = self.accessible

        blocks = self.blocks

        chart: None | str | Unset
        if isinstance(self.chart, Unset):
            chart = UNSET
        else:
            chart = self.chart

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

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        visible_blocks = self.visible_blocks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if accessible is not UNSET:
            field_dict["accessible"] = accessible
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if chart is not UNSET:
            field_dict["chart"] = chart
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if group is not UNSET:
            field_dict["group"] = group
        if title is not UNSET:
            field_dict["title"] = title
        if visible_blocks is not UNSET:
            field_dict["visibleBlocks"] = visible_blocks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accessible = d.pop("accessible", UNSET)

        blocks = d.pop("blocks", UNSET)

        def _parse_chart(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chart = _parse_chart(d.pop("chart", UNSET))


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


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        visible_blocks = d.pop("visibleBlocks", UNSET)

        report_report_catalog_item = cls(
            accessible=accessible,
            blocks=blocks,
            chart=chart,
            code=code,
            description=description,
            group=group,
            title=title,
            visible_blocks=visible_blocks,
        )

        return report_report_catalog_item


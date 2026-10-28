from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeCreateExportRequest")



@_attrs_define
class OfficeCreateExportRequest:
    

    filters: Any | Unset = UNSET
    format_: None | str | Unset = UNSET
    report_type: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        filters = self.filters

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        report_type: None | str | Unset
        if isinstance(self.report_type, Unset):
            report_type = UNSET
        else:
            report_type = self.report_type

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if filters is not UNSET:
            field_dict["filters"] = filters
        if format_ is not UNSET:
            field_dict["format"] = format_
        if report_type is not UNSET:
            field_dict["reportType"] = report_type
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filters = d.pop("filters", UNSET)

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))


        def _parse_report_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_type = _parse_report_type(d.pop("reportType", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        office_create_export_request = cls(
            filters=filters,
            format_=format_,
            report_type=report_type,
            type_=type_,
        )

        return office_create_export_request


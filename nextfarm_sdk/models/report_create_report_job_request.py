from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReportCreateReportJobRequest")



@_attrs_define
class ReportCreateReportJobRequest:
    

    format_: None | str | Unset = UNSET
    parameters_json: None | str | Unset = UNSET
    report_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        parameters_json: None | str | Unset
        if isinstance(self.parameters_json, Unset):
            parameters_json = UNSET
        else:
            parameters_json = self.parameters_json

        report_type: None | str | Unset
        if isinstance(self.report_type, Unset):
            report_type = UNSET
        else:
            report_type = self.report_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if format_ is not UNSET:
            field_dict["format"] = format_
        if parameters_json is not UNSET:
            field_dict["parametersJson"] = parameters_json
        if report_type is not UNSET:
            field_dict["reportType"] = report_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))


        def _parse_parameters_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parameters_json = _parse_parameters_json(d.pop("parametersJson", UNSET))


        def _parse_report_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_type = _parse_report_type(d.pop("reportType", UNSET))


        report_create_report_job_request = cls(
            format_=format_,
            parameters_json=parameters_json,
            report_type=report_type,
        )

        return report_create_report_job_request


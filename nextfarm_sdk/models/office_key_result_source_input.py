from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_metric_scope_input import OfficeMetricScopeInput





T = TypeVar("T", bound="OfficeKeyResultSourceInput")



@_attrs_define
class OfficeKeyResultSourceInput:
    

    metric_code: None | str | Unset = UNSET
    metric_scope: OfficeMetricScopeInput | Unset = UNSET
    source: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_metric_scope_input import OfficeMetricScopeInput # noqa: PLC0415
        metric_code: None | str | Unset
        if isinstance(self.metric_code, Unset):
            metric_code = UNSET
        else:
            metric_code = self.metric_code

        metric_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metric_scope, Unset):
            metric_scope = self.metric_scope.to_dict()

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if metric_code is not UNSET:
            field_dict["metricCode"] = metric_code
        if metric_scope is not UNSET:
            field_dict["metricScope"] = metric_scope
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_metric_scope_input import OfficeMetricScopeInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_metric_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_code = _parse_metric_code(d.pop("metricCode", UNSET))


        _metric_scope = d.pop("metricScope", UNSET)
        metric_scope: OfficeMetricScopeInput | Unset
        if isinstance(_metric_scope,  Unset):
            metric_scope = UNSET
        else:
            metric_scope = OfficeMetricScopeInput.from_dict(_metric_scope)




        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        office_key_result_source_input = cls(
            metric_code=metric_code,
            metric_scope=metric_scope,
            source=source,
        )

        return office_key_result_source_input


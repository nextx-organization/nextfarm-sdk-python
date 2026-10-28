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
  from ..models.office_metric_scope_input import OfficeMetricScopeInput





T = TypeVar("T", bound="OfficePreviewMetricRequest")



@_attrs_define
class OfficePreviewMetricRequest:
    

    from_: datetime.date | Unset = UNSET
    metric_code: None | str | Unset = UNSET
    scope: OfficeMetricScopeInput | Unset = UNSET
    to: datetime.date | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_metric_scope_input import OfficeMetricScopeInput # noqa: PLC0415
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        metric_code: None | str | Unset
        if isinstance(self.metric_code, Unset):
            metric_code = UNSET
        else:
            metric_code = self.metric_code

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if metric_code is not UNSET:
            field_dict["metricCode"] = metric_code
        if scope is not UNSET:
            field_dict["scope"] = scope
        if to is not UNSET:
            field_dict["to"] = to
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_metric_scope_input import OfficeMetricScopeInput # noqa: PLC0415
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        def _parse_metric_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_code = _parse_metric_code(d.pop("metricCode", UNSET))


        _scope = d.pop("scope", UNSET)
        scope: OfficeMetricScopeInput | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = OfficeMetricScopeInput.from_dict(_scope)




        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        office_preview_metric_request = cls(
            from_=from_,
            metric_code=metric_code,
            scope=scope,
            to=to,
            unit=unit,
        )

        return office_preview_metric_request


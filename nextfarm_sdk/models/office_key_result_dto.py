from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_metric_scope_input import OfficeMetricScopeInput





T = TypeVar("T", bound="OfficeKeyResultDto")



@_attrs_define
class OfficeKeyResultDto:
    

    current_value: float | Unset = UNSET
    has_value: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    is_stale: bool | Unset = UNSET
    last_check_in_at: datetime.datetime | None | Unset = UNSET
    last_source_at: datetime.datetime | None | Unset = UNSET
    metric_code: None | str | Unset = UNSET
    metric_curve: None | str | Unset = UNSET
    metric_scope: OfficeMetricScopeInput | Unset = UNSET
    metric_state: None | str | Unset = UNSET
    metric_state_since: datetime.datetime | None | Unset = UNSET
    name: None | str | Unset = UNSET
    objective_id: UUID | Unset = UNSET
    progress_percent: int | Unset = UNSET
    sort_order: int | Unset = UNSET
    source: None | str | Unset = UNSET
    start_value: float | Unset = UNSET
    target_value: float | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_metric_scope_input import OfficeMetricScopeInput # noqa: PLC0415
        current_value = self.current_value

        has_value = self.has_value

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_stale = self.is_stale

        last_check_in_at: None | str | Unset
        if isinstance(self.last_check_in_at, Unset):
            last_check_in_at = UNSET
        elif isinstance(self.last_check_in_at, datetime.datetime):
            last_check_in_at = self.last_check_in_at.isoformat()
        else:
            last_check_in_at = self.last_check_in_at

        last_source_at: None | str | Unset
        if isinstance(self.last_source_at, Unset):
            last_source_at = UNSET
        elif isinstance(self.last_source_at, datetime.datetime):
            last_source_at = self.last_source_at.isoformat()
        else:
            last_source_at = self.last_source_at

        metric_code: None | str | Unset
        if isinstance(self.metric_code, Unset):
            metric_code = UNSET
        else:
            metric_code = self.metric_code

        metric_curve: None | str | Unset
        if isinstance(self.metric_curve, Unset):
            metric_curve = UNSET
        else:
            metric_curve = self.metric_curve

        metric_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metric_scope, Unset):
            metric_scope = self.metric_scope.to_dict()

        metric_state: None | str | Unset
        if isinstance(self.metric_state, Unset):
            metric_state = UNSET
        else:
            metric_state = self.metric_state

        metric_state_since: None | str | Unset
        if isinstance(self.metric_state_since, Unset):
            metric_state_since = UNSET
        elif isinstance(self.metric_state_since, datetime.datetime):
            metric_state_since = self.metric_state_since.isoformat()
        else:
            metric_state_since = self.metric_state_since

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        objective_id: str | Unset = UNSET
        if not isinstance(self.objective_id, Unset):
            objective_id = str(self.objective_id)

        progress_percent = self.progress_percent

        sort_order = self.sort_order

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        start_value = self.start_value

        target_value = self.target_value

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if has_value is not UNSET:
            field_dict["hasValue"] = has_value
        if id is not UNSET:
            field_dict["id"] = id
        if is_stale is not UNSET:
            field_dict["isStale"] = is_stale
        if last_check_in_at is not UNSET:
            field_dict["lastCheckInAt"] = last_check_in_at
        if last_source_at is not UNSET:
            field_dict["lastSourceAt"] = last_source_at
        if metric_code is not UNSET:
            field_dict["metricCode"] = metric_code
        if metric_curve is not UNSET:
            field_dict["metricCurve"] = metric_curve
        if metric_scope is not UNSET:
            field_dict["metricScope"] = metric_scope
        if metric_state is not UNSET:
            field_dict["metricState"] = metric_state
        if metric_state_since is not UNSET:
            field_dict["metricStateSince"] = metric_state_since
        if name is not UNSET:
            field_dict["name"] = name
        if objective_id is not UNSET:
            field_dict["objectiveId"] = objective_id
        if progress_percent is not UNSET:
            field_dict["progressPercent"] = progress_percent
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if source is not UNSET:
            field_dict["source"] = source
        if start_value is not UNSET:
            field_dict["startValue"] = start_value
        if target_value is not UNSET:
            field_dict["targetValue"] = target_value
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_metric_scope_input import OfficeMetricScopeInput # noqa: PLC0415
        d = dict(src_dict)
        current_value = d.pop("currentValue", UNSET)

        has_value = d.pop("hasValue", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_stale = d.pop("isStale", UNSET)

        def _parse_last_check_in_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_check_in_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_check_in_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_check_in_at = _parse_last_check_in_at(d.pop("lastCheckInAt", UNSET))


        def _parse_last_source_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_source_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_source_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_source_at = _parse_last_source_at(d.pop("lastSourceAt", UNSET))


        def _parse_metric_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_code = _parse_metric_code(d.pop("metricCode", UNSET))


        def _parse_metric_curve(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_curve = _parse_metric_curve(d.pop("metricCurve", UNSET))


        _metric_scope = d.pop("metricScope", UNSET)
        metric_scope: OfficeMetricScopeInput | Unset
        if isinstance(_metric_scope,  Unset):
            metric_scope = UNSET
        else:
            metric_scope = OfficeMetricScopeInput.from_dict(_metric_scope)




        def _parse_metric_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_state = _parse_metric_state(d.pop("metricState", UNSET))


        def _parse_metric_state_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metric_state_since_type_0 = datetime.datetime.fromisoformat(data)



                return metric_state_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        metric_state_since = _parse_metric_state_since(d.pop("metricStateSince", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _objective_id = d.pop("objectiveId", UNSET)
        objective_id: UUID | Unset
        if isinstance(_objective_id,  Unset):
            objective_id = UNSET
        else:
            objective_id = UUID(_objective_id)




        progress_percent = d.pop("progressPercent", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        start_value = d.pop("startValue", UNSET)

        target_value = d.pop("targetValue", UNSET)

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        office_key_result_dto = cls(
            current_value=current_value,
            has_value=has_value,
            id=id,
            is_stale=is_stale,
            last_check_in_at=last_check_in_at,
            last_source_at=last_source_at,
            metric_code=metric_code,
            metric_curve=metric_curve,
            metric_scope=metric_scope,
            metric_state=metric_state,
            metric_state_since=metric_state_since,
            name=name,
            objective_id=objective_id,
            progress_percent=progress_percent,
            sort_order=sort_order,
            source=source,
            start_value=start_value,
            target_value=target_value,
            unit=unit,
        )

        return office_key_result_dto


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
  from ..models.office_quota_status_dto import OfficeQuotaStatusDto





T = TypeVar("T", bound="OfficePlanUsageDto")



@_attrs_define
class OfficePlanUsageDto:
    

    is_read_only: bool | Unset = UNSET
    plan_code: None | str | Unset = UNSET
    quotas: list[OfficeQuotaStatusDto] | None | Unset = UNSET
    trial_ends_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_quota_status_dto import OfficeQuotaStatusDto # noqa: PLC0415
        is_read_only = self.is_read_only

        plan_code: None | str | Unset
        if isinstance(self.plan_code, Unset):
            plan_code = UNSET
        else:
            plan_code = self.plan_code

        quotas: list[dict[str, Any]] | None | Unset
        if isinstance(self.quotas, Unset):
            quotas = UNSET
        elif isinstance(self.quotas, list):
            quotas = []
            for quotas_type_0_item_data in self.quotas:
                quotas_type_0_item = quotas_type_0_item_data.to_dict()
                quotas.append(quotas_type_0_item)


        else:
            quotas = self.quotas

        trial_ends_at: None | str | Unset
        if isinstance(self.trial_ends_at, Unset):
            trial_ends_at = UNSET
        elif isinstance(self.trial_ends_at, datetime.datetime):
            trial_ends_at = self.trial_ends_at.isoformat()
        else:
            trial_ends_at = self.trial_ends_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if plan_code is not UNSET:
            field_dict["planCode"] = plan_code
        if quotas is not UNSET:
            field_dict["quotas"] = quotas
        if trial_ends_at is not UNSET:
            field_dict["trialEndsAt"] = trial_ends_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_quota_status_dto import OfficeQuotaStatusDto # noqa: PLC0415
        d = dict(src_dict)
        is_read_only = d.pop("isReadOnly", UNSET)

        def _parse_plan_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_code = _parse_plan_code(d.pop("planCode", UNSET))


        def _parse_quotas(data: object) -> list[OfficeQuotaStatusDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                quotas_type_0 = []
                _quotas_type_0 = data
                for quotas_type_0_item_data in (_quotas_type_0):
                    quotas_type_0_item = OfficeQuotaStatusDto.from_dict(quotas_type_0_item_data)



                    quotas_type_0.append(quotas_type_0_item)

                return quotas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeQuotaStatusDto] | None | Unset, data)

        quotas = _parse_quotas(d.pop("quotas", UNSET))


        def _parse_trial_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trial_ends_at_type_0 = datetime.datetime.fromisoformat(data)



                return trial_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        trial_ends_at = _parse_trial_ends_at(d.pop("trialEndsAt", UNSET))


        office_plan_usage_dto = cls(
            is_read_only=is_read_only,
            plan_code=plan_code,
            quotas=quotas,
            trial_ends_at=trial_ends_at,
        )

        return office_plan_usage_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeWorkspaceSettingDto")



@_attrs_define
class OfficeWorkspaceSettingDto:
    

    company_name: None | str | Unset = UNSET
    ip_restriction_enabled: bool | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    plan_code: None | str | Unset = UNSET
    tax_code: None | str | Unset = UNSET
    time_zone_id: None | str | Unset = UNSET
    trial_ends_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        ip_restriction_enabled = self.ip_restriction_enabled

        is_read_only = self.is_read_only

        plan_code: None | str | Unset
        if isinstance(self.plan_code, Unset):
            plan_code = UNSET
        else:
            plan_code = self.plan_code

        tax_code: None | str | Unset
        if isinstance(self.tax_code, Unset):
            tax_code = UNSET
        else:
            tax_code = self.tax_code

        time_zone_id: None | str | Unset
        if isinstance(self.time_zone_id, Unset):
            time_zone_id = UNSET
        else:
            time_zone_id = self.time_zone_id

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
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if ip_restriction_enabled is not UNSET:
            field_dict["ipRestrictionEnabled"] = ip_restriction_enabled
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if plan_code is not UNSET:
            field_dict["planCode"] = plan_code
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code
        if time_zone_id is not UNSET:
            field_dict["timeZoneId"] = time_zone_id
        if trial_ends_at is not UNSET:
            field_dict["trialEndsAt"] = trial_ends_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))


        ip_restriction_enabled = d.pop("ipRestrictionEnabled", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        def _parse_plan_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_code = _parse_plan_code(d.pop("planCode", UNSET))


        def _parse_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_code = _parse_tax_code(d.pop("taxCode", UNSET))


        def _parse_time_zone_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone_id = _parse_time_zone_id(d.pop("timeZoneId", UNSET))


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


        office_workspace_setting_dto = cls(
            company_name=company_name,
            ip_restriction_enabled=ip_restriction_enabled,
            is_read_only=is_read_only,
            plan_code=plan_code,
            tax_code=tax_code,
            time_zone_id=time_zone_id,
            trial_ends_at=trial_ends_at,
        )

        return office_workspace_setting_dto


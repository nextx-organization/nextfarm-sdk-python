from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeAssetValueSummaryDto")



@_attrs_define
class OfficeAssetValueSummaryDto:
    

    as_of: datetime.date | Unset = UNSET
    asset_count: int | Unset = UNSET
    in_use_count: int | Unset = UNSET
    total_accumulated_depreciation: float | None | Unset = UNSET
    total_original_cost: float | None | Unset = UNSET
    total_residual_value: float | None | Unset = UNSET
    warranty_expiring_soon_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        as_of: str | Unset = UNSET
        if not isinstance(self.as_of, Unset):
            as_of = self.as_of.isoformat()

        asset_count = self.asset_count

        in_use_count = self.in_use_count

        total_accumulated_depreciation: float | None | Unset
        if isinstance(self.total_accumulated_depreciation, Unset):
            total_accumulated_depreciation = UNSET
        else:
            total_accumulated_depreciation = self.total_accumulated_depreciation

        total_original_cost: float | None | Unset
        if isinstance(self.total_original_cost, Unset):
            total_original_cost = UNSET
        else:
            total_original_cost = self.total_original_cost

        total_residual_value: float | None | Unset
        if isinstance(self.total_residual_value, Unset):
            total_residual_value = UNSET
        else:
            total_residual_value = self.total_residual_value

        warranty_expiring_soon_count = self.warranty_expiring_soon_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if asset_count is not UNSET:
            field_dict["assetCount"] = asset_count
        if in_use_count is not UNSET:
            field_dict["inUseCount"] = in_use_count
        if total_accumulated_depreciation is not UNSET:
            field_dict["totalAccumulatedDepreciation"] = total_accumulated_depreciation
        if total_original_cost is not UNSET:
            field_dict["totalOriginalCost"] = total_original_cost
        if total_residual_value is not UNSET:
            field_dict["totalResidualValue"] = total_residual_value
        if warranty_expiring_soon_count is not UNSET:
            field_dict["warrantyExpiringSoonCount"] = warranty_expiring_soon_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _as_of = d.pop("asOf", UNSET)
        as_of: datetime.date | Unset
        if isinstance(_as_of,  Unset):
            as_of = UNSET
        else:
            as_of = datetime.date.fromisoformat(_as_of)




        asset_count = d.pop("assetCount", UNSET)

        in_use_count = d.pop("inUseCount", UNSET)

        def _parse_total_accumulated_depreciation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_accumulated_depreciation = _parse_total_accumulated_depreciation(d.pop("totalAccumulatedDepreciation", UNSET))


        def _parse_total_original_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_original_cost = _parse_total_original_cost(d.pop("totalOriginalCost", UNSET))


        def _parse_total_residual_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_residual_value = _parse_total_residual_value(d.pop("totalResidualValue", UNSET))


        warranty_expiring_soon_count = d.pop("warrantyExpiringSoonCount", UNSET)

        office_asset_value_summary_dto = cls(
            as_of=as_of,
            asset_count=asset_count,
            in_use_count=in_use_count,
            total_accumulated_depreciation=total_accumulated_depreciation,
            total_original_cost=total_original_cost,
            total_residual_value=total_residual_value,
            warranty_expiring_soon_count=warranty_expiring_soon_count,
        )

        return office_asset_value_summary_dto


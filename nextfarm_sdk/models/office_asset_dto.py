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






T = TypeVar("T", bound="OfficeAssetDto")



@_attrs_define
class OfficeAssetDto:
    

    accumulated_depreciation: float | None | Unset = UNSET
    as_of: datetime.date | Unset = UNSET
    code: None | str | Unset = UNSET
    condition: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    depreciated_months: int | Unset = UNSET
    depreciation_months: int | Unset = UNSET
    depreciation_percent: int | Unset = UNSET
    depreciation_start_date: datetime.date | Unset = UNSET
    holder_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    is_warranty_expiring_soon: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    original_cost: float | None | Unset = UNSET
    purchased_date: datetime.date | Unset = UNSET
    residual_value: float | None | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    warranty_end: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        accumulated_depreciation: float | None | Unset
        if isinstance(self.accumulated_depreciation, Unset):
            accumulated_depreciation = UNSET
        else:
            accumulated_depreciation = self.accumulated_depreciation

        as_of: str | Unset = UNSET
        if not isinstance(self.as_of, Unset):
            as_of = self.as_of.isoformat()

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        condition: None | str | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        depreciated_months = self.depreciated_months

        depreciation_months = self.depreciation_months

        depreciation_percent = self.depreciation_percent

        depreciation_start_date: str | Unset = UNSET
        if not isinstance(self.depreciation_start_date, Unset):
            depreciation_start_date = self.depreciation_start_date.isoformat()

        holder_id: None | str | Unset
        if isinstance(self.holder_id, Unset):
            holder_id = UNSET
        elif isinstance(self.holder_id, UUID):
            holder_id = str(self.holder_id)
        else:
            holder_id = self.holder_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_warranty_expiring_soon = self.is_warranty_expiring_soon

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        original_cost: float | None | Unset
        if isinstance(self.original_cost, Unset):
            original_cost = UNSET
        else:
            original_cost = self.original_cost

        purchased_date: str | Unset = UNSET
        if not isinstance(self.purchased_date, Unset):
            purchased_date = self.purchased_date.isoformat()

        residual_value: float | None | Unset
        if isinstance(self.residual_value, Unset):
            residual_value = UNSET
        else:
            residual_value = self.residual_value

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        warranty_end: None | str | Unset
        if isinstance(self.warranty_end, Unset):
            warranty_end = UNSET
        elif isinstance(self.warranty_end, datetime.date):
            warranty_end = self.warranty_end.isoformat()
        else:
            warranty_end = self.warranty_end


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if accumulated_depreciation is not UNSET:
            field_dict["accumulatedDepreciation"] = accumulated_depreciation
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if code is not UNSET:
            field_dict["code"] = code
        if condition is not UNSET:
            field_dict["condition"] = condition
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if depreciated_months is not UNSET:
            field_dict["depreciatedMonths"] = depreciated_months
        if depreciation_months is not UNSET:
            field_dict["depreciationMonths"] = depreciation_months
        if depreciation_percent is not UNSET:
            field_dict["depreciationPercent"] = depreciation_percent
        if depreciation_start_date is not UNSET:
            field_dict["depreciationStartDate"] = depreciation_start_date
        if holder_id is not UNSET:
            field_dict["holderId"] = holder_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_warranty_expiring_soon is not UNSET:
            field_dict["isWarrantyExpiringSoon"] = is_warranty_expiring_soon
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if original_cost is not UNSET:
            field_dict["originalCost"] = original_cost
        if purchased_date is not UNSET:
            field_dict["purchasedDate"] = purchased_date
        if residual_value is not UNSET:
            field_dict["residualValue"] = residual_value
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if warranty_end is not UNSET:
            field_dict["warrantyEnd"] = warranty_end

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_accumulated_depreciation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        accumulated_depreciation = _parse_accumulated_depreciation(d.pop("accumulatedDepreciation", UNSET))


        _as_of = d.pop("asOf", UNSET)
        as_of: datetime.date | Unset
        if isinstance(_as_of,  Unset):
            as_of = UNSET
        else:
            as_of = datetime.date.fromisoformat(_as_of)




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        depreciated_months = d.pop("depreciatedMonths", UNSET)

        depreciation_months = d.pop("depreciationMonths", UNSET)

        depreciation_percent = d.pop("depreciationPercent", UNSET)

        _depreciation_start_date = d.pop("depreciationStartDate", UNSET)
        depreciation_start_date: datetime.date | Unset
        if isinstance(_depreciation_start_date,  Unset):
            depreciation_start_date = UNSET
        else:
            depreciation_start_date = datetime.date.fromisoformat(_depreciation_start_date)




        def _parse_holder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                holder_id_type_0 = UUID(data)



                return holder_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        holder_id = _parse_holder_id(d.pop("holderId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_warranty_expiring_soon = d.pop("isWarrantyExpiringSoon", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_original_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        original_cost = _parse_original_cost(d.pop("originalCost", UNSET))


        _purchased_date = d.pop("purchasedDate", UNSET)
        purchased_date: datetime.date | Unset
        if isinstance(_purchased_date,  Unset):
            purchased_date = UNSET
        else:
            purchased_date = datetime.date.fromisoformat(_purchased_date)




        def _parse_residual_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        residual_value = _parse_residual_value(d.pop("residualValue", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        def _parse_warranty_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                warranty_end_type_0 = datetime.date.fromisoformat(data)



                return warranty_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        warranty_end = _parse_warranty_end(d.pop("warrantyEnd", UNSET))


        office_asset_dto = cls(
            accumulated_depreciation=accumulated_depreciation,
            as_of=as_of,
            code=code,
            condition=condition,
            created_at=created_at,
            depreciated_months=depreciated_months,
            depreciation_months=depreciation_months,
            depreciation_percent=depreciation_percent,
            depreciation_start_date=depreciation_start_date,
            holder_id=holder_id,
            id=id,
            is_warranty_expiring_soon=is_warranty_expiring_soon,
            name=name,
            note=note,
            original_cost=original_cost,
            purchased_date=purchased_date,
            residual_value=residual_value,
            updated_at=updated_at,
            warranty_end=warranty_end,
        )

        return office_asset_dto


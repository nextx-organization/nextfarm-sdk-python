from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeUpdateAssetRequest")



@_attrs_define
class OfficeUpdateAssetRequest:
    

    condition: None | str | Unset = UNSET
    depreciation_months: int | Unset = UNSET
    depreciation_start_date: datetime.date | None | Unset = UNSET
    name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    original_cost: float | Unset = UNSET
    purchased_date: datetime.date | Unset = UNSET
    warranty_end: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        condition: None | str | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        depreciation_months = self.depreciation_months

        depreciation_start_date: None | str | Unset
        if isinstance(self.depreciation_start_date, Unset):
            depreciation_start_date = UNSET
        elif isinstance(self.depreciation_start_date, datetime.date):
            depreciation_start_date = self.depreciation_start_date.isoformat()
        else:
            depreciation_start_date = self.depreciation_start_date

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

        original_cost = self.original_cost

        purchased_date: str | Unset = UNSET
        if not isinstance(self.purchased_date, Unset):
            purchased_date = self.purchased_date.isoformat()

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
        if condition is not UNSET:
            field_dict["condition"] = condition
        if depreciation_months is not UNSET:
            field_dict["depreciationMonths"] = depreciation_months
        if depreciation_start_date is not UNSET:
            field_dict["depreciationStartDate"] = depreciation_start_date
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if original_cost is not UNSET:
            field_dict["originalCost"] = original_cost
        if purchased_date is not UNSET:
            field_dict["purchasedDate"] = purchased_date
        if warranty_end is not UNSET:
            field_dict["warrantyEnd"] = warranty_end

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))


        depreciation_months = d.pop("depreciationMonths", UNSET)

        def _parse_depreciation_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                depreciation_start_date_type_0 = datetime.date.fromisoformat(data)



                return depreciation_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        depreciation_start_date = _parse_depreciation_start_date(d.pop("depreciationStartDate", UNSET))


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


        original_cost = d.pop("originalCost", UNSET)

        _purchased_date = d.pop("purchasedDate", UNSET)
        purchased_date: datetime.date | Unset
        if isinstance(_purchased_date,  Unset):
            purchased_date = UNSET
        else:
            purchased_date = datetime.date.fromisoformat(_purchased_date)




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


        office_update_asset_request = cls(
            condition=condition,
            depreciation_months=depreciation_months,
            depreciation_start_date=depreciation_start_date,
            name=name,
            note=note,
            original_cost=original_cost,
            purchased_date=purchased_date,
            warranty_end=warranty_end,
        )

        return office_update_asset_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestUpdateHarvestRecordRequest")



@_attrs_define
class HarvestUpdateHarvestRecordRequest:
    

    declared_quantity_kg: float | Unset = UNSET
    harvest_date: datetime.date | Unset = UNSET
    notes: None | str | Unset = UNSET
    phi_override_reason: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        declared_quantity_kg = self.declared_quantity_kg

        harvest_date: str | Unset = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        phi_override_reason: None | str | Unset
        if isinstance(self.phi_override_reason, Unset):
            phi_override_reason = UNSET
        else:
            phi_override_reason = self.phi_override_reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if declared_quantity_kg is not UNSET:
            field_dict["declared_quantity_kg"] = declared_quantity_kg
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if phi_override_reason is not UNSET:
            field_dict["phi_override_reason"] = phi_override_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declared_quantity_kg = d.pop("declared_quantity_kg", UNSET)

        _harvest_date = d.pop("harvest_date", UNSET)
        harvest_date: datetime.date | Unset
        if isinstance(_harvest_date,  Unset):
            harvest_date = UNSET
        else:
            harvest_date = datetime.date.fromisoformat(_harvest_date)




        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_phi_override_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phi_override_reason = _parse_phi_override_reason(d.pop("phi_override_reason", UNSET))


        harvest_update_harvest_record_request = cls(
            declared_quantity_kg=declared_quantity_kg,
            harvest_date=harvest_date,
            notes=notes,
            phi_override_reason=phi_override_reason,
        )

        return harvest_update_harvest_record_request


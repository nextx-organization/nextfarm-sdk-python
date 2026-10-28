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






T = TypeVar("T", bound="HarvestCreateHusbandryLogRequest")



@_attrs_define
class HarvestCreateHusbandryLogRequest:
    

    avg_weight_g: float | None | Unset = UNSET
    head_count: int | None | Unset = UNSET
    kind: None | str | Unset = UNSET
    material_name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    quantity: float | None | Unset = UNSET
    recorded_at: datetime.datetime | None | Unset = UNSET
    recorded_via: None | str | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    unit: None | str | Unset = UNSET
    withdrawal_days: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avg_weight_g: float | None | Unset
        if isinstance(self.avg_weight_g, Unset):
            avg_weight_g = UNSET
        else:
            avg_weight_g = self.avg_weight_g

        head_count: int | None | Unset
        if isinstance(self.head_count, Unset):
            head_count = UNSET
        else:
            head_count = self.head_count

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        material_name: None | str | Unset
        if isinstance(self.material_name, Unset):
            material_name = UNSET
        else:
            material_name = self.material_name

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        quantity: float | None | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        recorded_at: None | str | Unset
        if isinstance(self.recorded_at, Unset):
            recorded_at = UNSET
        elif isinstance(self.recorded_at, datetime.datetime):
            recorded_at = self.recorded_at.isoformat()
        else:
            recorded_at = self.recorded_at

        recorded_via: None | str | Unset
        if isinstance(self.recorded_via, Unset):
            recorded_via = UNSET
        else:
            recorded_via = self.recorded_via

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        withdrawal_days: int | None | Unset
        if isinstance(self.withdrawal_days, Unset):
            withdrawal_days = UNSET
        else:
            withdrawal_days = self.withdrawal_days


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avg_weight_g is not UNSET:
            field_dict["avg_weight_g"] = avg_weight_g
        if head_count is not UNSET:
            field_dict["head_count"] = head_count
        if kind is not UNSET:
            field_dict["kind"] = kind
        if material_name is not UNSET:
            field_dict["material_name"] = material_name
        if note is not UNSET:
            field_dict["note"] = note
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if recorded_at is not UNSET:
            field_dict["recorded_at"] = recorded_at
        if recorded_via is not UNSET:
            field_dict["recorded_via"] = recorded_via
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if unit is not UNSET:
            field_dict["unit"] = unit
        if withdrawal_days is not UNSET:
            field_dict["withdrawal_days"] = withdrawal_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_avg_weight_g(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_weight_g = _parse_avg_weight_g(d.pop("avg_weight_g", UNSET))


        def _parse_head_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        head_count = _parse_head_count(d.pop("head_count", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_material_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        material_name = _parse_material_name(d.pop("material_name", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        def _parse_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))


        def _parse_recorded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recorded_at_type_0 = datetime.datetime.fromisoformat(data)



                return recorded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        recorded_at = _parse_recorded_at(d.pop("recorded_at", UNSET))


        def _parse_recorded_via(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recorded_via = _parse_recorded_via(d.pop("recorded_via", UNSET))


        def _parse_season_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)



                return season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        season_id = _parse_season_id(d.pop("season_id", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        def _parse_withdrawal_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        withdrawal_days = _parse_withdrawal_days(d.pop("withdrawal_days", UNSET))


        harvest_create_husbandry_log_request = cls(
            avg_weight_g=avg_weight_g,
            head_count=head_count,
            kind=kind,
            material_name=material_name,
            note=note,
            parcel_id=parcel_id,
            quantity=quantity,
            recorded_at=recorded_at,
            recorded_via=recorded_via,
            season_id=season_id,
            unit=unit,
            withdrawal_days=withdrawal_days,
        )

        return harvest_create_husbandry_log_request


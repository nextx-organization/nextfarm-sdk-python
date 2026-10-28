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






T = TypeVar("T", bound="HarvestHarvestRecordDto")



@_attrs_define
class HarvestHarvestRecordDto:
    

    created_at: datetime.datetime | Unset = UNSET
    crop_type_id: UUID | Unset = UNSET
    crop_type_name: None | str | Unset = UNSET
    declared_quantity_kg: float | Unset = UNSET
    farming_task_id: None | Unset | UUID = UNSET
    harvest_date: datetime.date | Unset = UNSET
    id: UUID | Unset = UNSET
    needs_review: bool | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    return_reason: None | str | Unset = UNSET
    returned_at: datetime.datetime | None | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    trace_id: None | Unset | UUID = UNSET
    warnings: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

        crop_type_name: None | str | Unset
        if isinstance(self.crop_type_name, Unset):
            crop_type_name = UNSET
        else:
            crop_type_name = self.crop_type_name

        declared_quantity_kg = self.declared_quantity_kg

        farming_task_id: None | str | Unset
        if isinstance(self.farming_task_id, Unset):
            farming_task_id = UNSET
        elif isinstance(self.farming_task_id, UUID):
            farming_task_id = str(self.farming_task_id)
        else:
            farming_task_id = self.farming_task_id

        harvest_date: str | Unset = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        needs_review = self.needs_review

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        return_reason: None | str | Unset
        if isinstance(self.return_reason, Unset):
            return_reason = UNSET
        else:
            return_reason = self.return_reason

        returned_at: None | str | Unset
        if isinstance(self.returned_at, Unset):
            returned_at = UNSET
        elif isinstance(self.returned_at, datetime.datetime):
            returned_at = self.returned_at.isoformat()
        else:
            returned_at = self.returned_at

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        trace_id: None | str | Unset
        if isinstance(self.trace_id, Unset):
            trace_id = UNSET
        elif isinstance(self.trace_id, UUID):
            trace_id = str(self.trace_id)
        else:
            trace_id = self.trace_id

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings


        else:
            warnings = self.warnings


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if crop_type_name is not UNSET:
            field_dict["crop_type_name"] = crop_type_name
        if declared_quantity_kg is not UNSET:
            field_dict["declared_quantity_kg"] = declared_quantity_kg
        if farming_task_id is not UNSET:
            field_dict["farming_task_id"] = farming_task_id
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if id is not UNSET:
            field_dict["id"] = id
        if needs_review is not UNSET:
            field_dict["needs_review"] = needs_review
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if return_reason is not UNSET:
            field_dict["return_reason"] = return_reason
        if returned_at is not UNSET:
            field_dict["returned_at"] = returned_at
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if status is not UNSET:
            field_dict["status"] = status
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _crop_type_id = d.pop("crop_type_id", UNSET)
        crop_type_id: UUID | Unset
        if isinstance(_crop_type_id,  Unset):
            crop_type_id = UNSET
        else:
            crop_type_id = UUID(_crop_type_id)




        def _parse_crop_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_type_name = _parse_crop_type_name(d.pop("crop_type_name", UNSET))


        declared_quantity_kg = d.pop("declared_quantity_kg", UNSET)

        def _parse_farming_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                farming_task_id_type_0 = UUID(data)



                return farming_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        farming_task_id = _parse_farming_task_id(d.pop("farming_task_id", UNSET))


        _harvest_date = d.pop("harvest_date", UNSET)
        harvest_date: datetime.date | Unset
        if isinstance(_harvest_date,  Unset):
            harvest_date = UNSET
        else:
            harvest_date = datetime.date.fromisoformat(_harvest_date)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        needs_review = d.pop("needs_review", UNSET)

        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcel_code", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        def _parse_return_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_reason = _parse_return_reason(d.pop("return_reason", UNSET))


        def _parse_returned_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                returned_at_type_0 = datetime.datetime.fromisoformat(data)



                return returned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        returned_at = _parse_returned_at(d.pop("returned_at", UNSET))


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


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_trace_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trace_id_type_0 = UUID(data)



                return trace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        trace_id = _parse_trace_id(d.pop("trace_id", UNSET))


        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))


        harvest_harvest_record_dto = cls(
            created_at=created_at,
            crop_type_id=crop_type_id,
            crop_type_name=crop_type_name,
            declared_quantity_kg=declared_quantity_kg,
            farming_task_id=farming_task_id,
            harvest_date=harvest_date,
            id=id,
            needs_review=needs_review,
            parcel_code=parcel_code,
            parcel_id=parcel_id,
            return_reason=return_reason,
            returned_at=returned_at,
            season_id=season_id,
            status=status,
            trace_id=trace_id,
            warnings=warnings,
        )

        return harvest_harvest_record_dto


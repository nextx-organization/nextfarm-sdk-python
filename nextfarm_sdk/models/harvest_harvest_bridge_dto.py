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






T = TypeVar("T", bound="HarvestHarvestBridgeDto")



@_attrs_define
class HarvestHarvestBridgeDto:
    

    actual_quantity_kg: float | None | Unset = UNSET
    crop_type_id: UUID | Unset = UNSET
    crop_type_name: None | str | Unset = UNSET
    harvest_date: datetime.date | Unset = UNSET
    id: UUID | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    workspace_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        actual_quantity_kg: float | None | Unset
        if isinstance(self.actual_quantity_kg, Unset):
            actual_quantity_kg = UNSET
        else:
            actual_quantity_kg = self.actual_quantity_kg

        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

        crop_type_name: None | str | Unset
        if isinstance(self.crop_type_name, Unset):
            crop_type_name = UNSET
        else:
            crop_type_name = self.crop_type_name

        harvest_date: str | Unset = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

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

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actual_quantity_kg is not UNSET:
            field_dict["actual_quantity_kg"] = actual_quantity_kg
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if crop_type_name is not UNSET:
            field_dict["crop_type_name"] = crop_type_name
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if id is not UNSET:
            field_dict["id"] = id
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if status is not UNSET:
            field_dict["status"] = status
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_actual_quantity_kg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        actual_quantity_kg = _parse_actual_quantity_kg(d.pop("actual_quantity_kg", UNSET))


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




        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




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


        _workspace_id = d.pop("workspace_id", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        harvest_harvest_bridge_dto = cls(
            actual_quantity_kg=actual_quantity_kg,
            crop_type_id=crop_type_id,
            crop_type_name=crop_type_name,
            harvest_date=harvest_date,
            id=id,
            parcel_id=parcel_id,
            season_id=season_id,
            status=status,
            workspace_id=workspace_id,
        )

        return harvest_harvest_bridge_dto


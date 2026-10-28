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
  from ..models.harvest_harvest_organism_input import HarvestHarvestOrganismInput





T = TypeVar("T", bound="HarvestDeclareHarvestRequest")



@_attrs_define
class HarvestDeclareHarvestRequest:
    

    confirm: bool | Unset = UNSET
    crop_type_id: UUID | Unset = UNSET
    declared_quantity_kg: float | Unset = UNSET
    farming_task_id: None | Unset | UUID = UNSET
    harvest_date: datetime.date | Unset = UNSET
    notes: None | str | Unset = UNSET
    organisms: list[HarvestHarvestOrganismInput] | None | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    phi_override_reason: None | str | Unset = UNSET
    photo_urls: list[str] | None | Unset = UNSET
    season_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_harvest_organism_input import HarvestHarvestOrganismInput # noqa: PLC0415
        confirm = self.confirm

        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

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

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        organisms: list[dict[str, Any]] | None | Unset
        if isinstance(self.organisms, Unset):
            organisms = UNSET
        elif isinstance(self.organisms, list):
            organisms = []
            for organisms_type_0_item_data in self.organisms:
                organisms_type_0_item = organisms_type_0_item_data.to_dict()
                organisms.append(organisms_type_0_item)


        else:
            organisms = self.organisms

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        phi_override_reason: None | str | Unset
        if isinstance(self.phi_override_reason, Unset):
            phi_override_reason = UNSET
        else:
            phi_override_reason = self.phi_override_reason

        photo_urls: list[str] | None | Unset
        if isinstance(self.photo_urls, Unset):
            photo_urls = UNSET
        elif isinstance(self.photo_urls, list):
            photo_urls = self.photo_urls


        else:
            photo_urls = self.photo_urls

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if confirm is not UNSET:
            field_dict["confirm"] = confirm
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if declared_quantity_kg is not UNSET:
            field_dict["declared_quantity_kg"] = declared_quantity_kg
        if farming_task_id is not UNSET:
            field_dict["farming_task_id"] = farming_task_id
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if organisms is not UNSET:
            field_dict["organisms"] = organisms
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if phi_override_reason is not UNSET:
            field_dict["phi_override_reason"] = phi_override_reason
        if photo_urls is not UNSET:
            field_dict["photo_urls"] = photo_urls
        if season_id is not UNSET:
            field_dict["season_id"] = season_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_harvest_organism_input import HarvestHarvestOrganismInput # noqa: PLC0415
        d = dict(src_dict)
        confirm = d.pop("confirm", UNSET)

        _crop_type_id = d.pop("crop_type_id", UNSET)
        crop_type_id: UUID | Unset
        if isinstance(_crop_type_id,  Unset):
            crop_type_id = UNSET
        else:
            crop_type_id = UUID(_crop_type_id)




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




        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_organisms(data: object) -> list[HarvestHarvestOrganismInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organisms_type_0 = []
                _organisms_type_0 = data
                for organisms_type_0_item_data in (_organisms_type_0):
                    organisms_type_0_item = HarvestHarvestOrganismInput.from_dict(organisms_type_0_item_data)



                    organisms_type_0.append(organisms_type_0_item)

                return organisms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestHarvestOrganismInput] | None | Unset, data)

        organisms = _parse_organisms(d.pop("organisms", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        def _parse_phi_override_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phi_override_reason = _parse_phi_override_reason(d.pop("phi_override_reason", UNSET))


        def _parse_photo_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                photo_urls_type_0 = cast(list[str], data)

                return photo_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        photo_urls = _parse_photo_urls(d.pop("photo_urls", UNSET))


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


        harvest_declare_harvest_request = cls(
            confirm=confirm,
            crop_type_id=crop_type_id,
            declared_quantity_kg=declared_quantity_kg,
            farming_task_id=farming_task_id,
            harvest_date=harvest_date,
            notes=notes,
            organisms=organisms,
            parcel_id=parcel_id,
            phi_override_reason=phi_override_reason,
            photo_urls=photo_urls,
            season_id=season_id,
        )

        return harvest_declare_harvest_request


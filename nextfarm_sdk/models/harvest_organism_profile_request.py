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






T = TypeVar("T", bound="HarvestOrganismProfileRequest")



@_attrs_define
class HarvestOrganismProfileRequest:
    

    crop_type_id: None | Unset | UUID = UNSET
    note: None | str | Unset = UNSET
    origin: None | str | Unset = UNSET
    planted_estimated: bool | Unset = UNSET
    planted_on: datetime.date | None | Unset = UNSET
    planted_year: int | None | Unset = UNSET
    rootstock_id: None | Unset | UUID = UNSET
    rootstock_name: None | str | Unset = UNSET
    species_name: None | str | Unset = UNSET
    variety_id: None | Unset | UUID = UNSET
    variety_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        crop_type_id: None | str | Unset
        if isinstance(self.crop_type_id, Unset):
            crop_type_id = UNSET
        elif isinstance(self.crop_type_id, UUID):
            crop_type_id = str(self.crop_type_id)
        else:
            crop_type_id = self.crop_type_id

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        planted_estimated = self.planted_estimated

        planted_on: None | str | Unset
        if isinstance(self.planted_on, Unset):
            planted_on = UNSET
        elif isinstance(self.planted_on, datetime.date):
            planted_on = self.planted_on.isoformat()
        else:
            planted_on = self.planted_on

        planted_year: int | None | Unset
        if isinstance(self.planted_year, Unset):
            planted_year = UNSET
        else:
            planted_year = self.planted_year

        rootstock_id: None | str | Unset
        if isinstance(self.rootstock_id, Unset):
            rootstock_id = UNSET
        elif isinstance(self.rootstock_id, UUID):
            rootstock_id = str(self.rootstock_id)
        else:
            rootstock_id = self.rootstock_id

        rootstock_name: None | str | Unset
        if isinstance(self.rootstock_name, Unset):
            rootstock_name = UNSET
        else:
            rootstock_name = self.rootstock_name

        species_name: None | str | Unset
        if isinstance(self.species_name, Unset):
            species_name = UNSET
        else:
            species_name = self.species_name

        variety_id: None | str | Unset
        if isinstance(self.variety_id, Unset):
            variety_id = UNSET
        elif isinstance(self.variety_id, UUID):
            variety_id = str(self.variety_id)
        else:
            variety_id = self.variety_id

        variety_name: None | str | Unset
        if isinstance(self.variety_name, Unset):
            variety_name = UNSET
        else:
            variety_name = self.variety_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if note is not UNSET:
            field_dict["note"] = note
        if origin is not UNSET:
            field_dict["origin"] = origin
        if planted_estimated is not UNSET:
            field_dict["planted_estimated"] = planted_estimated
        if planted_on is not UNSET:
            field_dict["planted_on"] = planted_on
        if planted_year is not UNSET:
            field_dict["planted_year"] = planted_year
        if rootstock_id is not UNSET:
            field_dict["rootstock_id"] = rootstock_id
        if rootstock_name is not UNSET:
            field_dict["rootstock_name"] = rootstock_name
        if species_name is not UNSET:
            field_dict["species_name"] = species_name
        if variety_id is not UNSET:
            field_dict["variety_id"] = variety_id
        if variety_name is not UNSET:
            field_dict["variety_name"] = variety_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_crop_type_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                crop_type_id_type_0 = UUID(data)



                return crop_type_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        crop_type_id = _parse_crop_type_id(d.pop("crop_type_id", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))


        planted_estimated = d.pop("planted_estimated", UNSET)

        def _parse_planted_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planted_on_type_0 = datetime.date.fromisoformat(data)



                return planted_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        planted_on = _parse_planted_on(d.pop("planted_on", UNSET))


        def _parse_planted_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        planted_year = _parse_planted_year(d.pop("planted_year", UNSET))


        def _parse_rootstock_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rootstock_id_type_0 = UUID(data)



                return rootstock_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        rootstock_id = _parse_rootstock_id(d.pop("rootstock_id", UNSET))


        def _parse_rootstock_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rootstock_name = _parse_rootstock_name(d.pop("rootstock_name", UNSET))


        def _parse_species_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        species_name = _parse_species_name(d.pop("species_name", UNSET))


        def _parse_variety_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variety_id_type_0 = UUID(data)



                return variety_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        variety_id = _parse_variety_id(d.pop("variety_id", UNSET))


        def _parse_variety_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variety_name = _parse_variety_name(d.pop("variety_name", UNSET))


        harvest_organism_profile_request = cls(
            crop_type_id=crop_type_id,
            note=note,
            origin=origin,
            planted_estimated=planted_estimated,
            planted_on=planted_on,
            planted_year=planted_year,
            rootstock_id=rootstock_id,
            rootstock_name=rootstock_name,
            species_name=species_name,
            variety_id=variety_id,
            variety_name=variety_name,
        )

        return harvest_organism_profile_request


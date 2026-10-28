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






T = TypeVar("T", bound="HarvestPlanRequest")



@_attrs_define
class HarvestPlanRequest:
    

    crop_name: None | str | Unset = UNSET
    crop_type_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    period_from: datetime.date | Unset = UNSET
    period_to: datetime.date | Unset = UNSET
    season_template_id: None | Unset | UUID = UNSET
    target_yield_per_ha: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        crop_name: None | str | Unset
        if isinstance(self.crop_name, Unset):
            crop_name = UNSET
        else:
            crop_name = self.crop_name

        crop_type_id: None | str | Unset
        if isinstance(self.crop_type_id, Unset):
            crop_type_id = UNSET
        elif isinstance(self.crop_type_id, UUID):
            crop_type_id = str(self.crop_type_id)
        else:
            crop_type_id = self.crop_type_id

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

        period_from: str | Unset = UNSET
        if not isinstance(self.period_from, Unset):
            period_from = self.period_from.isoformat()

        period_to: str | Unset = UNSET
        if not isinstance(self.period_to, Unset):
            period_to = self.period_to.isoformat()

        season_template_id: None | str | Unset
        if isinstance(self.season_template_id, Unset):
            season_template_id = UNSET
        elif isinstance(self.season_template_id, UUID):
            season_template_id = str(self.season_template_id)
        else:
            season_template_id = self.season_template_id

        target_yield_per_ha: float | None | Unset
        if isinstance(self.target_yield_per_ha, Unset):
            target_yield_per_ha = UNSET
        else:
            target_yield_per_ha = self.target_yield_per_ha


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_name is not UNSET:
            field_dict["crop_name"] = crop_name
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if period_from is not UNSET:
            field_dict["period_from"] = period_from
        if period_to is not UNSET:
            field_dict["period_to"] = period_to
        if season_template_id is not UNSET:
            field_dict["season_template_id"] = season_template_id
        if target_yield_per_ha is not UNSET:
            field_dict["target_yield_per_ha"] = target_yield_per_ha

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_crop_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_name = _parse_crop_name(d.pop("crop_name", UNSET))


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


        _period_from = d.pop("period_from", UNSET)
        period_from: datetime.date | Unset
        if isinstance(_period_from,  Unset):
            period_from = UNSET
        else:
            period_from = datetime.date.fromisoformat(_period_from)




        _period_to = d.pop("period_to", UNSET)
        period_to: datetime.date | Unset
        if isinstance(_period_to,  Unset):
            period_to = UNSET
        else:
            period_to = datetime.date.fromisoformat(_period_to)




        def _parse_season_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_template_id_type_0 = UUID(data)



                return season_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        season_template_id = _parse_season_template_id(d.pop("season_template_id", UNSET))


        def _parse_target_yield_per_ha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target_yield_per_ha = _parse_target_yield_per_ha(d.pop("target_yield_per_ha", UNSET))


        harvest_plan_request = cls(
            crop_name=crop_name,
            crop_type_id=crop_type_id,
            name=name,
            note=note,
            period_from=period_from,
            period_to=period_to,
            season_template_id=season_template_id,
            target_yield_per_ha=target_yield_per_ha,
        )

        return harvest_plan_request


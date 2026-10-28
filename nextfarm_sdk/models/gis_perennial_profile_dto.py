from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.gis_life_stage_dto import GisLifeStageDto





T = TypeVar("T", bound="GisPerennialProfileDto")



@_attrs_define
class GisPerennialProfileDto:
    

    bearing_age_years: int | None | Unset = UNSET
    crop_type_id: UUID | Unset = UNSET
    default_row_spacing_m: float | None | Unset = UNSET
    default_tree_spacing_m: float | None | Unset = UNSET
    effective_lifecycle: None | str | Unset = UNSET
    life_stages: list[GisLifeStageDto] | None | Unset = UNSET
    lifecycle: None | str | Unset = UNSET
    lifecycle_guessed: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_life_stage_dto import GisLifeStageDto # noqa: PLC0415
        bearing_age_years: int | None | Unset
        if isinstance(self.bearing_age_years, Unset):
            bearing_age_years = UNSET
        else:
            bearing_age_years = self.bearing_age_years

        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

        default_row_spacing_m: float | None | Unset
        if isinstance(self.default_row_spacing_m, Unset):
            default_row_spacing_m = UNSET
        else:
            default_row_spacing_m = self.default_row_spacing_m

        default_tree_spacing_m: float | None | Unset
        if isinstance(self.default_tree_spacing_m, Unset):
            default_tree_spacing_m = UNSET
        else:
            default_tree_spacing_m = self.default_tree_spacing_m

        effective_lifecycle: None | str | Unset
        if isinstance(self.effective_lifecycle, Unset):
            effective_lifecycle = UNSET
        else:
            effective_lifecycle = self.effective_lifecycle

        life_stages: list[dict[str, Any]] | None | Unset
        if isinstance(self.life_stages, Unset):
            life_stages = UNSET
        elif isinstance(self.life_stages, list):
            life_stages = []
            for life_stages_type_0_item_data in self.life_stages:
                life_stages_type_0_item = life_stages_type_0_item_data.to_dict()
                life_stages.append(life_stages_type_0_item)


        else:
            life_stages = self.life_stages

        lifecycle: None | str | Unset
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = self.lifecycle

        lifecycle_guessed = self.lifecycle_guessed


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bearing_age_years is not UNSET:
            field_dict["bearing_age_years"] = bearing_age_years
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if default_row_spacing_m is not UNSET:
            field_dict["default_row_spacing_m"] = default_row_spacing_m
        if default_tree_spacing_m is not UNSET:
            field_dict["default_tree_spacing_m"] = default_tree_spacing_m
        if effective_lifecycle is not UNSET:
            field_dict["effective_lifecycle"] = effective_lifecycle
        if life_stages is not UNSET:
            field_dict["life_stages"] = life_stages
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if lifecycle_guessed is not UNSET:
            field_dict["lifecycle_guessed"] = lifecycle_guessed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_life_stage_dto import GisLifeStageDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_bearing_age_years(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bearing_age_years = _parse_bearing_age_years(d.pop("bearing_age_years", UNSET))


        _crop_type_id = d.pop("crop_type_id", UNSET)
        crop_type_id: UUID | Unset
        if isinstance(_crop_type_id,  Unset):
            crop_type_id = UNSET
        else:
            crop_type_id = UUID(_crop_type_id)




        def _parse_default_row_spacing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_row_spacing_m = _parse_default_row_spacing_m(d.pop("default_row_spacing_m", UNSET))


        def _parse_default_tree_spacing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_tree_spacing_m = _parse_default_tree_spacing_m(d.pop("default_tree_spacing_m", UNSET))


        def _parse_effective_lifecycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_lifecycle = _parse_effective_lifecycle(d.pop("effective_lifecycle", UNSET))


        def _parse_life_stages(data: object) -> list[GisLifeStageDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                life_stages_type_0 = []
                _life_stages_type_0 = data
                for life_stages_type_0_item_data in (_life_stages_type_0):
                    life_stages_type_0_item = GisLifeStageDto.from_dict(life_stages_type_0_item_data)



                    life_stages_type_0.append(life_stages_type_0_item)

                return life_stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisLifeStageDto] | None | Unset, data)

        life_stages = _parse_life_stages(d.pop("life_stages", UNSET))


        def _parse_lifecycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))


        lifecycle_guessed = d.pop("lifecycle_guessed", UNSET)

        gis_perennial_profile_dto = cls(
            bearing_age_years=bearing_age_years,
            crop_type_id=crop_type_id,
            default_row_spacing_m=default_row_spacing_m,
            default_tree_spacing_m=default_tree_spacing_m,
            effective_lifecycle=effective_lifecycle,
            life_stages=life_stages,
            lifecycle=lifecycle,
            lifecycle_guessed=lifecycle_guessed,
        )

        return gis_perennial_profile_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_life_stage_dto import GisLifeStageDto





T = TypeVar("T", bound="GisSetPerennialProfileRequest")



@_attrs_define
class GisSetPerennialProfileRequest:
    

    bearing_age_years: int | None | Unset = UNSET
    default_row_spacing_m: float | None | Unset = UNSET
    default_tree_spacing_m: float | None | Unset = UNSET
    life_stages: list[GisLifeStageDto] | None | Unset = UNSET
    lifecycle: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_life_stage_dto import GisLifeStageDto # noqa: PLC0415
        bearing_age_years: int | None | Unset
        if isinstance(self.bearing_age_years, Unset):
            bearing_age_years = UNSET
        else:
            bearing_age_years = self.bearing_age_years

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bearing_age_years is not UNSET:
            field_dict["bearing_age_years"] = bearing_age_years
        if default_row_spacing_m is not UNSET:
            field_dict["default_row_spacing_m"] = default_row_spacing_m
        if default_tree_spacing_m is not UNSET:
            field_dict["default_tree_spacing_m"] = default_tree_spacing_m
        if life_stages is not UNSET:
            field_dict["life_stages"] = life_stages
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle

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


        gis_set_perennial_profile_request = cls(
            bearing_age_years=bearing_age_years,
            default_row_spacing_m=default_row_spacing_m,
            default_tree_spacing_m=default_tree_spacing_m,
            life_stages=life_stages,
            lifecycle=lifecycle,
        )

        return gis_set_perennial_profile_request


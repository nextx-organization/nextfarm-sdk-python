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
  from ..models.gis_care_rule import GisCareRule
  from ..models.gis_season_template_stage_input import GisSeasonTemplateStageInput





T = TypeVar("T", bound="GisSaveSeasonTemplateRequest")



@_attrs_define
class GisSaveSeasonTemplateRequest:
    

    crop_type_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    rules: list[GisCareRule] | None | Unset = UNSET
    stages: list[GisSeasonTemplateStageInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_care_rule import GisCareRule # noqa: PLC0415
        from ..models.gis_season_template_stage_input import GisSeasonTemplateStageInput # noqa: PLC0415
        crop_type_id: None | str | Unset
        if isinstance(self.crop_type_id, Unset):
            crop_type_id = UNSET
        elif isinstance(self.crop_type_id, UUID):
            crop_type_id = str(self.crop_type_id)
        else:
            crop_type_id = self.crop_type_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, list):
            rules = []
            for rules_type_0_item_data in self.rules:
                rules_type_0_item = rules_type_0_item_data.to_dict()
                rules.append(rules_type_0_item)


        else:
            rules = self.rules

        stages: list[dict[str, Any]] | None | Unset
        if isinstance(self.stages, Unset):
            stages = UNSET
        elif isinstance(self.stages, list):
            stages = []
            for stages_type_0_item_data in self.stages:
                stages_type_0_item = stages_type_0_item_data.to_dict()
                stages.append(stages_type_0_item)


        else:
            stages = self.stages


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if rules is not UNSET:
            field_dict["rules"] = rules
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_care_rule import GisCareRule # noqa: PLC0415
        from ..models.gis_season_template_stage_input import GisSeasonTemplateStageInput # noqa: PLC0415
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


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_rules(data: object) -> list[GisCareRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = []
                _rules_type_0 = data
                for rules_type_0_item_data in (_rules_type_0):
                    rules_type_0_item = GisCareRule.from_dict(rules_type_0_item_data)



                    rules_type_0.append(rules_type_0_item)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisCareRule] | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))


        def _parse_stages(data: object) -> list[GisSeasonTemplateStageInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stages_type_0 = []
                _stages_type_0 = data
                for stages_type_0_item_data in (_stages_type_0):
                    stages_type_0_item = GisSeasonTemplateStageInput.from_dict(stages_type_0_item_data)



                    stages_type_0.append(stages_type_0_item)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisSeasonTemplateStageInput] | None | Unset, data)

        stages = _parse_stages(d.pop("stages", UNSET))


        gis_save_season_template_request = cls(
            crop_type_id=crop_type_id,
            description=description,
            name=name,
            rules=rules,
            stages=stages,
        )

        return gis_save_season_template_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.gis_season_stage_input import GisSeasonStageInput





T = TypeVar("T", bound="GisUpdateSeasonRequest")



@_attrs_define
class GisUpdateSeasonRequest:
    

    expected_harvest_on: datetime.date | None | Unset = UNSET
    name: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    planted_on: datetime.date | Unset = UNSET
    stages: list[GisSeasonStageInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_season_stage_input import GisSeasonStageInput # noqa: PLC0415
        expected_harvest_on: None | str | Unset
        if isinstance(self.expected_harvest_on, Unset):
            expected_harvest_on = UNSET
        elif isinstance(self.expected_harvest_on, datetime.date):
            expected_harvest_on = self.expected_harvest_on.isoformat()
        else:
            expected_harvest_on = self.expected_harvest_on

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        planted_on: str | Unset = UNSET
        if not isinstance(self.planted_on, Unset):
            planted_on = self.planted_on.isoformat()

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
        if expected_harvest_on is not UNSET:
            field_dict["expected_harvest_on"] = expected_harvest_on
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if planted_on is not UNSET:
            field_dict["planted_on"] = planted_on
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_season_stage_input import GisSeasonStageInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_expected_harvest_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_harvest_on_type_0 = datetime.date.fromisoformat(data)



                return expected_harvest_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expected_harvest_on = _parse_expected_harvest_on(d.pop("expected_harvest_on", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        _planted_on = d.pop("planted_on", UNSET)
        planted_on: datetime.date | Unset
        if isinstance(_planted_on,  Unset):
            planted_on = UNSET
        else:
            planted_on = datetime.date.fromisoformat(_planted_on)




        def _parse_stages(data: object) -> list[GisSeasonStageInput] | None | Unset:
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
                    stages_type_0_item = GisSeasonStageInput.from_dict(stages_type_0_item_data)



                    stages_type_0.append(stages_type_0_item)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisSeasonStageInput] | None | Unset, data)

        stages = _parse_stages(d.pop("stages", UNSET))


        gis_update_season_request = cls(
            expected_harvest_on=expected_harvest_on,
            name=name,
            notes=notes,
            planted_on=planted_on,
            stages=stages,
        )

        return gis_update_season_request


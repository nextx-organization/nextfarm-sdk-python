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
  from ..models.gis_season_stage_input import GisSeasonStageInput





T = TypeVar("T", bound="GisCreateSeasonCommand")



@_attrs_define
class GisCreateSeasonCommand:
    

    crop_type_id: UUID | Unset = UNSET
    expected_harvest_on: datetime.date | None | Unset = UNSET
    kind: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    planted_on: datetime.date | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET
    stages: list[GisSeasonStageInput] | None | Unset = UNSET
    year: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_season_stage_input import GisSeasonStageInput # noqa: PLC0415
        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

        expected_harvest_on: None | str | Unset
        if isinstance(self.expected_harvest_on, Unset):
            expected_harvest_on = UNSET
        elif isinstance(self.expected_harvest_on, datetime.date):
            expected_harvest_on = self.expected_harvest_on.isoformat()
        else:
            expected_harvest_on = self.expected_harvest_on

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

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

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        planted_on: str | Unset = UNSET
        if not isinstance(self.planted_on, Unset):
            planted_on = self.planted_on.isoformat()

        plot_id: None | str | Unset
        if isinstance(self.plot_id, Unset):
            plot_id = UNSET
        elif isinstance(self.plot_id, UUID):
            plot_id = str(self.plot_id)
        else:
            plot_id = self.plot_id

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

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if expected_harvest_on is not UNSET:
            field_dict["expected_harvest_on"] = expected_harvest_on
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if planted_on is not UNSET:
            field_dict["planted_on"] = planted_on
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id
        if stages is not UNSET:
            field_dict["stages"] = stages
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_season_stage_input import GisSeasonStageInput # noqa: PLC0415
        d = dict(src_dict)
        _crop_type_id = d.pop("crop_type_id", UNSET)
        crop_type_id: UUID | Unset
        if isinstance(_crop_type_id,  Unset):
            crop_type_id = UNSET
        else:
            crop_type_id = UUID(_crop_type_id)




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


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


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


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        _planted_on = d.pop("planted_on", UNSET)
        planted_on: datetime.date | Unset
        if isinstance(_planted_on,  Unset):
            planted_on = UNSET
        else:
            planted_on = datetime.date.fromisoformat(_planted_on)




        def _parse_plot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                plot_id_type_0 = UUID(data)



                return plot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        plot_id = _parse_plot_id(d.pop("plot_id", UNSET))


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


        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))


        gis_create_season_command = cls(
            crop_type_id=crop_type_id,
            expected_harvest_on=expected_harvest_on,
            kind=kind,
            name=name,
            notes=notes,
            parcel_id=parcel_id,
            planted_on=planted_on,
            plot_id=plot_id,
            stages=stages,
            year=year,
        )

        return gis_create_season_command


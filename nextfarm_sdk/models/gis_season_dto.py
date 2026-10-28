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
  from ..models.gis_season_stage_dto import GisSeasonStageDto





T = TypeVar("T", bound="GisSeasonDto")



@_attrs_define
class GisSeasonDto:
    

    branch_id: None | Unset | UUID = UNSET
    closed_on: datetime.date | None | Unset = UNSET
    crop_name: None | str | Unset = UNSET
    crop_type_id: UUID | Unset = UNSET
    expected_harvest_on: datetime.date | None | Unset = UNSET
    id: UUID | Unset = UNSET
    kind: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    planted_on: datetime.date | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET
    stages: list[GisSeasonStageDto] | None | Unset = UNSET
    status: None | str | Unset = UNSET
    year: int | None | Unset = UNSET
    yield_kg: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_season_stage_dto import GisSeasonStageDto # noqa: PLC0415
        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        closed_on: None | str | Unset
        if isinstance(self.closed_on, Unset):
            closed_on = UNSET
        elif isinstance(self.closed_on, datetime.date):
            closed_on = self.closed_on.isoformat()
        else:
            closed_on = self.closed_on

        crop_name: None | str | Unset
        if isinstance(self.crop_name, Unset):
            crop_name = UNSET
        else:
            crop_name = self.crop_name

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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        yield_kg: float | None | Unset
        if isinstance(self.yield_kg, Unset):
            yield_kg = UNSET
        else:
            yield_kg = self.yield_kg


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if closed_on is not UNSET:
            field_dict["closed_on"] = closed_on
        if crop_name is not UNSET:
            field_dict["crop_name"] = crop_name
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if expected_harvest_on is not UNSET:
            field_dict["expected_harvest_on"] = expected_harvest_on
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if planted_on is not UNSET:
            field_dict["planted_on"] = planted_on
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id
        if stages is not UNSET:
            field_dict["stages"] = stages
        if status is not UNSET:
            field_dict["status"] = status
        if year is not UNSET:
            field_dict["year"] = year
        if yield_kg is not UNSET:
            field_dict["yield_kg"] = yield_kg

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_season_stage_dto import GisSeasonStageDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branch_id", UNSET))


        def _parse_closed_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_on_type_0 = datetime.date.fromisoformat(data)



                return closed_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        closed_on = _parse_closed_on(d.pop("closed_on", UNSET))


        def _parse_crop_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_name = _parse_crop_name(d.pop("crop_name", UNSET))


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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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


        def _parse_stages(data: object) -> list[GisSeasonStageDto] | None | Unset:
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
                    stages_type_0_item = GisSeasonStageDto.from_dict(stages_type_0_item_data)



                    stages_type_0.append(stages_type_0_item)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisSeasonStageDto] | None | Unset, data)

        stages = _parse_stages(d.pop("stages", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))


        def _parse_yield_kg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        yield_kg = _parse_yield_kg(d.pop("yield_kg", UNSET))


        gis_season_dto = cls(
            branch_id=branch_id,
            closed_on=closed_on,
            crop_name=crop_name,
            crop_type_id=crop_type_id,
            expected_harvest_on=expected_harvest_on,
            id=id,
            kind=kind,
            name=name,
            notes=notes,
            parcel_code=parcel_code,
            parcel_id=parcel_id,
            planted_on=planted_on,
            plot_id=plot_id,
            stages=stages,
            status=status,
            year=year,
            yield_kg=yield_kg,
        )

        return gis_season_dto


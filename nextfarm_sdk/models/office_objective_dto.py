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
  from ..models.office_key_result_dto import OfficeKeyResultDto





T = TypeVar("T", bound="OfficeObjectiveDto")



@_attrs_define
class OfficeObjectiveDto:
    

    branch_id: None | Unset | UUID = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    department_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    expected_progress: int | Unset = UNSET
    id: UUID | Unset = UNSET
    is_at_risk: bool | Unset = UNSET
    key_results: list[OfficeKeyResultDto] | None | Unset = UNSET
    level: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    pace_status: None | str | Unset = UNSET
    parent_objective_id: None | Unset | UUID = UNSET
    period_kind: None | str | Unset = UNSET
    progress: int | Unset = UNSET
    quarter: int | Unset = UNSET
    retrospective: None | str | Unset = UNSET
    season_dates_at: datetime.datetime | None | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    season_key: None | str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    year: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_key_result_dto import OfficeKeyResultDto # noqa: PLC0415
        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        expected_progress = self.expected_progress

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_at_risk = self.is_at_risk

        key_results: list[dict[str, Any]] | None | Unset
        if isinstance(self.key_results, Unset):
            key_results = UNSET
        elif isinstance(self.key_results, list):
            key_results = []
            for key_results_type_0_item_data in self.key_results:
                key_results_type_0_item = key_results_type_0_item_data.to_dict()
                key_results.append(key_results_type_0_item)


        else:
            key_results = self.key_results

        level: None | str | Unset
        if isinstance(self.level, Unset):
            level = UNSET
        else:
            level = self.level

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        owner_id: str | Unset = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = str(self.owner_id)

        pace_status: None | str | Unset
        if isinstance(self.pace_status, Unset):
            pace_status = UNSET
        else:
            pace_status = self.pace_status

        parent_objective_id: None | str | Unset
        if isinstance(self.parent_objective_id, Unset):
            parent_objective_id = UNSET
        elif isinstance(self.parent_objective_id, UUID):
            parent_objective_id = str(self.parent_objective_id)
        else:
            parent_objective_id = self.parent_objective_id

        period_kind: None | str | Unset
        if isinstance(self.period_kind, Unset):
            period_kind = UNSET
        else:
            period_kind = self.period_kind

        progress = self.progress

        quarter = self.quarter

        retrospective: None | str | Unset
        if isinstance(self.retrospective, Unset):
            retrospective = UNSET
        else:
            retrospective = self.retrospective

        season_dates_at: None | str | Unset
        if isinstance(self.season_dates_at, Unset):
            season_dates_at = UNSET
        elif isinstance(self.season_dates_at, datetime.datetime):
            season_dates_at = self.season_dates_at.isoformat()
        else:
            season_dates_at = self.season_dates_at

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        season_key: None | str | Unset
        if isinstance(self.season_key, Unset):
            season_key = UNSET
        else:
            season_key = self.season_key

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        year = self.year


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if expected_progress is not UNSET:
            field_dict["expectedProgress"] = expected_progress
        if id is not UNSET:
            field_dict["id"] = id
        if is_at_risk is not UNSET:
            field_dict["isAtRisk"] = is_at_risk
        if key_results is not UNSET:
            field_dict["keyResults"] = key_results
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if pace_status is not UNSET:
            field_dict["paceStatus"] = pace_status
        if parent_objective_id is not UNSET:
            field_dict["parentObjectiveId"] = parent_objective_id
        if period_kind is not UNSET:
            field_dict["periodKind"] = period_kind
        if progress is not UNSET:
            field_dict["progress"] = progress
        if quarter is not UNSET:
            field_dict["quarter"] = quarter
        if retrospective is not UNSET:
            field_dict["retrospective"] = retrospective
        if season_dates_at is not UNSET:
            field_dict["seasonDatesAt"] = season_dates_at
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season_key is not UNSET:
            field_dict["seasonKey"] = season_key
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_key_result_dto import OfficeKeyResultDto # noqa: PLC0415
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

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)



                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closedAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)



                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("departmentId", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        expected_progress = d.pop("expectedProgress", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_at_risk = d.pop("isAtRisk", UNSET)

        def _parse_key_results(data: object) -> list[OfficeKeyResultDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                key_results_type_0 = []
                _key_results_type_0 = data
                for key_results_type_0_item_data in (_key_results_type_0):
                    key_results_type_0_item = OfficeKeyResultDto.from_dict(key_results_type_0_item_data)



                    key_results_type_0.append(key_results_type_0_item)

                return key_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeKeyResultDto] | None | Unset, data)

        key_results = _parse_key_results(d.pop("keyResults", UNSET))


        def _parse_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level = _parse_level(d.pop("level", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _owner_id = d.pop("ownerId", UNSET)
        owner_id: UUID | Unset
        if isinstance(_owner_id,  Unset):
            owner_id = UNSET
        else:
            owner_id = UUID(_owner_id)




        def _parse_pace_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pace_status = _parse_pace_status(d.pop("paceStatus", UNSET))


        def _parse_parent_objective_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_objective_id_type_0 = UUID(data)



                return parent_objective_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_objective_id = _parse_parent_objective_id(d.pop("parentObjectiveId", UNSET))


        def _parse_period_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_kind = _parse_period_kind(d.pop("periodKind", UNSET))


        progress = d.pop("progress", UNSET)

        quarter = d.pop("quarter", UNSET)

        def _parse_retrospective(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retrospective = _parse_retrospective(d.pop("retrospective", UNSET))


        def _parse_season_dates_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_dates_at_type_0 = datetime.datetime.fromisoformat(data)



                return season_dates_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        season_dates_at = _parse_season_dates_at(d.pop("seasonDatesAt", UNSET))


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

        season_id = _parse_season_id(d.pop("seasonId", UNSET))


        def _parse_season_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        season_key = _parse_season_key(d.pop("seasonKey", UNSET))


        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        year = d.pop("year", UNSET)

        office_objective_dto = cls(
            branch_id=branch_id,
            closed_at=closed_at,
            created_at=created_at,
            department_id=department_id,
            description=description,
            end_date=end_date,
            expected_progress=expected_progress,
            id=id,
            is_at_risk=is_at_risk,
            key_results=key_results,
            level=level,
            name=name,
            owner_id=owner_id,
            pace_status=pace_status,
            parent_objective_id=parent_objective_id,
            period_kind=period_kind,
            progress=progress,
            quarter=quarter,
            retrospective=retrospective,
            season_dates_at=season_dates_at,
            season_id=season_id,
            season_key=season_key,
            start_date=start_date,
            updated_at=updated_at,
            year=year,
        )

        return office_objective_dto


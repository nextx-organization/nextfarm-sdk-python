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
  from ..models.office_create_key_result_input import OfficeCreateKeyResultInput





T = TypeVar("T", bound="OfficeCreateObjectiveRequest")



@_attrs_define
class OfficeCreateObjectiveRequest:
    

    branch_id: None | Unset | UUID = UNSET
    department_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    key_results: list[OfficeCreateKeyResultInput] | None | Unset = UNSET
    level: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    parent_objective_id: None | Unset | UUID = UNSET
    period_kind: None | str | Unset = UNSET
    quarter: int | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    season_key: None | str | Unset = UNSET
    year: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_create_key_result_input import OfficeCreateKeyResultInput # noqa: PLC0415
        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

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

        quarter = self.quarter

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

        year = self.year


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if description is not UNSET:
            field_dict["description"] = description
        if key_results is not UNSET:
            field_dict["keyResults"] = key_results
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if parent_objective_id is not UNSET:
            field_dict["parentObjectiveId"] = parent_objective_id
        if period_kind is not UNSET:
            field_dict["periodKind"] = period_kind
        if quarter is not UNSET:
            field_dict["quarter"] = quarter
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season_key is not UNSET:
            field_dict["seasonKey"] = season_key
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_create_key_result_input import OfficeCreateKeyResultInput # noqa: PLC0415
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


        def _parse_key_results(data: object) -> list[OfficeCreateKeyResultInput] | None | Unset:
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
                    key_results_type_0_item = OfficeCreateKeyResultInput.from_dict(key_results_type_0_item_data)



                    key_results_type_0.append(key_results_type_0_item)

                return key_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCreateKeyResultInput] | None | Unset, data)

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


        quarter = d.pop("quarter", UNSET)

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


        year = d.pop("year", UNSET)

        office_create_objective_request = cls(
            branch_id=branch_id,
            department_id=department_id,
            description=description,
            key_results=key_results,
            level=level,
            name=name,
            owner_id=owner_id,
            parent_objective_id=parent_objective_id,
            period_kind=period_kind,
            quarter=quarter,
            season_id=season_id,
            season_key=season_key,
            year=year,
        )

        return office_create_objective_request


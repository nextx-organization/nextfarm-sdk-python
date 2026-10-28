from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeRolloverRequest")



@_attrs_define
class OfficeRolloverRequest:
    

    objective_ids: list[UUID] | None | Unset = UNSET
    period_kind: None | str | Unset = UNSET
    quarter: int | None | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    season_key: None | str | Unset = UNSET
    year: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        objective_ids: list[str] | None | Unset
        if isinstance(self.objective_ids, Unset):
            objective_ids = UNSET
        elif isinstance(self.objective_ids, list):
            objective_ids = []
            for objective_ids_type_0_item_data in self.objective_ids:
                objective_ids_type_0_item = str(objective_ids_type_0_item_data)
                objective_ids.append(objective_ids_type_0_item)


        else:
            objective_ids = self.objective_ids

        period_kind: None | str | Unset
        if isinstance(self.period_kind, Unset):
            period_kind = UNSET
        else:
            period_kind = self.period_kind

        quarter: int | None | Unset
        if isinstance(self.quarter, Unset):
            quarter = UNSET
        else:
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

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if objective_ids is not UNSET:
            field_dict["objectiveIds"] = objective_ids
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
        d = dict(src_dict)
        def _parse_objective_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                objective_ids_type_0 = []
                _objective_ids_type_0 = data
                for objective_ids_type_0_item_data in (_objective_ids_type_0):
                    objective_ids_type_0_item = UUID(objective_ids_type_0_item_data)



                    objective_ids_type_0.append(objective_ids_type_0_item)

                return objective_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        objective_ids = _parse_objective_ids(d.pop("objectiveIds", UNSET))


        def _parse_period_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_kind = _parse_period_kind(d.pop("periodKind", UNSET))


        def _parse_quarter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quarter = _parse_quarter(d.pop("quarter", UNSET))


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


        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))


        office_rollover_request = cls(
            objective_ids=objective_ids,
            period_kind=period_kind,
            quarter=quarter,
            season_id=season_id,
            season_key=season_key,
            year=year,
        )

        return office_rollover_request


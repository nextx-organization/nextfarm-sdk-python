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
  from ..models.report_labor_cost_quantity_dto import ReportLaborCostQuantityDto





T = TypeVar("T", bound="ReportLaborCostRowDto")



@_attrs_define
class ReportLaborCostRowDto:
    

    cost_per_kg: int | None | Unset = UNSET
    crop_name: None | str | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    parcel_id: None | Unset | UUID = UNSET
    piecework_cost: int | Unset = UNSET
    piecework_quantities: list[ReportLaborCostQuantityDto] | None | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    season_name: None | str | Unset = UNSET
    time_cost: int | Unset = UNSET
    total_cost: int | Unset = UNSET
    work_units: float | Unset = UNSET
    worker_count: int | Unset = UNSET
    yield_kg: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_labor_cost_quantity_dto import ReportLaborCostQuantityDto # noqa: PLC0415
        cost_per_kg: int | None | Unset
        if isinstance(self.cost_per_kg, Unset):
            cost_per_kg = UNSET
        else:
            cost_per_kg = self.cost_per_kg

        crop_name: None | str | Unset
        if isinstance(self.crop_name, Unset):
            crop_name = UNSET
        else:
            crop_name = self.crop_name

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        parcel_id: None | str | Unset
        if isinstance(self.parcel_id, Unset):
            parcel_id = UNSET
        elif isinstance(self.parcel_id, UUID):
            parcel_id = str(self.parcel_id)
        else:
            parcel_id = self.parcel_id

        piecework_cost = self.piecework_cost

        piecework_quantities: list[dict[str, Any]] | None | Unset
        if isinstance(self.piecework_quantities, Unset):
            piecework_quantities = UNSET
        elif isinstance(self.piecework_quantities, list):
            piecework_quantities = []
            for piecework_quantities_type_0_item_data in self.piecework_quantities:
                piecework_quantities_type_0_item = piecework_quantities_type_0_item_data.to_dict()
                piecework_quantities.append(piecework_quantities_type_0_item)


        else:
            piecework_quantities = self.piecework_quantities

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        season_name: None | str | Unset
        if isinstance(self.season_name, Unset):
            season_name = UNSET
        else:
            season_name = self.season_name

        time_cost = self.time_cost

        total_cost = self.total_cost

        work_units = self.work_units

        worker_count = self.worker_count

        yield_kg: float | None | Unset
        if isinstance(self.yield_kg, Unset):
            yield_kg = UNSET
        else:
            yield_kg = self.yield_kg


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cost_per_kg is not UNSET:
            field_dict["costPerKg"] = cost_per_kg
        if crop_name is not UNSET:
            field_dict["cropName"] = crop_name
        if parcel_code is not UNSET:
            field_dict["parcelCode"] = parcel_code
        if parcel_id is not UNSET:
            field_dict["parcelId"] = parcel_id
        if piecework_cost is not UNSET:
            field_dict["pieceworkCost"] = piecework_cost
        if piecework_quantities is not UNSET:
            field_dict["pieceworkQuantities"] = piecework_quantities
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season_name is not UNSET:
            field_dict["seasonName"] = season_name
        if time_cost is not UNSET:
            field_dict["timeCost"] = time_cost
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if work_units is not UNSET:
            field_dict["workUnits"] = work_units
        if worker_count is not UNSET:
            field_dict["workerCount"] = worker_count
        if yield_kg is not UNSET:
            field_dict["yieldKg"] = yield_kg

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_labor_cost_quantity_dto import ReportLaborCostQuantityDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_cost_per_kg(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cost_per_kg = _parse_cost_per_kg(d.pop("costPerKg", UNSET))


        def _parse_crop_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_name = _parse_crop_name(d.pop("cropName", UNSET))


        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcelCode", UNSET))


        def _parse_parcel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parcel_id_type_0 = UUID(data)



                return parcel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parcel_id = _parse_parcel_id(d.pop("parcelId", UNSET))


        piecework_cost = d.pop("pieceworkCost", UNSET)

        def _parse_piecework_quantities(data: object) -> list[ReportLaborCostQuantityDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                piecework_quantities_type_0 = []
                _piecework_quantities_type_0 = data
                for piecework_quantities_type_0_item_data in (_piecework_quantities_type_0):
                    piecework_quantities_type_0_item = ReportLaborCostQuantityDto.from_dict(piecework_quantities_type_0_item_data)



                    piecework_quantities_type_0.append(piecework_quantities_type_0_item)

                return piecework_quantities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportLaborCostQuantityDto] | None | Unset, data)

        piecework_quantities = _parse_piecework_quantities(d.pop("pieceworkQuantities", UNSET))


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


        def _parse_season_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        season_name = _parse_season_name(d.pop("seasonName", UNSET))


        time_cost = d.pop("timeCost", UNSET)

        total_cost = d.pop("totalCost", UNSET)

        work_units = d.pop("workUnits", UNSET)

        worker_count = d.pop("workerCount", UNSET)

        def _parse_yield_kg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        yield_kg = _parse_yield_kg(d.pop("yieldKg", UNSET))


        report_labor_cost_row_dto = cls(
            cost_per_kg=cost_per_kg,
            crop_name=crop_name,
            parcel_code=parcel_code,
            parcel_id=parcel_id,
            piecework_cost=piecework_cost,
            piecework_quantities=piecework_quantities,
            season_id=season_id,
            season_name=season_name,
            time_cost=time_cost,
            total_cost=total_cost,
            work_units=work_units,
            worker_count=worker_count,
            yield_kg=yield_kg,
        )

        return report_labor_cost_row_dto


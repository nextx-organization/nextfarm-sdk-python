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
  from ..models.harvest_dataset_row_dims_type_0 import HarvestDatasetRowDimsType0
  from ..models.harvest_dataset_row_values_type_0 import HarvestDatasetRowValuesType0





T = TypeVar("T", bound="HarvestDatasetRow")



@_attrs_define
class HarvestDatasetRow:
    

    date: datetime.date | None | Unset = UNSET
    dims: HarvestDatasetRowDimsType0 | None | Unset = UNSET
    id: None | str | Unset = UNSET
    values: HarvestDatasetRowValuesType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_dataset_row_dims_type_0 import HarvestDatasetRowDimsType0 # noqa: PLC0415
        from ..models.harvest_dataset_row_values_type_0 import HarvestDatasetRowValuesType0 # noqa: PLC0415
        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        dims: dict[str, Any] | None | Unset
        if isinstance(self.dims, Unset):
            dims = UNSET
        elif isinstance(self.dims, HarvestDatasetRowDimsType0):
            dims = self.dims.to_dict()
        else:
            dims = self.dims

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        values: dict[str, Any] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, HarvestDatasetRowValuesType0):
            values = self.values.to_dict()
        else:
            values = self.values


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if dims is not UNSET:
            field_dict["dims"] = dims
        if id is not UNSET:
            field_dict["id"] = id
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_dataset_row_dims_type_0 import HarvestDatasetRowDimsType0 # noqa: PLC0415
        from ..models.harvest_dataset_row_values_type_0 import HarvestDatasetRowValuesType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.date.fromisoformat(data)



                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        def _parse_dims(data: object) -> HarvestDatasetRowDimsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dims_type_0 = HarvestDatasetRowDimsType0.from_dict(data)



                return dims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HarvestDatasetRowDimsType0 | None | Unset, data)

        dims = _parse_dims(d.pop("dims", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_values(data: object) -> HarvestDatasetRowValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                values_type_0 = HarvestDatasetRowValuesType0.from_dict(data)



                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HarvestDatasetRowValuesType0 | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))


        harvest_dataset_row = cls(
            date=date,
            dims=dims,
            id=id,
            values=values,
        )

        return harvest_dataset_row


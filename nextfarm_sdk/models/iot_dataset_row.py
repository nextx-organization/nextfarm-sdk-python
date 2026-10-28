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
  from ..models.iot_dataset_row_dims_type_0 import IotDatasetRowDimsType0
  from ..models.iot_dataset_row_values_type_0 import IotDatasetRowValuesType0





T = TypeVar("T", bound="IotDatasetRow")



@_attrs_define
class IotDatasetRow:
    

    date: datetime.date | None | Unset = UNSET
    dims: IotDatasetRowDimsType0 | None | Unset = UNSET
    id: None | str | Unset = UNSET
    values: IotDatasetRowValuesType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_dataset_row_dims_type_0 import IotDatasetRowDimsType0 # noqa: PLC0415
        from ..models.iot_dataset_row_values_type_0 import IotDatasetRowValuesType0 # noqa: PLC0415
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
        elif isinstance(self.dims, IotDatasetRowDimsType0):
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
        elif isinstance(self.values, IotDatasetRowValuesType0):
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
        from ..models.iot_dataset_row_dims_type_0 import IotDatasetRowDimsType0 # noqa: PLC0415
        from ..models.iot_dataset_row_values_type_0 import IotDatasetRowValuesType0 # noqa: PLC0415
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


        def _parse_dims(data: object) -> IotDatasetRowDimsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dims_type_0 = IotDatasetRowDimsType0.from_dict(data)



                return dims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IotDatasetRowDimsType0 | None | Unset, data)

        dims = _parse_dims(d.pop("dims", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_values(data: object) -> IotDatasetRowValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                values_type_0 = IotDatasetRowValuesType0.from_dict(data)



                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IotDatasetRowValuesType0 | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))


        iot_dataset_row = cls(
            date=date,
            dims=dims,
            id=id,
            values=values,
        )

        return iot_dataset_row


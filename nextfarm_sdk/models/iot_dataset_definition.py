from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotDatasetDefinition")



@_attrs_define
class IotDatasetDefinition:
    

    description: None | str | Unset = UNSET
    dims: list[str] | None | Unset = UNSET
    measures: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        dims: list[str] | None | Unset
        if isinstance(self.dims, Unset):
            dims = UNSET
        elif isinstance(self.dims, list):
            dims = self.dims


        else:
            dims = self.dims

        measures: list[str] | None | Unset
        if isinstance(self.measures, Unset):
            measures = UNSET
        elif isinstance(self.measures, list):
            measures = self.measures


        else:
            measures = self.measures

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if dims is not UNSET:
            field_dict["dims"] = dims
        if measures is not UNSET:
            field_dict["measures"] = measures
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_dims(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dims_type_0 = cast(list[str], data)

                return dims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        dims = _parse_dims(d.pop("dims", UNSET))


        def _parse_measures(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                measures_type_0 = cast(list[str], data)

                return measures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        measures = _parse_measures(d.pop("measures", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        iot_dataset_definition = cls(
            description=description,
            dims=dims,
            measures=measures,
            name=name,
        )

        return iot_dataset_definition


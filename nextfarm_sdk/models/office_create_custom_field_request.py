from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeCreateCustomFieldRequest")



@_attrs_define
class OfficeCreateCustomFieldRequest:
    

    config: None | str | Unset = UNSET
    field_type: None | str | Unset = UNSET
    module: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    sort_order: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        config: None | str | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        else:
            config = self.config

        field_type: None | str | Unset
        if isinstance(self.field_type, Unset):
            field_type = UNSET
        else:
            field_type = self.field_type

        module: None | str | Unset
        if isinstance(self.module, Unset):
            module = UNSET
        else:
            module = self.module

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if config is not UNSET:
            field_dict["config"] = config
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if module is not UNSET:
            field_dict["module"] = module
        if name is not UNSET:
            field_dict["name"] = name
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config = _parse_config(d.pop("config", UNSET))


        def _parse_field_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_type = _parse_field_type(d.pop("fieldType", UNSET))


        def _parse_module(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module = _parse_module(d.pop("module", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        office_create_custom_field_request = cls(
            config=config,
            field_type=field_type,
            module=module,
            name=name,
            sort_order=sort_order,
        )

        return office_create_custom_field_request


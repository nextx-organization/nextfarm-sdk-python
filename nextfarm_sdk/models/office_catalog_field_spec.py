from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_catalog_option import OfficeCatalogOption





T = TypeVar("T", bound="OfficeCatalogFieldSpec")



@_attrs_define
class OfficeCatalogFieldSpec:
    

    description: None | str | Unset = UNSET
    input_: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    options: list[OfficeCatalogOption] | None | Unset = UNSET
    options_source: None | str | Unset = UNSET
    required: bool | Unset = UNSET
    type_: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_catalog_option import OfficeCatalogOption # noqa: PLC0415
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        input_: None | str | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)


        else:
            options = self.options

        options_source: None | str | Unset
        if isinstance(self.options_source, Unset):
            options_source = UNSET
        else:
            options_source = self.options_source

        required = self.required

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if input_ is not UNSET:
            field_dict["input"] = input_
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if options_source is not UNSET:
            field_dict["optionsSource"] = options_source
        if required is not UNSET:
            field_dict["required"] = required
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_catalog_option import OfficeCatalogOption # noqa: PLC0415
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_input_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_options(data: object) -> list[OfficeCatalogOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in (_options_type_0):
                    options_type_0_item = OfficeCatalogOption.from_dict(options_type_0_item_data)



                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCatalogOption] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        def _parse_options_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        options_source = _parse_options_source(d.pop("optionsSource", UNSET))


        required = d.pop("required", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        office_catalog_field_spec = cls(
            description=description,
            input_=input_,
            label=label,
            name=name,
            options=options,
            options_source=options_source,
            required=required,
            type_=type_,
        )

        return office_catalog_field_spec


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_catalog_field_spec import OfficeCatalogFieldSpec





T = TypeVar("T", bound="OfficeCatalogEntry")



@_attrs_define
class OfficeCatalogEntry:
    

    config_fields: list[OfficeCatalogFieldSpec] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_catalog_field_spec import OfficeCatalogFieldSpec # noqa: PLC0415
        config_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.config_fields, Unset):
            config_fields = UNSET
        elif isinstance(self.config_fields, list):
            config_fields = []
            for config_fields_type_0_item_data in self.config_fields:
                config_fields_type_0_item = config_fields_type_0_item_data.to_dict()
                config_fields.append(config_fields_type_0_item)


        else:
            config_fields = self.config_fields

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if config_fields is not UNSET:
            field_dict["configFields"] = config_fields
        if description is not UNSET:
            field_dict["description"] = description
        if group is not UNSET:
            field_dict["group"] = group
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_catalog_field_spec import OfficeCatalogFieldSpec # noqa: PLC0415
        d = dict(src_dict)
        def _parse_config_fields(data: object) -> list[OfficeCatalogFieldSpec] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                config_fields_type_0 = []
                _config_fields_type_0 = data
                for config_fields_type_0_item_data in (_config_fields_type_0):
                    config_fields_type_0_item = OfficeCatalogFieldSpec.from_dict(config_fields_type_0_item_data)



                    config_fields_type_0.append(config_fields_type_0_item)

                return config_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCatalogFieldSpec] | None | Unset, data)

        config_fields = _parse_config_fields(d.pop("configFields", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        office_catalog_entry = cls(
            config_fields=config_fields,
            description=description,
            group=group,
            label=label,
            type_=type_,
        )

        return office_catalog_entry


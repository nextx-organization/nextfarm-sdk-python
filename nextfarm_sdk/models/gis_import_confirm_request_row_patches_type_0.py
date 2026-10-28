from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.gis_import_confirm_request_row_patches_type_0_additional_property import GisImportConfirmRequestRowPatchesType0AdditionalProperty





T = TypeVar("T", bound="GisImportConfirmRequestRowPatchesType0")



@_attrs_define
class GisImportConfirmRequestRowPatchesType0:
    

    additional_properties: dict[str, GisImportConfirmRequestRowPatchesType0AdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_import_confirm_request_row_patches_type_0_additional_property import GisImportConfirmRequestRowPatchesType0AdditionalProperty # noqa: PLC0415
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_import_confirm_request_row_patches_type_0_additional_property import GisImportConfirmRequestRowPatchesType0AdditionalProperty # noqa: PLC0415
        d = dict(src_dict)
        gis_import_confirm_request_row_patches_type_0 = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GisImportConfirmRequestRowPatchesType0AdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        gis_import_confirm_request_row_patches_type_0.additional_properties = additional_properties
        return gis_import_confirm_request_row_patches_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GisImportConfirmRequestRowPatchesType0AdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GisImportConfirmRequestRowPatchesType0AdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

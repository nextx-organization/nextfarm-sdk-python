from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_print_field_group_dto import OfficePrintFieldGroupDto
  from ..models.office_print_variable_catalog_dto_sample_data_type_0 import OfficePrintVariableCatalogDtoSampleDataType0
  from ..models.office_print_variable_catalog_dto_var_labels_type_0 import OfficePrintVariableCatalogDtoVarLabelsType0
  from ..models.office_print_variable_catalog_dto_var_types_type_0 import OfficePrintVariableCatalogDtoVarTypesType0





T = TypeVar("T", bound="OfficePrintVariableCatalogDto")



@_attrs_define
class OfficePrintVariableCatalogDto:
    

    document_type: None | str | Unset = UNSET
    field_groups: list[OfficePrintFieldGroupDto] | None | Unset = UNSET
    sample_data: None | OfficePrintVariableCatalogDtoSampleDataType0 | Unset = UNSET
    var_labels: None | OfficePrintVariableCatalogDtoVarLabelsType0 | Unset = UNSET
    var_types: None | OfficePrintVariableCatalogDtoVarTypesType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_print_field_group_dto import OfficePrintFieldGroupDto # noqa: PLC0415
        from ..models.office_print_variable_catalog_dto_sample_data_type_0 import OfficePrintVariableCatalogDtoSampleDataType0 # noqa: PLC0415
        from ..models.office_print_variable_catalog_dto_var_labels_type_0 import OfficePrintVariableCatalogDtoVarLabelsType0 # noqa: PLC0415
        from ..models.office_print_variable_catalog_dto_var_types_type_0 import OfficePrintVariableCatalogDtoVarTypesType0 # noqa: PLC0415
        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        field_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.field_groups, Unset):
            field_groups = UNSET
        elif isinstance(self.field_groups, list):
            field_groups = []
            for field_groups_type_0_item_data in self.field_groups:
                field_groups_type_0_item = field_groups_type_0_item_data.to_dict()
                field_groups.append(field_groups_type_0_item)


        else:
            field_groups = self.field_groups

        sample_data: dict[str, Any] | None | Unset
        if isinstance(self.sample_data, Unset):
            sample_data = UNSET
        elif isinstance(self.sample_data, OfficePrintVariableCatalogDtoSampleDataType0):
            sample_data = self.sample_data.to_dict()
        else:
            sample_data = self.sample_data

        var_labels: dict[str, Any] | None | Unset
        if isinstance(self.var_labels, Unset):
            var_labels = UNSET
        elif isinstance(self.var_labels, OfficePrintVariableCatalogDtoVarLabelsType0):
            var_labels = self.var_labels.to_dict()
        else:
            var_labels = self.var_labels

        var_types: dict[str, Any] | None | Unset
        if isinstance(self.var_types, Unset):
            var_types = UNSET
        elif isinstance(self.var_types, OfficePrintVariableCatalogDtoVarTypesType0):
            var_types = self.var_types.to_dict()
        else:
            var_types = self.var_types


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if field_groups is not UNSET:
            field_dict["fieldGroups"] = field_groups
        if sample_data is not UNSET:
            field_dict["sampleData"] = sample_data
        if var_labels is not UNSET:
            field_dict["varLabels"] = var_labels
        if var_types is not UNSET:
            field_dict["varTypes"] = var_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_print_field_group_dto import OfficePrintFieldGroupDto # noqa: PLC0415
        from ..models.office_print_variable_catalog_dto_sample_data_type_0 import OfficePrintVariableCatalogDtoSampleDataType0 # noqa: PLC0415
        from ..models.office_print_variable_catalog_dto_var_labels_type_0 import OfficePrintVariableCatalogDtoVarLabelsType0 # noqa: PLC0415
        from ..models.office_print_variable_catalog_dto_var_types_type_0 import OfficePrintVariableCatalogDtoVarTypesType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type = _parse_document_type(d.pop("documentType", UNSET))


        def _parse_field_groups(data: object) -> list[OfficePrintFieldGroupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_groups_type_0 = []
                _field_groups_type_0 = data
                for field_groups_type_0_item_data in (_field_groups_type_0):
                    field_groups_type_0_item = OfficePrintFieldGroupDto.from_dict(field_groups_type_0_item_data)



                    field_groups_type_0.append(field_groups_type_0_item)

                return field_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficePrintFieldGroupDto] | None | Unset, data)

        field_groups = _parse_field_groups(d.pop("fieldGroups", UNSET))


        def _parse_sample_data(data: object) -> None | OfficePrintVariableCatalogDtoSampleDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sample_data_type_0 = OfficePrintVariableCatalogDtoSampleDataType0.from_dict(data)



                return sample_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficePrintVariableCatalogDtoSampleDataType0 | Unset, data)

        sample_data = _parse_sample_data(d.pop("sampleData", UNSET))


        def _parse_var_labels(data: object) -> None | OfficePrintVariableCatalogDtoVarLabelsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                var_labels_type_0 = OfficePrintVariableCatalogDtoVarLabelsType0.from_dict(data)



                return var_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficePrintVariableCatalogDtoVarLabelsType0 | Unset, data)

        var_labels = _parse_var_labels(d.pop("varLabels", UNSET))


        def _parse_var_types(data: object) -> None | OfficePrintVariableCatalogDtoVarTypesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                var_types_type_0 = OfficePrintVariableCatalogDtoVarTypesType0.from_dict(data)



                return var_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficePrintVariableCatalogDtoVarTypesType0 | Unset, data)

        var_types = _parse_var_types(d.pop("varTypes", UNSET))


        office_print_variable_catalog_dto = cls(
            document_type=document_type,
            field_groups=field_groups,
            sample_data=sample_data,
            var_labels=var_labels,
            var_types=var_types,
        )

        return office_print_variable_catalog_dto


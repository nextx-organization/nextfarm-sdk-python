from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeDocumentRegistersControllerUpdateRegisterRequest")



@_attrs_define
class OfficeDocumentRegistersControllerUpdateRegisterRequest:
    

    document_type_code: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    org_abbreviation: None | str | Unset = UNSET
    register_name: None | str | Unset = UNSET
    symbol_pattern: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_type_code: None | str | Unset
        if isinstance(self.document_type_code, Unset):
            document_type_code = UNSET
        else:
            document_type_code = self.document_type_code

        is_active = self.is_active

        org_abbreviation: None | str | Unset
        if isinstance(self.org_abbreviation, Unset):
            org_abbreviation = UNSET
        else:
            org_abbreviation = self.org_abbreviation

        register_name: None | str | Unset
        if isinstance(self.register_name, Unset):
            register_name = UNSET
        else:
            register_name = self.register_name

        symbol_pattern: None | str | Unset
        if isinstance(self.symbol_pattern, Unset):
            symbol_pattern = UNSET
        else:
            symbol_pattern = self.symbol_pattern


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if document_type_code is not UNSET:
            field_dict["documentTypeCode"] = document_type_code
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if org_abbreviation is not UNSET:
            field_dict["orgAbbreviation"] = org_abbreviation
        if register_name is not UNSET:
            field_dict["registerName"] = register_name
        if symbol_pattern is not UNSET:
            field_dict["symbolPattern"] = symbol_pattern

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_document_type_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type_code = _parse_document_type_code(d.pop("documentTypeCode", UNSET))


        is_active = d.pop("isActive", UNSET)

        def _parse_org_abbreviation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_abbreviation = _parse_org_abbreviation(d.pop("orgAbbreviation", UNSET))


        def _parse_register_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        register_name = _parse_register_name(d.pop("registerName", UNSET))


        def _parse_symbol_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol_pattern = _parse_symbol_pattern(d.pop("symbolPattern", UNSET))


        office_document_registers_controller_update_register_request = cls(
            document_type_code=document_type_code,
            is_active=is_active,
            org_abbreviation=org_abbreviation,
            register_name=register_name,
            symbol_pattern=symbol_pattern,
        )

        return office_document_registers_controller_update_register_request


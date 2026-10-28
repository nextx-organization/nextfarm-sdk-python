from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_document_registers_controller_seed_registers_request_current_numbers_type_0 import OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0





T = TypeVar("T", bound="OfficeDocumentRegistersControllerSeedRegistersRequest")



@_attrs_define
class OfficeDocumentRegistersControllerSeedRegistersRequest:
    

    current_numbers: None | OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0 | Unset = UNSET
    org_abbreviation: None | str | Unset = UNSET
    year: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_document_registers_controller_seed_registers_request_current_numbers_type_0 import OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0 # noqa: PLC0415
        current_numbers: dict[str, Any] | None | Unset
        if isinstance(self.current_numbers, Unset):
            current_numbers = UNSET
        elif isinstance(self.current_numbers, OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0):
            current_numbers = self.current_numbers.to_dict()
        else:
            current_numbers = self.current_numbers

        org_abbreviation: None | str | Unset
        if isinstance(self.org_abbreviation, Unset):
            org_abbreviation = UNSET
        else:
            org_abbreviation = self.org_abbreviation

        year = self.year


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current_numbers is not UNSET:
            field_dict["currentNumbers"] = current_numbers
        if org_abbreviation is not UNSET:
            field_dict["orgAbbreviation"] = org_abbreviation
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_document_registers_controller_seed_registers_request_current_numbers_type_0 import OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_current_numbers(data: object) -> None | OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_numbers_type_0 = OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0.from_dict(data)



                return current_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeDocumentRegistersControllerSeedRegistersRequestCurrentNumbersType0 | Unset, data)

        current_numbers = _parse_current_numbers(d.pop("currentNumbers", UNSET))


        def _parse_org_abbreviation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_abbreviation = _parse_org_abbreviation(d.pop("orgAbbreviation", UNSET))


        year = d.pop("year", UNSET)

        office_document_registers_controller_seed_registers_request = cls(
            current_numbers=current_numbers,
            org_abbreviation=org_abbreviation,
            year=year,
        )

        return office_document_registers_controller_seed_registers_request


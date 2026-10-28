from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeOfficeEntitlementsResponse")



@_attrs_define
class OfficeOfficeEntitlementsResponse:
    

    configured: bool | Unset = UNSET
    disabled_modules: list[str] | None | Unset = UNSET
    known_modules: list[str] | None | Unset = UNSET
    modules: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        disabled_modules: list[str] | None | Unset
        if isinstance(self.disabled_modules, Unset):
            disabled_modules = UNSET
        elif isinstance(self.disabled_modules, list):
            disabled_modules = self.disabled_modules


        else:
            disabled_modules = self.disabled_modules

        known_modules: list[str] | None | Unset
        if isinstance(self.known_modules, Unset):
            known_modules = UNSET
        elif isinstance(self.known_modules, list):
            known_modules = self.known_modules


        else:
            known_modules = self.known_modules

        modules: list[str] | None | Unset
        if isinstance(self.modules, Unset):
            modules = UNSET
        elif isinstance(self.modules, list):
            modules = self.modules


        else:
            modules = self.modules


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if configured is not UNSET:
            field_dict["configured"] = configured
        if disabled_modules is not UNSET:
            field_dict["disabledModules"] = disabled_modules
        if known_modules is not UNSET:
            field_dict["knownModules"] = known_modules
        if modules is not UNSET:
            field_dict["modules"] = modules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configured = d.pop("configured", UNSET)

        def _parse_disabled_modules(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disabled_modules_type_0 = cast(list[str], data)

                return disabled_modules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        disabled_modules = _parse_disabled_modules(d.pop("disabledModules", UNSET))


        def _parse_known_modules(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                known_modules_type_0 = cast(list[str], data)

                return known_modules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        known_modules = _parse_known_modules(d.pop("knownModules", UNSET))


        def _parse_modules(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modules_type_0 = cast(list[str], data)

                return modules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        modules = _parse_modules(d.pop("modules", UNSET))


        office_office_entitlements_response = cls(
            configured=configured,
            disabled_modules=disabled_modules,
            known_modules=known_modules,
            modules=modules,
        )

        return office_office_entitlements_response


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficePrintFieldGroupDto")



@_attrs_define
class OfficePrintFieldGroupDto:
    

    key: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    vars_: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        vars_: list[str] | None | Unset
        if isinstance(self.vars_, Unset):
            vars_ = UNSET
        elif isinstance(self.vars_, list):
            vars_ = self.vars_


        else:
            vars_ = self.vars_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if vars_ is not UNSET:
            field_dict["vars"] = vars_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_vars_(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                vars_type_0 = cast(list[str], data)

                return vars_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        vars_ = _parse_vars_(d.pop("vars", UNSET))


        office_print_field_group_dto = cls(
            key=key,
            label=label,
            vars_=vars_,
        )

        return office_print_field_group_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAutomationDiagnosisCheckDto")



@_attrs_define
class OfficeAutomationDiagnosisCheckDto:
    

    blocking: bool | Unset = UNSET
    code: None | str | Unset = UNSET
    detail: None | str | Unset = UNSET
    ok: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        blocking = self.blocking

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if blocking is not UNSET:
            field_dict["blocking"] = blocking
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail
        if ok is not UNSET:
            field_dict["ok"] = ok

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blocking = d.pop("blocking", UNSET)

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        ok = d.pop("ok", UNSET)

        office_automation_diagnosis_check_dto = cls(
            blocking=blocking,
            code=code,
            detail=detail,
            ok=ok,
        )

        return office_automation_diagnosis_check_dto


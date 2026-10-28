from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeTaskWarningDto")



@_attrs_define
class OfficeTaskWarningDto:
    

    args: list[str] | None | Unset = UNSET
    code: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    message_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        args: list[str] | None | Unset
        if isinstance(self.args, Unset):
            args = UNSET
        elif isinstance(self.args, list):
            args = self.args


        else:
            args = self.args

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        message_key: None | str | Unset
        if isinstance(self.message_key, Unset):
            message_key = UNSET
        else:
            message_key = self.message_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if args is not UNSET:
            field_dict["args"] = args
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if message_key is not UNSET:
            field_dict["messageKey"] = message_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_args(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                args_type_0 = cast(list[str], data)

                return args_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        args = _parse_args(d.pop("args", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        def _parse_message_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_key = _parse_message_key(d.pop("messageKey", UNSET))


        office_task_warning_dto = cls(
            args=args,
            code=code,
            message=message,
            message_key=message_key,
        )

        return office_task_warning_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotSetupStepDto")



@_attrs_define
class IotSetupStepDto:
    

    count: int | None | Unset = UNSET
    detail: None | str | Unset = UNSET
    done: bool | Unset = UNSET
    key: None | str | Unset = UNSET
    warning: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        done = self.done

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        warning: None | str | Unset
        if isinstance(self.warning, Unset):
            warning = UNSET
        else:
            warning = self.warning


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if detail is not UNSET:
            field_dict["detail"] = detail
        if done is not UNSET:
            field_dict["done"] = done
        if key is not UNSET:
            field_dict["key"] = key
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))


        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        done = d.pop("done", UNSET)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        warning = _parse_warning(d.pop("warning", UNSET))


        iot_setup_step_dto = cls(
            count=count,
            detail=detail,
            done=done,
            key=key,
            warning=warning,
        )

        return iot_setup_step_dto


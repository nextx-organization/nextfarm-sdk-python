from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_service_event_key_dto import OfficeServiceEventKeyDto





T = TypeVar("T", bound="OfficeServiceEventDto")



@_attrs_define
class OfficeServiceEventDto:
    

    code: None | str | Unset = UNSET
    keys: list[OfficeServiceEventKeyDto] | None | Unset = UNSET
    label: None | str | Unset = UNSET
    per_minute_cap: int | Unset = UNSET
    requires_filter: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_service_event_key_dto import OfficeServiceEventKeyDto # noqa: PLC0415
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        keys: list[dict[str, Any]] | None | Unset
        if isinstance(self.keys, Unset):
            keys = UNSET
        elif isinstance(self.keys, list):
            keys = []
            for keys_type_0_item_data in self.keys:
                keys_type_0_item = keys_type_0_item_data.to_dict()
                keys.append(keys_type_0_item)


        else:
            keys = self.keys

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        per_minute_cap = self.per_minute_cap

        requires_filter = self.requires_filter


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if keys is not UNSET:
            field_dict["keys"] = keys
        if label is not UNSET:
            field_dict["label"] = label
        if per_minute_cap is not UNSET:
            field_dict["perMinuteCap"] = per_minute_cap
        if requires_filter is not UNSET:
            field_dict["requiresFilter"] = requires_filter

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_service_event_key_dto import OfficeServiceEventKeyDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_keys(data: object) -> list[OfficeServiceEventKeyDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keys_type_0 = []
                _keys_type_0 = data
                for keys_type_0_item_data in (_keys_type_0):
                    keys_type_0_item = OfficeServiceEventKeyDto.from_dict(keys_type_0_item_data)



                    keys_type_0.append(keys_type_0_item)

                return keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeServiceEventKeyDto] | None | Unset, data)

        keys = _parse_keys(d.pop("keys", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        per_minute_cap = d.pop("perMinuteCap", UNSET)

        requires_filter = d.pop("requiresFilter", UNSET)

        office_service_event_dto = cls(
            code=code,
            keys=keys,
            label=label,
            per_minute_cap=per_minute_cap,
            requires_filter=requires_filter,
        )

        return office_service_event_dto


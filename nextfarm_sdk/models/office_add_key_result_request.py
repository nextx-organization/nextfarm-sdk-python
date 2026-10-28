from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_key_result_source_input import OfficeKeyResultSourceInput





T = TypeVar("T", bound="OfficeAddKeyResultRequest")



@_attrs_define
class OfficeAddKeyResultRequest:
    

    current_value: float | Unset = UNSET
    name: None | str | Unset = UNSET
    source: OfficeKeyResultSourceInput | Unset = UNSET
    start_value: float | Unset = UNSET
    target_value: float | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_key_result_source_input import OfficeKeyResultSourceInput # noqa: PLC0415
        current_value = self.current_value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        start_value = self.start_value

        target_value = self.target_value

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if start_value is not UNSET:
            field_dict["startValue"] = start_value
        if target_value is not UNSET:
            field_dict["targetValue"] = target_value
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_key_result_source_input import OfficeKeyResultSourceInput # noqa: PLC0415
        d = dict(src_dict)
        current_value = d.pop("currentValue", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _source = d.pop("source", UNSET)
        source: OfficeKeyResultSourceInput | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = OfficeKeyResultSourceInput.from_dict(_source)




        start_value = d.pop("startValue", UNSET)

        target_value = d.pop("targetValue", UNSET)

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        office_add_key_result_request = cls(
            current_value=current_value,
            name=name,
            source=source,
            start_value=start_value,
            target_value=target_value,
            unit=unit,
        )

        return office_add_key_result_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_norm_line_input import HarvestNormLineInput
  from ..models.harvest_norm_yield_age_input import HarvestNormYieldAgeInput





T = TypeVar("T", bound="HarvestNormSetRequest")



@_attrs_define
class HarvestNormSetRequest:
    

    crop_name: None | str | Unset = UNSET
    lines: list[HarvestNormLineInput] | None | Unset = UNSET
    note: None | str | Unset = UNSET
    yield_by_age: list[HarvestNormYieldAgeInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_norm_line_input import HarvestNormLineInput # noqa: PLC0415
        from ..models.harvest_norm_yield_age_input import HarvestNormYieldAgeInput # noqa: PLC0415
        crop_name: None | str | Unset
        if isinstance(self.crop_name, Unset):
            crop_name = UNSET
        else:
            crop_name = self.crop_name

        lines: list[dict[str, Any]] | None | Unset
        if isinstance(self.lines, Unset):
            lines = UNSET
        elif isinstance(self.lines, list):
            lines = []
            for lines_type_0_item_data in self.lines:
                lines_type_0_item = lines_type_0_item_data.to_dict()
                lines.append(lines_type_0_item)


        else:
            lines = self.lines

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        yield_by_age: list[dict[str, Any]] | None | Unset
        if isinstance(self.yield_by_age, Unset):
            yield_by_age = UNSET
        elif isinstance(self.yield_by_age, list):
            yield_by_age = []
            for yield_by_age_type_0_item_data in self.yield_by_age:
                yield_by_age_type_0_item = yield_by_age_type_0_item_data.to_dict()
                yield_by_age.append(yield_by_age_type_0_item)


        else:
            yield_by_age = self.yield_by_age


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_name is not UNSET:
            field_dict["crop_name"] = crop_name
        if lines is not UNSET:
            field_dict["lines"] = lines
        if note is not UNSET:
            field_dict["note"] = note
        if yield_by_age is not UNSET:
            field_dict["yield_by_age"] = yield_by_age

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_norm_line_input import HarvestNormLineInput # noqa: PLC0415
        from ..models.harvest_norm_yield_age_input import HarvestNormYieldAgeInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_crop_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_name = _parse_crop_name(d.pop("crop_name", UNSET))


        def _parse_lines(data: object) -> list[HarvestNormLineInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lines_type_0 = []
                _lines_type_0 = data
                for lines_type_0_item_data in (_lines_type_0):
                    lines_type_0_item = HarvestNormLineInput.from_dict(lines_type_0_item_data)



                    lines_type_0.append(lines_type_0_item)

                return lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestNormLineInput] | None | Unset, data)

        lines = _parse_lines(d.pop("lines", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_yield_by_age(data: object) -> list[HarvestNormYieldAgeInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                yield_by_age_type_0 = []
                _yield_by_age_type_0 = data
                for yield_by_age_type_0_item_data in (_yield_by_age_type_0):
                    yield_by_age_type_0_item = HarvestNormYieldAgeInput.from_dict(yield_by_age_type_0_item_data)



                    yield_by_age_type_0.append(yield_by_age_type_0_item)

                return yield_by_age_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestNormYieldAgeInput] | None | Unset, data)

        yield_by_age = _parse_yield_by_age(d.pop("yield_by_age", UNSET))


        harvest_norm_set_request = cls(
            crop_name=crop_name,
            lines=lines,
            note=note,
            yield_by_age=yield_by_age,
        )

        return harvest_norm_set_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_quiz_option_input import OfficeQuizOptionInput





T = TypeVar("T", bound="OfficeQuizQuestionInput")



@_attrs_define
class OfficeQuizQuestionInput:
    

    allow_multiple: bool | Unset = UNSET
    options: list[OfficeQuizOptionInput] | None | Unset = UNSET
    text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_quiz_option_input import OfficeQuizOptionInput # noqa: PLC0415
        allow_multiple = self.allow_multiple

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)


        else:
            options = self.options

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allow_multiple is not UNSET:
            field_dict["allowMultiple"] = allow_multiple
        if options is not UNSET:
            field_dict["options"] = options
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_quiz_option_input import OfficeQuizOptionInput # noqa: PLC0415
        d = dict(src_dict)
        allow_multiple = d.pop("allowMultiple", UNSET)

        def _parse_options(data: object) -> list[OfficeQuizOptionInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in (_options_type_0):
                    options_type_0_item = OfficeQuizOptionInput.from_dict(options_type_0_item_data)



                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeQuizOptionInput] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        office_quiz_question_input = cls(
            allow_multiple=allow_multiple,
            options=options,
            text=text,
        )

        return office_quiz_question_input


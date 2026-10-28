from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_objective_template_key_result_dto import OfficeObjectiveTemplateKeyResultDto





T = TypeVar("T", bound="OfficeObjectiveTemplateDto")



@_attrs_define
class OfficeObjectiveTemplateDto:
    

    category: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    key_results: list[OfficeObjectiveTemplateKeyResultDto] | None | Unset = UNSET
    kind: None | str | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_objective_template_key_result_dto import OfficeObjectiveTemplateKeyResultDto # noqa: PLC0415
        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        key_results: list[dict[str, Any]] | None | Unset
        if isinstance(self.key_results, Unset):
            key_results = UNSET
        elif isinstance(self.key_results, list):
            key_results = []
            for key_results_type_0_item_data in self.key_results:
                key_results_type_0_item = key_results_type_0_item_data.to_dict()
                key_results.append(key_results_type_0_item)


        else:
            key_results = self.key_results

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if key_results is not UNSET:
            field_dict["keyResults"] = key_results
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_objective_template_key_result_dto import OfficeObjectiveTemplateKeyResultDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_key_results(data: object) -> list[OfficeObjectiveTemplateKeyResultDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                key_results_type_0 = []
                _key_results_type_0 = data
                for key_results_type_0_item_data in (_key_results_type_0):
                    key_results_type_0_item = OfficeObjectiveTemplateKeyResultDto.from_dict(key_results_type_0_item_data)



                    key_results_type_0.append(key_results_type_0_item)

                return key_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeObjectiveTemplateKeyResultDto] | None | Unset, data)

        key_results = _parse_key_results(d.pop("keyResults", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_objective_template_dto = cls(
            category=category,
            description=description,
            icon=icon,
            id=id,
            key_results=key_results,
            kind=kind,
            name=name,
        )

        return office_objective_template_dto


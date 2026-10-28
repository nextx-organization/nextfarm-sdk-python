from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GisCareOccurrenceDto")



@_attrs_define
class GisCareOccurrenceDto:
    

    anchor: None | str | Unset = UNSET
    due_on: None | str | Unset = UNSET
    material: None | str | Unset = UNSET
    quantity: float | None | Unset = UNSET
    rule_key: None | str | Unset = UNSET
    task_type: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    trees: int | Unset = UNSET
    unit: None | str | Unset = UNSET
    unknown_age_trees: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        anchor: None | str | Unset
        if isinstance(self.anchor, Unset):
            anchor = UNSET
        else:
            anchor = self.anchor

        due_on: None | str | Unset
        if isinstance(self.due_on, Unset):
            due_on = UNSET
        else:
            due_on = self.due_on

        material: None | str | Unset
        if isinstance(self.material, Unset):
            material = UNSET
        else:
            material = self.material

        quantity: float | None | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        rule_key: None | str | Unset
        if isinstance(self.rule_key, Unset):
            rule_key = UNSET
        else:
            rule_key = self.rule_key

        task_type: None | str | Unset
        if isinstance(self.task_type, Unset):
            task_type = UNSET
        else:
            task_type = self.task_type

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        trees = self.trees

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        unknown_age_trees = self.unknown_age_trees


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor is not UNSET:
            field_dict["anchor"] = anchor
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if material is not UNSET:
            field_dict["material"] = material
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if rule_key is not UNSET:
            field_dict["rule_key"] = rule_key
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if trees is not UNSET:
            field_dict["trees"] = trees
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unknown_age_trees is not UNSET:
            field_dict["unknown_age_trees"] = unknown_age_trees

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_anchor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anchor = _parse_anchor(d.pop("anchor", UNSET))


        def _parse_due_on(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_on = _parse_due_on(d.pop("due_on", UNSET))


        def _parse_material(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        material = _parse_material(d.pop("material", UNSET))


        def _parse_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))


        def _parse_rule_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rule_key = _parse_rule_key(d.pop("rule_key", UNSET))


        def _parse_task_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_type = _parse_task_type(d.pop("task_type", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        trees = d.pop("trees", UNSET)

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        unknown_age_trees = d.pop("unknown_age_trees", UNSET)

        gis_care_occurrence_dto = cls(
            anchor=anchor,
            due_on=due_on,
            material=material,
            quantity=quantity,
            rule_key=rule_key,
            task_type=task_type,
            title=title,
            trees=trees,
            unit=unit,
            unknown_age_trees=unknown_age_trees,
        )

        return gis_care_occurrence_dto


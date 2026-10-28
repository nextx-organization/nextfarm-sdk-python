from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_catalog_entry import OfficeCatalogEntry





T = TypeVar("T", bound="OfficeAutomationCatalogSnapshot")



@_attrs_define
class OfficeAutomationCatalogSnapshot:
    

    actions: list[OfficeCatalogEntry] | None | Unset = UNSET
    steps: list[OfficeCatalogEntry] | None | Unset = UNSET
    triggers: list[OfficeCatalogEntry] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_catalog_entry import OfficeCatalogEntry # noqa: PLC0415
        actions: list[dict[str, Any]] | None | Unset
        if isinstance(self.actions, Unset):
            actions = UNSET
        elif isinstance(self.actions, list):
            actions = []
            for actions_type_0_item_data in self.actions:
                actions_type_0_item = actions_type_0_item_data.to_dict()
                actions.append(actions_type_0_item)


        else:
            actions = self.actions

        steps: list[dict[str, Any]] | None | Unset
        if isinstance(self.steps, Unset):
            steps = UNSET
        elif isinstance(self.steps, list):
            steps = []
            for steps_type_0_item_data in self.steps:
                steps_type_0_item = steps_type_0_item_data.to_dict()
                steps.append(steps_type_0_item)


        else:
            steps = self.steps

        triggers: list[dict[str, Any]] | None | Unset
        if isinstance(self.triggers, Unset):
            triggers = UNSET
        elif isinstance(self.triggers, list):
            triggers = []
            for triggers_type_0_item_data in self.triggers:
                triggers_type_0_item = triggers_type_0_item_data.to_dict()
                triggers.append(triggers_type_0_item)


        else:
            triggers = self.triggers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actions is not UNSET:
            field_dict["actions"] = actions
        if steps is not UNSET:
            field_dict["steps"] = steps
        if triggers is not UNSET:
            field_dict["triggers"] = triggers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_catalog_entry import OfficeCatalogEntry # noqa: PLC0415
        d = dict(src_dict)
        def _parse_actions(data: object) -> list[OfficeCatalogEntry] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actions_type_0 = []
                _actions_type_0 = data
                for actions_type_0_item_data in (_actions_type_0):
                    actions_type_0_item = OfficeCatalogEntry.from_dict(actions_type_0_item_data)



                    actions_type_0.append(actions_type_0_item)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCatalogEntry] | None | Unset, data)

        actions = _parse_actions(d.pop("actions", UNSET))


        def _parse_steps(data: object) -> list[OfficeCatalogEntry] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                steps_type_0 = []
                _steps_type_0 = data
                for steps_type_0_item_data in (_steps_type_0):
                    steps_type_0_item = OfficeCatalogEntry.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCatalogEntry] | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))


        def _parse_triggers(data: object) -> list[OfficeCatalogEntry] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                triggers_type_0 = []
                _triggers_type_0 = data
                for triggers_type_0_item_data in (_triggers_type_0):
                    triggers_type_0_item = OfficeCatalogEntry.from_dict(triggers_type_0_item_data)



                    triggers_type_0.append(triggers_type_0_item)

                return triggers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCatalogEntry] | None | Unset, data)

        triggers = _parse_triggers(d.pop("triggers", UNSET))


        office_automation_catalog_snapshot = cls(
            actions=actions,
            steps=steps,
            triggers=triggers,
        )

        return office_automation_catalog_snapshot


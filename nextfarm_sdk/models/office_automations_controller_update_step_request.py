from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAutomationsControllerUpdateStepRequest")



@_attrs_define
class OfficeAutomationsControllerUpdateStepRequest:
    

    action_type: None | str | Unset = UNSET
    condition_config: None | str | Unset = UNSET
    config: None | str | Unset = UNSET
    false_next_step_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    split_ratio: int | None | Unset = UNSET
    true_next_step_id: None | Unset | UUID = UNSET
    wait_config: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action_type: None | str | Unset
        if isinstance(self.action_type, Unset):
            action_type = UNSET
        else:
            action_type = self.action_type

        condition_config: None | str | Unset
        if isinstance(self.condition_config, Unset):
            condition_config = UNSET
        else:
            condition_config = self.condition_config

        config: None | str | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        else:
            config = self.config

        false_next_step_id: None | str | Unset
        if isinstance(self.false_next_step_id, Unset):
            false_next_step_id = UNSET
        elif isinstance(self.false_next_step_id, UUID):
            false_next_step_id = str(self.false_next_step_id)
        else:
            false_next_step_id = self.false_next_step_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        split_ratio: int | None | Unset
        if isinstance(self.split_ratio, Unset):
            split_ratio = UNSET
        else:
            split_ratio = self.split_ratio

        true_next_step_id: None | str | Unset
        if isinstance(self.true_next_step_id, Unset):
            true_next_step_id = UNSET
        elif isinstance(self.true_next_step_id, UUID):
            true_next_step_id = str(self.true_next_step_id)
        else:
            true_next_step_id = self.true_next_step_id

        wait_config: None | str | Unset
        if isinstance(self.wait_config, Unset):
            wait_config = UNSET
        else:
            wait_config = self.wait_config


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if condition_config is not UNSET:
            field_dict["conditionConfig"] = condition_config
        if config is not UNSET:
            field_dict["config"] = config
        if false_next_step_id is not UNSET:
            field_dict["falseNextStepId"] = false_next_step_id
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if split_ratio is not UNSET:
            field_dict["splitRatio"] = split_ratio
        if true_next_step_id is not UNSET:
            field_dict["trueNextStepId"] = true_next_step_id
        if wait_config is not UNSET:
            field_dict["waitConfig"] = wait_config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_action_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_type = _parse_action_type(d.pop("actionType", UNSET))


        def _parse_condition_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition_config = _parse_condition_config(d.pop("conditionConfig", UNSET))


        def _parse_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config = _parse_config(d.pop("config", UNSET))


        def _parse_false_next_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                false_next_step_id_type_0 = UUID(data)



                return false_next_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        false_next_step_id = _parse_false_next_step_id(d.pop("falseNextStepId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_split_ratio(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        split_ratio = _parse_split_ratio(d.pop("splitRatio", UNSET))


        def _parse_true_next_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                true_next_step_id_type_0 = UUID(data)



                return true_next_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        true_next_step_id = _parse_true_next_step_id(d.pop("trueNextStepId", UNSET))


        def _parse_wait_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wait_config = _parse_wait_config(d.pop("waitConfig", UNSET))


        office_automations_controller_update_step_request = cls(
            action_type=action_type,
            condition_config=condition_config,
            config=config,
            false_next_step_id=false_next_step_id,
            name=name,
            source=source,
            split_ratio=split_ratio,
            true_next_step_id=true_next_step_id,
            wait_config=wait_config,
        )

        return office_automations_controller_update_step_request


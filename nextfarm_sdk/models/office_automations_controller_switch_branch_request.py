from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAutomationsControllerSwitchBranchRequest")



@_attrs_define
class OfficeAutomationsControllerSwitchBranchRequest:
    

    condition_config: Any | Unset = UNSET
    label: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        condition_config = self.condition_config

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if condition_config is not UNSET:
            field_dict["conditionConfig"] = condition_config
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition_config = d.pop("conditionConfig", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        office_automations_controller_switch_branch_request = cls(
            condition_config=condition_config,
            label=label,
        )

        return office_automations_controller_switch_branch_request


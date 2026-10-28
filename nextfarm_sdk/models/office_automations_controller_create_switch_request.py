from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_automations_controller_switch_branch_request import OfficeAutomationsControllerSwitchBranchRequest





T = TypeVar("T", bound="OfficeAutomationsControllerCreateSwitchRequest")



@_attrs_define
class OfficeAutomationsControllerCreateSwitchRequest:
    

    after_step_id: None | Unset | UUID = UNSET
    branch_step_id: None | Unset | UUID = UNSET
    branches: list[OfficeAutomationsControllerSwitchBranchRequest] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    true_branch: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automations_controller_switch_branch_request import OfficeAutomationsControllerSwitchBranchRequest # noqa: PLC0415
        after_step_id: None | str | Unset
        if isinstance(self.after_step_id, Unset):
            after_step_id = UNSET
        elif isinstance(self.after_step_id, UUID):
            after_step_id = str(self.after_step_id)
        else:
            after_step_id = self.after_step_id

        branch_step_id: None | str | Unset
        if isinstance(self.branch_step_id, Unset):
            branch_step_id = UNSET
        elif isinstance(self.branch_step_id, UUID):
            branch_step_id = str(self.branch_step_id)
        else:
            branch_step_id = self.branch_step_id

        branches: list[dict[str, Any]] | None | Unset
        if isinstance(self.branches, Unset):
            branches = UNSET
        elif isinstance(self.branches, list):
            branches = []
            for branches_type_0_item_data in self.branches:
                branches_type_0_item = branches_type_0_item_data.to_dict()
                branches.append(branches_type_0_item)


        else:
            branches = self.branches

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        true_branch: bool | None | Unset
        if isinstance(self.true_branch, Unset):
            true_branch = UNSET
        else:
            true_branch = self.true_branch


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if after_step_id is not UNSET:
            field_dict["afterStepId"] = after_step_id
        if branch_step_id is not UNSET:
            field_dict["branchStepId"] = branch_step_id
        if branches is not UNSET:
            field_dict["branches"] = branches
        if name is not UNSET:
            field_dict["name"] = name
        if true_branch is not UNSET:
            field_dict["trueBranch"] = true_branch

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automations_controller_switch_branch_request import OfficeAutomationsControllerSwitchBranchRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_after_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                after_step_id_type_0 = UUID(data)



                return after_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        after_step_id = _parse_after_step_id(d.pop("afterStepId", UNSET))


        def _parse_branch_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_step_id_type_0 = UUID(data)



                return branch_step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_step_id = _parse_branch_step_id(d.pop("branchStepId", UNSET))


        def _parse_branches(data: object) -> list[OfficeAutomationsControllerSwitchBranchRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                branches_type_0 = []
                _branches_type_0 = data
                for branches_type_0_item_data in (_branches_type_0):
                    branches_type_0_item = OfficeAutomationsControllerSwitchBranchRequest.from_dict(branches_type_0_item_data)



                    branches_type_0.append(branches_type_0_item)

                return branches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAutomationsControllerSwitchBranchRequest] | None | Unset, data)

        branches = _parse_branches(d.pop("branches", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_true_branch(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        true_branch = _parse_true_branch(d.pop("trueBranch", UNSET))


        office_automations_controller_create_switch_request = cls(
            after_step_id=after_step_id,
            branch_step_id=branch_step_id,
            branches=branches,
            name=name,
            true_branch=true_branch,
        )

        return office_automations_controller_create_switch_request


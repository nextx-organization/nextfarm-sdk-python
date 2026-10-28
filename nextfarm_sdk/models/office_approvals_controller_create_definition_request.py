from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_approval_step_input import OfficeApprovalStepInput





T = TypeVar("T", bound="OfficeApprovalsControllerCreateDefinitionRequest")



@_attrs_define
class OfficeApprovalsControllerCreateDefinitionRequest:
    

    code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    execution_mode: None | str | Unset = UNSET
    form_schema: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    steps: list[OfficeApprovalStepInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_approval_step_input import OfficeApprovalStepInput # noqa: PLC0415
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        execution_mode: None | str | Unset
        if isinstance(self.execution_mode, Unset):
            execution_mode = UNSET
        else:
            execution_mode = self.execution_mode

        form_schema: None | str | Unset
        if isinstance(self.form_schema, Unset):
            form_schema = UNSET
        else:
            form_schema = self.form_schema

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if execution_mode is not UNSET:
            field_dict["executionMode"] = execution_mode
        if form_schema is not UNSET:
            field_dict["formSchema"] = form_schema
        if name is not UNSET:
            field_dict["name"] = name
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_approval_step_input import OfficeApprovalStepInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_execution_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_mode = _parse_execution_mode(d.pop("executionMode", UNSET))


        def _parse_form_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_schema = _parse_form_schema(d.pop("formSchema", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_steps(data: object) -> list[OfficeApprovalStepInput] | None | Unset:
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
                    steps_type_0_item = OfficeApprovalStepInput.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeApprovalStepInput] | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))


        office_approvals_controller_create_definition_request = cls(
            code=code,
            description=description,
            execution_mode=execution_mode,
            form_schema=form_schema,
            name=name,
            steps=steps,
        )

        return office_approvals_controller_create_definition_request


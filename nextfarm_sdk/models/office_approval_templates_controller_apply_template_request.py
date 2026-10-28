from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_approval_templates_controller_apply_template_request_step_approvers_type_0 import OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0





T = TypeVar("T", bound="OfficeApprovalTemplatesControllerApplyTemplateRequest")



@_attrs_define
class OfficeApprovalTemplatesControllerApplyTemplateRequest:
    

    definition_code: None | str | Unset = UNSET
    step_approvers: None | OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_approval_templates_controller_apply_template_request_step_approvers_type_0 import OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0 # noqa: PLC0415
        definition_code: None | str | Unset
        if isinstance(self.definition_code, Unset):
            definition_code = UNSET
        else:
            definition_code = self.definition_code

        step_approvers: dict[str, Any] | None | Unset
        if isinstance(self.step_approvers, Unset):
            step_approvers = UNSET
        elif isinstance(self.step_approvers, OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0):
            step_approvers = self.step_approvers.to_dict()
        else:
            step_approvers = self.step_approvers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if definition_code is not UNSET:
            field_dict["definitionCode"] = definition_code
        if step_approvers is not UNSET:
            field_dict["stepApprovers"] = step_approvers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_approval_templates_controller_apply_template_request_step_approvers_type_0 import OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_definition_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        definition_code = _parse_definition_code(d.pop("definitionCode", UNSET))


        def _parse_step_approvers(data: object) -> None | OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                step_approvers_type_0 = OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0.from_dict(data)



                return step_approvers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeApprovalTemplatesControllerApplyTemplateRequestStepApproversType0 | Unset, data)

        step_approvers = _parse_step_approvers(d.pop("stepApprovers", UNSET))


        office_approval_templates_controller_apply_template_request = cls(
            definition_code=definition_code,
            step_approvers=step_approvers,
        )

        return office_approval_templates_controller_apply_template_request


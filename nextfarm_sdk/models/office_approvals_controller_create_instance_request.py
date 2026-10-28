from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_approvals_controller_create_instance_request_free_approvers_type_0 import OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0





T = TypeVar("T", bound="OfficeApprovalsControllerCreateInstanceRequest")



@_attrs_define
class OfficeApprovalsControllerCreateInstanceRequest:
    

    definition_code: None | str | Unset = UNSET
    form_value: None | str | Unset = UNSET
    free_approvers: None | OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_approvals_controller_create_instance_request_free_approvers_type_0 import OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0 # noqa: PLC0415
        definition_code: None | str | Unset
        if isinstance(self.definition_code, Unset):
            definition_code = UNSET
        else:
            definition_code = self.definition_code

        form_value: None | str | Unset
        if isinstance(self.form_value, Unset):
            form_value = UNSET
        else:
            form_value = self.form_value

        free_approvers: dict[str, Any] | None | Unset
        if isinstance(self.free_approvers, Unset):
            free_approvers = UNSET
        elif isinstance(self.free_approvers, OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0):
            free_approvers = self.free_approvers.to_dict()
        else:
            free_approvers = self.free_approvers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if definition_code is not UNSET:
            field_dict["definitionCode"] = definition_code
        if form_value is not UNSET:
            field_dict["formValue"] = form_value
        if free_approvers is not UNSET:
            field_dict["freeApprovers"] = free_approvers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_approvals_controller_create_instance_request_free_approvers_type_0 import OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_definition_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        definition_code = _parse_definition_code(d.pop("definitionCode", UNSET))


        def _parse_form_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_value = _parse_form_value(d.pop("formValue", UNSET))


        def _parse_free_approvers(data: object) -> None | OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                free_approvers_type_0 = OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0.from_dict(data)



                return free_approvers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeApprovalsControllerCreateInstanceRequestFreeApproversType0 | Unset, data)

        free_approvers = _parse_free_approvers(d.pop("freeApprovers", UNSET))


        office_approvals_controller_create_instance_request = cls(
            definition_code=definition_code,
            form_value=form_value,
            free_approvers=free_approvers,
        )

        return office_approvals_controller_create_instance_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeWebhookTriggerResultDto")



@_attrs_define
class OfficeWebhookTriggerResultDto:
    

    accepted: bool | Unset = UNSET
    enrollment_id: None | Unset | UUID = UNSET
    reason: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        enrollment_id: None | str | Unset
        if isinstance(self.enrollment_id, Unset):
            enrollment_id = UNSET
        elif isinstance(self.enrollment_id, UUID):
            enrollment_id = str(self.enrollment_id)
        else:
            enrollment_id = self.enrollment_id

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if enrollment_id is not UNSET:
            field_dict["enrollmentId"] = enrollment_id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted", UNSET)

        def _parse_enrollment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrollment_id_type_0 = UUID(data)



                return enrollment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        enrollment_id = _parse_enrollment_id(d.pop("enrollmentId", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        office_webhook_trigger_result_dto = cls(
            accepted=accepted,
            enrollment_id=enrollment_id,
            reason=reason,
        )

        return office_webhook_trigger_result_dto


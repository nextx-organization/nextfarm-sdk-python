from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeAutomationsControllerWebhookSampleRequest")



@_attrs_define
class OfficeAutomationsControllerWebhookSampleRequest:
    

    sample: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        sample = self.sample


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if sample is not UNSET:
            field_dict["sample"] = sample

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sample = d.pop("sample", UNSET)

        office_automations_controller_webhook_sample_request = cls(
            sample=sample,
        )

        return office_automations_controller_webhook_sample_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestRenewQrCodeRequest")



@_attrs_define
class HarvestRenewQrCodeRequest:
    

    new_effective_to: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        new_effective_to: str | Unset = UNSET
        if not isinstance(self.new_effective_to, Unset):
            new_effective_to = self.new_effective_to.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if new_effective_to is not UNSET:
            field_dict["new_effective_to"] = new_effective_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _new_effective_to = d.pop("new_effective_to", UNSET)
        new_effective_to: datetime.date | Unset
        if isinstance(_new_effective_to,  Unset):
            new_effective_to = UNSET
        else:
            new_effective_to = datetime.date.fromisoformat(_new_effective_to)




        harvest_renew_qr_code_request = cls(
            new_effective_to=new_effective_to,
        )

        return harvest_renew_qr_code_request


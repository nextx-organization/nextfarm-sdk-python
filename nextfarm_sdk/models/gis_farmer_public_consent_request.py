from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GisFarmerPublicConsentRequest")



@_attrs_define
class GisFarmerPublicConsentRequest:
    

    public_name: bool | Unset = UNSET
    public_phone: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        public_name = self.public_name

        public_phone = self.public_phone


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if public_name is not UNSET:
            field_dict["public_name"] = public_name
        if public_phone is not UNSET:
            field_dict["public_phone"] = public_phone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_name = d.pop("public_name", UNSET)

        public_phone = d.pop("public_phone", UNSET)

        gis_farmer_public_consent_request = cls(
            public_name=public_name,
            public_phone=public_phone,
        )

        return gis_farmer_public_consent_request


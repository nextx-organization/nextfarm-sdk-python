from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest





T = TypeVar("T", bound="HarvestReplantOrganismRequest")



@_attrs_define
class HarvestReplantOrganismRequest:
    

    note: None | str | Unset = UNSET
    profile: HarvestOrganismProfileRequest | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if note is not UNSET:
            field_dict["note"] = note
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        _profile = d.pop("profile", UNSET)
        profile: HarvestOrganismProfileRequest | Unset
        if isinstance(_profile,  Unset):
            profile = UNSET
        else:
            profile = HarvestOrganismProfileRequest.from_dict(_profile)




        harvest_replant_organism_request = cls(
            note=note,
            profile=profile,
        )

        return harvest_replant_organism_request


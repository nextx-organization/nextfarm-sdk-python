from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_phone_directory_person import OfficePhoneDirectoryPerson





T = TypeVar("T", bound="OfficePhoneLookupResultDto")



@_attrs_define
class OfficePhoneLookupResultDto:
    

    cross_workspace: bool | Unset = UNSET
    people: list[OfficePhoneDirectoryPerson] | None | Unset = UNSET
    phone: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_phone_directory_person import OfficePhoneDirectoryPerson # noqa: PLC0415
        cross_workspace = self.cross_workspace

        people: list[dict[str, Any]] | None | Unset
        if isinstance(self.people, Unset):
            people = UNSET
        elif isinstance(self.people, list):
            people = []
            for people_type_0_item_data in self.people:
                people_type_0_item = people_type_0_item_data.to_dict()
                people.append(people_type_0_item)


        else:
            people = self.people

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cross_workspace is not UNSET:
            field_dict["crossWorkspace"] = cross_workspace
        if people is not UNSET:
            field_dict["people"] = people
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_phone_directory_person import OfficePhoneDirectoryPerson # noqa: PLC0415
        d = dict(src_dict)
        cross_workspace = d.pop("crossWorkspace", UNSET)

        def _parse_people(data: object) -> list[OfficePhoneDirectoryPerson] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                people_type_0 = []
                _people_type_0 = data
                for people_type_0_item_data in (_people_type_0):
                    people_type_0_item = OfficePhoneDirectoryPerson.from_dict(people_type_0_item_data)



                    people_type_0.append(people_type_0_item)

                return people_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficePhoneDirectoryPerson] | None | Unset, data)

        people = _parse_people(d.pop("people", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        office_phone_lookup_result_dto = cls(
            cross_workspace=cross_workspace,
            people=people,
            phone=phone,
        )

        return office_phone_lookup_result_dto


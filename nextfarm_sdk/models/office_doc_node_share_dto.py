from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_doc_node_share_dto_my_permission import check_office_doc_node_share_dto_my_permission
from ..models.office_doc_node_share_dto_my_permission import OfficeDocNodeShareDtoMyPermission
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_doc_node_share_grant_dto import OfficeDocNodeShareGrantDto





T = TypeVar("T", bound="OfficeDocNodeShareDto")



@_attrs_define
class OfficeDocNodeShareDto:
    

    grants: list[OfficeDocNodeShareGrantDto] | None | Unset = UNSET
    is_restricted: bool | Unset = UNSET
    my_permission: OfficeDocNodeShareDtoMyPermission | Unset = UNSET
    node_id: UUID | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    restricted_by_name: None | str | Unset = UNSET
    restricted_here: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_doc_node_share_grant_dto import OfficeDocNodeShareGrantDto # noqa: PLC0415
        grants: list[dict[str, Any]] | None | Unset
        if isinstance(self.grants, Unset):
            grants = UNSET
        elif isinstance(self.grants, list):
            grants = []
            for grants_type_0_item_data in self.grants:
                grants_type_0_item = grants_type_0_item_data.to_dict()
                grants.append(grants_type_0_item)


        else:
            grants = self.grants

        is_restricted = self.is_restricted

        my_permission: str | Unset = UNSET
        if not isinstance(self.my_permission, Unset):
            my_permission = self.my_permission


        node_id: str | Unset = UNSET
        if not isinstance(self.node_id, Unset):
            node_id = str(self.node_id)

        owner_id: str | Unset = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = str(self.owner_id)

        restricted_by_name: None | str | Unset
        if isinstance(self.restricted_by_name, Unset):
            restricted_by_name = UNSET
        else:
            restricted_by_name = self.restricted_by_name

        restricted_here = self.restricted_here


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if grants is not UNSET:
            field_dict["grants"] = grants
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if my_permission is not UNSET:
            field_dict["myPermission"] = my_permission
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if restricted_by_name is not UNSET:
            field_dict["restrictedByName"] = restricted_by_name
        if restricted_here is not UNSET:
            field_dict["restrictedHere"] = restricted_here

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_doc_node_share_grant_dto import OfficeDocNodeShareGrantDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_grants(data: object) -> list[OfficeDocNodeShareGrantDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                grants_type_0 = []
                _grants_type_0 = data
                for grants_type_0_item_data in (_grants_type_0):
                    grants_type_0_item = OfficeDocNodeShareGrantDto.from_dict(grants_type_0_item_data)



                    grants_type_0.append(grants_type_0_item)

                return grants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDocNodeShareGrantDto] | None | Unset, data)

        grants = _parse_grants(d.pop("grants", UNSET))


        is_restricted = d.pop("isRestricted", UNSET)

        _my_permission = d.pop("myPermission", UNSET)
        my_permission: OfficeDocNodeShareDtoMyPermission | Unset
        if isinstance(_my_permission,  Unset):
            my_permission = UNSET
        else:
            my_permission = check_office_doc_node_share_dto_my_permission(_my_permission)




        _node_id = d.pop("nodeId", UNSET)
        node_id: UUID | Unset
        if isinstance(_node_id,  Unset):
            node_id = UNSET
        else:
            node_id = UUID(_node_id)




        _owner_id = d.pop("ownerId", UNSET)
        owner_id: UUID | Unset
        if isinstance(_owner_id,  Unset):
            owner_id = UNSET
        else:
            owner_id = UUID(_owner_id)




        def _parse_restricted_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        restricted_by_name = _parse_restricted_by_name(d.pop("restrictedByName", UNSET))


        restricted_here = d.pop("restrictedHere", UNSET)

        office_doc_node_share_dto = cls(
            grants=grants,
            is_restricted=is_restricted,
            my_permission=my_permission,
            node_id=node_id,
            owner_id=owner_id,
            restricted_by_name=restricted_by_name,
            restricted_here=restricted_here,
        )

        return office_doc_node_share_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_wiki_page_share_dto_my_permission import check_office_wiki_page_share_dto_my_permission
from ..models.office_wiki_page_share_dto_my_permission import OfficeWikiPageShareDtoMyPermission
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_wiki_page_share_grant_dto import OfficeWikiPageShareGrantDto





T = TypeVar("T", bound="OfficeWikiPageShareDto")



@_attrs_define
class OfficeWikiPageShareDto:
    

    grants: list[OfficeWikiPageShareGrantDto] | None | Unset = UNSET
    is_restricted: bool | Unset = UNSET
    my_permission: OfficeWikiPageShareDtoMyPermission | Unset = UNSET
    node_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_wiki_page_share_grant_dto import OfficeWikiPageShareGrantDto # noqa: PLC0415
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


        node_id: None | str | Unset
        if isinstance(self.node_id, Unset):
            node_id = UNSET
        elif isinstance(self.node_id, UUID):
            node_id = str(self.node_id)
        else:
            node_id = self.node_id


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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_wiki_page_share_grant_dto import OfficeWikiPageShareGrantDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_grants(data: object) -> list[OfficeWikiPageShareGrantDto] | None | Unset:
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
                    grants_type_0_item = OfficeWikiPageShareGrantDto.from_dict(grants_type_0_item_data)



                    grants_type_0.append(grants_type_0_item)

                return grants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeWikiPageShareGrantDto] | None | Unset, data)

        grants = _parse_grants(d.pop("grants", UNSET))


        is_restricted = d.pop("isRestricted", UNSET)

        _my_permission = d.pop("myPermission", UNSET)
        my_permission: OfficeWikiPageShareDtoMyPermission | Unset
        if isinstance(_my_permission,  Unset):
            my_permission = UNSET
        else:
            my_permission = check_office_wiki_page_share_dto_my_permission(_my_permission)




        def _parse_node_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                node_id_type_0 = UUID(data)



                return node_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        node_id = _parse_node_id(d.pop("nodeId", UNSET))


        office_wiki_page_share_dto = cls(
            grants=grants,
            is_restricted=is_restricted,
            my_permission=my_permission,
            node_id=node_id,
        )

        return office_wiki_page_share_dto


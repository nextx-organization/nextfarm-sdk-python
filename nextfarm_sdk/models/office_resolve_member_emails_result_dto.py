from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_resolved_member_email_dto import OfficeResolvedMemberEmailDto





T = TypeVar("T", bound="OfficeResolveMemberEmailsResultDto")



@_attrs_define
class OfficeResolveMemberEmailsResultDto:
    

    matched: list[OfficeResolvedMemberEmailDto] | None | Unset = UNSET
    unmatched: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_resolved_member_email_dto import OfficeResolvedMemberEmailDto # noqa: PLC0415
        matched: list[dict[str, Any]] | None | Unset
        if isinstance(self.matched, Unset):
            matched = UNSET
        elif isinstance(self.matched, list):
            matched = []
            for matched_type_0_item_data in self.matched:
                matched_type_0_item = matched_type_0_item_data.to_dict()
                matched.append(matched_type_0_item)


        else:
            matched = self.matched

        unmatched: list[str] | None | Unset
        if isinstance(self.unmatched, Unset):
            unmatched = UNSET
        elif isinstance(self.unmatched, list):
            unmatched = self.unmatched


        else:
            unmatched = self.unmatched


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if matched is not UNSET:
            field_dict["matched"] = matched
        if unmatched is not UNSET:
            field_dict["unmatched"] = unmatched

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_resolved_member_email_dto import OfficeResolvedMemberEmailDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_matched(data: object) -> list[OfficeResolvedMemberEmailDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                matched_type_0 = []
                _matched_type_0 = data
                for matched_type_0_item_data in (_matched_type_0):
                    matched_type_0_item = OfficeResolvedMemberEmailDto.from_dict(matched_type_0_item_data)



                    matched_type_0.append(matched_type_0_item)

                return matched_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeResolvedMemberEmailDto] | None | Unset, data)

        matched = _parse_matched(d.pop("matched", UNSET))


        def _parse_unmatched(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unmatched_type_0 = cast(list[str], data)

                return unmatched_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        unmatched = _parse_unmatched(d.pop("unmatched", UNSET))


        office_resolve_member_emails_result_dto = cls(
            matched=matched,
            unmatched=unmatched,
        )

        return office_resolve_member_emails_result_dto


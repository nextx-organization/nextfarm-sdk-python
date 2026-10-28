from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeOutgoingDocumentsControllerIssueRequest")



@_attrs_define
class OfficeOutgoingDocumentsControllerIssueRequest:
    

    issued_date: datetime.date | None | Unset = UNSET
    signer_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        issued_date: None | str | Unset
        if isinstance(self.issued_date, Unset):
            issued_date = UNSET
        elif isinstance(self.issued_date, datetime.date):
            issued_date = self.issued_date.isoformat()
        else:
            issued_date = self.issued_date

        signer_id: None | str | Unset
        if isinstance(self.signer_id, Unset):
            signer_id = UNSET
        elif isinstance(self.signer_id, UUID):
            signer_id = str(self.signer_id)
        else:
            signer_id = self.signer_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issued_date is not UNSET:
            field_dict["issuedDate"] = issued_date
        if signer_id is not UNSET:
            field_dict["signerId"] = signer_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_issued_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issued_date_type_0 = datetime.date.fromisoformat(data)



                return issued_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        issued_date = _parse_issued_date(d.pop("issuedDate", UNSET))


        def _parse_signer_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signer_id_type_0 = UUID(data)



                return signer_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        signer_id = _parse_signer_id(d.pop("signerId", UNSET))


        office_outgoing_documents_controller_issue_request = cls(
            issued_date=issued_date,
            signer_id=signer_id,
        )

        return office_outgoing_documents_controller_issue_request


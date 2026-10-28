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






T = TypeVar("T", bound="OfficeOutgoingDocumentsControllerSaveRequest")



@_attrs_define
class OfficeOutgoingDocumentsControllerSaveRequest:
    

    abstract: None | str | Unset = UNSET
    cc_recipients: None | str | Unset = UNSET
    confidentiality: None | str | Unset = UNSET
    copy_count: int | Unset = UNSET
    document_type_code: None | str | Unset = UNSET
    drafting_unit: None | str | Unset = UNSET
    file_id: None | Unset | UUID = UNSET
    note: None | str | Unset = UNSET
    planned_issued_date: datetime.date | None | Unset = UNSET
    recipients: None | str | Unset = UNSET
    register_id: UUID | Unset = UNSET
    signer_id: None | Unset | UUID = UNSET
    title_type: None | str | Unset = UNSET
    urgency: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        abstract: None | str | Unset
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        else:
            abstract = self.abstract

        cc_recipients: None | str | Unset
        if isinstance(self.cc_recipients, Unset):
            cc_recipients = UNSET
        else:
            cc_recipients = self.cc_recipients

        confidentiality: None | str | Unset
        if isinstance(self.confidentiality, Unset):
            confidentiality = UNSET
        else:
            confidentiality = self.confidentiality

        copy_count = self.copy_count

        document_type_code: None | str | Unset
        if isinstance(self.document_type_code, Unset):
            document_type_code = UNSET
        else:
            document_type_code = self.document_type_code

        drafting_unit: None | str | Unset
        if isinstance(self.drafting_unit, Unset):
            drafting_unit = UNSET
        else:
            drafting_unit = self.drafting_unit

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        elif isinstance(self.file_id, UUID):
            file_id = str(self.file_id)
        else:
            file_id = self.file_id

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        planned_issued_date: None | str | Unset
        if isinstance(self.planned_issued_date, Unset):
            planned_issued_date = UNSET
        elif isinstance(self.planned_issued_date, datetime.date):
            planned_issued_date = self.planned_issued_date.isoformat()
        else:
            planned_issued_date = self.planned_issued_date

        recipients: None | str | Unset
        if isinstance(self.recipients, Unset):
            recipients = UNSET
        else:
            recipients = self.recipients

        register_id: str | Unset = UNSET
        if not isinstance(self.register_id, Unset):
            register_id = str(self.register_id)

        signer_id: None | str | Unset
        if isinstance(self.signer_id, Unset):
            signer_id = UNSET
        elif isinstance(self.signer_id, UUID):
            signer_id = str(self.signer_id)
        else:
            signer_id = self.signer_id

        title_type: None | str | Unset
        if isinstance(self.title_type, Unset):
            title_type = UNSET
        else:
            title_type = self.title_type

        urgency: None | str | Unset
        if isinstance(self.urgency, Unset):
            urgency = UNSET
        else:
            urgency = self.urgency


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if cc_recipients is not UNSET:
            field_dict["ccRecipients"] = cc_recipients
        if confidentiality is not UNSET:
            field_dict["confidentiality"] = confidentiality
        if copy_count is not UNSET:
            field_dict["copyCount"] = copy_count
        if document_type_code is not UNSET:
            field_dict["documentTypeCode"] = document_type_code
        if drafting_unit is not UNSET:
            field_dict["draftingUnit"] = drafting_unit
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if note is not UNSET:
            field_dict["note"] = note
        if planned_issued_date is not UNSET:
            field_dict["plannedIssuedDate"] = planned_issued_date
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if register_id is not UNSET:
            field_dict["registerId"] = register_id
        if signer_id is not UNSET:
            field_dict["signerId"] = signer_id
        if title_type is not UNSET:
            field_dict["titleType"] = title_type
        if urgency is not UNSET:
            field_dict["urgency"] = urgency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_abstract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abstract = _parse_abstract(d.pop("abstract", UNSET))


        def _parse_cc_recipients(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cc_recipients = _parse_cc_recipients(d.pop("ccRecipients", UNSET))


        def _parse_confidentiality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confidentiality = _parse_confidentiality(d.pop("confidentiality", UNSET))


        copy_count = d.pop("copyCount", UNSET)

        def _parse_document_type_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type_code = _parse_document_type_code(d.pop("documentTypeCode", UNSET))


        def _parse_drafting_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drafting_unit = _parse_drafting_unit(d.pop("draftingUnit", UNSET))


        def _parse_file_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_id_type_0 = UUID(data)



                return file_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        file_id = _parse_file_id(d.pop("fileId", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_planned_issued_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_issued_date_type_0 = datetime.date.fromisoformat(data)



                return planned_issued_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        planned_issued_date = _parse_planned_issued_date(d.pop("plannedIssuedDate", UNSET))


        def _parse_recipients(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipients = _parse_recipients(d.pop("recipients", UNSET))


        _register_id = d.pop("registerId", UNSET)
        register_id: UUID | Unset
        if isinstance(_register_id,  Unset):
            register_id = UNSET
        else:
            register_id = UUID(_register_id)




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


        def _parse_title_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_type = _parse_title_type(d.pop("titleType", UNSET))


        def _parse_urgency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        urgency = _parse_urgency(d.pop("urgency", UNSET))


        office_outgoing_documents_controller_save_request = cls(
            abstract=abstract,
            cc_recipients=cc_recipients,
            confidentiality=confidentiality,
            copy_count=copy_count,
            document_type_code=document_type_code,
            drafting_unit=drafting_unit,
            file_id=file_id,
            note=note,
            planned_issued_date=planned_issued_date,
            recipients=recipients,
            register_id=register_id,
            signer_id=signer_id,
            title_type=title_type,
            urgency=urgency,
        )

        return office_outgoing_documents_controller_save_request


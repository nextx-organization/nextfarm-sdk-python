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






T = TypeVar("T", bound="OfficeAiReviewItemDto")



@_attrs_define
class OfficeAiReviewItemDto:
    

    cau_hoi: None | str | Unset = UNSET
    cau_tra_loi: None | str | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    do_tin: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    message_id: UUID | Unset = UNSET
    ten_kenh: None | str | Unset = UNSET
    tra_luc: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cau_hoi: None | str | Unset
        if isinstance(self.cau_hoi, Unset):
            cau_hoi = UNSET
        else:
            cau_hoi = self.cau_hoi

        cau_tra_loi: None | str | Unset
        if isinstance(self.cau_tra_loi, Unset):
            cau_tra_loi = UNSET
        else:
            cau_tra_loi = self.cau_tra_loi

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        do_tin: None | str | Unset
        if isinstance(self.do_tin, Unset):
            do_tin = UNSET
        else:
            do_tin = self.do_tin

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        ten_kenh: None | str | Unset
        if isinstance(self.ten_kenh, Unset):
            ten_kenh = UNSET
        else:
            ten_kenh = self.ten_kenh

        tra_luc: str | Unset = UNSET
        if not isinstance(self.tra_luc, Unset):
            tra_luc = self.tra_luc.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cau_hoi is not UNSET:
            field_dict["cauHoi"] = cau_hoi
        if cau_tra_loi is not UNSET:
            field_dict["cauTraLoi"] = cau_tra_loi
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if do_tin is not UNSET:
            field_dict["doTin"] = do_tin
        if id is not UNSET:
            field_dict["id"] = id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if ten_kenh is not UNSET:
            field_dict["tenKenh"] = ten_kenh
        if tra_luc is not UNSET:
            field_dict["traLuc"] = tra_luc

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cau_hoi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cau_hoi = _parse_cau_hoi(d.pop("cauHoi", UNSET))


        def _parse_cau_tra_loi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cau_tra_loi = _parse_cau_tra_loi(d.pop("cauTraLoi", UNSET))


        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_do_tin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        do_tin = _parse_do_tin(d.pop("doTin", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        def _parse_ten_kenh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ten_kenh = _parse_ten_kenh(d.pop("tenKenh", UNSET))


        _tra_luc = d.pop("traLuc", UNSET)
        tra_luc: datetime.datetime | Unset
        if isinstance(_tra_luc,  Unset):
            tra_luc = UNSET
        else:
            tra_luc = datetime.datetime.fromisoformat(_tra_luc)




        office_ai_review_item_dto = cls(
            cau_hoi=cau_hoi,
            cau_tra_loi=cau_tra_loi,
            channel_id=channel_id,
            do_tin=do_tin,
            id=id,
            message_id=message_id,
            ten_kenh=ten_kenh,
            tra_luc=tra_luc,
        )

        return office_ai_review_item_dto


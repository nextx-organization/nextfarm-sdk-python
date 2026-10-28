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






T = TypeVar("T", bound="OfficeSupportQueueItemDto")



@_attrs_define
class OfficeSupportQueueItemDto:
    

    channel_id: UUID | Unset = UNSET
    cho_tu: datetime.datetime | None | Unset = UNSET
    chua_doc: int | Unset = UNSET
    cong_ty_khach: UUID | Unset = UNSET
    da_xong_luc: datetime.datetime | None | Unset = UNSET
    dung_thu: bool | Unset = UNSET
    goi: None | str | Unset = UNSET
    ma_cong_ty: None | str | Unset = UNSET
    nguoi_gui_cuoi: None | Unset | UUID = UNSET
    nguoi_nhan: None | Unset | UUID = UNSET
    ten_hien_thi: None | str | Unset = UNSET
    ten_nguoi_gui_cuoi: None | str | Unset = UNSET
    ten_nguoi_nhan: None | str | Unset = UNSET
    tin_cuoi: None | str | Unset = UNSET
    tin_cuoi_luc: datetime.datetime | None | Unset = UNSET
    trang_thai_khach: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        cho_tu: None | str | Unset
        if isinstance(self.cho_tu, Unset):
            cho_tu = UNSET
        elif isinstance(self.cho_tu, datetime.datetime):
            cho_tu = self.cho_tu.isoformat()
        else:
            cho_tu = self.cho_tu

        chua_doc = self.chua_doc

        cong_ty_khach: str | Unset = UNSET
        if not isinstance(self.cong_ty_khach, Unset):
            cong_ty_khach = str(self.cong_ty_khach)

        da_xong_luc: None | str | Unset
        if isinstance(self.da_xong_luc, Unset):
            da_xong_luc = UNSET
        elif isinstance(self.da_xong_luc, datetime.datetime):
            da_xong_luc = self.da_xong_luc.isoformat()
        else:
            da_xong_luc = self.da_xong_luc

        dung_thu = self.dung_thu

        goi: None | str | Unset
        if isinstance(self.goi, Unset):
            goi = UNSET
        else:
            goi = self.goi

        ma_cong_ty: None | str | Unset
        if isinstance(self.ma_cong_ty, Unset):
            ma_cong_ty = UNSET
        else:
            ma_cong_ty = self.ma_cong_ty

        nguoi_gui_cuoi: None | str | Unset
        if isinstance(self.nguoi_gui_cuoi, Unset):
            nguoi_gui_cuoi = UNSET
        elif isinstance(self.nguoi_gui_cuoi, UUID):
            nguoi_gui_cuoi = str(self.nguoi_gui_cuoi)
        else:
            nguoi_gui_cuoi = self.nguoi_gui_cuoi

        nguoi_nhan: None | str | Unset
        if isinstance(self.nguoi_nhan, Unset):
            nguoi_nhan = UNSET
        elif isinstance(self.nguoi_nhan, UUID):
            nguoi_nhan = str(self.nguoi_nhan)
        else:
            nguoi_nhan = self.nguoi_nhan

        ten_hien_thi: None | str | Unset
        if isinstance(self.ten_hien_thi, Unset):
            ten_hien_thi = UNSET
        else:
            ten_hien_thi = self.ten_hien_thi

        ten_nguoi_gui_cuoi: None | str | Unset
        if isinstance(self.ten_nguoi_gui_cuoi, Unset):
            ten_nguoi_gui_cuoi = UNSET
        else:
            ten_nguoi_gui_cuoi = self.ten_nguoi_gui_cuoi

        ten_nguoi_nhan: None | str | Unset
        if isinstance(self.ten_nguoi_nhan, Unset):
            ten_nguoi_nhan = UNSET
        else:
            ten_nguoi_nhan = self.ten_nguoi_nhan

        tin_cuoi: None | str | Unset
        if isinstance(self.tin_cuoi, Unset):
            tin_cuoi = UNSET
        else:
            tin_cuoi = self.tin_cuoi

        tin_cuoi_luc: None | str | Unset
        if isinstance(self.tin_cuoi_luc, Unset):
            tin_cuoi_luc = UNSET
        elif isinstance(self.tin_cuoi_luc, datetime.datetime):
            tin_cuoi_luc = self.tin_cuoi_luc.isoformat()
        else:
            tin_cuoi_luc = self.tin_cuoi_luc

        trang_thai_khach: None | str | Unset
        if isinstance(self.trang_thai_khach, Unset):
            trang_thai_khach = UNSET
        else:
            trang_thai_khach = self.trang_thai_khach


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if cho_tu is not UNSET:
            field_dict["choTu"] = cho_tu
        if chua_doc is not UNSET:
            field_dict["chuaDoc"] = chua_doc
        if cong_ty_khach is not UNSET:
            field_dict["congTyKhach"] = cong_ty_khach
        if da_xong_luc is not UNSET:
            field_dict["daXongLuc"] = da_xong_luc
        if dung_thu is not UNSET:
            field_dict["dungThu"] = dung_thu
        if goi is not UNSET:
            field_dict["goi"] = goi
        if ma_cong_ty is not UNSET:
            field_dict["maCongTy"] = ma_cong_ty
        if nguoi_gui_cuoi is not UNSET:
            field_dict["nguoiGuiCuoi"] = nguoi_gui_cuoi
        if nguoi_nhan is not UNSET:
            field_dict["nguoiNhan"] = nguoi_nhan
        if ten_hien_thi is not UNSET:
            field_dict["tenHienThi"] = ten_hien_thi
        if ten_nguoi_gui_cuoi is not UNSET:
            field_dict["tenNguoiGuiCuoi"] = ten_nguoi_gui_cuoi
        if ten_nguoi_nhan is not UNSET:
            field_dict["tenNguoiNhan"] = ten_nguoi_nhan
        if tin_cuoi is not UNSET:
            field_dict["tinCuoi"] = tin_cuoi
        if tin_cuoi_luc is not UNSET:
            field_dict["tinCuoiLuc"] = tin_cuoi_luc
        if trang_thai_khach is not UNSET:
            field_dict["trangThaiKhach"] = trang_thai_khach

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_cho_tu(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cho_tu_type_0 = datetime.datetime.fromisoformat(data)



                return cho_tu_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cho_tu = _parse_cho_tu(d.pop("choTu", UNSET))


        chua_doc = d.pop("chuaDoc", UNSET)

        _cong_ty_khach = d.pop("congTyKhach", UNSET)
        cong_ty_khach: UUID | Unset
        if isinstance(_cong_ty_khach,  Unset):
            cong_ty_khach = UNSET
        else:
            cong_ty_khach = UUID(_cong_ty_khach)




        def _parse_da_xong_luc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                da_xong_luc_type_0 = datetime.datetime.fromisoformat(data)



                return da_xong_luc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        da_xong_luc = _parse_da_xong_luc(d.pop("daXongLuc", UNSET))


        dung_thu = d.pop("dungThu", UNSET)

        def _parse_goi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        goi = _parse_goi(d.pop("goi", UNSET))


        def _parse_ma_cong_ty(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ma_cong_ty = _parse_ma_cong_ty(d.pop("maCongTy", UNSET))


        def _parse_nguoi_gui_cuoi(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                nguoi_gui_cuoi_type_0 = UUID(data)



                return nguoi_gui_cuoi_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        nguoi_gui_cuoi = _parse_nguoi_gui_cuoi(d.pop("nguoiGuiCuoi", UNSET))


        def _parse_nguoi_nhan(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                nguoi_nhan_type_0 = UUID(data)



                return nguoi_nhan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        nguoi_nhan = _parse_nguoi_nhan(d.pop("nguoiNhan", UNSET))


        def _parse_ten_hien_thi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ten_hien_thi = _parse_ten_hien_thi(d.pop("tenHienThi", UNSET))


        def _parse_ten_nguoi_gui_cuoi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ten_nguoi_gui_cuoi = _parse_ten_nguoi_gui_cuoi(d.pop("tenNguoiGuiCuoi", UNSET))


        def _parse_ten_nguoi_nhan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ten_nguoi_nhan = _parse_ten_nguoi_nhan(d.pop("tenNguoiNhan", UNSET))


        def _parse_tin_cuoi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tin_cuoi = _parse_tin_cuoi(d.pop("tinCuoi", UNSET))


        def _parse_tin_cuoi_luc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tin_cuoi_luc_type_0 = datetime.datetime.fromisoformat(data)



                return tin_cuoi_luc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        tin_cuoi_luc = _parse_tin_cuoi_luc(d.pop("tinCuoiLuc", UNSET))


        def _parse_trang_thai_khach(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trang_thai_khach = _parse_trang_thai_khach(d.pop("trangThaiKhach", UNSET))


        office_support_queue_item_dto = cls(
            channel_id=channel_id,
            cho_tu=cho_tu,
            chua_doc=chua_doc,
            cong_ty_khach=cong_ty_khach,
            da_xong_luc=da_xong_luc,
            dung_thu=dung_thu,
            goi=goi,
            ma_cong_ty=ma_cong_ty,
            nguoi_gui_cuoi=nguoi_gui_cuoi,
            nguoi_nhan=nguoi_nhan,
            ten_hien_thi=ten_hien_thi,
            ten_nguoi_gui_cuoi=ten_nguoi_gui_cuoi,
            ten_nguoi_nhan=ten_nguoi_nhan,
            tin_cuoi=tin_cuoi,
            tin_cuoi_luc=tin_cuoi_luc,
            trang_thai_khach=trang_thai_khach,
        )

        return office_support_queue_item_dto


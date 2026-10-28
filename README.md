# nextfarm-sdk

Thư viện chính thức để gọi NextFarm API từ Python, hỗ trợ cả đồng bộ và `async`.

Mã trong kho này được sinh tự động từ [OpenAPI của NextFarm](https://developers.nextfarm.vn/openapi.json). Vui lòng không sửa trực tiếp, xem [CONTRIBUTING.md](CONTRIBUTING.md).

## Cài đặt

```sh
pip install nextfarm-sdk
```

Yêu cầu Python 3.11 trở lên.

## Bắt đầu

```python
import os
from nextfarm_sdk import create_client, SANDBOX_URL
from nextfarm_sdk.api.iot import get_api_v1_iot_devices

nf = create_client(api_key=os.environ["NEXTFARM_API_KEY"], base_url=SANDBOX_URL)

page = get_api_v1_iot_devices.sync(client=nf, page=1, page_size=20)
for d in page.items or []:
    print(d.name)

# async
page = await get_api_v1_iot_devices.asyncio(client=nf, page=1)
```

## Ghi chú

- Mỗi endpoint là một module trong `nextfarm_sdk.api.<nhóm>`, gồm bốn hàm `sync`, `sync_detailed`, `asyncio` và `asyncio_detailed`. Các hàm `*_detailed` trả thêm mã trạng thái và header.
- Mặc định client gọi môi trường production. Khi thử nghiệm, dùng `SANDBOX_URL` với khoá sandbox.
- Mã trạng thái không có trong tài liệu sẽ ném `nextfarm_sdk.errors.UnexpectedStatus`.

## Tài liệu

- Hướng dẫn: https://developers.nextfarm.vn/docs/sdk
- Phiên bản và chính sách ngừng hỗ trợ: [VERSIONING.md](VERSIONING.md)
- Nhật ký thay đổi: [CHANGELOG.md](CHANGELOG.md)

Giấy phép MIT.

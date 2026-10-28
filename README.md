# nextfarm-sdk

> Mã trong kho này được sinh tự động từ [OpenAPI công khai](https://developers.nextfarm.vn/openapi.json). Đừng sửa tay — xem [CONTRIBUTING.md](CONTRIBUTING.md).

Gọi NextFarm API từ Python, có kiểu đầy đủ (đồng bộ và `async`). Mã sinh từ [`/openapi.json`](https://developers.nextfarm.vn/openapi.json)
và chỉ gồm các tuyến khoá API gọi được.

```sh
pip install nextfarm-sdk
```

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

- Python ≥ 3.11. Mỗi tuyến là một mô-đun trong `nextfarm_sdk.api.<phân hệ>` với 4 hàm: `sync`, `sync_detailed`, `asyncio`, `asyncio_detailed`.
  Bản `*_detailed` trả thêm mã trạng thái và header.
- Mặc định gọi prod (`PROD_URL`). Thử nghiệm thì dùng `SANDBOX_URL` với khoá sandbox.
- Mã trạng thái ngoài tài liệu ném `nextfarm_sdk.errors.UnexpectedStatus`.

Tài liệu: https://developers.nextfarm.vn/docs/sdk · Phiên bản và bỏ dần: [VERSIONING.md](https://github.com/nextx-organization/nextfarm-sdk-python/blob/main/VERSIONING.md) · Giấy phép MIT

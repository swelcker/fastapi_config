from pydantic import BaseModel


class SiteConfig(BaseModel):
    name: str = ""
    url: str = ""


async def test_string_key(config_store):
    key = "key1"
    val = "value1"
    data = await config_store.get(key)
    assert data is None

    await config_store.set(key, val)
    data = await config_store.get(key)
    assert data == val


async def test_schema_key(config_store):
    key = SiteConfig
    data = await config_store.get(key)
    assert data is None

    val = SiteConfig(name="amisadmin", url="https://docs.amis.work")
    await config_store.set(val)
    data = await config_store.get(key)
    assert data == val

    val2 = SiteConfig(name="amisadmin2", url="https://docs.amis.work")
    await config_store.set(SiteConfig, val2.json())
    data = await config_store.get(key)
    assert data == val2

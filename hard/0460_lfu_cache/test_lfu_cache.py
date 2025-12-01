import pytest
from lfu_cache import LFUCache


@pytest.fixture
def cache(request):
    """Fixture nhận capacity từ param."""
    capacity = request.param
    return LFUCache(capacity)


@pytest.mark.parametrize("cache", [2], indirect=True)
def test_basic_operations(cache):

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # freq(1)=2

    cache.put(3, 3)  # evict key 2 (freq=1)
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    cache.put(4, 4)  # evict key 1 (freq=2)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


@pytest.mark.parametrize("cache", [2], indirect=True)
def test_update_existing(cache):

    cache.put(1, 10)
    cache.put(2, 20)

    cache.put(1, 100)  # update + freq++
    assert cache.get(1) == 100
    assert cache.get(2) == 20


@pytest.mark.parametrize("cache", [0], indirect=True)
def test_zero_capacity(cache):
    cache.put(1, 1)
    assert cache.get(1) == -1
import pytest
from queue_using_stacks import MyQueue


@pytest.fixture
def queue():
    return MyQueue()


def test_push_and_peek(queue):
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1  # front is 1

def test_pop(queue):
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    assert queue.peek() == 2

def test_empty(queue):
    assert queue.empty() is True
    queue.push(10)
    assert queue.empty() is False

def test_push_pop_multiple(queue):
    for i in range(5):
        queue.push(i)
    for i in range(5):
        assert queue.pop() == i

def test_alternate_push_pop(queue):
    queue.push(1)
    assert queue.pop() == 1
    queue.push(2)
    queue.push(3)
    assert queue.pop() == 2
    assert queue.peek() == 3

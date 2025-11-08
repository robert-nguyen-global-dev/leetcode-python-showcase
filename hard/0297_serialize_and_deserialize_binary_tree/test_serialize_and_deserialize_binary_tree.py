import pytest
from serialize_and_deserialize_binary_tree import Codec, TreeNode


def build_sample_tree():
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left, n1.right = n2, n3
    n3.left, n3.right = n4, n5
    return n1


def test_serialization_deserialization():
    codec = Codec()
    root = build_sample_tree()
    serialized = codec.serialize(root)
    assert serialized == "1,2,3,null,null,4,5"

    deserialized = codec.deserialize(serialized)
    assert codec.serialize(deserialized) == "1,2,3,null,null,4,5"

def test_empty_tree():
    codec = Codec()
    assert codec.serialize(None) == ""
    assert codec.deserialize("") is None

def test_single_node():
    codec = Codec()
    node = TreeNode(42)
    data = codec.serialize(node)
    assert data == "42"
    restored = codec.deserialize(data)
    assert restored.val == 42
    assert restored.left is None
    assert restored.right is None

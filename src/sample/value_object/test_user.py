"""値オブジェクトuserクラスのテスト"""
import pytest
from user import User


def test_create_user():
    """生成と比較のテスト"""
    user = User(first_name="hoge", last_name="fuga")
    user2 = User(first_name="hoge", last_name="fuga")
    user3 = User(first_name="tste", last_name="name")
    assert user == user2
    assert user != user3

    with pytest.raises(ValueError) as error:
        User(first_name="tst", last_name="tset")
    assert str(error.value) == "first_name は最小要件を満たしていませんtst"

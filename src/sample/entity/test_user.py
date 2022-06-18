"""エンティティトuserクラスのテスト"""
import pytest
from user import UserId, User


def test_create_user():
    """生成と比較のテスト"""
    user_id1 = UserId(prefix="abc", number=1)
    user_id2 = UserId(prefix="abc", number=2)

    user1 = User(user_id=user_id1, first_name="hoge", last_name="fuga")
    user2 = User(user_id=user_id1, first_name="hoge", last_name="fuga")
    user3 = User(user_id=user_id2, first_name="tste", last_name="name")
    assert user1 == user2
    assert user1 != user3

    with pytest.raises(ValueError) as error:
        User(user_id=user_id1, first_name="tst", last_name="tset")
    assert str(error.value) == "first_name は3文字以上必要ですtst"

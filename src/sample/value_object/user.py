"""値オブジェクト"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class User:
    """ユーザーの値オブジェクト

    値オブジェクトは下記の3点を満たす必要がある
    - 不変
    - 交換可能
    - 等価性による比較

    不変であることをfrozen=Trueを実装することで表現

    """

    first_name: str
    last_name: str
    MIN_LENGTH: ClassVar[str] = 3

    def __init__(self, first_name: str, last_name: str) -> None:
        """完全コンストラクタ

        値オブジェクトでは生成のタイミングで,
        バリデーションを実施して不正なオブジェクトを生成できないようにする.
        意図しない値を渡された場合,ValueErrorをraiseする.

        Args:
            first_name (str): 名
            last_name (str): 姓
        """
        if not self._validate_name(first_name):
            raise ValueError(f"first_name は要件を満たしていません{first_name}")
        if not self._validate_name(last_name):
            raise ValueError(f"last_nameは要件を満たしていません{last_name}")
        object.__setattr__(self, "first_name", first_name)
        object.__setattr__(self, "last_name", last_name)

    def __eq__(self, __o: object) -> bool:
        """比較メソッド　等価性の比較を行う

        pythonの比較 == の結果は 特殊メソッド __eq__により定義できるため、
        等価性の比較を__eq__メソッドに実装する

        Args:
            __o (object): 比較対象 A == B と記載した際のB

        Returns:
            bool: 比較結果
        """
        return (
            isinstance(__o, User)
            and self.first_name == __o.first_name
            and self.last_name == __o.last_name
        )

    def __ne__(self, __o: object) -> bool:
        """not equalの実装

        Args:
            __o (object): 比較対象　A != B と記載した際のB

        Returns:
            bool: 比較結果
        """
        return not self.__eq__(__o)

    @classmethod
    def _validate_name(cls, name: str) -> bool:
        """nameのバリデーション

        Args:
            name (str): バリデーションの対象

        Returns:
            bool: 問題ない場合、True
        """
        return name.isalpha and len(name) > cls.MIN_LENGTH

    def get_full_name_japanese_style(self) -> str:
        """日本式のフルネームを取得　姓名の順で文字列を取得

        値オブジェクトの振る舞いに関しても、値オブジェクトに定義する。

        Returns:
            str: フルネーム　姓 名
        """
        return self.last_name + " " + self.first_name

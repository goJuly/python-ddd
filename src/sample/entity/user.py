"""エンティティ"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class UserId:
    """ユーザーの識別するためのID

    このクラス自体は値オブジェクト
    """

    prefix: str
    number: int
    PREFIX_LENGTH: ClassVar[int] = 3
    MAX_NUMBER_LENGTH: ClassVar[int] = 999999999999

    def __init__(self, prefix: str, number: int) -> None:
        """コンストラクタ

        Args:
            prefix (str): プレフィックス
            number (int): ユーザー番号
        """
        if len(prefix) != self.PREFIX_LENGTH:
            raise ValueError("プレフィックスの文字数が不正です")
        if number > self.MAX_NUMBER_LENGTH:
            raise ValueError("ユーザー番号の桁数が不正です")
        object.__setattr__(self, "prefix", prefix)
        object.__setattr__(self, "number", number)

    def __str__(self) -> str:
        return self.prefix + str(self.number)

    def __eq__(self, __o: object) -> bool:
        return (
            isinstance(__o, UserId)
            and self.prefix == __o.prefix
            and self.number == __o.number
        )

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)


@dataclass
class User:
    """ユーザーのエンティティ

    エンティティは下記の3点を満たす必要がある
    - 可変
    - 同じ属性であっても区別される
    - 同一性により区別される
    """

    user_id: UserId
    first_name: str
    last_name: str
    MIN_LENGTH: ClassVar[str] = 3

    def __init__(self, user_id: UserId, first_name, last_name: str) -> None:
        """バリデーションをコンストラクタで実施するのは値オブジェクトと同様

        frozen = Falseのため、アトリビュートに直接セットする.

        Args:
            user_id (UserId): ユーザーID ユーザーの識別を行う
            first_name (_type_): 名
            last_name (str): 姓

        Raises:
            ValueError: 渡された引数がクラス生成の要件を満たしていない場合
        """
        self.user_id = user_id
        if not len(first_name) > self.MIN_LENGTH:
            raise ValueError(f"first_name は3文字以上必要です{first_name}")
        if not self._validate_name(first_name):
            raise ValueError(f"first_name は要件を満たしていません{first_name}")
        if not len(first_name) > self.MIN_LENGTH:
            raise ValueError(f"last_name は3文字以上必要です{first_name}")
        if not self._validate_name(last_name):
            raise ValueError(f"last_name は要件を満たしていません{last_name}")
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def _validate_name(cls, name: str) -> bool:
        """nameのバリデーション

        Args:
            name (str): バリデーションの対象

        Returns:
            bool: 生成するための要件を満たしている場合、True
        """
        return name.isalpha

    def __eq__(self, __o: object) -> bool:
        """比較メソッド 同一性のある項目で比較を行う.

        同姓同名でも別人のケースがあるように,個人を特定できる情報で比較を行う.
        ECサイトのように、ユーザーIDが一意に付与される場合,
        同一自分と判定するのにユーザーIDを利用する.

        Args:
            __o (object): 比較対象 A == B と記載した際のB

        Returns:
            bool: 比較結果
        """
        return isinstance(__o, User) and self.user_id == __o.user_id

    def __ne__(self, __o: object) -> bool:
        """_summary_

        Args:
            __o (object): _description_

        Returns:
            bool: _description_
        """
        return not self.__eq__(__o)

    def 
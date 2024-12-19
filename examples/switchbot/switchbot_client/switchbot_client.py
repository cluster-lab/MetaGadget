from switchbot_client.case_insensitive_invoke_mixin import CaseInsensitiveInvokeMixin
from switchbot_client.switchbot_base_client import SwitchBotBaseClient
from switchbot_client.switchbot_mixin import SwitchBotDeviceOpsMixin


class SwitchBotClient(SwitchBotBaseClient, SwitchBotDeviceOpsMixin, CaseInsensitiveInvokeMixin):
    """
    Main SwitchBot client implementation combining base functionality, device operations, and case-insensitive method invocation.
    基本機能、デバイス操作、大文字小文字を区別しないメソッド呼び出しを組み合わせたメインのSwitchBotクライアント実装。

    This class inherits from:
    - SwitchBotBaseClient: Provides core API communication
    - SwitchBotDeviceOpsMixin: Adds device-specific operations
    - CaseInsensitiveInvokeMixin: Enables case-insensitive method calls

    このクラスは以下のクラスを継承します：
    - SwitchBotBaseClient: コアAPIの通信機能を提供
    - SwitchBotDeviceOpsMixin: デバイス固有の操作を追加
    - CaseInsensitiveInvokeMixin: 大文字小文字を区別しないメソッド呼び出しを可能にする
    """
    def __init__(self, token: str, secret: str):
        """
        Initialize the SwitchBot client with authentication credentials.
        認証情報を使用してSwitchBotクライアントを初期化します。

        Args:
            token (str): SwitchBot API token / SwitchBot APIトークン
            secret (str): SwitchBot API secret / SwitchBot APIシークレット

        Note:
            When using multiple inheritance, super() calls are made in sequence to properly initialize all parent classes:
            多重継承を使用する場合、すべての親クラスを適切に初期化するために、super()呼び出しは順番に行われます：
            1. SwitchBotBaseClient.__init__(token, secret)
            2. SwitchBotDeviceOpsMixin.__init__()
            3. CaseInsensitiveInvokeMixin.__init__()
        """
        # Initialize parent classes in sequence
        # 親クラスを順番に初期化
        super(SwitchBotClient, self).__init__(token, secret)  # SwitchBotBaseClient.__init__(token, secret)
        super(SwitchBotBaseClient, self).__init__()  # SwitchBotDeviceOpsMixin.__init__()
        super(SwitchBotDeviceOpsMixin, self).__init__()  # CaseInsensitiveInvokeMixin.__init__()


import base64
import hashlib
import hmac
import time
import uuid
from typing import Protocol, Type

import httpx
from pydantic import BaseModel

from .switchbot_models import SBListDeviceResponse


class SwitchBotClientProtocol(Protocol):
    """
    Protocol defining the interface for SwitchBot client implementations.
    SwitchBotクライアントの実装に必要なインターフェースを定義するプロトコル。
    """
    def list_devices(self) -> SBListDeviceResponse:
        """
        List all available SwitchBot devices.
        利用可能なすべてのSwitchBotデバイスを一覧表示する。

        Returns:
            SBListDeviceResponse: Response containing list of devices.
            SBListDeviceResponse: デバイスリストを含むレスポンス。
        """
        pass

    def get_device_status(self, device_id: str):
        """
        Get the current status of a specific device.
        特定のデバイスの現在のステータスを取得する。

        Args:
            device_id (str): ID of the device to query.
            device_id (str): クエリするデバイスのID。
        """
        pass

    def _get_device_status_typed[T: BaseModel](self, device_id: str, cls: Type[T]) -> T:
        """
        Get device status with type validation using Pydantic models.
        Pydanticモデルを使用して型検証付きでデバイスステータスを取得する。

        Args:
            device_id (str): ID of the device to query.
            device_id (str): クエリするデバイスのID。
            cls (Type[T]): Pydantic model class for response validation.
            cls (Type[T]): レスポンス検証用のPydanticモデルクラス。

        Returns:
            T: Validated device status response of type T.
            T: 型Tの検証済みデバイスステータスレスポンス。
        """
        pass

    def commands(self, device_id: str, command: str, command_type: str = "command", parameter: str | int = "default"):
        """
        Send a command to a specific device.
        特定のデバイスにコマンドを送信する。

        Args:
            device_id (str): ID of the target device.
            device_id (str): ターゲットデバイスのID。
            command (str): Command to execute.
            command (str): 実行するコマンド。
            command_type (str): Type of command (default: "command").
            command_type (str): コマンドの種類（デフォルト: "command"）。
            parameter (str | int): Command parameter (default: "default").
            parameter (str | int): コマンドパラメータ（デフォルト: "default"）。
        """
        pass

    def execute_scene(self, scene_id: str):
        """
        Execute a specific scene by its ID.
        IDで指定したシーンを実行する。

        Args:
            scene_id (str): ID of the scene to execute.
            scene_id (str): 実行するシーンのID。
        """
        pass

    def list_scenes(self):
        """
        List all available scenes.
        利用可能なすべてのシーンを一覧表示する。
        """
        pass

class SwitchBotBaseClient(SwitchBotClientProtocol):
    """
    Base implementation of the SwitchBot client providing core API functionality.
    コアAPIの機能を提供するSwitchBotクライアントの基本実装。
    """
    def __init__(self, token: str, secret: str):
        """
        Initialize the SwitchBot client with authentication credentials.
        認証情報でSwitchBotクライアントを初期化する。

        Args:
            token (str): SwitchBot API token.
            token (str): SwitchBot APIトークン。
            secret (str): SwitchBot API secret.
            secret (str): SwitchBot APIシークレット。
        """
        self._token = token
        self._secret = secret
        self._api_url = "https://api.switch-bot.com/v1.1"

    def _generate_sign(self):
        """
        Generate authentication signature for API requests.
        APIリクエスト用の認証署名を生成する。

        Returns:
            tuple: Token, timestamp, nonce, and signature.
            tuple: トークン、タイムスタンプ、ノンス、署名。
        """
        token = self._token
        secret = self._secret
        nonce = uuid.uuid4()
        t = int(round(time.time() * 1000))
        string_to_sign = '{}{}{}'.format(token, t, nonce)

        string_to_sign = bytes(string_to_sign, 'utf-8')
        secret = bytes(secret, 'utf-8')

        sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
        return token, t, nonce, sign

    def _generate_headers(self):
        """
        Generate HTTP headers for API requests including authentication.
        認証情報を含むAPIリクエスト用のHTTPヘッダーを生成する。

        Returns:
            dict: Headers required for API authentication.
            dict: API認証に必要なヘッダー。
        """
        token, t, nonce, sign = self._generate_sign()
        return {
            'Authorization': token,
            'Content-Type': 'application/json',
            'charset': 'utf8',
            't': str(t),
            'sign': str(sign, 'utf-8'),
            'nonce': str(nonce)
        }

    def list_devices(self) -> SBListDeviceResponse:
        """
        List all available SwitchBot devices.
        利用可能なすべてのSwitchBotデバイスを一覧表示する。

        Returns:
            SBListDeviceResponse: Response containing list of devices.
            SBListDeviceResponse: デバイスリストを含むレスポンス。
        """
        res = httpx.get(f'{self._api_url}/devices', headers=self._generate_headers())
        return SBListDeviceResponse.model_validate(res.json())

    def get_device_status(self, device_id: str):
        """
        Get the current status of a specific device.
        特定のデバイスの現在のステータスを取得する。

        Args:
            device_id (str): ID of the device to query.
            device_id (str): クエリするデバイスのID。
        """
        res = httpx.get(f'{self._api_url}/devices/{device_id}/status', headers=self._generate_headers())
        return res.json()

    def _get_device_status_typed[T: BaseModel](self, device_id: str, cls: Type[T]) -> T:
        """
        Get device status with type validation using Pydantic models.
        Pydanticモデルを使用して型検証付きでデバイスステータスを取得する。

        Args:
            device_id (str): ID of the device to query.
            device_id (str): クエリするデバイスのID。
            cls (Type[T]): Pydantic model class for response validation.
            cls (Type[T]): レスポンス検証用のPydanticモデルクラス。

        Returns:
            T: Validated device status response of type T.
            T: 型Tの検証済みデバイスステータスレスポンス。
        """
        res = self.get_device_status(device_id)
        return cls.model_validate(res)

    def commands(self, device_id: str, command: str, command_type: str = "command", parameter: str | int = "default"):
        """
        Send a command to a specific device.
        特定のデバイスにコマンドを送信する。

        Args:
            device_id (str): ID of the target device.
            device_id (str): ターゲットデバイスのID。
            command (str): Command to execute.
            command (str): 実行するコマンド。
            command_type (str): Type of command (default: "command").
            command_type (str): コマンドの種類（デフォルト: "command"）。
            parameter (str | int): Command parameter (default: "default").
            parameter (str | int): コマンドパラメータ（デフォルト: "default"）。
        """
        request_body = {
            "command_type": command_type,
            "command": command,
            "parameter": parameter
        }
        res = httpx.post(f'{self._api_url}/devices/{device_id}/commands', headers=self._generate_headers(), json=request_body)
        return res.json()

    def execute_scene(self, scene_id: str):
        """
        Execute a specific scene by its ID.
        IDで指定したシーンを実行する。

        Args:
            scene_id (str): ID of the scene to execute.
            scene_id (str): 実行するシーンのID。
        """
        res = httpx.post(f'{self._api_url}/scenes/{scene_id}/execute', headers=self._generate_headers())
        return res.json()

    def list_scenes(self):
        """
        List all available scenes.
        利用可能なすべてのシーンを一覧表示する。

        Returns:
            dict: Response containing list of scenes.
            dict: シーンリストを含むレスポンス。
        """
        res = httpx.get(f'{self._api_url}/scenes', headers=self._generate_headers())
        return res.json()


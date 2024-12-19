from typing import TypeVar

from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)


class ListDeviceBody(BaseModel):
    """
    Model representing a SwitchBot device in the device list.
    デバイスリストに表示されるSwitchBotデバイスを表すモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceName: str  # Device name / デバイス名
    deviceType: str  # Device type, e.g., MeterPro(CO2) / デバイスタイプ（例：MeterPro(CO2)）
    hubDeviceId: str  # Device's parent hub ID / 親ハブのデバイスID
    # enabledCloudService: bool  # Cloud service status / クラウドサービスの状態

class ListDeviceBodyRoot(BaseModel):
    """
    Root model containing the list of SwitchBot devices.
    SwitchBotデバイスのリストを含むルートモデル。
    """
    deviceList: list[ListDeviceBody]  # List of devices / デバイスのリスト
    # infraredRemoteList: list[ListDeviceBody]  # List of infrared devices / 赤外線デバイスのリスト

class SBListDeviceResponse(BaseModel):
    """
    Response model for the list devices API endpoint.
    デバイス一覧取得APIエンドポイントのレスポンスモデル。
    """
    statusCode: int  # HTTP status code of the response / レスポンスのHTTPステータスコード
    message: str  # Response message or error description / レスポンスメッセージまたはエラー説明
    body: ListDeviceBodyRoot  # Response body containing device list / デバイスリストを含むレスポンスボディ


class SBDeviceStatusResponse[T](BaseModel):
    """
    Generic response model for device status API endpoints.
    デバイスステータスAPIエンドポイントの汎用レスポンスモデル。
    """
    statusCode: int  # HTTP status code of the response / レスポンスのHTTPステータスコード
    message: str  # Response message or error description / レスポンスメッセージまたはエラー説明
    body: T  # Body of the response containing device-specific information / デバイス固有の情報を含むレスポンスボディ


class MeterProCO2StatusBody(BaseModel):
    """
    Status model for SwitchBot Meter Pro CO2 device.
    SwitchBotメータープロCO2デバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., MeterPro(CO2) / デバイスタイプ（例：MeterPro(CO2)）
    hubDeviceId: str  # Device's parent hub ID / 親ハブのデバイスID
    battery: int  # Current battery level, from 0 to 100 / バッテリー残量（0-100）
    version: str  # Current firmware version, e.g., V4.2 / 現在のファームウェアバージョン（例：V4.2）
    temperature: float  # Temperature in Celsius / 温度（摂氏）
    humidity: int  # Humidity percentage / 湿度（%）
    CO2: int  # CO2 concentration in parts per million (ppm), from 0 to 9999 / CO2濃度（ppm、0-9999）


class BotStatusBody(BaseModel):
    """
    Status model for SwitchBot Bot device.
    SwitchBotボットデバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., Bot / デバイスタイプ（例：Bot）
    power: str  # ON/OFF state / 電源状態（ON/OFF）
    battery: int  # Current battery level, from 0 to 100 / バッテリー残量（0-100）
    version: str  # Current firmware version, e.g., V6.3 / 現在のファームウェアバージョン（例：V6.3）
    deviceMode: str  # Mode: pressMode, switchMode, or customizeMode / モード：pressMode、switchMode、またはcustomizeMode
    hubDeviceId: str  # Device's parent Hub ID / 親ハブのデバイスID


class MotionSensorStatusBody(BaseModel):
    """
    Status model for SwitchBot Motion Sensor device.
    SwitchBotモーションセンサーデバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., Motion Sensor / デバイスタイプ（例：Motion Sensor）
    hubDeviceId: str  # Device's parent Hub ID / 親ハブのデバイスID
    battery: int  # The current battery level, from 0 to 100 / バッテリー残量（0-100）
    version: str  # The current firmware version, e.g., V4.2 / 現在のファームウェアバージョン（例：V4.2）
    moveDetected: bool  # Determines if motion is detected / モーション検知状態
    brightness: str  # The ambient brightness, bright or dim / 周囲の明るさ（brightまたはdim）


class PlugMiniJPStatusBody(BaseModel):
    """
    Status model for SwitchBot Plug Mini (JP) device.
    SwitchBotプラグミニ（JP）デバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., Plug Mini (JP) / デバイスタイプ（例：Plug Mini (JP)）
    hubDeviceId: str  # Device's parent Hub ID / 親ハブのデバイスID
    voltage: float  # The voltage of the device, measured in Volts / デバイスの電圧（V）
    version: str  # The current BLE and Wi-Fi firmware version, e.g., V3.1-6.3 / 現在のBLEとWi-Fiファームウェアバージョン（例：V3.1-6.3）
    weight: float  # The power consumed in a day, measured in Watts / 1日の消費電力（W）
    electricityOfDay: int  # The duration used in a day, measured in minutes / 1日の使用時間（分）
    electricCurrent: float  # The current of the device, measured in Amps / デバイスの電流（A）


class StripLightStatusBody(BaseModel):
    """
    Status model for SwitchBot Strip Light device.
    SwitchBotストリップライトデバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., Strip Light / デバイスタイプ（例：Strip Light）
    hubDeviceId: str  # Device's parent Hub ID / 親ハブのデバイスID
    power: str  # ON/OFF state / 電源状態（ON/OFF）
    version: str  # The current BLE and Wi-Fi firmware version, e.g., V3.1-6.3 / 現在のBLEとWi-Fiファームウェアバージョン（例：V3.1-6.3）
    brightness: int  # The brightness, range from 1 to 100 / 明るさ（1-100）
    color: str  # The color value, RGB "255:255:255" / RGB色値（"255:255:255"）


class ColorBulbStatusBody(BaseModel):
    """
    Status model for SwitchBot Color Bulb device.
    SwitchBotカラー電球デバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., Color Bulb / デバイスタイプ（例：Color Bulb）
    hubDeviceId: str  # Device's parent Hub ID / 親ハブのデバイスID
    power: str  # ON/OFF state / 電源状態（ON/OFF）
    brightness: int  # Brightness value, range from 1 to 100 / 明るさ（1-100）
    version: str  # Current BLE and Wi-Fi firmware version, e.g., V3.1-6.3 / 現在のBLEとWi-Fiファームウェアバージョン（例：V3.1-6.3）
    color: str  # RGB color value, e.g., "255:255:255" / RGB色値（例："255:255:255"）
    colorTemperature: int  # Color temperature, range from 2700 to 6500 / 色温度（2700-6500）


class HumidifierStatusBody(BaseModel):
    """
    Status model for SwitchBot Humidifier device.
    SwitchBot加湿器デバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., Humidifier / デバイスタイプ（例：Humidifier）
    power: str  # ON/OFF state / 電源状態（ON/OFF）
    humidity: int  # Humidity percentage / 湿度（%）
    temperature: float  # Temperature in Celsius / 温度（摂氏）
    nebulizationEfficiency: int  # Atomization efficiency percentage / 霧化効率（%）
    auto: bool  # Auto Mode status / 自動モード状態
    childLock: bool  # Child lock status / チャイルドロック状態
    sound: bool  # Mute status / 消音状態
    lackWater: bool  # Empty water tank status / 水切れ状態


class Hub2StatusBody(BaseModel):
    """
    Status model for SwitchBot Hub 2 device.
    SwitchBotハブ2デバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceType: str  # Device type, e.g., Hub 2 / デバイスタイプ（例：Hub 2）
    hubDeviceId: str  # Equivalent to device ID / デバイスIDと同じ
    temperature: float  # Temperature in Celsius / 温度（摂氏）
    lightLevel: int  # Level of ambient light, range from 1 to 20 / 周囲の明るさレベル（1-20）
    version: str  # Current firmware version, e.g., V4.2 / 現在のファームウェアバージョン（例：V4.2）
    humidity: int  # Humidity percentage / 湿度（%）


class CirculatorFanStatusBody(BaseModel):
    """
    Status model for SwitchBot Circulator Fan device.
    SwitchBotサーキュレーターデバイスのステータスモデル。
    """
    deviceId: str  # Device ID / デバイスID
    deviceName: str  # Device name / デバイス名
    deviceType: str  # Device type, e.g., Circulator Fan / デバイスタイプ（例：Circulator Fan）
    mode: str  # Fan mode: direct, natural, sleep, or baby / ファンモード：direct、natural、sleep、またはbaby
    version: str  # Current firmware version, e.g., V4.2 / 現在のファームウェアバージョン（例：V4.2）
    power: str  # ON/OFF state / 電源状態（ON/OFF）
    nightStatus: int  # Nightlight status, off or mode 1/2 / ナイトライト状態（オフまたはモード1/2）
    oscillation: str  # Horizontal oscillation state / 水平首振り状態
    verticalOscillation: str  # Vertical oscillation state / 垂直首振り状態
    fanSpeed: int  # Fan speed, range from 1 to 100 / ファン速度（1-100）

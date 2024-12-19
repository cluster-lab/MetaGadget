import re
from typing import Self

from switchbot_client.switchbot_base_client import SwitchBotClientProtocol
from switchbot_client.switchbot_models import SBDeviceStatusResponse, PlugMiniJPStatusBody, BotStatusBody, MeterProCO2StatusBody, MotionSensorStatusBody, StripLightStatusBody, ColorBulbStatusBody, HumidifierStatusBody, Hub2StatusBody, CirculatorFanStatusBody


class SwitchBotDeviceOpsMixin:
    """
    SwitchBotClientMixin provides methods to control SwitchBot devices.
    SwitchBotデバイスごとに固有の操作のfacadesを提供する
    """

    def _turn_on(self: SwitchBotClientProtocol, device_id: str):
        """
        Turn on a SwitchBot device.
        SwitchBotデバイスの電源をオンにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self.commands(device_id, "turnOn")

    def _turn_off(self: SwitchBotClientProtocol, device_id: str):
        """
        Turn off a SwitchBot device.
        SwitchBotデバイスの電源をオフにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self.commands(device_id, "turnOff")

    def _toggle(self: SwitchBotClientProtocol, device_id: str):
        """
        Toggle the power state of a SwitchBot device.
        SwitchBotデバイスの電源状態を切り替える。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self.commands(device_id, "toggle")

    def _set_brightness(self: SwitchBotClientProtocol, device_id: str, brightness: int):
        """
        Set the brightness level of a light device.
        照明デバイスの明るさを設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            brightness (int): Brightness level (1-100).
            brightness (int): 明るさレベル（1-100）。
        """
        assert 1 <= brightness <= 100, "Invalid brightness, should be 1-100"
        return self.commands(device_id, "setBrightness", parameter=brightness)

    def _set_color_temperature(self: SwitchBotClientProtocol, device_id: str, color_temperature: int):
        """
        Set the color temperature of a light device.
        照明デバイスの色温度を設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            color_temperature (int): Color temperature in Kelvin (2700-6500).
            color_temperature (int): 色温度（ケルビン、2700-6500）。
        """
        assert 2700 <= color_temperature <= 6500, "Invalid color temperature, should be 2700-6500"
        return self.commands(device_id, "setColorTemperature", parameter=color_temperature)

    def _set_color(self: SwitchBotClientProtocol, device_id: str, color: str):
        """
        Set the RGB color of a light device.
        照明デバイスのRGB色を設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            color (str): RGB color in format "R:G:B" (0-255 each).
            color (str): RGB色、"R:G:B"形式（各0-255）。
        """
        assert re.match(r"\d{1,3}:\d{1,3}:\d{1,3}", color), "Invalid color format, should be '{0-255}:{0-255}:{0-255}'"
        assert any(0 <= int(c) <= 255 for c in color.split(":")), "Invalid color value, should be 0-255)"
        return self.commands(device_id, "setColor", parameter=color)

    # Humidifier

    def humidifier_turn_on(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn on a SwitchBot Humidifier.
        SwitchBot加湿器の電源をオンにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_on(device_id)

    def humidifier_set_mode(self: SwitchBotClientProtocol | Self, device_id: str, mode: str | int):
        """
        Set the operation mode of a SwitchBot Humidifier.
        SwitchBot加湿器の動作モードを設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            mode (str | int): Mode setting ('auto' or 0-103).
            mode (str | int): モード設定（'auto'または0-103）。
        """
        assert mode == "auto" or 0 <= int(mode) <= 103, "Invalid mode, should be 'auto' or 0-103"
        return self.commands(device_id, "set", parameter=mode)

    def humidifier_turn_off(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn off a SwitchBot Humidifier.
        SwitchBot加湿器の電源をオフにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_off(device_id)

    # Color Bulb

    def bulb_turn_on(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn on a SwitchBot Color Bulb.
        SwitchBotカラー電球の電源をオンにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_on(device_id)

    def bulb_turn_off(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn off a SwitchBot Color Bulb.
        SwitchBotカラー電球の電源をオフにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_off(device_id)

    def bulb_toggle(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Toggle the power state of a SwitchBot Color Bulb.
        SwitchBotカラー電球の電源状態を切り替える。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._toggle(device_id)

    def bulb_set_brightness(self: SwitchBotClientProtocol | Self, device_id: str, brightness: int):
        """
        Set the brightness of a SwitchBot Color Bulb.
        SwitchBotカラー電球の明るさを設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            brightness (int): Brightness level (1-100).
            brightness (int): 明るさレベル（1-100）。
        """
        return self._set_brightness(device_id, brightness)

    def bulb_set_color_temperature(self: SwitchBotClientProtocol | Self, device_id: str, color_temperature: int):
        """
        Set the color temperature of a SwitchBot Color Bulb.
        SwitchBotカラー電球の色温度を設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            color_temperature (int): Color temperature in Kelvin (2700-6500).
            color_temperature (int): 色温度（ケルビン、2700-6500）。
        """
        return self._set_color_temperature(device_id, color_temperature)

    def bulb_set_color(self: SwitchBotClientProtocol | Self, device_id: str, color: str):
        """
        Set the RGB color of a SwitchBot Color Bulb.
        SwitchBotカラー電球のRGB色を設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            color (str): RGB color in format "R:G:B" (0-255 each).
            color (str): RGB色、"R:G:B"形式（各0-255）。
        """
        return self._set_color(device_id, color)

    # Strip Light

    def strip_turn_on(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn on a SwitchBot Strip Light.
        SwitchBotストリップライトの電源をオンにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_on(device_id)

    def strip_turn_off(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn off a SwitchBot Strip Light.
        SwitchBotストリップライトの電源をオフにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_off(device_id)

    def strip_toggle(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Toggle the power state of a SwitchBot Strip Light.
        SwitchBotストリップライトの電源状態を切り替える。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._toggle(device_id)

    def strip_set_brightness(self: SwitchBotClientProtocol | Self, device_id: str, brightness: int):
        """
        Set the brightness of a SwitchBot Strip Light.
        SwitchBotストリップライトの明るさを設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            brightness (int): Brightness level (1-100).
            brightness (int): 明るさレベル（1-100）。
        """
        return self._set_brightness(device_id, brightness)

    def strip_set_color_temperature(self: SwitchBotClientProtocol | Self, device_id: str, color_temperature: int):
        """
        Set the color temperature of a SwitchBot Strip Light.
        SwitchBotストリップライトの色温度を設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            color_temperature (int): Color temperature in Kelvin (2700-6500).
            color_temperature (int): 色温度（ケルビン、2700-6500）。
        """
        return self._set_color_temperature(device_id, color_temperature)

    def strip_set_color(self: SwitchBotClientProtocol | Self, device_id: str, color: str):
        """
        Set the RGB color of a SwitchBot Strip Light.
        SwitchBotストリップライトのRGB色を設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            color (str): RGB color in format "R:G:B" (0-255 each).
            color (str): RGB色、"R:G:B"形式（各0-255）。
        """
        return self._set_color(device_id, color)

    # Smart Plug

    def plug_turn_on(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn on a SwitchBot Smart Plug.
        SwitchBotスマートプラグの電源をオンにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_on(device_id)

    def plug_turn_off(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn off a SwitchBot Smart Plug.
        SwitchBotスマートプラグの電源をオフにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_off(device_id)

    def plug_toggle(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Toggle the power state of a SwitchBot Smart Plug.
        SwitchBotスマートプラグの電源状態を切り替える。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._toggle(device_id)

    # SwitchBot Bot

    def bot_turn_on(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn on a device using SwitchBot Bot.
        SwitchBotボットを使用してデバイスの電源をオンにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_on(device_id)

    def bot_turn_off(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn off a device using SwitchBot Bot.
        SwitchBotボットを使用してデバイスの電源をオフにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_off(device_id)

    def bot_press(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Trigger a press action on SwitchBot Bot.
        SwitchBotボットのプレスアクションを実行する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self.commands(device_id, "press")

    # Circulator Fan

    def circulator_fan_turn_on(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn on a SwitchBot Circulator Fan.
        SwitchBotサーキュレーターの電源をオンにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_on(device_id)

    def circulator_fan_turn_off(self: SwitchBotClientProtocol | Self, device_id: str):
        """
        Turn off a SwitchBot Circulator Fan.
        SwitchBotサーキュレーターの電源をオフにする。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
        """
        return self._turn_off(device_id)

    def circulator_fan_set_night_light_mode(self: SwitchBotClientProtocol | Self, device_id: str, mode: str | int):
        """
        Set the night light mode of a SwitchBot Circulator Fan.
        SwitchBotサーキュレーターのナイトライトモードを設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            mode (str | int): Night light mode ('off', 1 for bright, 2 for dim).
            mode (str | int): ナイトライトモード（'off'、1は明るい、2は暗い）。
        """
        assert mode in ("off", 1, 2), "Invalid mode, should be 'off' (off), 1 (bright), or 2 (dim)"
        return self.commands(device_id, "setNightLightMode", parameter=mode)

    def circulator_fan_set_wind_mode(self: SwitchBotClientProtocol | Self, device_id: str, mode: str):
        """
        Set the wind mode of a SwitchBot Circulator Fan.
        SwitchBotサーキュレーターの風モードを設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            mode (str): Wind mode ('direct', 'natural', 'sleep', or 'baby').
            mode (str): 風モード（'direct'、'natural'、'sleep'、'baby'）。
        """
        assert mode in ("direct", "natural", "sleep", "baby"), \
            "Invalid mode, should be 'direct', 'natural', 'sleep', or 'baby'"
        return self.commands(device_id, "setWindMode", parameter=mode)

    def circulator_fan_set_wind_speed(self: SwitchBotClientProtocol | Self, device_id: str, speed: int):
        """
        Set the wind speed of a SwitchBot Circulator Fan.
        SwitchBotサーキュレーターの風速を設定する。

        Args:
            device_id (str): Device ID to control.
            device_id (str): 制御するデバイスのID。
            speed (int): Wind speed (1-100).
            speed (int): 風速（1-100）。
        """
        assert 1 <= speed <= 100, "Invalid speed, should be between 1 and 100"
        return self.commands(device_id, "setWindSpeed", parameter=speed)

    # get device status

    def bot_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[BotStatusBody]:
        """
        Get the status of a SwitchBot Bot.
        SwitchBotボットのステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[BotStatusBody]: Device status response.
            SBDeviceStatusResponse[BotStatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[BotStatusBody])

    def meter_pro_co2_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[MeterProCO2StatusBody]:
        """
        Get the status of a SwitchBot Meter Pro CO2.
        SwitchBotメータープロCO2のステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[MeterProCO2StatusBody]: Device status response.
            SBDeviceStatusResponse[MeterProCO2StatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[MeterProCO2StatusBody])

    def motion_sensor_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[MotionSensorStatusBody]:
        """
        Get the status of a SwitchBot Motion Sensor.
        SwitchBotモーションセンサーのステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[MotionSensorStatusBody]: Device status response.
            SBDeviceStatusResponse[MotionSensorStatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[MotionSensorStatusBody])

    def plug_mini_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[PlugMiniJPStatusBody]:
        """
        Get the status of a SwitchBot Plug Mini.
        SwitchBotプラグミニのステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[PlugMiniJPStatusBody]: Device status response.
            SBDeviceStatusResponse[PlugMiniJPStatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[PlugMiniJPStatusBody])


    def strip_light_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[StripLightStatusBody]:
        """
        Get the status of a SwitchBot Strip Light.
        SwitchBotストリップライトのステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[StripLightStatusBody]: Device status response.
            SBDeviceStatusResponse[StripLightStatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[StripLightStatusBody])

    def color_bulb_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[ColorBulbStatusBody]:
        """
        Get the status of a SwitchBot Color Bulb.
        SwitchBotカラー電球のステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[ColorBulbStatusBody]: Device status response.
            SBDeviceStatusResponse[ColorBulbStatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[ColorBulbStatusBody])

    def humidifier_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[HumidifierStatusBody]:
        """
        Get the status of a SwitchBot Humidifier.
        SwitchBot加湿器のステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[HumidifierStatusBody]: Device status response.
            SBDeviceStatusResponse[HumidifierStatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[HumidifierStatusBody])

    def hub2_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[Hub2StatusBody]:
        """
        Get the status of a SwitchBot Hub 2.
        SwitchBotハブ2のステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[Hub2StatusBody]: Device status response.
            SBDeviceStatusResponse[Hub2StatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[Hub2StatusBody])

    def circulator_fan_get_device_status(self: SwitchBotClientProtocol | Self, device_id: str) -> SBDeviceStatusResponse[CirculatorFanStatusBody]:
        """
        Get the status of a SwitchBot Circulator Fan.
        SwitchBotサーキュレーターのステータスを取得する。

        Args:
            device_id (str): Device ID to query.
            device_id (str): クエリするデバイスのID。

        Returns:
            SBDeviceStatusResponse[CirculatorFanStatusBody]: Device status response.
            SBDeviceStatusResponse[CirculatorFanStatusBody]: デバイスステータスのレスポンス。
        """
        return self._get_device_status_typed(device_id, SBDeviceStatusResponse[CirculatorFanStatusBody])


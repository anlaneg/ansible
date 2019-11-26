# Copyright: (c) 2017, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ConfigData(object):

    def __init__(self):
        self._global_settings = {}
        self._plugins = {}

    def get_setting(self, name, plugin=None):

        setting = None
        if plugin is None:
            #未指定plugin,自global中取name的配置
            setting = self._global_settings.get(name)
        elif plugin.type in self._plugins and plugin.name in self._plugins[plugin.type]:
            #通过插件类型及插件名，取name的配置
            setting = self._plugins[plugin.type][plugin.name].get(name)

        return setting

    def get_settings(self, plugin=None):

        settings = []
        if plugin is None:
            #未给定plugin,取所有全局配置
            settings = [self._global_settings[k] for k in self._global_settings]
        elif plugin.type in self._plugins and plugin.name in self._plugins[plugin.type]:
            #取插件类型及播件名称下所有key的value
            settings = [self._plugins[plugin.type][plugin.name][k] for k in self._plugins[plugin.type][plugin.name]]

        return settings

    def update_setting(self, setting, plugin=None):
        #按setting的name,value执行更新配置
        if plugin is None:
            self._global_settings[setting.name] = setting
        else:
            if plugin.type not in self._plugins:
                self._plugins[plugin.type] = {}
            if plugin.name not in self._plugins[plugin.type]:
                self._plugins[plugin.type][plugin.name] = {}
            self._plugins[plugin.type][plugin.name][setting.name] = setting

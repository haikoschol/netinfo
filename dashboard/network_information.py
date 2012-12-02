#encoding: utf-8
"""
This module contains functions for obtaining information about network
interfaces using GObject introspection and NetworkManager.

All strings passed to and returned from callables in this module are expected
to be unicode instances.
"""

import socket
import struct

from gi.repository import NetworkManager, NMClient

class NetworkInformation(object):

    def __init__(self):
        self.nmc = NMClient.Client.new()
        self.devices = self.nmc.get_devices()

    def get_interfaces(self):
        """
        Return a list of dicts with information about all network interfaces on the host.
        """
        return [format_device_info(d) for d in self.devices]

    def get_current_wifi_ssid(self):
        """
        Return the SSID of the wireless network that this host is currently connected to.
        """
        for dev in self.devices:
            if dev.get_device_type() == NetworkManager.DeviceType.WIFI:
                active_ap = dev.get_active_access_point()
                if active_ap:
                    return active_ap.get_ssid().decode('utf-8')

        return u''

    def get_visible_wifi_ssids(self):
        """
        Return a list of SSIDs of all currently visible wireless networks.
        """
        ssids = []

        for dev in self.devices:
            if dev.get_device_type() == NetworkManager.DeviceType.WIFI:
                for ap in dev.get_access_points():
                    ssids.append(ap.get_ssid().decode('utf-8'))

        return ssids


def format_device_info(device):
    """
    Extract data about the passed NMClient.Device instance into a dict.
    """
    info = {}
    info[u'name'] = device.get_iface()
    info[u'type'] = device.get_device_type().value_nick
    info[u'state'] = device.get_state().value_nick
    info[u'ip4_addresses'] = format_ip4_addresses(device.get_ip4_config())
    info[u'ip6_addresses'] = format_ip6_addresses(device.get_ip6_config())

    for key in info.keys():
        value = info[key]
        if isinstance(value, str): 
            info[key] = value.decode('utf-8')

    return info


def format_ip4_addresses(cfg):
    """
    Extract all IPv4 addresses from the passed NMIP4Config instance and return a
    list of strings in dotted quad notation.
    """
    if not cfg:
        return []

    addresses = []
    for addr_cfg in cfg.get_addresses():
       packed = struct.pack('>L', socket.htonl(addr_cfg.get_address()))
       ipaddr = socket.inet_ntoa(packed)
       addresses.append(ipaddr.decode('utf-8'))

    return addresses


def format_ip6_addresses(cfg):
    """
    Return a list of all IPv6 addresses from the passed NMIP6Config instance.
    """
    if not cfg:
        return []

    return [unicode(a.get_address()) for a in cfg.get_addresses()]


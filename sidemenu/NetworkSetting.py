from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os
import socket
import psutil
import subprocess
import ipaddress

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class NetSetting(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        # self.setWindowModality(Qt.ApplicationModal)

        self.setWindowTitle("Network Setting")
        self.setStyleSheet(style)

        self.w.ifList_cb.addItems(psutil.net_if_addrs().keys())
        self.w.ipSetting_cb.addItems(["Manual (Static IP)", "Automatic (DHCP)"])
        self.w.ipSetting_cb.currentIndexChanged.connect(self.on_ip_setting_changed)
        self.w.ifList_cb.currentIndexChanged.connect(self.on_ip_setting_changed)
        self.on_ip_setting_changed()

    def on_ip_setting_changed(self):
        if self.w.ipSetting_cb.currentText() == "Automatic (DHCP)":
            print(self.get_ip_network())
            self.dhcp_generate()
            self.set_manual_fields_enabled(False)
        else:
            self.w.ipAddr_edit.setText("")
            self.w.netMask_edit.setText("")
            self.w.gateaway_edit.setText("")
            self.w.dns1_edit.setText("")
            self.w.dns2_edit.setText("")
            self.set_manual_fields_enabled(True)
        self.update_network_speed()       

    def set_manual_fields_enabled(self, enabled):
        self.w.ipAddr_edit.setEnabled(enabled)
        self.w.netMask_edit.setEnabled(enabled)
        self.w.gateaway_edit.setEnabled(enabled)
        self.w.dns1_edit.setEnabled(enabled)
        self.w.dns2_edit.setEnabled(enabled)
        self.w.netSpeed_edit.setEnabled(False)
    
    def get_ip_network(self):
        interface = self.w.ifList_cb.currentText()
        if interface == "lo":
            self.w.ipAddr_edit.setText("")
            self.w.netMask_edit.setText("")
            self.w.gateaway_edit.setText("")
            self.w.dns1_edit.setText("")
            self.w.dns2_edit.setText("")
            return None
        
        elif interface in psutil.net_if_addrs():
            addrs = psutil.net_if_addrs()[interface]    # ip address
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ip_address = addr.address
                    netmask = addr.netmask
                    ip_network = ipaddress.ip_network(f"{ip_address}/{self.get_prefix(netmask)}", strict=False)
                    return ip_network
        print(f"Interface {interface} was not found or does not have an IP address.")
        return None

    def get_prefix(self, netmask):
        """Mengubah netmask menjadi prefix"""
        netmask = ipaddress.ip_address(netmask)
        for prefix in range(32, -1, -1):
            if ipaddress.ip_network(f'0.0.0.0/{prefix}').netmask == netmask:
                return prefix
        return 24  # Default prefix

    def find_available_ip(self, ip_network):
        for ip in ip_network.hosts():
            if not self.ping(str(ip)):
                return str(ip)
        return None

    def ping(self, ip):
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
        return result.returncode == 0

    def update_network_speed(self):
        interface = self.w.ifList_cb.currentText()
        if interface in psutil.net_if_stats():
            stats = psutil.net_if_stats()[interface]
            speed = f"{stats.speed} Mbps"
            self.w.netSpeed_edit.setText(speed)
        else:
            self.w.netSpeed_edit.setText("N/A")


    def dhcp_generate(self):
        ip_network = self.get_ip_network()
        if ip_network:
            available_ip = self.find_available_ip(ip_network)
            print(available_ip)
            if available_ip:
                self.w.ipAddr_edit.setText(available_ip)
                self.w.netMask_edit.setText(str(ip_network.netmask))  # Set netmask
                self.w.gateaway_edit.setText(f"{ip_network.network_address + 1}")    # Gateway 192.168.x.1
                self.w.dns1_edit.setText("8.8.8.8")  # DNS Google
                self.w.dns2_edit.setText("8.8.4.4")  # DNS Google
                self.w.netSpeed_edit.setText(str(0))
            else:
                print("There are no IPs available in that range.")
        else:
            print("Unable to determine IP range.")

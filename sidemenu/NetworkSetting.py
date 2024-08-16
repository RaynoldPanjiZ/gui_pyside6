from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QRegularExpression
from PySide6.QtNetwork import QHostAddress
from PySide6.QtGui import QRegularExpressionValidator
import re
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
        self.w.btn_cancel.clicked.connect(self.close)
        self.w.btn_save.clicked.connect(self.applyConfig)

        self.w.ifList_cb.addItems(psutil.net_if_addrs().keys())
        self.w.ipSetting_cb.addItems(["Manual (Static IP)", "Automatic (DHCP)"])
        self.w.ipSetting_cb.currentIndexChanged.connect(self.on_ip_setting_changed)
        self.w.ifList_cb.currentIndexChanged.connect(self.on_ip_setting_changed)
        self.on_ip_setting_changed()

    def on_ip_setting_changed(self):
        if self.w.ipSetting_cb.currentText() == "Automatic (DHCP)":
            self.updateDHCPInfo()
            self.set_manual_fields_enabled(False)
        else:
            self.w.ipAddr_edit.setText("")
            self.w.netMask_edit.setText("")
            self.w.gateway_edit.setText("")
            self.w.dns1_edit.setText("")
            self.w.dns2_edit.setText("")
            self.set_manual_fields_enabled(True)
            # ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # Part of the regular expression
            # # Regulare expression
            # ipRegex = QRegularExpression("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
            # ipValidator = QRegularExpressionValidator(ipRegex, self)
            # print(ipValidator)
            # self.w.ipAddr_edit.setValidator(ipValidator)  # https://evileg.com/en/post/57/

        self.update_network_speed()       

    def set_manual_fields_enabled(self, enabled):
        interface = self.w.ifList_cb.currentText()
        if interface == "lo":
            self.w.btn_save.setEnabled(False)
        else:
            self.w.ipAddr_edit.setEnabled(enabled)
            self.w.netMask_edit.setEnabled(enabled)
            self.w.gateway_edit.setEnabled(enabled)
            self.w.dns1_edit.setEnabled(enabled)
            self.w.dns2_edit.setEnabled(enabled)
            self.w.netSpeed_edit.setEnabled(False)
            self.w.btn_save.setEnabled(True)
        
    

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


    def updateDHCPInfo(self):       # https://docs.python.org/3/howto/ipaddress.html
        interface = self.w.ifList_cb.currentText()
        if interface == "lo":
            self.w.ipAddr_edit.setText("")
            self.w.netMask_edit.setText("")
            self.w.gateway_edit.setText("")
            self.w.dns1_edit.setText("")
            self.w.dns2_edit.setText("")
            self.w.btn_save.setEnabled(False)
        else:
            command = f"ip a | grep 'inet ' | grep {interface}"
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            result = process.communicate()[0].decode().strip()

            if result:
                ip_info = result.split()[1].split('/')
                self.w.ipAddr_edit.setText(ip_info[0])
                
                print(str(result.split()[1]))
                net4 = ipaddress.ip_network(str(result.split()[1]), False)
                self.w.netMask_edit.setText(str(net4.netmask))

                command_gateway = f"ip route | grep default | grep {interface}"
                process_gateway = subprocess.Popen(command_gateway, shell=True, stdout=subprocess.PIPE)
                gateway_result = process_gateway.communicate()[0].decode().strip()
                if gateway_result:
                    gateway_ip = gateway_result.split()[2]
                    self.w.gateway_edit.setText(gateway_ip)

                self.w.dns1_edit.setText("8.8.8.8")  # DNS Google
                self.w.dns2_edit.setText("8.8.4.4")  # DNS Google
            self.w.btn_save.setEnabled(True)

    def validate_input(self, ip_address, netmask, gateway, dns1, dns2):
        ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if not ip_pattern.match(ip_address):
            QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The IP address {ip_address} is not valid")
            return False
        else:
            bytes = ip_address.split(".")  
            for i, ip_byte in enumerate(bytes):  
                if int(ip_byte) < 1 or int(ip_byte) > 254:  
                    QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The IP address {ip_address} is not valid")
                    return False  
                
                if i == 3:
                    if int(ip_byte) < 199 or int(ip_byte) > 254:  
                        QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The IP address {ip_address} is not valid \n make sure that the Host ID is not under .200")
                        return False  
            print(f"The IP address {ip_address} is valid") 
        
        mask_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if not mask_pattern.match(netmask):
            QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The Net Mask {netmask} is not valid")
            return False
        else:
            bytes = netmask.split(".")  
            for ip_byte in bytes:  
                if int(ip_byte) < 0 or int(ip_byte) > 255:  
                    QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The Net Mask {netmask} is not valid")
                    return False  
            print(f"The NetMask {netmask} is valid")

        gateway_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if not gateway_pattern.match(gateway):
            QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The Gateway {gateway} is not valid")
            return False
        else:
            bytes = gateway.split(".")  
            for ip_byte in bytes:  
                if int(ip_byte) < 1 or int(ip_byte) > 254:  
                    QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The Gateway {gateway} is not valid")
                    return False  
            print(f"The Gateway {gateway} is valid")

        dns1_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if not dns1_pattern.match(dns1):
            QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The DNS 1 {dns1} is not valid")
            return False
        else:
            bytes = dns1.split(".")  
            for ip_byte in bytes:  
                if int(ip_byte) < 1 or int(ip_byte) > 254:   
                    QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The DNS 1 {dns1} is not valid")
                    return False  
            print(f"The DNS-1 {dns1} is valid")

        dns2_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if not dns2_pattern.match(dns2):
            QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The DNS 2 {dns2} is not valid")
            return False
        else:
            bytes = dns2.split(".")  
            for ip_byte in bytes:  
                if int(ip_byte) < 1 or int(ip_byte) > 254: 
                    QtWidgets.QMessageBox.critical(self, "Invalid Input", f"The DNS 2 {dns2} is not valid")
                    return False  
            print(f"The DNS-2 {dns2} is valid") 
        QtWidgets.QMessageBox.about(self, "Valid Input", f"Network configuration is valid")
        return True


    def applyConfig(self):
        if self.w.ipSetting_cb.currentText() == "Automatic (DHCP)":
            pass
        else:
            ipaddr = self.w.ipAddr_edit.text()
            netmask =  self.w.netMask_edit.text()
            gateway = self.w.gateway_edit.text()
            dns1 = self.w.dns1_edit.text()
            dns2 = self.w.dns2_edit.text()  
            if not ipaddr or not netmask or not gateway or not dns1 or not dns2:
                QtWidgets.QMessageBox.critical(self, "Empty Fields", "All fields must be filled out.")
            else:
                print(self.validate_input(ipaddr, netmask, gateway, dns1, dns2))
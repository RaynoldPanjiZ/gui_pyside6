from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QTimer, QDate, QDateTime
import sys, os
import json
from datetime import datetime

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class SystemLog(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("System Settings")
        self.setStyleSheet(style)
        self.w.btn_close.clicked.connect(self.close)
        self.w.btn_autoDel.clicked.connect(self.auto_delete)
        self.w.btn_manualDel.clicked.connect(self.manual_delete)
        self.w.btn_search.clicked.connect(self.handle_filter)
        
        date_str = datetime.today().strftime('%Y-%m-%d')
        qdate = QDate.fromString(date_str, "yyyy-MM-dd")
        self.w.periodEnd_filter.setDate(qdate)

        self.curr_page = 1


        self.datas = []
        self.filtered_datas = []
        self.added_new_log = set()
        self.filter_log = False
        self.added_new_period = set()
        self.filter_date_start = False
        self.filter_date_end = False
        if os.path.exists('./datas/systemLog.json'):
            f = open('./datas/systemLog.json')
            self.datas = json.load(f)
    
        self.timer_fetch = QTimer()
        self.timer_fetch.timeout.connect(self.update_table)
        self.timer_fetch.start(700)
    
    def update_table(self):
        new_log = sorted(set(item["log_division"] for item in self.datas if item["log_division"] not in self.added_new_log))
        new_period = sorted(set(item["event_time"] for item in self.datas if item["event_time"] not in self.added_new_period))
        self.added_new_log.update(new_log)
        self.added_new_period.update(new_period)
        self.w.logDivision_filter.addItems(new_log)

        tb_show = self.w.tb_show
        
        header = tb_show.horizontalHeader()
        header.setMinimumHeight(34)
        header.setDefaultAlignment(Qt.AlignCenter | Qt.Alignment(Qt.TextWordWrap))
        for i in range(tb_show.columnCount()):
            if i == 0:
                tb_show.setColumnWidth(i, 20)
            else:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        data_to_show = self.filtered_datas if self.filter_log else self.datas
        position_start, position_end, num_perpage = self.numpage_filter(data_to_show)
        tb_show.setRowCount(num_perpage)
        if data_to_show:
            for idx, data_num in enumerate(range(position_start, position_end)):
                it = QtWidgets.QTableWidgetItem(str(data_num+1))
                it.setTextAlignment(Qt.AlignCenter)
                tb_show.setItem(int(idx), 0, it)
                for i, (key, value) in enumerate(data_to_show[data_num].items()):
                    if key == "id": continue
                    it = QtWidgets.QTableWidgetItem(str(value))
                    it.setTextAlignment(Qt.AlignCenter)
                    tb_show.setItem(int(idx), i, it)
                    # tb_show.cellClicked.connect(self.selected_row)
    
    def data_operation_pages(self, event):
        print("clicked:", event)
        self.curr_page = event

    def numpage_filter(self, data_to_show):
        import math
        num_perpage = int(self.w.numDisplay_filter.currentText())
        total_page = len(data_to_show) / num_perpage
        total_page = int(math.ceil(total_page))
        if self.curr_page > total_page:
            self.data_operation_pages(1)

        pg_layout = self.w.pages_frame.layout()
        while pg_layout.count():
            item = pg_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        btnpage = [QtWidgets.QPushButton(str(i + 1)) for i in range(total_page)]

        spacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        pg_layout.addItem(spacer1)
        prev_btn = QtWidgets.QPushButton("<<")
        prev_btn.clicked.connect(lambda :self.data_operation_pages(1))
        prev_btn.setFixedSize(30, 30)
        pg_layout.addWidget(prev_btn)
        for i, btn in enumerate(btnpage):
            btn.setFixedSize(30, 30)
            btn.setObjectName("pg_"+str(i))
            btn.clicked.connect(lambda _, x=i:self.data_operation_pages(x+1))
            pg_layout.addWidget(btn)
        next_btn = QtWidgets.QPushButton(">>")
        next_btn.setFixedSize(30, 30)
        next_btn.clicked.connect(lambda :self.data_operation_pages(total_page))
        pg_layout.addWidget(next_btn)
        spacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        pg_layout.addItem(spacer1)
        self.w.pages_frame.setLayout(pg_layout)

        if btnpage:
            btnpage[self.curr_page -1].setEnabled(False)
        if self.curr_page == 1:
            prev_btn.setEnabled(False)
        if self.curr_page == total_page or total_page == 0:
            next_btn.setEnabled(False)

        position_end = num_perpage * self.curr_page
        position_start = position_end - (position_end - (num_perpage*(self.curr_page-1)))
        
        if len(data_to_show) <= 0:
            position_start = 0
            position_end = 0
            return position_start, position_end, 0
        elif len(data_to_show) < num_perpage:
            position_start = 0
            position_end = len(data_to_show)
            return position_start, position_end, position_end
        elif len(data_to_show) < position_end:
            position_end = len(data_to_show)
            return position_start, position_end, position_end - position_start
        else:
            return position_start, position_end, num_perpage
    
    def handle_filter(self):
        self.filter_log = not self.filter_log
        self.filter_date_start = not self.filter_date_start
        self.filter_date_end = not self.filter_date_end
        if self.filter_log:
            self.w.btn_search.setText("Searching...")
        
            log_filter = self.w.logDivision_filter.currentText()
            dateStart_filter = self.w.periodStart_filter.date()
            dateEnd_filter = self.w.periodEnd_filter.date()

            print(f"Filter: {log_filter}, {dateStart_filter}, {dateStart_filter}")
            self.filtered_datas = []
            for data in self.datas:
                log_match = log_filter == 'Entire' or data["log_division"] == log_filter
                
                periodfilter = QDate.fromString(data["event_time"].split(' ')[0], 'yyyy-MM-dd')
                period_match = dateStart_filter <= periodfilter <= dateEnd_filter

                if log_match and period_match:
                    self.filtered_datas.append(data)
                    
                print(f"Filter Data: {self.filtered_datas}")
        else:
            self.w.btn_search.setText("Search")
            self.filtered_datas = []

    def auto_delete(self):
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/system_log/auto_delete_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.cancel_btn.clicked.connect(self.close)
        self.popup.setWindowTitle("Auto-Delete System Logs")
        self.popup.exec()

    def manual_delete(self):
        print("Success!")
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/system_log/manually_delete.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = ManualDeleteLogs(dialog)
        self.popup.show()
        self.close()
        


class ManualDeleteLogs(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Manually Delete System Logs")
        self.setStyleSheet(style)
        self.w.btn_close.clicked.connect(self.close)
        self.w.btn_search.clicked.connect(self.handle_filter)
        
        date_str = datetime.today().strftime('%Y-%m-%d')
        qdate = QDate.fromString(date_str, "yyyy-MM-dd")
        self.w.periodEnd_filter.setDate(qdate)

        self.datas = []
        self.filtered_datas = []
        self.added_new_period = set()
        self.filter_log = False
        if os.path.exists('./datas/systemLog.json'):
            f = open('./datas/systemLog.json')
            self.datas = json.load(f)
        
        self.timer_fetch = QTimer()
        self.timer_fetch.timeout.connect(self.update_table)
        self.timer_fetch.start(300)
    
    def update_table(self):
        new_period = sorted(set(item["event_time"] for item in self.datas if item["event_time"] not in self.added_new_period))
        self.added_new_period.update(new_period)

        tb_show = self.w.tb_show
        tb_show.setRowCount(len(self.datas))
        
        header = tb_show.horizontalHeader()
        header.setMinimumHeight(34)
        header.setDefaultAlignment(Qt.AlignCenter | Qt.Alignment(Qt.TextWordWrap))
        for i in range(tb_show.columnCount()):
            if i == 0:
                tb_show.setColumnWidth(i, 20)
            else:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        data_to_show = self.filtered_datas if self.filter_log else self.datas
        tb_show.setRowCount(len(data_to_show))
        if data_to_show:
            for idx, data_num in enumerate(range(len(data_to_show))):
                it = QtWidgets.QTableWidgetItem(str(idx+1))
                it.setTextAlignment(Qt.AlignCenter)
                tb_show.setItem(int(idx), 0, it)
                for i, (key, value) in enumerate(data_to_show[data_num].items()):
                    if key == "id": continue
                    it = QtWidgets.QTableWidgetItem(str(value))
                    it.setTextAlignment(Qt.AlignCenter)
                    tb_show.setItem(int(idx), i, it)
                    # tb_show.cellClicked.connect(self.selected_row)
    
    def handle_filter(self):
        self.filter_log = not self.filter_log
        if self.filter_log:
            self.w.btn_search.setText("Searching...")
        
            dateStart_filter = self.w.periodStart_filter.date()
            dateEnd_filter = self.w.periodEnd_filter.date()

            print(f"Filter: {dateStart_filter}, {dateStart_filter}")
            self.filtered_datas = []
            for data in self.datas:                
                periodfilter = QDate.fromString(data["event_time"].split(' ')[0], 'yyyy-MM-dd')
                period_match = dateStart_filter <= periodfilter <= dateEnd_filter

                if period_match:
                    self.filtered_datas.append(data)
                    
                print(f"Filter Data: {self.filtered_datas}")
        else:
            self.w.btn_search.setText("Search")
            self.filtered_datas = []
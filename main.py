# import sys
# import os
# from PySide6 import QtSvg
# from PyQt6.QtWidgets import QApplication
# from PyQt6.QtCore import Qt
# from PyQt5.QtCore import *
# from qt_material import *
# import psutil
# from multiprocessing import cpu_count
# import datetime
# from platform import platform
# from shutil import disk_usage
# import shutil
# from time import sleep
# from tkinter.ttk import Progressbar, Sizegrip
# from turtle import position
# from tkinter import *
# from unicodedata import name
# from ui_interface import *
import sys
import os
#from PySide2 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_material import *
import psutil
from PySide2extn import *
from multiprocessing import cpu_count
import datetime
import platform
import shutil
from ui_interface import *

platforms = {
    'linux' : 'Linux',
    'linux1': 'Linux',
    'linux2' : 'Linux',
    'drawin': 'OS x',
    'win32': 'Windowa'
    
}

# ui->py pyuic5 interface.ui -o ui_interface2.py


# mainwindow class
class MainWindow (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        apply_stylesheet(app, theme='dark_eyan.xml')

        # remov window title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(2, 92, 157, 550))
        # apply shadow to central wiget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        # set window icon
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/airplay.svg"))
        # set window title
        self.setWindowTitle("UTTL Manaher")
        # window Size grip to resize window
        Sizegrip(self.ui.size_grip)
        # minimize
        self.ui.minimize_window_button.clicked.connect(
            lambda: self.showMinimized())
        # close
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        # restore/maximize
        self.ui.restore_window_button.clicked.connect(
            lambda: self.restore_or_maximize_window())

        # stacked page navigation
        # cpu
        self.ui.cpu_info_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))
        # battry
        self.ui.battry_info_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battrey))
        # systrm info
        self.ui.system_info_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_information))
        # activity
        self.ui.activity_info_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activities))
        # storage
        self.ui.storage_info_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.stroage))
        # sensors
        self.ui.sensors_info_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
        # neytwork
        self.ui.network_info_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.networks))

    # moving window on mouse drag on title bar
        def moveWindow(e):
            # detect normal size
            if self.isMaximize() == False:  # not maximize
                # move window when window is normal
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # move
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        # add click event to the top header to move window
        self.ui.header_frame.mouseMoveEvent = moveWindow
        # left menu toggle button
        self.ui.open_close_side_bar_btn.clicked.connect(
            lambda: self.slideLeftMenu())

        for w in self.ui.menu_frame.findChildren(QPushButton):
            # add click event listerner
            w.clicked.connect(self.applyButtonStyle)

        self.show()
        self.battery()
        self.cpu_ram()
        self.system_info()
        self.processes()
        self.storage()
        self.sensors()
        self.network()
        
        
    #netWork Function
    def network(self):
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()
            
            rowPosition = self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition, 0, x, "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].isup), "net_stats_table")
            self.create_table_widget(rowPosition, 2, str(z[x].duplex), "net_stats_table")
            self.create_table_widget(rowPosition, 3, str(z[x].speed), "net_stats_table")
            self.create_table_widget(rowPosition, 4, str(z[x].mtu), "net_stats_table")

            #io
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)
            rowPosition = self.ui.net_io_table.rowCount()
            self.ui.net_io_table.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition, 0, x, "net_io_table")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_sent), "net_io_table")
            self.create_table_widget(rowPosition, 2, str(z[x].bytes_recv), "net_io_table")
            self.create_table_widget(rowPosition, 3, str(z[x].packets_sent), "net_io_table")
            self.create_table_widget(rowPosition, 4, str(z[x].packets_recv), "net_io_table")
            self.create_table_widget(rowPosition, 5, str(z[x].errin), "net_io_table")
            self.create_table_widget(rowPosition, 6, str(z[x].errout), "net_io_table")
            self.create_table_widget(rowPosition, 7, str(z[x].dropin), "net_io_table")
            self.create_table_widget(rowPosition, 8, str(z[x].dropout), "net_io_table")
        #addrsss
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()
            for y in z[x]:
                
                rowPosition = self.ui.net_addresses_table.rowCount()
                self.ui.net_addresses_table.insertRow(rowPosition)
            
                self.create_table_widget(rowPosition, 0, str(x), "net_addresses_table")
                self.create_table_widget(rowPosition, 1, str(y.family), "net_addresses_table")
                self.create_table_widget(rowPosition, 2, str(y.address), "net_addresses_table")
                self.create_table_widget(rowPosition, 3, str(y.netmask), "net_addresses_table")
                self.create_table_widget(rowPosition, 4, str(y.broadcast), "net_addresses_table")
                self.create_table_widget(rowPosition, 5, str(y.ptp), "net_addresses_table")
        #connection       
                 
        for x in psutil.net_connections():
            z = psutil.net_connections()
            rowPosition = self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition, 0, str(x.fd), "net_connections_table")
            self.create_table_widget(rowPosition, 1, str(x.family), "net_connections_table")
            self.create_table_widget(rowPosition, 2, str(x.type), "net_connections_table")
            self.create_table_widget(rowPosition, 3, str(x.laddr), "net_connections_table")
            self.create_table_widget(rowPosition, 4, str(x.raddr), "net_connections_table")
            self.create_table_widget(rowPosition, 5, str(x.status), "net_connections_table")
            self.create_table_widget(rowPosition, 6, str(x.pid), "net_connections_table")
    #sensor information
    
    def sensors(self):
        if sys.platform =='linux' or sys.platform =='linux1' or sys.platform == 'linux2':
            for x in psutil.sensors_temperatures():
                for y in psutil.sensors_temperatures()(x):
                    rowPosition = self.ui.sensorTable.rowCount()
                    self.ui.sensorTable.inssertRow(rowPosition)
                    
                    self.create_table_widget(rowPosition, 0, x, "sensorTable")
                    self.create_table_widget(rowPosition, 1, y.label, "sensorTable")
                    self.create_table_widget(rowPosition, 2, str(y.current), "sensorTable")
                    self.create_table_widget(rowPosition, 3, str(y.high), "sensorTable")
                    self.create_table_widget(rowPosition, 4, str(y.critical), "sensorTable")
                    
                    temp_per =(y.current / y.high) * 100
                    progressBar = QProgressBAr(self.ui.sensorTable)
                    progressBar.setObjectName(u"ProgressBar")
                    progressBar.setValue(temp_per)
                    self.ui.sensorTable.setCellWidget(rowPosition, 5, progressBar)
        else:
            global platforms
            
            rowPosition = self.ui.sensorTable.rowCount()
            self.ui.sensorTable.insertRow(rowPosition)
            self.create_table_widget(rowPosition,0,"Function not supported on " + platforms[sys.platform], "sensorTable")
             
            self.create_table_widget(rowPosition, 1, "N/A", "sensorTable" )
            self.create_table_widget(rowPosition, 2, "N/A", "sensorTable" )
            self.create_table_widget(rowPosition, 3, "N/A", "sensorTable" )
            self.create_table_widget(rowPosition, 4, "N/A", "sensorTable" )
            self.create_table_widget(rowPosition, 5, "N/A", "sensorTable" )
            
                   
                    
        
    def storage(self):
        global platforms
        storage_device = psutil.disk_partitions(all=False)
        z=0
        for x in storage_device:
            rowPosition = self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, x.device, "storageTable")
            self.create_table_widget(rowPosition, 1, x.mountpoint, "storageTable")
            self.create_table_widget(rowPosition, 2, x.fstype, "storageTable")
            self.create_table_widget(rowPosition, 3, x.opts, "storageTable")
            
            if sys.platform == 'linux' or sys.platform =='linux1' or sys.platform =='linux2':
                self.create_table_widget(rowPosition, 4, str(x.maxfile), "storageTable")
                self.create_table_widget(rowPosition, 5, str(x.maxpath), "storageTable")
            else:
                self.create_table_widget(rowPosition, 4, "Function not avilable on " + platforms[sys.platform], "storageTable")
                self.create_table_widget(rowPosition, 5, "Function not avilable on " + platforms[sys.platform], "storageTable")
        
        disk_usage = shutil.disk_usage(x.mountpoint)
        self.create_table_widget(rowPosition, 6, str((disk_usage.total / (1024*1024*1024))) + "GB", "storageTable")
        self.create_table_widget(rowPosition, 6, str((disk_usage.free / (1024*1024*1024))) + "GB", "storageTable")   
        self.create_table_widget(rowPosition, 6, str((disk_usage.used / (1024*1024*1024))) + "GB", "storageTable")   
        
        
        full_disk = (disk_usage.used / disk_usage.total) * 100
        progressBar = QProgressBar(self.ui.stroageTable)  
        progressBar.setObjectName(u"progressBar") 
        progressBar.setValue(full_disk)
        self.ui.stroageTable.setCellWidget(rowPosition, 9, progressBar)            
        
    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetItem = QTableWidgetItem()
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetItem)
        qtablewidgetItem=getattr(self.ui, tableName).item(rowPosition, columnPosition)
        qtablewidgetItem.setText(text);
            
        
        #Running process
    def processes(self):
        for x in psutil.pids():
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            
            try:
                process = psutil.Process(x)
                
                self.create_table_widget(rowPosition, 0, str(process.pid), "tableWidget")
                self.create_table_widget(rowPosition, 1, process.name(), "tableWidget")
                self.create_table_widget(rowPosition, 2, process.status(), "tableWidget")
                self.create_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')), "tableWidget")
                
                
                suspend_btn = QPushButton(self.ui.tableWidget)
                suspend_btn.setText('Suspended')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.tableWidget.setCellWidget(rowPosition, 4, suspend_btn)
                
                rusume_btn = QPushButton(self.ui.tableWidget)
                rusume_btn.setText('Resume')
                rusume_btn.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition, 5, rusume_btn)
                
                
                terminating_btn = QPushButton(self.ui.tableWidget)
                terminating_btn.setText('Terminating')
                terminating_btn.setStyleSheet("color: orange")
                self.ui.tableWidget.setCellWidget(rowPosition, 6, terminating_btn)
                
                kill_btn = QPushButton(self.ui.tableWidget)
                kill_btn.setText('Kill')
                kill_btn.setStyleSheet("color: red")
                self.ui.tableWidget.setCellWidget(rowPosition, 7, kill_btn)
            except Exception as e:
                print(e)
                
            
            self.ui.activity_search.textChanged.connect(self.findName)
         
     #search activity       
    def findName(self):
        name= self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rawCount()):
            item = self.ui.tableWidget.item(row, 1)
            self.ui.tableWidget.setRowHidden(row, name not in item.text().lower())
            
            
        
        
                        
        
        #system info
    def system_info(self):
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.ui.system_date.setText(str(time))
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.system_time.setText(str(date))
        
        self.ui.system_machine.setText(platform.machine())
        self.ui.system_version.setText(platform.version())
        self.ui.system_platform.setText(platform.platform())
        self.ui.system_system.setText(platform.system())
        self.ui.system_processor.setText(platform.processor())
                
        
        
    def cpu_ram(self):
        totalRam =  1.0
        totalRam = psutil.virtual_memory()[0]+totalRam
        totalRam = totalRam / (1024*1024*1024)
        self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + 'GB'))
        
        avilRam= 1.0
        avilRam= psutil.virtual_memory()[1] * avilRam
        avilRam= avilRam/(1024*1024*1024)
        self.ui.avilable_ram.setText(str("{:.4f}".format(avilRam) + 'GB'))
        
        ramUsed =1.0
        ramUsed= psutil.virtual_memory()[3] * ramUsed
        ramUsed= ramUsed/(1024*1024*1024)
        self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + 'GB'))

        ramFree =1.0
        ramFree= psutil.virtual_memory()[3] * ramFree
        ramFree= ramFree/(1024*1024*1024)
        self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + 'GB'))
        ramUsed = str(psutil.virtual_memory()[2]) + '%'
        self.ui.ram_usage.setText(str("{:.4f}".format(totalRam) + 'GB'))
        
        core = cpu_count()
        self.ui.cpu_count.setText(str(core))
        
        cpuPer = psutil.cpu_percent()
        self.ui.cpu_per.setText(str(cpuPer)+ "%"  )
        
        cpuMainCore = psutil.cpu_count(logical=False)
        self.ui.cpu_main_core.setText(str(cpuMainCore))
        
        #cpu indicatror
        self.ui.cpu_percentage.rpb_setMaximum(100)
        self.cpu_percentage.rpb_setValue(cpuPer)
        self.cpu_percentage.rpb_setBarStyle('Hybrid2')
        self.cpu_percentagee.rpb_setLineColor((255, 30, 99))
        self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
        self.ui.cpu_percentage.rpb_setTextColor((255, 255, 255))
        self.ui.cpu_percentage.rpb_setInitialPos('West')
        self.ui.cpu_percentage.rpb_setTextFormat('pecentage')
        self.ui.cpu_percentage.rpb_setTextFont('Aeial')
        self.ui.cpu_percentage.rpb_setLineWidth(15)
        self.ui.cpu_percentage.rpb_setPathWidth(15)
        self.ui.cpu_percentage.rpb_setLineCap('RoundCap')
        
        
        #Ram usage indicator
        self.ui.ram_percentage.spb_setMinimum((0,0,0,0))
        
        self.ui.ram_percentage.spb_setMaximum((totalRam, totalRam, totalRam))
         
        self.ui.ram_percentage.spb_setValue((avilRam, ramUsed,ramFree))       
        
        self.ui.ram_percentage.spb_lineColor(((6,233,38),(6,201,233),(233,6.201)))
        
        self.ui.ram_percentage.spb_setInitialPos(('West','West','West'))
        self.ui.ram_percentage.spb_lineWidth(15)
        self.ui.ram_percentage.spb_lineStyle(('SolidLine','SolidLine','SolidLine'))
        self.ui.ram_percentage.spb_lineCap(('RoundCap','RoundCap','RoundCap'))
        self.ui.ram_percentage.spb_setPathHodden(True)
        
        
    def secs2hours (self, secs):
        mm, ss = divmod(secs, 60)
        hh, ss = divmod(mm, 60) 
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)
    

    def battery(self):
        batt = psutil.sensor_battry()

        if not hasattr(psutil, "sensors_battery"):
            self.ui.battery_status.setText("Platform not supported!")
        if batt is None:
            self.ui.battery_status.setText("NO Battery Installed!")
        if batt.power_plugged:
            self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
            self.ui.battery_time_left.setText("N/A")
            if batt.percent < 100:
                self.ui.battery_status.setText("Charging")
            else:
                self.ui.battrey_status.setText("Fully charged")
            self.ui.battery_plugged.setText("yes")
        else:
            self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
            self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))

            if batt.percent < 100:
                self.ui.battery_status.setText("Discharging")
            else:
                self.ui.battrey_status.setText("Fully charged")
            self.ui.battery_plugged.setText("No")

        # battery power inductor using  round progress bar
        self.ui.battery_usage.rpb_setMaximum(100)
        self.battery_usage.rpb_setValue(batt.percent)
        self.battery_usage.rpb_setBarStyle('Hybrid2')
        self.battery_usage.rpb_setLineColor((255, 30, 99))
        self.ui.battery_usage.rpb_setPieColor((45, 74, 83))
        self.ui.battery_usage.rpb_setTextColor((255, 255, 255))
        self.ui.battery_usage.rpb_setInitialPos('West')
        self.ui.battery_usage.rpb_setTextFormat('pecentage')
        self.ui.battery_usage.rpb_setLineWidth(15)
        self.ui.battery_usage.rpb_setPathWidth(15)
        self.ui.battery_usage.rpb_setLineCap('RoundCap')

    # side menu button styling function

    def applyButtonStyle(self):
        for w in self.ui.menu_frame.findChildren(QPushButton):
            # if button name is not equal to clicked button name
            if w.objectName() != self.sender().objectName():
                # creating default style by removing left border
                w.setStyleSheet("border-bottom: none;")

                # apply new style to click button
                self.sender().setStyleSheet("border-bottom: 2px solid")

                return

    def slideLeftMenu(self):
        # get current left menu width
        width = self.ui.menu_frame.width()
        # if minimized
        if width == 40:
            # expand
            newWidth = 200
            # if maximize
        else:
            # restore
            newWidth = 40

    # animate the transition
        self.animation = QPrpertyAnimation(
            self.ui.left_menu_cont_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # add mouse event to the window
    def mousePressEvent(self, event):
        # get current position of mouse
        self.clickPosition = event.globalPos()

    # update restore button icon on maximizing or minimizing window
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u":/icons/icons/maximize-2.svg"))


# execute app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

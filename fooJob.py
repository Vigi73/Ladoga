import psutil as pu
import pyautogui as bot
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QTableWidgetItem

from mainFoo import fish_tank
from mainForm import Ui_MainForm  # импорт нашего сгенерированного файла

bot.FAILSAFE = True
bot.PAUSE = .2


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.f_lesh = 0
        self.f_gustera = 0
        self.f_beloglazka = 0
        self.f_ripus = 0
        self.f_korushka = 0
        self.f_rybec = 0
        self.f_sig = 0
        self.f_ludoga = 0
        self.f_shuka = 0
        self.f_big_shuka = 0

        self.count_fish = 0

        self.ripus_width = 0
        self.corushka_width = 0
        self.rybec_width = 0
        self.sig_width = 0
        self.ludoga_width = 0
        self.shuka_width = 0
        self.big_shuka_width = 0

        self.setFixedSize(800, 600)

        self.ui.stopLesh.setVisible(False)
        self.ui.btnStopRipus.setVisible(False)
        self.ui.btnStopSig.setVisible(False)
        self.ui.btnStopShuka.setVisible(False)
        self.ui.startLesh.clicked.connect(self.start_timer_lesh)
        self.ui.stopLesh.clicked.connect(self.stop_timer_lesh)
        self.ui.btnStartRipus.clicked.connect(self.start_timer_ripus)
        self.ui.btnStopRipus.clicked.connect(self.stop_timer_ripus)
        self.ui.btnStartSig.clicked.connect(self.start_timer_sig)
        self.ui.btnStopSig.clicked.connect(self.stop_timer_sig)
        self.ui.btnStartShuka.clicked.connect(self.start_timer_shuka)
        self.ui.btnStopShuka.clicked.connect(self.stop_timer_shuka)

        self.ui.tableLesh.setRowCount(9)
        self.ui.tableGustera.setRowCount(3)
        self.ui.tableBeloglazka.setRowCount(6)

        self.ui.tableRipus.setRowCount(200)
        self.ui.tableKorushka.setRowCount(200)

        # self.shortcutStart = QShortcut(QKeySequence("Alt+A"), self)
        # self.shortcutStart.activated.connect(self.start_Timer)

        # Таймер для вкладки Лещ
        self.timer_lesh = QTimer()
        self.timer_lesh.timeout.connect(self.main_loop_lesh)

        # Таймер для вкладки Рипус
        self.timer_ripus = QTimer()
        self.timer_ripus.timeout.connect(self.main_loop_ripus)

        # Таймер для вкладки Сиг
        self.timer_sig = QTimer()
        self.timer_sig.timeout.connect(self.main_loop_sig)

        # Таймер для вкладки Щука
        self.timer_shuka = QTimer()
        self.timer_shuka.timeout.connect(self.main_loop_shuka)

    # ---------------------------------- SHUKA_____________________________________________


    def stop_timer_shuka(self):
        self.ui.tableShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBigShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.shuka_width = 0
        self.big_shuka_width = 0

        self.ui.tableShuka.setRowCount(0)
        self.ui.tableBigShuka.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdShuka.display(str(self.count_fish))
        self.ui.tableShuka.setRowCount(5)
        self.ui.tableBigShuka.setRowCount(1)
        self.f_shuka = 0
        self.f_big_shuka = 0

        self.ui.btnStopShuka.setVisible(False)
        self.ui.btnStartShuka.setVisible(True)
        self.timer_shuka.stop()

    def start_timer_shuka(self):
        self.ui.tableShuka.setRowCount(5)
        self.ui.tableBigShuka.setRowCount(1)
        self.ui.tableShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBigShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_4.clear()
        self.ui.btnStopShuka.setVisible(True)
        self.ui.btnStartShuka.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_shuka.start(500)  # Запуск оснавного таймера

        else:
            self.timer_shuka.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartShuka.setVisible(True)
            self.ui.btnStopShuka.setVisible(False)

    def main_loop_shuka(self):
        # Основной цикл вылова (Щука)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 100:
                width_f *= 1000

            if str(ulov[0]) == 'Щука' and width_f >= 15000 and self.f_shuka < 5:
                self.ui.tableShuka.setItem(self.f_shuka, 0, QTableWidgetItem('Щука'))
                self.ui.tableShuka.setItem(self.f_shuka, 1, QTableWidgetItem(str(int(width_f))))
                self.f_shuka += 1
            if self.f_shuka > 4:
                self.ui.tableShuka.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Глубинная щука' and self.f_shuka < 1:
                self.ui.tableBigShuka.setItem(self.f_big_shuka, 0, QTableWidgetItem('Глубинная щука'))
                self.ui.tableBigShuka.setItem(self.f_big_shuka, 1, QTableWidgetItem(str(int(width_f))))
                self.f_big_shuka += 1
            if self.f_big_shuka > 0:
                self.ui.tableBigShuka.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_4.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdShuka.display(str(self.count_fish))

        except:
            pass


    # ---------------------------------- END SHUKA_________________________________________

    # ---------------------------------- SIG_______________________________________________

    def start_timer_sig(self):
        self.ui.tableRybec.setRowCount(8)
        self.ui.tableSig.setRowCount(8)
        self.ui.tableLudoga.setRowCount(8)
        self.ui.tableRybec.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableSig.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableLudoga.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_3.clear()
        self.ui.btnStopSig.setVisible(True)
        self.ui.btnStartSig.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_sig.start(500)  # Запуск оснавного таймера

        else:
            self.timer_sig.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartSig.setVisible(True)
            self.ui.btnStopSig.setVisible(False)

    def stop_timer_sig(self):
        self.ui.tableRybec.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableSig.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableLudoga.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.rybec_width = 0
        self.sig_width = 0

        self.ui.tableRybec.setRowCount(0)
        self.ui.tableSig.setRowCount(0)
        self.ui.tableLudoga.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdSig.display(str(self.count_fish))
        self.ui.tableRybec.setRowCount(8)
        self.ui.tableSig.setRowCount(8)
        self.ui.tableLudoga.setRowCount(8)
        self.f_rybec = 0
        self.f_sig = 0
        self.f_ludoga = 0

        self.ui.btnStopSig.setVisible(False)
        self.ui.btnStartSig.setVisible(True)
        self.timer_sig.stop()

    def main_loop_sig(self):
        # Основной цикл вылова (Рипус)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 10:
                width_f *= 1000

            if str(ulov[0]) == 'Рыбец' and width_f >= 250 and self.f_rybec < 8:
                self.ui.tableRybec.setItem(self.f_rybec, 0, QTableWidgetItem('Рыбец'))
                self.ui.tableRybec.setItem(self.f_rybec, 1, QTableWidgetItem(str(int(width_f))))
                self.f_rybec += 1
            if self.f_rybec > 7:
                self.ui.tableRybec.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Сиг' and width_f >= 3000 and self.f_rybec < 8:
                self.ui.tableSig.setItem(self.f_sig, 0, QTableWidgetItem('Сиг'))
                self.ui.tableSig.setItem(self.f_sig, 1, QTableWidgetItem(str(int(width_f))))
                self.f_sig += 1
            if self.f_sig > 7:
                self.ui.tableSig.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Лудога' and width_f >= 350 and self.f_rybec < 8:
                self.ui.tableLudoga.setItem(self.f_ludoga, 0, QTableWidgetItem('Лудога'))
                self.ui.tableLudoga.setItem(self.f_ludoga, 1, QTableWidgetItem(str(int(width_f))))
                self.f_ludoga += 1
            if self.f_ludoga > 7:
                self.ui.tableLudoga.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_3.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdSig.display(str(self.count_fish))
        except:
            pass

    # ---------------------------------- END SIG_____________________________________________

    # ---------------------------------- RIPUS_____________________________________________
    def start_timer_ripus(self):
        self.ui.tableRipus.setRowCount(200)
        self.ui.tableKorushka.setRowCount(200)
        self.ui.tableRipus.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableKorushka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_2.clear()
        self.ui.btnStopRipus.setVisible(True)
        self.ui.btnStartRipus.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_ripus.start(600)  # Запуск оснавного таймера

        else:
            self.timer_ripus.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartRipus.setVisible(True)
            self.ui.btnStopRipus.setVisible(False)

    def stop_timer_ripus(self):
        self.ui.tableRipus.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableKorushka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ripus_width = 0
        self.ui.lcdR.display(str(self.ripus_width))
        self.corushka_width = 0
        self.ui.lcdK.display(str(self.corushka_width))
        self.ui.tableRipus.setRowCount(0)
        self.ui.tableKorushka.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdRipus.display(str(self.count_fish))
        self.ui.tableRipus.setRowCount(200)
        self.ui.tableKorushka.setRowCount(200)
        self.f_ripus = 0
        self.f_korushka = 0
        self.ui.btnStopRipus.setVisible(False)
        self.ui.btnStartRipus.setVisible(True)
        self.timer_ripus.stop()

    def main_loop_ripus(self):
        # Основной цикл вылова (Рипус)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 10:
                width_f *= 1000

            if str(ulov[0]) == 'Рипус':
                self.ui.tableRipus.setItem(self.f_ripus, 0, QTableWidgetItem('Рипус'))
                self.ui.tableRipus.setItem(self.f_ripus, 1, QTableWidgetItem(str(width_f)))
                self.f_ripus += 1
                self.ripus_width += width_f

            if str(ulov[0]) == 'Корюшка':
                self.ui.tableKorushka.setItem(self.f_korushka, 0, QTableWidgetItem('Корюшка'))
                self.ui.tableKorushka.setItem(self.f_korushka, 1, QTableWidgetItem(str(width_f)))
                self.f_korushka += 1
                self.corushka_width += width_f

            self.ui.lcdR.display(str(self.ripus_width))
            self.ui.lcdK.display(str(self.corushka_width))

            if self.ripus_width >= 15000:
                self.ui.tableRipus.setStyleSheet("background-color: rgb(0, 170, 0);")
            if self.corushka_width >= 5000:
                self.ui.tableKorushka.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_2.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdRipus.display(str(self.count_fish))
        except:
            pass

    # ---------------------------------- END RIPUS_____________________________________________

    # --------------------------------------1 TAB----------------------------------------------

    def stop_timer_lesh(self):
        self.ui.tableLesh.setRowCount(0)
        self.ui.tableGustera.setRowCount(0)
        self.ui.tableBeloglazka.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdLesh.display(str(self.count_fish))

        self.ui.tableLesh.setRowCount(9)
        self.ui.tableGustera.setRowCount(3)
        self.ui.tableBeloglazka.setRowCount(6)

        self.f_lesh = 0
        self.f_gustera = 0
        self.f_beloglazka = 0
        self.ui.stopLesh.setVisible(False)
        self.ui.startLesh.setVisible(True)
        self.timer_lesh.stop()

    def start_timer_lesh(self):
        self.ui.tableLesh.setRowCount(9)
        self.ui.tableGustera.setRowCount(3)
        self.ui.tableBeloglazka.setRowCount(6)
        self.ui.tableLesh.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableGustera.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBeloglazka.setStyleSheet("background-color: rgb(170, 170, 127);")

        self.ui.textBrowser.clear()
        self.ui.stopLesh.setVisible(True)
        self.ui.startLesh.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_lesh.start(600)  # Запуск оснавного таймера

        else:
            self.timer_lesh.stop()
            bot.alert('Запустите рыбалку')
            self.ui.startLesh.setVisible(True)
            self.ui.stopLesh.setVisible(False)

    def main_loop_lesh(self):

        # Основной цикл вылова (Лещ)

        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))

            """Если лещ"""
            if str(ulov[0]) == 'Лещ' and width_f >= 5 and self.f_lesh < 9:
                self.ui.tableLesh.setItem(self.f_lesh, 0, QTableWidgetItem('Лещ'))
                self.ui.tableLesh.setItem(self.f_lesh, 1, QTableWidgetItem(str(width_f)))
                self.f_lesh += 1

            """Если Густера"""
            if str(ulov[0]) == 'Густера' and width_f >= 300 and self.f_gustera < 4:
                self.ui.tableGustera.setItem(self.f_gustera, 0, QTableWidgetItem('Густера'))
                self.ui.tableGustera.setItem(self.f_gustera, 1, QTableWidgetItem(str(width_f)))
                self.f_gustera += 1

            """Если Белоглазка"""
            if str(ulov[0]) == 'Белоглазка' and width_f >= 250 and self.f_beloglazka < 7:
                self.ui.tableBeloglazka.setItem(self.f_beloglazka, 0, QTableWidgetItem('Белоглазка'))
                self.ui.tableBeloglazka.setItem(self.f_beloglazka, 1, QTableWidgetItem(str(width_f)))
                self.f_beloglazka += 1
            self.count_fish += 1
            self.ui.textBrowser.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdLesh.display(str(self.count_fish))

            if self.f_lesh > 8:
                self.ui.tableLesh.setStyleSheet("background-color: rgb(0, 170, 0);")
            if self.f_gustera > 2:
                self.ui.tableGustera.setStyleSheet("background-color: rgb(0, 170, 0);")

            if self.f_beloglazka > 5:
                self.ui.tableBeloglazka.setStyleSheet("background-color: rgb(0, 170, 0);")

            if self.f_lesh > 8 and self.f_gustera > 2 and self.f_beloglazka > 5:
                self.timer_lesh.stop()
        #  ------------------------------------------- END 1 TAB --------------------------------------------------------------

        except:
            pass
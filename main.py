import sys
import os
from pathlib import Path
import numpy as np
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QFileDialog, QDialog, QDialogButtonBox
from PySide6.QtCore import QSize, Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ui_Kriv import Ui_MainWindow  # Подключаем ваш сгенерированный файл с интерфейсом
from ui_about import Ui_Form as Ui_AboutForm
from ui_license import Ui_Form as Ui_LicenseForm
from ui_howto import Ui_Form as Ui_HowtoForm


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutForm()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)  # Блокируем основное окно

# Класс для модального окна License
class LicenseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LicenseForm()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)  # Блокируем основное окно

# Класс для модального окна HowTo с функционалом кнопки "OK"
class HowToDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HowtoForm()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)  # Блокируем основное окно
        self.ui.ok.clicked.connect(self.close)  # Кнопка "OK" закрывает окно



def get_user_data_directory():
    """Получение пользовательской директории для хранения истории"""
    user_dir = Path.home()
    if sys.platform == 'win32':  # Для Windows
        app_data_dir = user_dir / 'AppData' / 'Roaming' / 'Krivulka'
    else:  # Для macOS/Linux
        app_data_dir = user_dir / '.krivulka'

    # Создаем директорию, если её нет
    app_data_dir.mkdir(parents=True, exist_ok=True)
    return app_data_dir


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Переменные для графика
        self.a = 0
        self.b = 0
        self.x_coord = None  # Координата x для нахождения пересечения
        self.y_coord = None  # Координата y для нахождения пересечения
        self.graph_color = 'black'  # Цвет графика по умолчанию

        # Настройка макета для виджета output
        layout = QVBoxLayout(self.ui.output)
        self.canvas = MplCanvas(self.ui.output, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        # Настройка макета для output_r и output_l на странице duo
        layout_r = QVBoxLayout(self.ui.output_r)
        self.canvas_r = MplCanvas(self.ui.output_r, width=5, height=4, dpi=100)
        layout_r.addWidget(self.canvas_r)

        layout_l = QVBoxLayout(self.ui.output_l)
        self.canvas_l = MplCanvas(self.ui.output_l, width=5, height=4, dpi=100)
        layout_l.addWidget(self.canvas_l)

        # Создание виджета для вывода координаты пересечения
        self.label = QLabel(self.ui.centralwidget)
        self.ui.verticalLayout_2.addWidget(self.label)

        # Привязка событий потери фокуса и нажатия кнопки draw
        self.ui.input_a.editingFinished.connect(self.update_a)
        self.ui.input_b.editingFinished.connect(self.update_b)
        self.ui.input_x.editingFinished.connect(self.update_x)
        self.ui.input_y.editingFinished.connect(self.update_y)  # Добавлено
        self.ui.draw.clicked.connect(self.force_update)

        # Привязка событий для изменения цвета графика
        self.ui.color.currentIndexChanged.connect(self.update_color)
        self.ui.hex.editingFinished.connect(self.update_color_from_hex)

        # Изначально поле hex заблокировано
        self.ui.hex.setEnabled(False)

        # Привязка изменения состояния split_option
        self.ui.split_option.stateChanged.connect(self.toggle_split)

        # Блокировка block_y по умолчанию
        self.ui.block_y.setEnabled(False)

        # Отрисовка графика
        self.plot()

        #Обработка закрытия окна
        self.closeEvent = self.save_history_on_exit

        # Меню Recent
        self.update_recent_menu()

        self.ui.clear.triggered.connect(self.clear_history)
        self.ui.exit.triggered.connect(self.close)
        self.ui.save.triggered.connect(self.save_graph)
        self.ui.forget.triggered.connect(self.forget_fields)

        # Привязка сигналов к QAction в меню info
        self.ui.about.triggered.connect(self.show_about_window)
        self.ui.license.triggered.connect(self.show_license_window)
        self.ui.howto.triggered.connect(self.show_howto_window)

    def update_a(self):
        """Обновление переменной a при потере фокуса поля input_a"""
        try:
            self.a = float(self.ui.input_a.text())
        except ValueError:
            self.a = 0
        self.plot()

    def update_b(self):
        """Обновление переменной b при потере фокуса поля input_b"""
        try:
            self.b = float(self.ui.input_b.text())
        except ValueError:
            self.b = 0
        self.plot()

    def update_x(self):
        """Обновление координаты x и перерисовка графика"""
        try:
            self.x_coord = float(self.ui.input_x.text())
        except ValueError:
            self.x_coord = None
        self.plot()

    def update_y(self):
        """Обновление координаты y и перерисовка графика"""
        try:
            self.y_coord = float(self.ui.input_y.text())
        except ValueError:
            self.y_coord = None

    def force_update(self):
        """Принудительное обновление графика при нажатии на кнопку draw"""
        self.update_a()
        self.update_b()
        self.update_x()
        # Обновление графиков на обеих страницах, если split_option включен
        if self.ui.split_option.isChecked():
            self.plot_duo()
        else:
            self.plot()

    def toggle_split(self):
        """Переключение между страницами в зависимости от состояния split_option"""
        if self.ui.split_option.isChecked():
            # Включаем split: переключаем на вторую страницу и разблокируем block_y
            self.ui.pager.setCurrentIndex(1)
            self.ui.block_y.setEnabled(True)
            self.plot_duo()  # Отрисовка графиков на обеих страницах
        else:
            # Выключаем split: переключаем на первую страницу и блокируем block_y
            self.ui.pager.setCurrentIndex(0)
            self.ui.block_y.setEnabled(False)
            self.ui.input_y.clear()  # Очищаем поле input_y
            self.y_coord = None  # Сбрасываем значение y
            self.plot()  # Отрисовка графика только на первой странице

    def update_color(self):
        """Изменение цвета графика в зависимости от выбора в ComboBox"""
        selected_color = self.ui.color.currentText()

        color_map = {
            'Черный': 'black',
            'Красный': 'red',
            'Синий': 'blue',
            'Желтый': 'yellow',
            'Оранжевый': 'orange',
            'Голубой': 'cyan',
            'Серый': 'gray',
            'Белый': 'white',
            'Фиолетовый': 'purple',
            'Другой': 'other'
        }

        if selected_color == 'Другой':
            self.ui.hex.setEnabled(True)
        else:
            self.ui.hex.setEnabled(False)
            self.graph_color = color_map.get(selected_color, 'black')

        if self.graph_color == 'white':
            self.canvas.setStyleSheet("background-color: darkgray;")
        else:
            self.canvas.setStyleSheet("")

        self.plot()

    def update_color_from_hex(self):
        """Обновление цвета графика при вводе HEX-кода"""
        hex_code = self.ui.hex.text().strip()
        if len(hex_code) == 6:
            self.graph_color = f"#{hex_code}"
            self.plot()
            if self.ui.split_option.isChecked():
                self.canvas_r.axes.set_color(self.graph_color)
                self.canvas_l.axes.set_color(self.graph_color)
                self.canvas_r.draw()
                self.canvas_l.draw()
        else:
            self.ui.hex.setText('000000')

    def plot(self):
        """Отрисовка параболы и отображение точки пересечения"""
        self.canvas.axes.clear()

        # Диапазон значений для x
        x = np.linspace(-10, 10, 400)
        y = self.a * x ** 2 + self.b

        # Построение графика
        self.canvas.axes.plot(x, y, color=self.graph_color)

        # Проверка, если задано значение x для пересечения
        if self.x_coord is not None:
            # Вычисление y на основе введённой x координаты
            y_intersection = self.a * self.x_coord ** 2 + self.b

            # Отображение пунктирной линии на графике по x
            self.canvas.axes.axvline(self.x_coord, color='green', linestyle='--')

            # Отображение точки пересечения
            self.canvas.axes.plot(self.x_coord, y_intersection, 'ro')  # Красная точка

            # Установка области отображения графика, чтобы приблизить к точке
            self.canvas.axes.set_xlim(self.x_coord - 2, self.x_coord + 2)
            self.canvas.axes.set_ylim(y_intersection - 5, y_intersection + 5)

            # Обновление метки с координатами пересечения
            self.label.setText(f"Координата пересечения: ({self.x_coord}, {y_intersection})")

        self.canvas.axes.set_title(f"Парабола: y = {self.a} * x^2 + {self.b}")
        self.canvas.draw()

    def plot_duo(self):
        """Отрисовка параболы на двух графиках в режиме split-screen"""
        self.canvas_r.axes.clear()
        self.canvas_l.axes.clear()

        # Диапазон значений для x
        x = np.linspace(-10, 10, 400)
        y = self.a * x ** 2 + self.b

        # Построение графиков
        self.canvas_r.axes.plot(x, y, color=self.graph_color)
        self.canvas_l.axes.plot(x, y, color=self.graph_color)

        # Если введено значение y, отобразить горизонтальную линию
        if self.y_coord is not None:
            self.canvas_r.axes.axhline(self.y_coord, color='blue', linestyle='--')
            self.canvas_l.axes.axhline(self.y_coord, color='blue', linestyle='--')

            # Решаем квадратное уравнение для нахождения пересечений
            c = self.b - self.y_coord
            discriminant = self.a ** 2 - 4 * self.a * c

            if discriminant > 0:  # Две точки пересечения
                x1 = (-self.a + np.sqrt(discriminant)) / (2 * self.a)
                x2 = (-self.a - np.sqrt(discriminant)) / (2 * self.a)

                x1 += 0.5
                x2 += 0.48

                # Отображение точек пересечения на обоих графиках
                self.canvas_l.axes.plot(x1, self.y_coord, 'ro')  # Красная точка на output_l
                self.canvas_r.axes.plot(x2, self.y_coord, 'ro')  # Красная точка на output_r

                # Приближаем графики к точкам пересечения
                self.canvas_l.axes.set_xlim(x1 - 2, x1 + 2)
                self.canvas_l.axes.set_ylim(self.y_coord - 5, self.y_coord + 5)

                self.canvas_r.axes.set_xlim(x2 - 2, x2 + 2)
                self.canvas_r.axes.set_ylim(self.y_coord - 5, self.y_coord + 5)

                # Обновление метки с координатами пересечений на обоих графиках
                self.label.setText(f"Пересечение: ({x1:.2f}, {self.y_coord:.2f}) и ({x2:.2f}, {self.y_coord:.2f})")

            elif discriminant == 0:  # Одна точка касания
                x_touch = -self.a / (2 * self.a)

                # Отображение точки касания
                self.canvas_l.axes.plot(x_touch, self.y_coord, 'ro')  # Красная точка на output_l
                self.canvas_r.axes.plot(x_touch, self.y_coord, 'ro')  # Красная точка на output_r

                # Приближаем график к точке касания
                self.canvas_l.axes.set_xlim(x_touch - 2, x_touch + 2)
                self.canvas_l.axes.set_ylim(self.y_coord - 5, self.y_coord + 5)

                # Обновление метки с координатами касания
                self.label.setText(f"Касание: ({x_touch:.2f}, {self.y_coord:.2f})")

        self.canvas_r.axes.set_title(f"Парабола (правый): y = {self.a} * x^2 + {self.b}")
        self.canvas_l.axes.set_title(f"Парабола (левый): y = {self.a} * x^2 + {self.b}")

        # Рисуем графики
        self.canvas_r.draw()
        self.canvas_l.draw()

    def save_history_on_exit(self, event):
        """Сохранение истории перед выходом"""
        a_value = self.ui.input_a.text().strip() or 'empty'
        b_value = self.ui.input_b.text().strip() or 'empty'

        # Если оба значения a и b пусты, не сохраняем историю
        if a_value == 'empty' and b_value == 'empty':
            event.accept()
            return

        # Получаем остальные значения
        color_value = self.ui.color.currentText()
        hex_code = self.ui.hex.text().strip() or '000000'
        x_value = self.ui.input_x.text().strip() or 'empty'
        split_option_value = '1' if self.ui.split_option.isChecked() else '0'
        y_value = self.ui.input_y.text().strip() or 'empty'

        # Формируем строку для записи
        history_entry = f"{a_value} {b_value} {color_value} {hex_code} {x_value} {split_option_value} {y_value}\n"

        # Записываем в файл
        app_data_dir = get_user_data_directory()
        history_file = app_data_dir / 'history.txt'

        with open(history_file, 'a') as f:
            f.write(history_entry)

        event.accept()

    def update_recent_menu(self):
        """Обновление меню recent на основе истории"""
        app_data_dir = get_user_data_directory()
        history_file = app_data_dir / 'history.txt'

        # Очищаем меню перед обновлением
        self.ui.recent.clear()

        if not history_file.exists() or os.stat(history_file).st_size == 0:
            # Если файл не существует или пустой, добавляем NONE
            none_action = QAction('NONE', self)
            self.ui.recent.addAction(none_action)
            return

        with open(history_file, 'r') as file:
            lines = file.readlines()

            if not lines:
                # Если нет строк в истории, добавляем NONE
                none_action = QAction('NONE', self)
                self.ui.recent.addAction(none_action)
            else:
                for line in lines:
                    parts = line.split()

                    # Проверяем, что в строке есть хотя бы 2 значения
                    if len(parts) >= 2:
                        a_value = parts[0]
                        b_value = parts[1]
                        equation = f"ƒ(x) = {a_value}*x² + {b_value}"

                        # Создаём QAction для каждой строки
                        action = QAction(equation, self)
                        action.triggered.connect(lambda _, l=line: self.load_config_from_history(l))

                        # Добавляем действие в меню recent
                        self.ui.recent.addAction(action)

    def load_config_from_history(self, line):
        """Загрузка конфигурации из строки истории"""
        parts = line.split()

        if len(parts) == 7:
            # Загружаем значения в поля
            self.ui.input_a.setText('' if parts[0] == 'empty' else parts[0])
            self.ui.input_b.setText('' if parts[1] == 'empty' else parts[1])
            self.ui.color.setCurrentText(parts[2])
            self.ui.hex.setText(parts[3])
            self.ui.input_x.setText('' if parts[4] == 'empty' else parts[4])
            self.ui.split_option.setChecked(parts[5] == '1')
            self.ui.input_y.setText('' if parts[6] == 'empty' else parts[6])

            # Обновляем график после загрузки данных
            self.plot()

    def clear_history(self):
        """Очистка файла history.txt"""
        app_data_dir = get_user_data_directory()
        history_file = app_data_dir / 'history.txt'

        with open(history_file, 'w'):  # Очищаем файл
            pass

        # Обновляем меню recent
        self.update_recent_menu()

    def save_graph(self):
        """Сохранение графика в файл"""
        save_dialog = QFileDialog(self)
        save_dialog.setAcceptMode(QFileDialog.AcceptSave)
        save_dialog.setFileMode(QFileDialog.AnyFile)
        save_dialog.setNameFilter("Images (*.png *.xpm *.jpg)")

        if save_dialog.exec():
            selected_file = save_dialog.selectedFiles()[0]

            # Если включён split-screen, сохраняем оба графика
            if self.ui.split_option.isChecked():
                # Сохраняем график в output_r и output_l
                self.canvas_r.figure.savefig(f"{selected_file}_right.png")
                self.canvas_l.figure.savefig(f"{selected_file}_left.png")
            else:
                # Сохраняем график в output
                self.canvas.figure.savefig(f"{selected_file}.png")

    def forget_fields(self):
        """Сброс всех полей в окне"""
        self.ui.input_a.clear()
        self.ui.input_b.clear()
        self.ui.input_x.clear()
        self.ui.input_y.clear()
        self.ui.split_option.setChecked(False)
        self.ui.color.setCurrentIndex(0)  # Устанавливаем на Черный
        self.ui.hex.setText("000000")

        # Обновляем график после сброса
        self.plot()
#
    def show_about_window(self):
        """Открытие окна 'About'."""
        about_window = AboutDialog(self)
        about_window.setWindowModality(Qt.ApplicationModal)
        about_window.show()

    def show_license_window(self):
        """Открытие окна 'License'."""
        license_window = LicenseDialog(self)
        license_window.setWindowModality(Qt.ApplicationModal)
        license_window.show()

    def show_howto_window(self):
        """Открытие окна 'Howto'."""
        howto_window = HowToDialog(self)
        howto_window.setWindowModality(Qt.ApplicationModal)
        howto_window.ui.ok.clicked.connect(howto_window.close)
        howto_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(QSize(800, 600))
    window.show()
    sys.exit(app.exec())

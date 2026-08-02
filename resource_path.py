import sys
import os


def resource_path(relative_path):
    """Возвращает путь к ресурсу как при разработке, так и после сборки."""
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
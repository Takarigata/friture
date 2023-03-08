import logging
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtQuickWidgets import QQuickWidget

class TextBoxWidget(QtWidgets.QWidget):

    def __init__(self, parent, engine):
        super().__init__(parent)

        self.logger = logging.getLogger(__name__)

        self.setObjectName("Text Box")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.TextBoxLabel = QtWidgets.QLabel("Text To Read")
        self.TextBoxLabel.setAlignment(QtCore.Qt.AlignCenter )
        self.TextBox = QtWidgets.QLineEdit("Sample Text")
        self.TextBox.setAlignment(QtCore.Qt.AlignTop)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.sizePolicy.setHorizontalStretch(1)
        self.sizePolicy.setVerticalStretch(1)
        self.TextBoxLabel.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                                 QtWidgets.QSizePolicy.Minimum))
        self.TextBox.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                                              QtWidgets.QSizePolicy.Expanding))

        self.layout.addWidget(self.TextBoxLabel, stretch=1)
        self.layout.addWidget(self.TextBox, stretch=80)

    # method
    def set_buffer(self, buffer):
        self.audiobuffer = buffer

    def handle_new_data(self, floatdata):
        pass

    # method
    def canvasUpdate(self):
        # nothing to do here
        return

    # slot
    def settings_called(self, checked):
        pass
        #self.settings_dialog.show()

    # method
    def saveState(self, settings):
        pass
        #self.settings_dialog.saveState(settings)

    # method
    def restoreState(self, settings):
        pass
        #self.settings_dialog.restoreState(settings)
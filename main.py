import sys
from Desktops import desktops
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

import config
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Source/app_icon.png'))
    app.setApplicationDisplayName(config.App_name)
    main_win = desktops.Main()
    sys.exit(app.exec_())
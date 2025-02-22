import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import asyncio
from qasync import QEventLoop, asyncSlot


class Window(QMainWindow):
    def __init__(self, loop=None):
        super().__init__()
        button1 = QPushButton("ClickHere")
        self.setCentralWidget(button1)
        button1.clicked.connect(self.button1_clicked)
        self.loop = loop or asyncio.get_event_loop

    @asyncSlot()
    async def button1_clicked(self):
        print("clicked")
        await asyncio.sleep(1, self.loop)


async def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    widget = Window(loop)
    widget.show()

    with loop:
        loop.run_forever()


if __name__ == "__main__":
    print("About to start")
    asyncio.run(main())

# encoding: utf-8
# acthor: Twobox

import wx
import webbrowser

class Mywin(wx.Frame):
    """Author: Twobox"""
    about = """
    强行仿造微软记事本
    """
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title = title)

        self.textBoxIsChange = False

        self.fileIsOpen = False
        self.fileName = "无标题"
        self.filePath = ""

        self.wildcard = "文本文件 (*.txt)|*.txt"

        self.InitUI()

    def InitUI(self):
        self.initUIMenuBar()            # 初始化 菜单栏
        self.initUIStatusBar()          # 初始化 状态栏
        self.initUIMainWindow()         # 构建 窗口面板
        self.adjustmentWin()            # 调整 窗口框体参数

    def initUIMainWindow(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.textBox = wx.TextCtrl(panel, id = -1, style = wx.TE_MULTILINE)
        self.textBox.Bind(wx.EVT_TEXT, self.eventTextCtrl)
        vbox.Add(self.textBox, proportion = 1, flag = wx.EXPAND|wx.ALL, border = 0)

        panel.SetSizer(vbox)

    def initUIStatusBar(self):
        # 实例化一个 状态栏 对象
        self.statusBar = wx.StatusBar(parent = self, id = -1)
        self.statusBar.SetFieldsCount(2)
        self.statusBar.SetStatusWidths([-3.9, -1])
        self.statusBar.SetStatusText("  第 1 行 , 第 1 列", 1)
        self.SetStatusBar(self.statusBar)
        self.statusBar.Show(True)

    def adjustmentWin(self):
        self.SetTitle(self.fileName + " - 记事本")
        self.SetSize((400, 600))
        self.Center()
        self.Show()

    def initUIMenuBar(self):
        menuBar = wx.MenuBar()

        # 构造 文件 菜单
        fileMenu = wx.Menu()

        newItem = wx.MenuItem(fileMenu, id=wx.ID_NEW, text="新建(&N)\tCtrl+N", kind=wx.ITEM_NORMAL)
        openItem = wx.MenuItem(fileMenu, id=wx.ID_OPEN, text="打开(&O)\tCtrl+O", kind=wx.ITEM_NORMAL)
        saveItem = wx.MenuItem(fileMenu, id=wx.ID_SAVE, text="保存(&S)\tCtrl+S", kind=wx.ITEM_NORMAL)
        saveasItem = wx.MenuItem(fileMenu, id=wx.ID_SAVEAS, text="另存为(&A)...", kind=wx.ITEM_NORMAL)

        fileMenu.AppendItem(newItem)
        fileMenu.AppendItem(openItem)
        fileMenu.AppendItem(saveItem)
        fileMenu.AppendItem(saveasItem)
        fileMenu.AppendSeparator()

        exitItem = wx.MenuItem(fileMenu, id=wx.ID_EXIT, text="退出(&X)", kind=wx.ITEM_NORMAL)
        fileMenu.AppendItem(exitItem)

        menuBar.Append(fileMenu, title="文件(&F)")

        # 构建 编辑 菜单
        deitMenu = wx.Menu()

        deitMenu.Append(id=21, item="撤销(&U)\tCtrl+Z", kind=wx.ITEM_NORMAL)
        deitMenu.AppendSeparator()
        deitMenu.Append(id=wx.ID_CUT, item="剪切(&T)\tCtrl+X", kind=wx.ITEM_NORMAL)
        deitMenu.Append(id=wx.ID_COPY, item="复制(&C)\tCtrl+C", kind=wx.ITEM_NORMAL)
        deitMenu.Append(id=wx.ID_PASTE, item="粘贴(&P)\tCtrl+V", kind=wx.ITEM_NORMAL)
        deitMenu.Append(id=wx.ID_DELETE, item="删除(&L)\tDel", kind=wx.ITEM_NORMAL)
        deitMenu.AppendSeparator()
        deitMenu.Append(id=wx.ID_FIND, item="查找(&F)...\tCtrl+F", kind=wx.ITEM_NORMAL)
        deitMenu.Append(id=27, item="查找下一个(&N)\tF3")
        deitMenu.Append(id=wx.ID_REPLACE, item="替换(&R)...\tCtrl+H")
        deitMenu.Append(id=29, item="转到(&G)\tCtrl+G")
        deitMenu.AppendSeparator()
        deitMenu.Append(id=wx.ID_SELECTALL, item="全选(&A)\tCtrl+A")
        deitMenu.Append(id=211, item="时间/日期(&D)\tF5")

        menuBar.Append(deitMenu, title="编辑(&E)")

        #构建 格式 菜单
        formatMenu = wx.Menu()

        formatMenu.Append(id = 31, item = "自动换行(&W)", kind = wx.ITEM_CHECK)
        formatMenu.Append(id = wx.ID_SELECT_FONT, item = "字体(&F)...")

        menuBar.Append(formatMenu, title = "格式(&O)")

        #构建 查看 菜单
        seeMenu = wx.Menu()
        seeMenu.Append(id = 41, item = "状态栏(&S)", kind = wx.ITEM_CHECK).Check(True)     # 置为选中状态

        menuBar.Append(seeMenu, title = "查看(&V)")

        #构建 帮助 菜单
        helpMenu = wx.Menu()

        helpMenu.Append(id = wx.ID_HELP, item = "查看帮助(&H)")
        helpMenu.Append(id = wx.ID_ABOUT, item = "关于记事本(&A)")

        menuBar.Append(helpMenu, title = "帮助(&H)")
        menuBar.Bind(wx.EVT_MENU, self.eventMenuBar)
        self.SetMenuBar(menuBar)

    # 以下是 被绑定的事件
    def eventMenuBar(self, event):
        """传过来的 event 对象, 好像就是 发生事件的那个组件的对象，如果真是这样就灰常好理解了。
            id == 31 目前尚有 BUG。
            id == ID_DELETE 未搞

            new\打开 文件的时候 未修改标题栏
        """
        id = event.GetId()
        if id == wx.ID_ABOUT:
            msgDialog = wx.MessageDialog(parent = None, message = self.about, caption = '关于"记事本"', style = wx.OK)
            msgDialog.ShowModal()

        elif id == wx.ID_HELP:
            url = 'www.baidu.com'
            webbrowser.open(url)

        elif id == wx.ID_EXIT: self.Close()

        elif id == 41:
            if event.IsChecked():
                self.statusBar.Show(True)
                self.SetSize((self.GetSize()[0], (self.GetSize()[1] + 1)))
            else:
                self.statusBar.Show(False)
                self.SetSize((self.GetSize()[0], (self.GetSize()[1] - 1)))

        elif id == 31:
            if not event.IsChecked():
                self.textBox.SetWindowStyleFlag(style=wx.TE_MULTILINE | wx.HSCROLL)
                self.statusBar.Show(True)
                self.SetSize((self.GetSize()[0], (self.GetSize()[1] + 1)))

            else:
                self.textBox.SetWindowStyleFlag(style=wx.TE_MULTILINE)
                self.statusBar.Show(False)
                self.SetSize((self.GetSize()[0], (self.GetSize()[1] - 1)))

        elif id == wx.ID_SELECTALL: self.textBox.SelectAll()

        elif id == wx.ID_CUT: self.textBox.Cut()

        elif id == wx.ID_COPY: self.textBox.Copy()

        elif id == wx.ID_PASTE: self.textBox.Paste()

        elif id == wx.ID_NEW:
            if self.textBoxIsChange:
                if self.textBox.GetValue() == "" and self.fileIsOpen == False:
                    pass
                else:
                    dlg = wx.MessageDialog(self, "是否将更改保存到 " + self.fileName + "?", "记事本", wx.CANCEL | wx.YES_NO)
                    answer = dlg.ShowModal()
                    if answer == wx.ID_OK:
                        self.saveFile()
                    elif answer == wx.ID_CANCEL:
                        return None
                    else:
                        pass
            self.fileIsOpen = False
            self.filePath = ""
            self.fileName = "无标题"
            self.textBox.SetValue("")
            self.textBoxIsChange = False

        elif id == wx.ID_SAVE: self.saveFile()

        elif id == wx.ID_OPEN:
            if self.textBoxIsChange:
                dlg = wx.MessageDialog(self, "是否将更改保存到 " + self.fileName + "?", "记事本", wx.CANCEL | wx.YES_NO)
                answer = dlg.ShowModal()
                if answer == wx.ID_NO:
                    self.openFile()
                elif answer == wx.ID_CANCEL:
                    pass
                else:
                    self.saveFile()
            else:
                self.openFile()

        elif id == wx.ID_SAVEAS:
            self.fileIsOpen = False
            if self.saveFile() == False:
                self.fileIsOpen = True

        elif id == wx.ID_SELECT_FONT:
            dlg = wx.FontDialog(self, wx.FontData())

            if dlg.ShowModal() == wx.ID_OK:
                data = dlg.GetFontData()
                Font = data.GetChosenFont()
                colour = data.GetColour()
                self.textBox.SetFont(Font)
                self.textBox.SetForegroundColour(colour)  # 设置字体颜色
                # self.textBox.SetBackgroundColour(colour)  # 设置背景颜色
                # self.textBox.SetOwnBackgroundColour(colour)  # 不是要清楚 目前看出来的效果是背景颜色

            dlg.Destroy()

    def eventTextCtrl(self, event):
        self.textBoxIsChange = True

    def saveFile(self):
        if not self.fileIsOpen:
            wildcard = self.wildcard
            dlg = wx.FileDialog(self, "保存", wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                filePath = dlg.GetPath()
            else:
                return False
        else:
            filePath = self.filePath
        with open(filePath, "w") as f:
            f.write(self.textBox.GetValue())
            self.textBoxIsChange = False
        return True

    def openFile(self):
        wildcard = self.wildcard
        dlg = wx.FileDialog(self, "打开", style=wx.FD_OPEN, wildcard=wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filePath = dlg.GetPath()
            with open(filePath, "r") as f:
                self.textBox.SetValue(f.read())
                self.fileIsOpen = True
                self.filePath = filePath
                self.fileName = f.name
                self.textBoxIsChange = False
                self.changeTitle()
        else:
            pass

    def changeTitle(self):
        self.SetTitle(self.fileName + " - 记事本")

def main():
    print("GO...")
    app = wx.App()
    Mywin(None, "")
    app.MainLoop()
    exit(0)

if __name__ == "__main__":
    main()
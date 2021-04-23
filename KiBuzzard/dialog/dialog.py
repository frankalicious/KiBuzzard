"""Subclass of dialog_base, which is generated by wxFormBuilder."""
import os
import re
import copy

import wx

from . import dialog_text_base

def ParseFloat(InputString, DefaultValue=0.0):
    value = DefaultValue
    if InputString != "":
        try:
            value = float(InputString)
        except ValueError:
            print("Value not valid")
    return value

class Dialog(dialog_text_base.DIALOG_TEXT_BASE):
    def __init__(self, parent, config, buzzard, func):
        dialog_text_base.DIALOG_TEXT_BASE.__init__(self, parent)
        
        typeface_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'buzzard', 'typeface')
        for entry in os.listdir(typeface_path):
            entry_path = os.path.join(typeface_path, entry)
            
            if not entry_path.endswith('.ttf'):
                continue
            
            self.m_FontComboBox.Append(os.path.splitext(entry)[0])
        
        self.m_FontComboBox.SetSelection(0)

        #for fnt in buzzard.SystemFonts:
        #    self.m_FontComboBox.Append(fnt)


        self.m_HeightUnits.SetLabel("mm")
        self.m_WidthUnits.SetLabel("mm")
        self.m_PaddingUnits.SetLabel("")
        

        best_size = self.BestSize
        # hack for some gtk themes that incorrectly calculate best size
        best_size.IncBy(dx=0, dy=30)
        self.SetClientSize(best_size)
        self.config = config
        self.func = func

        self.error = None
        
        self.loadConfig()


        self.buzzard = buzzard
        self.sourceText = ""
        self.polys = []
        
        self.m_PreviewPanel.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Bind(wx.EVT_TIMER, self.labelEditOnText)
        self.m_sdbSizerCancel.Bind(wx.EVT_BUTTON, self.Cancel)

        self.timer = wx.Timer(self, 0)
        self.timer.Start(milliseconds=250, oneShot=True)

    def Cancel(self, e):
        self.timer.Stop()

        self.saveConfig()
        e.Skip()


    def loadConfig(self):

        try:
            self.config.SetPath('/')
            self.m_FontComboBox.SetStringSelection(self.config.Read('font', 'UbuntuMono-B'))
            self.m_MultiLineText.SetValue(self.config.Read('text', ''))
            self.m_HeightCtrl.SetValue(str(self.config.ReadFloat('scale', 1.0)))
            self.m_CapLeftChoice.SetStringSelection(self.config.Read('l-cap', ''))
            self.m_CapRightChoice.SetStringSelection(self.config.Read('r-cap', ''))
            self.m_AlignmentChoice.SetStringSelection(self.config.Read('align', ''))
            self.m_WidthCtrl.SetValue(self.config.Read('width', ''))
            self.m_PaddingTopCtrl.SetValue(self.config.Read('pad-top', ''))
            self.m_PaddingLeftCtrl.SetValue(self.config.Read('pad-left', ''))
            self.m_PaddingRightCtrl.SetValue(self.config.Read('pad-right', ''))
            self.m_PaddingBottomCtrl.SetValue(self.config.Read('pad-bot', ''))
            
        except:
            import traceback
            print(traceback.format_exc())
        
    def saveConfig(self):
        try:
            self.config.SetPath('/')
            self.config.Write('font', self.m_FontComboBox.GetStringSelection())
            self.config.Write('text', self.m_MultiLineText.GetValue())
            self.config.WriteFloat('scale', float(self.m_HeightCtrl.GetValue()))
            self.config.Write('l-cap', self.m_CapLeftChoice.GetStringSelection())
            self.config.Write('r-cap', self.m_CapRightChoice.GetStringSelection())
            self.config.Write('align', self.m_AlignmentChoice.GetStringSelection())
            self.config.Write('width', self.m_WidthCtrl.GetValue())
            self.config.Write('pad-top', self.m_PaddingTopCtrl.GetValue())
            self.config.Write('pad-left', self.m_PaddingTopCtrl.GetValue())
            self.config.Write('pad-right', self.m_PaddingRightCtrl.GetValue())
            self.config.Write('pad-bot', self.m_PaddingBottomCtrl.GetValue())

            self.config.Flush()
        except:
            import traceback
            print(traceback.format_exc())
            

    def CurrentSettings(self):
        values = [
            self.m_MultiLineText,
            self.m_HeightCtrl,
            self.m_FontComboBox,
            self.m_CapLeftChoice,
            self.m_CapRightChoice,
            self.m_PaddingTopCtrl,
            self.m_PaddingLeftCtrl,
            self.m_PaddingRightCtrl,
            self.m_PaddingBottomCtrl,
            self.m_WidthCtrl,
            self.m_AlignmentChoice,
        ]
        StrValue = "".encode('utf-8')

        for item in values:
            if hasattr(item, "GetValue"):
                StrValue += item.GetValue().encode('utf-8')
            elif hasattr(item, "GetStringSelection"):
                StrValue += item.GetStringSelection().encode('utf-8')
            else:
                raise Exception("Invalid item")    
        return StrValue


    def labelEditOnText( self, event ):
        while self.sourceText != self.CurrentSettings():
            self.sourceText = self.CurrentSettings()
            self.ReGeneratePreview()

        self.timer.Start(milliseconds=250, oneShot=True)
        event.Skip()

    def ReGenerateFlag(self, e):
        self.sourceText = ""

    def ReGeneratePreview(self, e=None):
        
        self.polys = []
        self.buzzard.fontName = self.m_FontComboBox.GetStringSelection()

        # Validate scale factor
        self.buzzard.scaleFactor = ParseFloat(self.m_HeightCtrl.GetValue(), 1.0) * 0.5

        DefaultPadding = self.buzzard.scaleFactor * 7.75 * 4 * 0.25
        self.buzzard.padding.top = ParseFloat(self.m_PaddingTopCtrl.GetValue(), DefaultPadding) * 0.5
        self.buzzard.padding.left = ParseFloat(self.m_PaddingLeftCtrl.GetValue(), DefaultPadding) * 0.5
        self.buzzard.padding.right = ParseFloat(self.m_PaddingRightCtrl.GetValue(), DefaultPadding) * 0.5
        self.buzzard.padding.bottom = ParseFloat(self.m_PaddingBottomCtrl.GetValue(), DefaultPadding) * 0.5

        self.buzzard.width = ParseFloat(self.m_WidthCtrl.GetValue(), 0.0) *  7.75

        self.buzzard.alignment = self.m_AlignmentChoice.GetStringSelection()

        styles = {'':'', '(':'round', '[':'square', '<':'pointer', '/':'fslash', '\\':'bslash', '>':'flagtail'}
        self.buzzard.leftCap = styles[self.m_CapLeftChoice.GetStringSelection()]

        styles = {'':'', ')':'round', ']':'square', '>':'pointer', '/':'fslash', '\\':'bslash', '<':'flagtail'}
        self.buzzard.rightCap = styles[self.m_CapRightChoice.GetStringSelection()]
        self.error = None

        if len(self.m_MultiLineText.GetValue()) == 0:
            self.RePaint()
            return
        if len(self.m_MultiLineText.GetValue()) > 128:
            self.error = "Text input loo long"
            return
        
        try:
            self.polys = self.buzzard.generate(self.m_MultiLineText.GetValue())
        except Exception as e:
            import traceback
            traceback.print_exc()

        self.RePaint()

    def RePaint(self, e=None):
        self.Layout()
        self.Refresh()
        self.Update()


    def OnPaint(self, e):
        dc = wx.PaintDC(self.m_PreviewPanel)

        if self.error is not None:
            font = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL)
            dc.SetFont(font)
            dc.SetTextForeground('#FF0000')

            rect = wx.Rect(0,0, self.m_PreviewPanel.GetSize().GetWidth(),self.m_PreviewPanel.GetSize().GetHeight())
            dc.DrawLabel(self.error, rect, wx.ALIGN_LEFT)
        else:
            dc.SetPen(wx.Pen('#000000', width=1))

            size_x, size_y = self.m_PreviewPanel.GetSize()

            dc.SetDeviceOrigin(int(size_x/2), int(size_y/2))
            dc.SetBrush(wx.Brush('#000000'))

            if len(self.polys):
                # Create copy of poly list for scaling preview
                polys = copy.deepcopy(self.polys)


                # TODO use matrix for scaling
                # TODO use bbox to determine scaling
                min_x = 0
                max_x = 0
                for i in range(len(self.polys)):
                    for j in range(len(self.polys[i])):
                        min_x = min(self.polys[i][j].x, min_x)
                        max_x = max(self.polys[i][j].x, max_x)

                min_y = 0
                max_y = 0
                for i in range(len(self.polys)):
                    for j in range(len(self.polys[i])):
                        min_y = min(self.polys[i][j].y, min_y)
                        max_y = max(self.polys[i][j].y, max_y)

                scale = (size_x * 0.95) / (max_x - min_x)

                scale = min(scale, (size_y * 0.95) / (max_y - min_y))

                #scale = min(15.0, scale)
                for i in range(len(polys)):
                    for j in range(len(polys[i])):
                        polys[i][j] = (scale*polys[i][j].x,scale*polys[i][j].y)

                dc.DrawPolygonList(polys)


    def OnOkClick(self, event):
        self.timer.Stop()

        self.saveConfig()
        self.func(self, self.buzzard)
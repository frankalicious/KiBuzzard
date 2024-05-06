# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from .compat import DialogShim
import wx
import wx.xrc
import wx.stc

import gettext
_ = gettext.gettext

###########################################################################
## Class DIALOG_TEXT_BASE
###########################################################################

class DIALOG_TEXT_BASE ( DialogShim ):

    def __init__( self, parent ):
        DialogShim.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"KiBuzzard Text Properties"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.SYSTEM_MENU )

        self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

        bMainSizer = wx.BoxSizer( wx.VERTICAL )

        m_MultiLineSizer = wx.BoxSizer( wx.VERTICAL )

        self.textLabel = wx.StaticText( self, wx.ID_ANY, _(u"Text:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textLabel.Wrap( -1 )

        m_MultiLineSizer.Add( self.textLabel, 0, wx.RIGHT|wx.LEFT, 5 )

        self.m_MultiLineText = wx.stc.StyledTextCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_MultiLineText.SetUseTabs ( True )
        self.m_MultiLineText.SetTabWidth ( 4 )
        self.m_MultiLineText.SetIndent ( 4 )
        self.m_MultiLineText.SetTabIndents( False )
        self.m_MultiLineText.SetBackSpaceUnIndents( False )
        self.m_MultiLineText.SetViewEOL( False )
        self.m_MultiLineText.SetViewWhiteSpace( False )
        self.m_MultiLineText.SetMarginWidth( 2, 0 )
        self.m_MultiLineText.SetIndentationGuides( True )
        self.m_MultiLineText.SetReadOnly( False );
        self.m_MultiLineText.SetMarginWidth( 1, 0 )
        self.m_MultiLineText.SetMarginWidth ( 0, 0 )
        self.m_MultiLineText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDER, wx.stc.STC_MARK_BOXPLUS )
        self.m_MultiLineText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDER, wx.BLACK)
        self.m_MultiLineText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDER, wx.WHITE)
        self.m_MultiLineText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.stc.STC_MARK_BOXMINUS )
        self.m_MultiLineText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.BLACK )
        self.m_MultiLineText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.WHITE )
        self.m_MultiLineText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERSUB, wx.stc.STC_MARK_EMPTY )
        self.m_MultiLineText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEREND, wx.stc.STC_MARK_BOXPLUS )
        self.m_MultiLineText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEREND, wx.BLACK )
        self.m_MultiLineText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEREND, wx.WHITE )
        self.m_MultiLineText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.stc.STC_MARK_BOXMINUS )
        self.m_MultiLineText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.BLACK)
        self.m_MultiLineText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.WHITE)
        self.m_MultiLineText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERMIDTAIL, wx.stc.STC_MARK_EMPTY )
        self.m_MultiLineText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERTAIL, wx.stc.STC_MARK_EMPTY )
        self.m_MultiLineText.SetSelBackground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_MultiLineText.SetSelForeground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        m_MultiLineSizer.Add( self.m_MultiLineText, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


        bMainSizer.Add( m_MultiLineSizer, 20, wx.EXPAND|wx.ALL, 10 )

        m_SingleLineSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_PreviewLabel = wx.StaticText( self, wx.ID_ANY, _(u"Preview:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_PreviewLabel.Wrap( -1 )

        m_SingleLineSizer.Add( self.m_PreviewLabel, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_PreviewPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_SingleLineSizer.Add( self.m_PreviewPanel, 1, wx.ALL|wx.EXPAND, 5 )


        bMainSizer.Add( m_SingleLineSizer, 20, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 10 )

        fgSizerSetup = wx.FlexGridSizer( 0, 5, 4, 0 )
        fgSizerSetup.AddGrowableCol( 1 )
        fgSizerSetup.AddGrowableCol( 4 )
        fgSizerSetup.SetFlexibleDirection( wx.BOTH )
        fgSizerSetup.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_FontLabel = wx.StaticText( self, wx.ID_ANY, _(u"Font:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_FontLabel.Wrap( -1 )

        fgSizerSetup.Add( self.m_FontLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        m_FontComboBoxChoices = []
        self.m_FontComboBox = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_FontComboBoxChoices, wx.CB_READONLY )
        fgSizerSetup.Add( self.m_FontComboBox, 2, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


        fgSizerSetup.Add( ( 0, 0), 0, wx.RIGHT|wx.LEFT, 40 )

        self.m_CapLeftLabel = wx.StaticText( self, wx.ID_ANY, _(u"Cap Left:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_CapLeftLabel.Wrap( -1 )

        fgSizerSetup.Add( self.m_CapLeftLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        m_CapLeftChoiceChoices = [ wx.EmptyString, _(u"["), _(u"("), _(u"/"), _(u"\\"), _(u"<"), _(u">") ]
        self.m_CapLeftChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_CapLeftChoiceChoices, 0 )
        self.m_CapLeftChoice.SetSelection( 0 )
        fgSizerSetup.Add( self.m_CapLeftChoice, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.RIGHT, 3 )

        self.m_HeightLabel = wx.StaticText( self, wx.ID_ANY, _(u"Height:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_HeightLabel.Wrap( -1 )

        fgSizerSetup.Add( self.m_HeightLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )

        self.m_HeightCtrl = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 128, 0, 0.1 )
        self.m_HeightCtrl.SetDigits( 1 )
        fgSizerSetup.Add( self.m_HeightCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_HeightUnits = wx.StaticText( self, wx.ID_ANY, _(u"unit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_HeightUnits.Wrap( -1 )

        fgSizerSetup.Add( self.m_HeightUnits, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )

        self.m_CapRightLabel = wx.StaticText( self, wx.ID_ANY, _(u"Cap Right:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_CapRightLabel.Wrap( -1 )

        fgSizerSetup.Add( self.m_CapRightLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )

        m_CapRightChoiceChoices = [ wx.EmptyString, _(u"]"), _(u")"), _(u"/"), _(u"\\"), _(u">"), _(u"<") ]
        self.m_CapRightChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_CapRightChoiceChoices, 0 )
        self.m_CapRightChoice.SetSelection( 0 )
        fgSizerSetup.Add( self.m_CapRightChoice, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.RIGHT, 3 )

        self.m_WidthLabel = wx.StaticText( self, wx.ID_ANY, _(u"Width:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_WidthLabel.Wrap( -1 )

        fgSizerSetup.Add( self.m_WidthLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        self.m_WidthCtrl = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 128, 0.000000, 0.1 )
        self.m_WidthCtrl.SetDigits( 1 )
        fgSizerSetup.Add( self.m_WidthCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_WidthUnits = wx.StaticText( self, wx.ID_ANY, _(u"unit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_WidthUnits.Wrap( -1 )

        fgSizerSetup.Add( self.m_WidthUnits, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        self.m_AlignmentLabel = wx.StaticText( self, wx.ID_ANY, _(u"Alignment:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_AlignmentLabel.Wrap( -1 )

        fgSizerSetup.Add( self.m_AlignmentLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        m_AlignmentChoiceChoices = [ _(u"Left"), _(u"Center"), _(u"Right") ]
        self.m_AlignmentChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AlignmentChoiceChoices, 0 )
        self.m_AlignmentChoice.SetSelection( 0 )
        fgSizerSetup.Add( self.m_AlignmentChoice, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.RIGHT, 3 )

        self.m_lineSpacingLabel = wx.StaticText( self, wx.ID_ANY, _(u"Line Spacing:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lineSpacingLabel.Wrap( -1 )

        fgSizerSetup.Add( self.m_lineSpacingLabel, 0, wx.ALL, 5 )

        self.m_LineSpacingCtrl = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.1, 100, 1.5, 0.1 )
        self.m_LineSpacingCtrl.SetDigits( 1 )
        fgSizerSetup.Add( self.m_LineSpacingCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


        fgSizerSetup.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_LayerComboBox1 = wx.StaticText( self, wx.ID_ANY, _(u"Layer:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_LayerComboBox1.Wrap( -1 )

        fgSizerSetup.Add( self.m_LayerComboBox1, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        m_LayerComboBoxChoices = []
        self.m_LayerComboBox = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_LayerComboBoxChoices, 0 )
        fgSizerSetup.Add( self.m_LayerComboBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


        bMainSizer.Add( fgSizerSetup, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bMainSizer.Add( self.m_staticline1, 0, wx.EXPAND|wx.ALL, 5 )

        fgSizerPadding = wx.FlexGridSizer( 0, 4, 4, 4 )
        fgSizerPadding.AddGrowableCol( 0 )
        fgSizerPadding.AddGrowableCol( 1 )
        fgSizerPadding.AddGrowableCol( 2 )
        fgSizerPadding.AddGrowableCol( 3 )
        fgSizerPadding.SetFlexibleDirection( wx.BOTH )
        fgSizerPadding.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_PaddingLabel = wx.StaticText( self, wx.ID_ANY, _(u"Padding:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_PaddingLabel.Wrap( -1 )

        fgSizerPadding.Add( self.m_PaddingLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )


        fgSizerPadding.Add( ( 0, 0), 0, wx.EXPAND, 5 )


        fgSizerPadding.Add( ( 0, 0), 0, wx.EXPAND, 5 )


        fgSizerPadding.Add( ( 0, 0), 0, wx.EXPAND, 5 )

        self.m_PaddingTopLabel = wx.StaticText( self, wx.ID_ANY, _(u"Top"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_PaddingTopLabel.Wrap( -1 )

        fgSizerPadding.Add( self.m_PaddingTopLabel, 0, wx.ALIGN_CENTER, 5 )

        self.m_PaddingLeftLabel = wx.StaticText( self, wx.ID_ANY, _(u"Left"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_PaddingLeftLabel.Wrap( -1 )

        fgSizerPadding.Add( self.m_PaddingLeftLabel, 0, wx.ALIGN_CENTER, 5 )

        self.m_PaddingRightLabel = wx.StaticText( self, wx.ID_ANY, _(u"Right"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_PaddingRightLabel.Wrap( -1 )

        fgSizerPadding.Add( self.m_PaddingRightLabel, 0, wx.ALIGN_CENTER, 5 )

        self.m_PaddingBottomLabel = wx.StaticText( self, wx.ID_ANY, _(u"Bottom"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_PaddingBottomLabel.Wrap( -1 )

        fgSizerPadding.Add( self.m_PaddingBottomLabel, 0, wx.ALIGN_CENTER, 5 )

        self.m_PaddingTopCtrl = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 100, 0, 1 )
        self.m_PaddingTopCtrl.SetDigits( 1 )
        fgSizerPadding.Add( self.m_PaddingTopCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_PaddingLeftCtrl = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 100, 0, 1 )
        self.m_PaddingLeftCtrl.SetDigits( 1 )
        fgSizerPadding.Add( self.m_PaddingLeftCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_PaddingRightCtrl = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 100, 0, 1 )
        self.m_PaddingRightCtrl.SetDigits( 1 )
        fgSizerPadding.Add( self.m_PaddingRightCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_PaddingBottomCtrl = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 100, 0, 1 )
        self.m_PaddingBottomCtrl.SetDigits( 1 )
        fgSizerPadding.Add( self.m_PaddingBottomCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


        bMainSizer.Add( fgSizerPadding, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 10 )

        self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bMainSizer.Add( self.m_staticline11, 0, wx.EXPAND|wx.ALL, 5 )

        self.m_lineoverPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizerLineover = wx.FlexGridSizer( 3, 5, 4, 4 )
        fgSizerLineover.SetFlexibleDirection( wx.BOTH )
        fgSizerLineover.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_lineoverLabel = wx.StaticText( self.m_lineoverPanel, wx.ID_ANY, _(u"Lineover:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lineoverLabel.Wrap( -1 )

        fgSizerLineover.Add( self.m_lineoverLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

        self.m_lineoverStyleLabel = wx.StaticText( self.m_lineoverPanel, wx.ID_ANY, _(u"Style"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lineoverStyleLabel.Wrap( -1 )

        fgSizerLineover.Add( self.m_lineoverStyleLabel, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_lineoverThicknessLabel = wx.StaticText( self.m_lineoverPanel, wx.ID_ANY, _(u"Thickness"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lineoverThicknessLabel.Wrap( -1 )

        fgSizerLineover.Add( self.m_lineoverThicknessLabel, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        fgSizerLineover.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        fgSizerLineover.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        fgSizerLineover.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        m_lineoverStyleChoiceChoices = [ _(u"Square"), _(u"Rounded") ]
        self.m_lineoverStyleChoice = wx.Choice( self.m_lineoverPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lineoverStyleChoiceChoices, 0 )
        self.m_lineoverStyleChoice.SetSelection( 0 )
        fgSizerLineover.Add( self.m_lineoverStyleChoice, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_lineoverThicknessCtrl = wx.SpinCtrl( self.m_lineoverPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 1 )
        fgSizerLineover.Add( self.m_lineoverThicknessCtrl, 0, wx.ALL, 5 )

        self.m_lineoverThicknessUnits = wx.StaticText( self.m_lineoverPanel, wx.ID_ANY, _(u"unit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lineoverThicknessUnits.Wrap( -1 )

        fgSizerLineover.Add( self.m_lineoverThicknessUnits, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )


        fgSizerLineover.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.m_lineoverPanel.SetSizer( fgSizerLineover )
        self.m_lineoverPanel.Layout()
        fgSizerLineover.Fit( self.m_lineoverPanel )
        bMainSizer.Add( self.m_lineoverPanel, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )

        self.m_spCharPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizerSpChar = wx.FlexGridSizer( 0, 6, 4, 4 )
        fgSizerSpChar.SetFlexibleDirection( wx.BOTH )
        fgSizerSpChar.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_spCharLabel = wx.StaticText( self.m_spCharPanel, wx.ID_ANY, _(u"Special Characters:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_spCharLabel.Wrap( -1 )

        fgSizerSpChar.Add( self.m_spCharLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )

        self.m_spCharOhm = wx.Button( self.m_spCharPanel, wx.ID_ANY, _(u" Ω "), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        self.m_spCharOhm.SetMinSize( wx.Size( 52,-1 ) )

        fgSizerSpChar.Add( self.m_spCharOhm, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spCharMu = wx.Button( self.m_spCharPanel, wx.ID_ANY, _(u" μ "), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        self.m_spCharMu.SetMinSize( wx.Size( 52,-1 ) )

        fgSizerSpChar.Add( self.m_spCharMu, 0, wx.TOP|wx.BOTTOM, 5 )

        self.m_spCharHyp2 = wx.Button( self.m_spCharPanel, wx.ID_ANY, _(u" ² "), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        self.m_spCharHyp2.SetMinSize( wx.Size( 52,-1 ) )

        fgSizerSpChar.Add( self.m_spCharHyp2, 0, wx.TOP|wx.BOTTOM, 5 )

        self.m_spCharDegree = wx.Button( self.m_spCharPanel, wx.ID_ANY, _(u" ° "), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        self.m_spCharDegree.SetMinSize( wx.Size( 52,-1 ) )

        fgSizerSpChar.Add( self.m_spCharDegree, 0, wx.TOP|wx.BOTTOM, 5 )

        self.m_spCharNumero = wx.Button( self.m_spCharPanel, wx.ID_ANY, _(u" № "), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        self.m_spCharNumero.SetMinSize( wx.Size( 52,-1 ) )

        fgSizerSpChar.Add( self.m_spCharNumero, 0, wx.TOP|wx.BOTTOM, 5 )

        self.m_inlineFormatTextbox = wx.CheckBox( self.m_spCharPanel, wx.ID_ANY, _(u"Inline Formatting"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizerSpChar.Add( self.m_inlineFormatTextbox, 0, wx.BOTTOM|wx.LEFT, 5 )


        self.m_spCharPanel.SetSizer( fgSizerSpChar )
        self.m_spCharPanel.Layout()
        fgSizerSpChar.Fit( self.m_spCharPanel )
        bMainSizer.Add( self.m_spCharPanel, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )

        self.m_AdvancedDivider = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bMainSizer.Add( self.m_AdvancedDivider, 0, wx.EXPAND |wx.ALL, 5 )

        lowerSizer = wx.BoxSizer( wx.HORIZONTAL )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_advancedCheckbox = wx.CheckBox( self, wx.ID_ANY, _(u"Advanced"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_advancedCheckbox, 0, wx.ALL, 5 )


        lowerSizer.Add( bSizer5, 1, wx.ALL, 5 )


        lowerSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        m_sdbSizer = wx.StdDialogButtonSizer()
        self.m_sdbSizerOK = wx.Button( self, wx.ID_OK )
        m_sdbSizer.AddButton( self.m_sdbSizerOK )
        self.m_sdbSizerCancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer.AddButton( self.m_sdbSizerCancel )
        m_sdbSizer.Realize();

        lowerSizer.Add( m_sdbSizer, 0, wx.ALL, 5 )


        bMainSizer.Add( lowerSizer, 0, wx.EXPAND, 5 )


        self.SetSizer( bMainSizer )
        self.Layout()
        bMainSizer.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_INIT_DIALOG, self.OnInitDlg )
        self.m_MultiLineText.Bind( wx.EVT_CHAR_HOOK, self.OnCharHook )
        self.m_lineoverStyleChoice.Bind( wx.EVT_CHOICE, self.lineoverStyleChange )
        self.m_lineoverThicknessCtrl.Bind( wx.EVT_SPINCTRL, self.thicknessCtrlChange )
        self.m_lineoverThicknessCtrl.Bind( wx.EVT_TEXT, self.thicknessCtrlChange )
        self.m_lineoverThicknessCtrl.Bind( wx.EVT_TEXT_ENTER, self.thicknessCtrlChange )
        self.m_spCharOhm.Bind( wx.EVT_BUTTON, self.addCharOhm )
        self.m_spCharMu.Bind( wx.EVT_BUTTON, self.addCharMu )
        self.m_spCharHyp2.Bind( wx.EVT_BUTTON, self.addCharSup2 )
        self.m_spCharDegree.Bind( wx.EVT_BUTTON, self.addCharDegree )
        self.m_spCharNumero.Bind( wx.EVT_BUTTON, self.addCharNumero )
        self.m_inlineFormatTextbox.Bind( wx.EVT_CHECKBOX, self.inlineFormatChange )
        self.m_advancedCheckbox.Bind( wx.EVT_CHECKBOX, self.advancedModeChange )
        self.m_sdbSizerOK.Bind( wx.EVT_BUTTON, self.OnOkClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnInitDlg( self, event ):
        pass

    def OnCharHook( self, event ):
        pass

    def lineoverStyleChange( self, event ):
        pass

    def thicknessCtrlChange( self, event ):
        pass



    def addCharOhm( self, event ):
        pass

    def addCharMu( self, event ):
        pass

    def addCharSup2( self, event ):
        pass

    def addCharDegree( self, event ):
        pass

    def addCharNumero( self, event ):
        pass

    def inlineFormatChange( self, event ):
        pass

    def advancedModeChange( self, event ):
        pass

    def OnOkClick( self, event ):
        pass



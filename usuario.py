#-Begin-----------------------------------------------------------------

#-Includes--------------------------------------------------------------
#from verify import verify
import sys, win32com.client
from Ticket import *
from datetime import datetime

class Usuario():
    def __init__(self):
        a = 1 ## apenas para ter o _init__

    @staticmethod
    def tratar_data(dados):
        data_departure = dados[13].replace("/",".")
        return data_departure

    @staticmethod
    def create_new_user(ticket):
        #print("Tipo de Request: " + str(ticket.tipoRequest))
        #print("Existiu: " + str(ticket.existiu))
        #print(ticket)
        if ticket.login != "":

            try:
                SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
                # SapGuiAuto = win32com.client.GetObject("SAPGUI")
                if not type(SapGuiAuto) == win32com.client.CDispatch:
                    #print("01")
                    return

                connection = SapGuiAuto.Children(0)
                if not type(connection) == win32com.client.CDispatch:
                    SapGuiAuto = None
                    #print("03")
                    return

                # session = SapGuiAuto.FindById("ses[0]")
                session = connection.FindById("ses[0]")
                if not type(session) == win32com.client.CDispatch:
                    connection = None
                    SapGuiAuto = None
                    #print("04")
                    return
                ####################################################################################################
                ####################################################################################################
                session.findById("wnd[0]").maximize()
                session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
                session.findById("wnd[0]").sendVKey(0)
                session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = ticket.login ###LOGIN

                session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").caretPosition = 8
                session.findById("wnd[0]/tbar[1]/btn[8]").press()

                if ticket.existiu == 1:
                    session.findById("wnd[1]/usr/btnBUTTON_2").press()

                #print("TESTE01")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_PERSON_NAME_EXT-TITLE_MEDI").key = "0002"  ##SEXO
                #print("TESTE02")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_PERSON_NAME-NAME_LAST").text = ticket.lastName  ##SOBRENOME
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_PERSON_NAME-NAME_FIRST").text = ticket.name   ##NOME
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_PERSON_NAME-LANGU").key = "PT"  ##LANGUAGE
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-FUNCTION").text = ticket.function ##FUNCAO
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-DEPARTMENT").text = ticket.department   ##DEPARTAMENTO
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_COMM_DATA-SMTP_ADDR").text = ticket.email  ##EMAIL
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_WORKPLACE-DEFLT_COMM").key = "INT"
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_WORKPLACE-DEFLT_COMM").setFocus()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO").select()

                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-USERALIAS").text = ticket.aliasUser  ##ALIAS USER
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-USERALIAS").caretPosition = 15
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-CLASS").text = ticket.group   ##GROUP-SITE
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGB").text = ticket.departureDate  ##DEPARTURE
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGV").text = Usuario().dataHoje() ##Data de Criação
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGV").setFocus()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/btnFKT_DEL").press()

                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").text = ticket.requestID  ##RequestID
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").setFocus()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").caretPosition = 8
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpSNC").select()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpSNC/ssubMAINAREA:SAPLSUID_MAINTENANCE:2002/txtSUID_ST_NODE_SNC-PNAME").text = ticket.sncName  ##SNCNAME
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpSNC/ssubMAINAREA:SAPLSUID_MAINTENANCE:2002/txtSUID_ST_NODE_SNC-PNAME").caretPosition = 20
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA").select()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA/ssubMAINAREA:SAPLSUID_MAINTENANCE:1105/chkSUID_ST_NODE_DEFAULTS-SPDB").selected = True
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA/ssubMAINAREA:SAPLSUID_MAINTENANCE:1105/chkSUID_ST_NODE_DEFAULTS-SPDA").selected = True
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA/ssubMAINAREA:SAPLSUID_MAINTENANCE:1105/ctxtSUID_ST_NODE_DEFAULTS-LANGU").text = "PT"
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA/ssubMAINAREA:SAPLSUID_MAINTENANCE:1105/ctxtSUID_ST_NODE_DEFAULTS-SPLD").text = "DEFAULT"
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA/ssubMAINAREA:SAPLSUID_MAINTENANCE:1105/chkSUID_ST_NODE_DEFAULTS-SPDA").setFocus()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA/ssubMAINAREA:SAPLSUID_MAINTENANCE:1105/ctxtSUID_ST_NODE_DEFAULTS-TZONE").text = "BRAZIL"
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpDEFA/ssubMAINAREA:SAPLSUID_MAINTENANCE:1105/ctxtSUID_ST_NODE_DEFAULTS-TZONE").setFocus()

                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG").select()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(0, "AGR_NAME", ticket.role01)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(1, "AGR_NAME", ticket.role02)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(2, "AGR_NAME", ticket.role03)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(3, "AGR_NAME", ticket.role04)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(4, "AGR_NAME", ticket.role05)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(5, "AGR_NAME", ticket.role06)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(6, "AGR_NAME", ticket.role07)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(7, "AGR_NAME", ticket.role08)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(8, "AGR_NAME", ticket.role09)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(9, "AGR_NAME", ticket.role10)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(10, "AGR_NAME", ticket.role11)

                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(11, "AGR_NAME", ticket.role12)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(12, "AGR_NAME", ticket.role13)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(13, "AGR_NAME", ticket.role14)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(14, "AGR_NAME", ticket.role15)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("15")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(15, "AGR_NAME", ticket.role16)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("16")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(16, "AGR_NAME", ticket.role17)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("17")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(17, "AGR_NAME", ticket.role18)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("18")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(18, "AGR_NAME", ticket.role19)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("19")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(19, "AGR_NAME", ticket.role20)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("20")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(20, "AGR_NAME", ticket.role21)

                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("21")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(21, "AGR_NAME", ticket.role22)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("22")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(22, "AGR_NAME", ticket.role23)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("23")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(23, "AGR_NAME", ticket.role24)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("24")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(24, "AGR_NAME", ticket.role25)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("25")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(25, "AGR_NAME", ticket.role26)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("26")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(26, "AGR_NAME", ticket.role27)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("27")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(27, "AGR_NAME", ticket.role28)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("28")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(28, "AGR_NAME", ticket.role29)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("29")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(29, "AGR_NAME", ticket.role30)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("30")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(30, "AGR_NAME", ticket.role31)

                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("31")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(31, "AGR_NAME", ticket.roleExceptional)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("32")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(32, "AGR_NAME", ticket.roleExceptional1)
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("33")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(33, "AGR_NAME", ticket.roleExceptional2)
                #session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").setCurrentCell(33, "AGR_NAME")
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").firstVisibleRow = 20
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressEnter()
                session.findById("wnd[0]").maximize()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpPROF").select()
                session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLAW").select()

                if ticket.tipoUsuario == 1:
                    session.findById(
                        "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "73"
                else:
                    session.findById(
                        "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "AX"

                session.findById("wnd[0]/tbar[0]/btn[11]").press()

                ####################################################################################################
                ####################################################################################################

            except:
                print(sys.exc_info()[0])
                #MyWindow.mensagem(sys.exc_info()[0])
            finally:
                session = None
                connection = None
                SapGuiAuto = None
        else:
            print("Login veio Vazio")


    @staticmethod
    def addNewProfile(ticket):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################

            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = ticket.login ###LOGIN
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").caretPosition = 6
            session.findById("wnd[0]/tbar[1]/btn[18]").press()

            # session.findById("wnd[0]/tbar[1]/btn[18]").press()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-CLASS").text = ticket.group  ##GROUP-SITE
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGV").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGB").text = ticket.departureDate  ##DEPARTURE

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").text = ticket.requestID  ##RequestID
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").caretPosition = 11
            # session.findById("wnd[0]/tbar[0]/btn[11]").press

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").setCurrentCell(- 1, "AGR_NAME")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").selectColumn("AGR_NAME")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressToolbarButton("&SORT_ASC")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(0, "AGR_NAME", ticket.role01)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(1, "AGR_NAME", ticket.role02)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(2, "AGR_NAME", ticket.role03)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(3, "AGR_NAME", ticket.role04)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(4, "AGR_NAME", ticket.role05)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(5, "AGR_NAME", ticket.role06)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(6, "AGR_NAME", ticket.role07)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(7, "AGR_NAME", ticket.role08)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(8, "AGR_NAME", ticket.role09)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(9, "AGR_NAME", ticket.role10)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(10, "AGR_NAME", ticket.role11)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(11, "AGR_NAME", ticket.role12)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(12, "AGR_NAME", ticket.role13)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(13, "AGR_NAME", ticket.role14)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(14, "AGR_NAME", ticket.role15)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("16")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").currentCellColumn = "AGR_NAME"
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressEnter()
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpPROF").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLAW").select()

            if ticket.tipoUsuario == 1:
                session.findById(
                    "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "73"
            else:
                session.findById(
                    "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "AX"

            session.findById("wnd[0]/tbar[0]/btn[11]").press()

            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            SapGuiAuto = None

    @staticmethod
    def addExceptionalRole(ticket):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = ticket.login ###LOGIN
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").caretPosition = 6
            session.findById("wnd[0]/tbar[1]/btn[18]").press()

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_PERSON_NAME_EXT-TITLE_MEDI").key = "0002"  ##SEXO
            # print("TESTE02")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_PERSON_NAME-NAME_LAST").text = ticket.lastName  ##SOBRENOME
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_PERSON_NAME-NAME_FIRST").text = ticket.name  ##NOME
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_PERSON_NAME-LANGU").key = "PT"  ##LANGUAGE
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-FUNCTION").text = ticket.function  ##FUNCAO
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-DEPARTMENT").text = ticket.department  ##DEPARTAMENTO
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_COMM_DATA-SMTP_ADDR").text = ticket.email  ##EMAIL
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_WORKPLACE-DEFLT_COMM").key = "INT"
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_WORKPLACE-DEFLT_COMM").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO").select()


            #session.findById("wnd[0]/tbar[1]/btn[18]").press()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-CLASS").text = ticket.group  ##GROUP-SITE
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGV").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGB").text = ticket.departureDate  ##DEPARTURE

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").text = ticket.requestID  ##RequestID
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").caretPosition = 11
            #session.findById("wnd[0]/tbar[0]/btn[11]").press

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").setCurrentCell(- 1, "AGR_NAME")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").selectColumn("AGR_NAME")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressToolbarButton("&SORT_ASC")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(0, "AGR_NAME", ticket.roleExceptional)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(1, "AGR_NAME", ticket.roleExceptional1)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(2, "AGR_NAME", ticket.roleExceptional2)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").currentCellColumn = "AGR_NAME"
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressEnter()
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpPROF").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLAW").select()

            if ticket.tipoUsuario == 1:
                session.findById(
                    "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "73"
            else:
                session.findById(
                    "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "AX"


            session.findById("wnd[0]/tbar[0]/btn[11]").press()
            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            SapGuiAuto = None

    @staticmethod
    def replaceProfile(ticket):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = ticket.login  ###LOGIN

            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").caretPosition = 8
            session.findById("wnd[0]/tbar[1]/btn[18]").press()

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_PERSON_NAME_EXT-TITLE_MEDI").key = "0002"  ##SEXO
            # print("TESTE02")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_PERSON_NAME-NAME_LAST").text = ticket.lastName  ##SOBRENOME
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_PERSON_NAME-NAME_FIRST").text = ticket.name  ##NOME
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_PERSON_NAME-LANGU").key = "PT"  ##LANGUAGE
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-FUNCTION").text = ticket.function  ##FUNCAO
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-DEPARTMENT").text = ticket.department  ##DEPARTAMENTO
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_COMM_DATA-SMTP_ADDR").text = ticket.email  ##EMAIL
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_WORKPLACE-DEFLT_COMM").key = "INT"
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/cmbSUID_ST_NODE_WORKPLACE-DEFLT_COMM").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO").select()

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-CLASS").text = ticket.group  ##GROUP-SITE
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGV").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/ctxtSUID_ST_NODE_LOGONDATA-GLTGB").text = ticket.departureDate  ##DEPARTURE

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").text = ticket.requestID  ##RequestID
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").caretPosition = 11
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").setCurrentCell(- 1, "")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").selectAll()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressToolbarButton("DEL_LINE")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(0, "AGR_NAME", ticket.role01)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(1, "AGR_NAME", ticket.role02)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(2, "AGR_NAME", ticket.role03)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(3, "AGR_NAME", ticket.role04)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(4, "AGR_NAME", ticket.role05)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(5, "AGR_NAME", ticket.role06)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(6, "AGR_NAME", ticket.role07)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(7, "AGR_NAME", ticket.role08)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(8, "AGR_NAME", ticket.role09)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(9, "AGR_NAME", ticket.role10)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(10, "AGR_NAME", ticket.role11)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(11, "AGR_NAME", ticket.role12)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(12, "AGR_NAME", ticket.role13)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(13, "AGR_NAME", ticket.role14)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(14, "AGR_NAME", ticket.role15)
            #session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").insertRows("16")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").currentCellColumn = "AGR_NAME"
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressEnter()
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpPROF").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLAW").select()

            if ticket.tipoUsuario == 1:
                session.findById(
                    "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "73"
            else:
                session.findById(
                    "wnd[0]/usr/tabsTABSTRIP1/tabpLAW/ssubMAINAREA:SAPLSUID_MAINTENANCE:1112/cmbSUID_ST_NODE_UCLASS-LIC_TYPE").key = "AX"


            session.findById("wnd[0]/tbar[0]/btn[11]").press()
            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            SapGuiAuto = None

    @staticmethod
    def deleteUser(ticket):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = ticket.login
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").caretPosition = 6
            session.findById("wnd[0]/tbar[1]/btn[18]").press()

            #session.findById("wnd[0]/tbar[1]/btn[18]").press()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").text = ticket.requestID  ##RequestID
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").setFocus()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpLOGO/ssubMAINAREA:SAPLSUID_MAINTENANCE:1101/txtSUID_ST_NODE_LOGONDATA-ACCNT").caretPosition = 11
            #session.findById("wnd[0]/tbar[0]/btn[11]").press

            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG").select()
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").setCurrentCell(- 1, "AGR_NAME")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").selectColumn("AGR_NAME")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressToolbarButton("&SORT_ASC")
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(0, "AGR_NAME", ticket.roleExceptional)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(1, "AGR_NAME", ticket.roleExceptional)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").modifyCell(2, "AGR_NAME", ticket.roleExceptional)
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").currentCellColumn = "AGR_NAME"
            session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpACTG/ssubMAINAREA:SAPLSUID_MAINTENANCE:1106/cntlG_ROLES_CONTAINER/shellcont/shell").pressEnter()
            session.findById("wnd[0]/tbar[0]/btn[11]").press()
            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            SapGuiAuto = None

     ##FUNÇÃO PARA VERIFICAR SE NO SAP, SE O USUÁRIO EXISTE
    @staticmethod
    def usuarioExiste(login):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################

            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = login
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").caretPosition = 6
            session.findById("wnd[0]").sendVKey(0)

        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            SapGuiAuto = None

    ##VERIFICAR USANDO A TRANSAÇÃO SE O USER EXISTOU
    @staticmethod
    def usuarioExistiu(login):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################

            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = login
            session.findById("wnd[0]/tbar[1]/btn[8]").press()

        except:
            print(sys.exc_info()[0])
        finally:
            session = None
            connection = None
            SapGuiAuto = None

    ##VERIFICAR COMPATIBILIDADE DE ALGUMA ROLE
    @staticmethod
    def verificarCompatibilidade(login, role):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nzlsf_check_compat"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtS_USERS-LOW").text = login
            session.findById("wnd[0]/usr/ctxtS_ROLES-LOW").text = role
            session.findById("wnd[0]/usr/ctxtS_ROLES-LOW").setFocus()
            session.findById("wnd[0]/usr/ctxtS_ROLES-LOW").caretPosition = 16
            session.findById("wnd[0]/tbar[1]/btn[8]").press()

            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])
        finally:
            session = None
            connection = None
            SapGuiAuto = None


    ##VERIFICAR COMPATIBILIDADE DE ALGUMA ROLE
    @staticmethod
    def verificarCompatibilidadeUser(login):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nzlsf_check_roles"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtS_USER-LOW").text = login
            session.findById("wnd[0]/usr/ctxtS_USER-LOW").setFocus()
            session.findById("wnd[0]/usr/ctxtS_USER-LOW").caretPosition = 6
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/tbar[1]/btn[8]").press()

            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])
        finally:
            session = None
            connection = None
            SapGuiAuto = None

    ##VERIFICAR COMPATIBILIDADE DAS TRÊS ROLES AO MESMO TEMPO
    @staticmethod
    def verificarCompatibilidade3(ticket):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nzlsf_check_compat"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtS_USERS-LOW").text = ticket.login
            session.findById("wnd[0]/usr/ctxtS_ROLES-LOW").text = ticket.roleExceptional
            session.findById("wnd[0]/usr/ctxtS_ROLES-LOW").setFocus()
            session.findById("wnd[0]/usr/ctxtS_ROLES-LOW").caretPosition = 17
            session.findById("wnd[0]/usr/btn%_S_ROLES_%_APP_%-VALU_PUSH").press()
            session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = ticket.roleExceptional1
            session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = ticket.roleExceptional2
            session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").setFocus()
            session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").caretPosition = 17
            session.findById("wnd[1]/tbar[0]/btn[8]").press()
            session.findById("wnd[0]/tbar[1]/btn[8]").press()

            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])
        finally:
            session = None
            connection = None
            SapGuiAuto = None


    ##DESBLOQUEAR USUÁRIO
    @staticmethod
    def unlockedUser(ticket):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                #print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                #print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                #print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsu01"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = ticket.login
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/tbar[1]/btn[29]").press()
            session.findById("wnd[1]/tbar[0]/btn[7]").press()

            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])
        finally:
            session = None
            connection = None
            SapGuiAuto = None

    @staticmethod
    def add_query_global(query):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                # print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                # print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsq03"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/mbar/menu[4]/menu[0]").select()
            session.findById("wnd[1]/usr/radRAD2").select()
            session.findById("wnd[1]/usr/radRAD2").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[2]").press()
            session.findById("wnd[0]/usr/ctxtRS38S-BGNUM").text = query
            session.findById("wnd[0]/usr/ctxtRS38S-BGNUM").caretPosition = 5
            session.findById("wnd[0]/usr/btnP6").press()

        except BaseException as ex:
            print(sys.exc_info()[0])
            print('Erro ao adicionar Query {}'.format(ex))

        finally:
            session = None
            connection = None
            SapGuiAuto = None



    @staticmethod
    def add_query_standard(query):
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            # SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                print("01")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                # print("03")
                return

            # session = SapGuiAuto.FindById("ses[0]")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                # print("04")
                return
            ####################################################################################################
            ####################################################################################################
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsq03"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/mbar/menu[4]/menu[0]").select()
            session.findById("wnd[1]/usr/radRAD1").select()
            session.findById("wnd[1]/tbar[0]/btn[2]").press()
            session.findById("wnd[0]/usr/ctxtRS38S-BGNUM").text = query
            session.findById("wnd[0]/usr/ctxtRS38S-BGNUM").caretPosition = 12
            session.findById("wnd[0]/usr/btnP6").press()

        except BaseException as ex:
            print(sys.exc_info()[0])
            print('Erro ao adicionar Query {}'.format(ex))

        finally:
            session = None
            connection = None
            SapGuiAuto = None

    @staticmethod
    def rodarZCHR():
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            print("Rodando 001")
            if not type(SapGuiAuto) == win32com.client.CDispatch:
                print("Rodando 002")
                return

            connection = SapGuiAuto.Children(0)
            if not type(connection) == win32com.client.CDispatch:
                SapGuiAuto = None
                print("Rodando 003")
                return

                print("Rodando 004")
            session = connection.FindById("ses[0]")
            if not type(session) == win32com.client.CDispatch:
                connection = None
                SapGuiAuto = None
                # print("04")
                return
            ####################################################################################################
            ####################################################################################################
            print("Local 001")
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nzchr"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/tbar[1]/btn[8]").press()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellColumn = "EXEC"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "0"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 1
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "1"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 2
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "2"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 3
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "3"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 4
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "4"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 5
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "5"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 6
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "6"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 7
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "7"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 8
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "8"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 9
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "9"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 10
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "10"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 11
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "11"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 12
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "12"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 13
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "13"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 14
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "14"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 15
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "15"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 16
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "16"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 17
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "17"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 18
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "18"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 19
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "19"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 20
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "20"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 21
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "21"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 22
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "22"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").setCurrentCell(20), "SP02_RESULTS"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = ""

            ####################################################################################################
            ####################################################################################################

        except:
            print(sys.exc_info()[0])

        finally:
            session = None
            connection = None
            SapGuiAuto = None


    def dataHoje(self):
        hoje = datetime.now()
        data = str(hoje.day) + "." + str(hoje.month) + "." + str(hoje.year)
        return data

# Author: Minh.Nguyen
# Created Date: August 15, 2016  
# Description: to store all elements on Login screen



# loading bar
LoadingBar = '//div[@id="loading-bar"]'

# loading screen
LoadingScreen = '//div[@id="ip-container"]/header/div[@class="ip-logo"]'


# side bar - navigation bar - left menu
HomePage_Navigation_StringFileFromMyComputer = '//nav[@role="navigation"]//a/span[@class="icon-my-computer"]'
HomePage_Navigation_StringFileFromMyCloud = '//nav[@role="navigation"]//a/span[@class="icon-cloud-download"]'




HomePage_Navigation_FilesLibrary = '//li[@id="filesLib"]'
HomePage_Navigation_FilesLibrary_MyFiles = '//li[@id="allFile"]'
HomePage_Navigation_FilesLibrary_ReceivedFiles = '//li[@id="shareFile"]'
HomePage_Navigation_FilesLibrary_ReceivedFiles_NewReceivedFiles = '//li[@id="shareFile"]//a[@title="New Received Files"]'

HomePage_StringFileSuccess = '//div[@class="ui-notification ng-scope success"]'





HomePage_Navigation_Footer = '//div[@class="navbar-footer"]'
HomePage_Navigation_Footer_Logout = '//a[@id="logout"]'










HomePage_ListOfFiles = '//table[@id="list-file"]/tbody'
HomePage_ListOfFiles_General = HomePage_ListOfFiles + '/tr'
HomePage_ListOfFiles_FileName = '/td[3]/a'
HomePage_ListOfFiles_SelectionBox = '/td[2]/a'


HomePage_ToolBar_DeleteItem = '//div[@id="toolbar"]/a[@class="delete"]'
HomePage_ToolBar_RevokeItem = '//div[@id="toolbar"]/a[@class="revoke"]'


HomePage_Popup = '//div[@role="dialog"]'
HomePage_Popup_Button1 = HomePage_Popup + '//div[@class="modal-footer"]/button[1]'
HomePage_Popup_Button2 = HomePage_Popup + '//div[@class="modal-footer"]/button[2]'





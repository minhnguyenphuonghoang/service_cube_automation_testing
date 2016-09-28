# Author: Minh.Nguyen
# Created Date: August 24, 2016  
# Description: to store all elements on Home Page - String File Popup


StringFilesPopup = '//div[@role="dialog"]'
StringFiles_UploadFile = StringFilesPopup + '//div[contains(@id,"primaryUploaderContainer")]/div[2]/input'
StringFiles_EmailAddressTextField = StringFilesPopup + '//tags-input[@ng-model="tags"]/div[@class="host"]/div/input'
StringFiles_AccessLevel_Reshare = StringFilesPopup + '//input[@value="reshare"]'
StringFiles_AccessLevel_ViewOnly = StringFilesPopup + '//input[@value="view"]'

StringFiles_CancelButton = StringFilesPopup + '//button[text()="Cancel"]'
StringFiles_StringButton = StringFilesPopup + '//button[@pb-profile="progressButton"]'


StringFiles_UploadProgressBar_Success = StringFilesPopup + '//span[@class="upload-bar success"]'







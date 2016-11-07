# Author: Minh.nguyen
# Date Created: Oct 13, 2016
#

# Reset Password screen - before clicking on CONTINUE button
ResetPassword_ServiceCubeLogo = '//a[@class="logo"]'
ResetPassword_Title = '//a[@class="close-dialog"]/following-sibling::h3'
ResetPassword_CloseButton = '//a[@class="close-dialog"]'
ResetPassword_Description = '//a[@class="close-dialog"]/following-sibling::ul/li[1]/p'
ResetPassword_EmailAddressTextField = '//input[@id="resetEmail"]'
ResetPassword_ContinueButton = '//button[@id="resetBtn"]'
ResetPassword_ErrorMessage = '//form[contains(@class,"resetPassForm")]/ul/li[2]/span[not(contains(@class,"hide"))]'

# Reset Password screen - After clicking on CONTINUE button
ResetPassword_EmailSentPopup_LeterIcon = '//div[contains(@class,"dialog")]/p[1]/i[contains(@class,"icon-mail")]'
ResetPassword_EmailSentPopup_Title = '//div[contains(@class,"dialog")]/h3'
ResetPassword_EmailSentPopup_Description = '//div[contains(@class,"dialog")]/p[2]'


# Reset Password screen - Choose your new password screen
ResetPassword_SetPassword_Title = '//form[contains(@class,"dialog")]/h3'
ResetPassword_SetPassword_PasswordTextField = '//input[@id="newPass"]'
ResetPassword_SetPassword_ConfirmPasswordTextField = '//input[@id="confirmPass"]'
ResetPassword_SetPassword_ContinueButton = '//button[@id="continueBtn"]'
ResetPassword_SetPassword_PasswordLengthError = '//span[@id="passLengthErr"]'
ResetPassword_SetPassword_ConfirmPasswordLengthError = '//span[@id="passLengthErrConf"]'
ResetPassword_SetPassword_ConfirmPasswordNotMatchError = '//span[@id="matchErr"]'





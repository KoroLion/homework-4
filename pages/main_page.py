from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = '/'

    SELF_USERNAME = '#profile-link-username'

    LISTING = '#dialogues-listing'
    MESSAGES_LISTING = '#messages-listing'

    FOLDER_ANY = '#dialogues-listing > li.folder'
    FOLDER_BY_NAME = '#dialogues-listing > .folder[data=\"%s\"]'
    FOLDER_BTN_DELETE_BY_NAME = FOLDER_BY_NAME + ' #delete-folder'
    FOLDER_BTN_RENAME_BY_NAME = FOLDER_BY_NAME + ' #rename-folder'
    FOLDER_INPUT_TITLE_BY_NAME = FOLDER_BY_NAME + ' input'
    FOLDER_BTN_CREATE = '.new-folder-button'
    FOLDER_BTN_EXPAND = '.folders-button'
    FOLDER_CURRENT_TITLE = '#dialogues-listing-divider > div'

    DIALOGUE_ANY = '#dialogues-listing > li:not(.folder)'
    DIALOGUE_BY_NAME = '#dialogues-listing li[data=\"%s\"]:not(.folder)'
    DIALOGUE_TITLE_BY_NAME = DIALOGUE_BY_NAME + ' .dialogue-title'
    DIALOGUE_IMAGE_BY_NAME = DIALOGUE_BY_NAME + ' > img'
    DIALOGUE_BTN_DELETE_BY_NAME = DIALOGUE_BY_NAME + ' #delete-dialogue'
    DIALOGUE_INPUT_FIND = '.find-input'
    DIALOGUE_BTN_ADD = '#find-dialogue-button'

    MESSAGE_ANY = '#messages-listing > div:not(.fullheight)'
    MESSAGE_LAST_ANY = MESSAGE_ANY + ':last-child'
    MESSAGE_LAST_YOUR = '#messages-listing > div.right-block:last-child'
    MESSAGE_LAST_NOT_YOUR = '#messages-listing > div.left-block:last-child'
    MESSAGE_TITLE = '%s .message-block-title'  # %s must be on of first four MESSAGE_... constants
    MESSAGE_BODY = '%s .message-body'
    MESSAGE_BTN_DELETE = '%s .delete-message'
    MESSAGE_INPUT_TITLE = '#theme-input'
    MESSAGE_INPUT_BODY = '#message-input'
    MESSAGE_BTN_SEND = '#message-send-button'
    MESSAGE_NOT_OPENED_PLUG = '#messages-listing > div.fullheight.table-rows'

    OVERLAY_INPUT = '.modal input'
    OVERLAY_SUBMIT = '.modal .submit'

    def __init__(self, driver):
        super().__init__(driver, '#messages-page')

    # --------- Folders ---------
    def expandFolders(self):
        self.click(self.FOLDER_BTN_EXPAND)

    def clickFolder(self, folderName):
        self.click(self.FOLDER_BY_NAME % folderName)

    def clickDeleteFolder(self, folderName):
        self.click_hidden(self.FOLDER_BTN_DELETE_BY_NAME % folderName)

    def clickRenameFolder(self, folderName):
        self.click_hidden(self.FOLDER_BTN_RENAME_BY_NAME % folderName)

    def clickCreateFolder(self):
        self.click(self.FOLDER_BTN_CREATE)

    def setFolderTitle(self, folderName, newTitle):
        el = self.locate_el(self.FOLDER_INPUT_TITLE_BY_NAME % folderName)
        el.send_keys(Keys.SHIFT + Keys.END)
        el.send_keys(newTitle)
        el.send_keys(Keys.ENTER)

    def getFolderTitle(self, folderName):
        return self.locate_el(self.FOLDER_INPUT_TITLE_BY_NAME % folderName).get_attribute("value")

    def getFoldersCount(self):
        return len(self.locate_el(self.LISTING).find_elements(By.CLASS_NAME, "folder"))

    def isFoldersExpanded(self):
        return self.locate_el(self.FOLDER_ANY).is_displayed()

    def isFolderExists(self, folderName):
        return self.locate_el(self.FOLDER_BY_NAME % folderName).is_displayed()

    # -------- Dialogues --------
    def clickDialogue(self, dialogueName):
        self.click(self.DIALOGUE_BY_NAME % dialogueName)

    def clickCreateDialogue(self):
        self.click(self.DIALOGUE_BTN_ADD)

    def setFindDialogue(self, value):
        self.set_field(self.DIALOGUE_INPUT_FIND, value)

    def clickDeleteDialogue(self, dialogueName):
        self.click_hidden(self.DIALOGUE_BTN_DELETE_BY_NAME % dialogueName)

    def dragAndDropDialogueToFolder(self, dialogueName, folderName):
        self.drag_and_drop(self.DIALOGUE_BY_NAME % dialogueName, self.FOLDER_BY_NAME % folderName)

    def isDialogueOpened(self, dialogueName):
        return self.locate_el(self.MESSAGE_ANY).is_displayed() and \
               self.locate_el(self.DIALOGUE_BY_NAME % dialogueName).get_attribute("class").find("active") != -1

    def isDialogueNotOpened(self):
        return self.locate_el(self.MESSAGE_NOT_OPENED_PLUG).is_displayed()

    def isDialogueExists(self, dialogueName):
        return self.locate_el(self.DIALOGUE_BY_NAME % dialogueName).is_displayed()

    def getDialogueTitle(self, dialogueName):
        return self.locate_el(self.DIALOGUE_TITLE_BY_NAME % dialogueName).text

    def getDialogueImage(self, dialogueName):
        return self.locate_el(self.DIALOGUE_IMAGE_BY_NAME % dialogueName).get_attribute("src")

    def getDialoguesCount(self):
        return len(self.locate_el(self.LISTING).find_elements(By.CSS_SELECTOR, "li:not(.folder)"))

    # -------- Messages --------
    def clickSendMessage(self):
        self.click(self.MESSAGE_BTN_SEND)

    def sendMessageByKeyboard(self):
        el = self.locate_el(self.MESSAGE_INPUT_BODY)
        el.send_keys(Keys.CONTROL + Keys.ENTER)

    def clickDeleteLastMessage(self, your: bool = None):
        if your is None:
            self.click(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_ANY)
        elif your:
            self.click(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_YOUR)
        else:
            self.click(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_NOT_YOUR)

    def setMessageTitle(self, value):
        self.set_field(self.MESSAGE_INPUT_TITLE, value)

    def setMessageBody(self, value):
        self.set_field(self.MESSAGE_INPUT_BODY, value)

    def isLastMessageYours(self):
        # return self.locate_el(self.MESSAGE_LAST_ANY).get_attribute('class').find('right-block') != -1
        return self.locate_el(self.MESSAGE_LAST_YOUR).is_displayed()

    def getLastYourMessageTitle(self):
        return self.locate_el(self.MESSAGE_TITLE % self.MESSAGE_LAST_YOUR).text

    def getLastYourMessageBody(self):
        return self.locate_el(self.MESSAGE_BODY % self.MESSAGE_LAST_YOUR).text

    def isLastMessageNotYours(self):
        return self.click(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_NOT_YOUR)

    def getMessagesCount(self):
        return len(self.locate_el(self.MESSAGES_LISTING).find_elements(By.CSS_SELECTOR, "div.message-block"))

    # --------- Overlay ----------
    def submitOverlay(self):
        self.click(self.OVERLAY_SUBMIT)

    def fillOverlay(self, value):
        self.set_field(self.OVERLAY_INPUT, value)

    # --------- Others ---------
    def get_authenticated_user_email(self):
        return self.locate_el(self.SELF_USERNAME).text

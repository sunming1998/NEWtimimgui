from Pages.Find.Publish_Journal import PublishJournal
from Pages.Login.login_by_phone import LoginByPhone
from Pages.StartUpApp.Privacy_Policy import PrivacyPolicy
from Pages.Organize_A_Team.Jurisdiction import Jurisdiction
from Pages.Wired_Intercom.Start_Connecting import StartConnecting


class Pages(object):
    """
    所有页面合集
    """
    def __init__(self):
        self.publishjournal = PublishJournal()  # 社交发布页
        self.loginbyphone = LoginByPhone()      # 登录页
        self.privacypolicy = PrivacyPolicy()    # 隐私政策
        self.jurisdiction = Jurisdiction()      # 权限页面
        self.startconnecting = StartConnecting() # 语聊房






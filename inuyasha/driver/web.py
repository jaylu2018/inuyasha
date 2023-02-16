class ChromeConfig:
    headless = False
    args = ['--no-sandbox']
    timeout = 10000


class FirefoxConfig:
    headless = False
    args = ['--no-sandbox']
    timeout = 10000


class EdgeConfig:
    headless = False
    args = ['--no-sandbox']
    timeout = 10000


class MobileConfig:
    headless = False
    args = ['--no-sandbox']
    timeout = 10000


class BasePage:

    def __new__(cls, playwright, name: str = None):

        if (name is None) or (name in ["chrome", "google chrome", "gc"]):
            return cls.chrome(playwright)
        if name in ["firefox", "ff"]:
            return cls.firefox(playwright)
        if name == "webkit":
            return cls.webkit(playwright)
        if name == "iphone":
            return cls.iphone(playwright)
        if name == "android":
            return cls.android(playwright)

    @staticmethod
    def chrome(playwright):
        browser = playwright.chromium.launch(headless=ChromeConfig.headless, args=ChromeConfig.args)
        context = browser.new_context()
        context.set_default_timeout(ChromeConfig.timeout)
        page = context.new_page()
        return page

    @staticmethod
    def firefox(playwright):
        browser = playwright.firefox.launch(headless=FirefoxConfig.headless, args=ChromeConfig.args)
        context = browser.new_context()
        context.set_default_timeout(FirefoxConfig.timeout)
        page = context.new_page()
        return page

    @staticmethod
    def webkit(playwright):
        browser = playwright.webkit.launch(headless=EdgeConfig.headless, args=ChromeConfig.args)
        context = browser.new_context()
        context.set_default_timeout(EdgeConfig.timeout)
        page = context.new_page()
        return page

    @staticmethod
    def iphone(playwright):
        browser = playwright.chromium.launch(headless=MobileConfig.headless, args=MobileConfig.args)
        iphone_12 = playwright.devices['iPhone 12 Pro']
        context_app = browser.new_context(
            **iphone_12,
        )
        context_app.set_default_timeout(MobileConfig.timeout)
        page_app = context_app.new_page()
        return page_app

    @staticmethod
    def ipad(playwright):
        browser = playwright.chromium.launch(headless=MobileConfig.headless, args=MobileConfig.args)
        ipad = playwright.devices['iPad Air']
        context_app = browser.new_context(
            **ipad,
        )
        context_app.set_default_timeout(MobileConfig.timeout)
        page_app = context_app.new_page()
        return page_app

    @staticmethod
    def android(playwright):
        browser = playwright.chromium.launch(headless=MobileConfig.headless, args=MobileConfig.args)
        Samsung = playwright.devices['Samsung Galaxy S20 Ultra']
        context_app = browser.new_context(
            **Samsung,
        )
        context_app.set_default_timeout(MobileConfig.timeout)
        page_app = context_app.new_page()
        return page_app

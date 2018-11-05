import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


class SchoolSpider:
    def __init__(self, username, password):
        self.url = 'http://jwgl.cust.edu.cn/teachwebsl/login.aspx'
        self.username = username
        self.password = password

        #self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome()

    def login_assess(self):
        '''
        登录和评估
        :return:
        '''
        try:
            print('---------')
            self.driver.get(self.url)
            user_button = self.driver.find_element_by_name('txtUserName')
            password_button = self.driver.find_element_by_name('txtPassWord')
            user_button.clear()
            user_button.send_keys(self.username)

            password_button.clear()
            password_button.send_keys(self.password)

            login = self.driver.find_element_by_name('Button1')
            login.click()


            self.driver.get('http://jwgl.cust.edu.cn/teachweb/jspg/TeacherEvaluate.aspx')
            values = self.driver.find_elements_by_css_selector('#m_ddlTeacher > option[value]')
            classes = []
            for value in values:
                classes.append({'value': value.get_attribute('value'), 'name': value.text.split('|')[0]})

            return classes

        except Exception as e:
            return False


    def assess(self, cls):
        '''
        评估
        :param cls:
        :return:
        '''
        try:
            selector = Select(self.driver.find_element_by_id('m_ddlTeacher'))
            selector.select_by_value(cls.get('value'))
            for id in range(40, 50):
                self.driver.find_element_by_xpath('//*[@id="{}"]'.format(str(id))).click()
            #time.sleep(0.5)

            for id in range(410, 422):
                self.driver.find_element_by_xpath('//*[@id="{}"]'.format(str(id))).click()
            #time.sleep(0.5)
            m_button = self.driver.find_element_by_name('m_submit')
            m_button.click()
            print(cls.get('name'), '已评估')
            return True

        except Exception as e:
            print(e.args)
            return False



if __name__ == '__main__':
    username = input('请输入用户名:')
    password = input('请输入密码:')
    spider = SchoolSpider(username, password)
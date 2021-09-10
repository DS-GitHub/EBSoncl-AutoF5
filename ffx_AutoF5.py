# AutoF5(with Firefox)
# Copyright (C) Dillot. All rights reserved. ANY EDITTING ON THIS FILE(CODE) IS DISALLOWED WITHOUT AUTHOR'S PERMISSION.
import time
from os import system
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

print("환영합니다! 본 프로그램에 입력된 모든 정보는 절대 이용목적 이외의 목적으로 사용되지 않으며, 이용목적(로그인) 달성 시 지체 없이 파기됩니다. 개인정보 책임자: '조동성' *본 프로그램 사용 시 발생하는 모든 책임(개인정보 관련 제외)은 사용자 본인에게 귀속됩니다.*")
print("AutoF5(with Firefox)\nCopyright (C) Dillot. All rights reserved.\n본 프로그램은 자유롭게 배포, 사용이 가능하며, 파일의 어떠한 2차 수정을 금합니다.\n\n")
ID = input("EBS 온라인클래스 계정 아이디를 입력하세요.\n >>>")
PW = input("EBS 온라인클래스 계정 비밀번호를 입력하세요.\n >>>")
system("cls")
print("필수 정보가 모두 성공적으로 입력되었으며, 시스템 동작을 시작합니다.")

driver = webdriver.Firefox()

# Login
driver.get('https://ebsoc.co.kr/login')

username = driver.find_element_by_name("j_username")
password = driver.find_element_by_name("j_password")
login = driver.find_elements_by_css_selector('.img_type')[-1]

username.send_keys(ID)
ID = None
print("개인정보(아이디)가 프로그램 메모리에서 파기되었습니다.")
password.send_keys(PW)
PW = None
print("개인정보(비밀번호)가 프로그램 메모리에서 파기되었습니다.")
login.click()
system('cls')
print("작동중...")
time.sleep(5)

# GoChatting
driver.get('https://sel3.ebsoc.co.kr/chatting')
time.sleep(4)

# IsChatRoom
def IsChatRoom():
    while True:
        try:
            driver.find_element_by_css_selector(".btn.btn_xs.btn_darkgrey")
            print("입장하기 버튼이 확인되어 다음 단계로 진행합니다.")
            break
        except exceptions.NoSuchElementException:
            print("입장하기 버튼이 확인되지 않아 3초 간격으로 새로고침합니다.")
            driver.refresh()
        time.sleep(3)
    # GOTO Main
    Main()

# Main
def Main():
    count = 0
    while True:
        count += 1
        print(f"{count}번째 시도...")
        try:
            enterchat = driver.find_element_by_css_selector(".btn.btn_xs.btn_darkgrey")
        except exceptions.NoSuchElementException:
            print("입장되기 버튼이 확인되지 않아 이전 단계로 넘어갑니다.")
            # GOTO IsChatRoom
            IsChatRoom()
        enterchat.click()
        time.sleep(0.1)
        enteralert = driver.switch_to.alert
        enteralert.accept()
        try:
            WebDriverWait(driver, 3).until(ec.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
            noteacher = driver.switch_to.alert
            noteacher.accept()
            print(f"{count}번째 시도 실패")
        except exceptions.TimeoutException:
            print(f"{count}번째 시도 성공")
            input("채팅방 입장에 성공했습니다. 엔터를 눌러 시스템을 종료하세요.")
            break
        time.sleep(1)
        driver.refresh()
        time.sleep(3)

IsChatRoom()

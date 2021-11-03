# AutoF5(with Firefox)
# Copyright (C) Dillot. All rights reserved. ANY EDITTING ON THIS FILE(CODE) IS DISALLOWED WITHOUT AUTHOR'S PERMISSION.
import time
from os import system
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

system("title AUTOF5 By Dillot")
system("mode 45,50")
system("color 0A")

while True:
    global MSGNUM, MSG
    print("환영합니다! 본 프로그램에 입력된 모든 정보는 절대 이용목적 이외의 목적으로 사용되지 않으며, 이용목적(로그인) 달성 시 지체 없이 파기됩니다. 개인정보 책임자: '조동성' *본 프로그램 사용 시 발생하는 모든 책임(개인정보 관련 제외)은 사용자 본인에게 귀속됩니다.*")
    print("\nAutoF5(with Firefox)\nCopyright (C) Dillot. All rights reserved.\n본 프로그램은 자유롭게 배포, 사용이 가능하며, 파일의 어떠한 2차 수정을 금합니다.\n\n")
    ID = input("EBS 온라인클래스 계정 아이디를 입력하세요.\n >>>")
    PW = input("EBS 온라인클래스 계정 비밀번호를 입력하세요.\n >>>")
    try:
        MSGNUM = int(input("자동으로 입력할 메시지의 수를 입력하세요.\n >>>"))
    except:
        system("cls")
        print("숫자만 입력해주세요. 처음부터 다시 시작합니다.")
        continue
    if MSGNUM < 0:
        system("cls")
        print("허용되지 않은 숫자가 확인되었습니다. 처음부터 다시 시작합니다.")
        continue
    MSG = []
    status = 0
    for i in range(MSGNUM):
        temp = input(f"자동으로 입력할 메시지를 입력하세요({i+1}번째). >>>")
        if temp == '':
            system("cls")
            print('허용되지 않은 문자가 확인되었습니다. 처음부터 다시 시작합니다.')
            status = 1
            break
        MSG.append(temp)
    if status == 1:
        continue
    else:
        break
        
system("cls")
print("필수 정보가 모두 성공적으로 입력되었습니다. 엔터를 눌러 시스템을 시작하세요.")
input()
print("엔터 입력됨. 시스템 시작.")

driver = webdriver.Firefox(keep_alive=True)

# Login
driver.get('https://ebsoc.co.kr/login')

username = driver.find_element(By.NAME, "j_username")
password = driver.find_element(By.NAME, "j_password")
login = driver.find_elements(By.CSS_SELECTOR, '.img_type')[-1]

username.send_keys(ID)
ID = None
print("개인정보(아이디)가 프로그램 메모리에서 파기되었습니다.")
password.send_keys(PW)
PW = None
print("개인정보(비밀번호)가 프로그램 메모리에서 파기되었습니다.")
login.click()
system('cls')
print("작동중...")
time.sleep(3)

# GoChatting
driver.get('https://sel3.ebsoc.co.kr/chatting')
time.sleep(3)

# IsChatRoom
def IsChatRoom():
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, ".btn.btn_xs.btn_darkgrey")
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
            enterchat = driver.find_element(By.CSS_SELECTOR, ".btn.btn_xs.btn_darkgrey")
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
            print("자동 입장 단계가 완료되어 다음 단계로 진행합니다.")
            time.sleep(2)
            another_window = list(set(driver.window_handles) - {driver.current_window_handle})[0]
            driver.switch_to.window(another_window)
            check = 1
            for NOW in range(MSGNUM):
                check = InputChat(NOW)
                if check != 1:
                    break
            if check != 1:
                another_window = list(set(driver.window_handles) - {driver.current_window_handle})[0]
                driver.current_window_handle.close()
                driver.switch_to.window(another_window)
                continue
            input(f"채팅방 입장 및 채팅 {MSGNUM}개 자동 입력에 모두 성공했습니다. 엔터를 눌러 시스템을 종료하세요.")
            break
        time.sleep(1)
        driver.refresh()
        time.sleep(3)

def InputChat(NOW):
    try:
        time.sleep(2)
        inputchat = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/textarea')
        inputchat.send_keys(MSG[NOW])
        sendbutton = driver.find_element(By.CSS_SELECTOR, '.btn.btn_md.btn_darkblue')
        sendbutton.click()
        return 1
    except Exception as e:
        print(e)
        input("채팅 보내기 작업 중 오류가 발생하여 이전 단계로 넘어갑니다. 엔터를 눌러 재입장 후 다시 시도하세요.")
        return 0

def InputChatSystem(msg):
    try:
        inputchat = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/textarea')
        inputchat.send_keys(msg)
        sendbutton = driver.find_element(By.CSS_SELECTOR, '.btn.btn_md.btn_darkblue')
        sendbutton.click()
    except Exception as e:
        print(e)

def AfterAll():
    umm = input("====================\n채팅 입력 시스템이 시작될 예정입니다. N 혹은 n 을 입력하여 취소 및 시스템을 완전히 종료하고, 다른 아무 키나 입력하여 계속 진행하세요.")
    if (umm == 'n') or (umm == 'N'):
        exit()
    while True:
        text = input("전송할 텍스트를 입력하세요. >>>")
        if text == 'exit()':
            print("명령에 의해 시스템을 종료합니다.")
            break
        elif text == 'exit(tab)':
            print("명령에 의해 탭과 시스템을 종료합니다.")
            driver.close()
            break
        elif text == 'exit(complete)':
            print("명령에 의해 시스템을 완전히 종료합니다.")
            driver.quit()
            break
        elif text == 'len(students)':
            element = driver.find_elements(By.CSS_SELECTOR, '.count')[-1].text
            print(f"명령에 의해 채팅방 인원수가 집계되었습니다. : {element}")
            continue
        elif text == 'students':
            html_list = driver.find_element(By.ID, "mCSB_1_container")
            html_list_ = html_list.find_element(By.TAG_NAME, "ul")
            items = html_list_.find_elements(By.TAG_NAME, "li")
            students = []
            for item in items:
                try:
                    temp = (item.find_element(By.XPATH, '//a[@href="#"]').text).lstrip("person\n")
                except Exception as error:
                    print(error)
                students.append(temp)
            students = ', '.join(students)
            print(f"명령에 의해 채팅방 전체 인원이 집계되었습니다. : {students}")
            continue
        elif text == 'offline_students':
            html_list = driver.find_element(By.ID, "mCSB_1_container")
            html_list_ = html_list.find_element(By.TAG_NAME, "ul")
            items = html_list_.find_elements(By.CSS_SELECTOR, ".logout")
            students = []
            for item in items:
                temp = (item.find_element(By.XPATH, '//a[@href="#"]').text).lstrip("person\n")
                students.append(temp)
            students = ', '.join(students)
            print(f"명령에 의해 채팅방 오프라인 인원이 집계되었습니다. : {students}")
            continue
        elif text == 'online_students':
            html_list = driver.find_element(By.ID, "mCSB_1_container")
            html_list_ = html_list.find_element(By.TAG_NAME, "ul")
            items = html_list_.find_elements(By.TAG_NAME, "li")
            offitems = html_list_.find_elements(By.CSS_SELECTOR, ".logout")
            students = []
            for item in offitems:
                items.remove(item)
            for item in items:
                temp = (item.find_element(By.XPATH, '//a[@href="#"]').text).lstrip("person\n")
                students.append(temp)
            students = ', '.join(students)
            print(f"명령에 의해 채팅방 온라인 인원이 집계되었습니다. : {students}")
            continue
        elif text == "listen()":
            print("명령에 의한 리스너 실행중...")
            print("--------------------")
            ChatListener()
            continue

        InputChatSystem(text)

def ChatListener():
    chatlist = driver.find_element(By.ID, 'mCSB_2_container')

    # get list of currently displayed messages
    allCL = chatlist.find_elements(By.TAG_NAME, 'div')
    for chat in allCL:
        author = 'SYSTEM'
        try:
            profile = chat.find_element(By.XPATH, ".//div[@class=\"profile\"]")
            author = profile.find_element(By.XPATH, './/span[@class="name"]').text
        except exceptions.NoSuchElementException:
            pass
        
        chatting = (chat.text).replace("person\n", "")
        print("[" + author + "] " + chatting.replace("person", ""))
    lenOfACL = len(allCL)

    # wait for new message...
    while True:

        chatlist = driver.find_element(By.ID, 'mCSB_2_container')
        allCL = chatlist.find_elements(By.TAG_NAME, 'div')

        if (len(allCL) > lenOfACL): # you have new message
            LastMessage = allCL[-1]
            LastAuthor = 'SYSTEM'
            try:
                LastProfile = LastMessage.find_element(By.XPATH, ".//div[@class=\"profile\"]")
                LastAuthor = LastProfile.find_element(By.XPATH, './/span[@class="name"]').text
            except exceptions.NoSuchElementException:
                pass
            LM = (LastMessage.text).replace("person\n", "")
            print("[" + LastAuthor + "] " + LM.replace("person", ""))

            lenOfACL = len(allCL) # update length of ul
        

        chatcontent = driver.find_elements(By.TAG_NAME, 'textarea')[-1].get_attribute('value')
        if chatcontent == "listen(stop)":
            print("--------------------")
            print("명령에 의해 리스너 실행을 종료합니다.")
            break

        sleep(3)




if __name__ == '__main__':
    try:
        a = 0
        IsChatRoom()
        a = 1
        AfterAll()
    except Exception as e:
        print(e)
        if a == 0:
            print('오류 발생으로 전단계 실행')
            IsChatRoom()
        elif a == 1:
            print('오류 발생으로 전단계 실행')
            AfterAll()
        else:
            input("엔터를 눌러 시스템을 종료하십시오.")
            exit()

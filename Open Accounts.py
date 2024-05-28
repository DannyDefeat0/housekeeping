import pyautogui
import time

# List of account IDs to select in Google Ads Editor
# GOALS
# Remove coordinates reference
# Use functions to avoid repeating time sleep so many times
# read documentation on locate & confidence (how do they determine this? Pillow Library)


excel_list = ['657-738-7348',	'232-245-0744',	'732-207-5231',	'934-002-9941',	'892-395-0719',	'897-074-6280',	'890-253-3185',	'423-554-9143',	'971-091-5799',	'118-627-7797',	'617-055-4547',	'291-636-1915',	'947-193-7029',	'578-733-7637',	'462-677-4760',	'764-989-2586',	'160-218-4358',	'896-861-2682',	'880-817-8519',	'203-198-5360',	'659-538-2935',	'956-253-1352',	'199-684-7860',	'176-460-3823',	'592-830-1646',	'576-433-3637',	'102-011-2629',	'337-334-5201',	'380-306-2056',	'992-831-4995',	'317-055-5752',	'212-269-9754',	'419-451-8705',	'205-857-8112',	'805-384-8023',	'743-798-2372',	'769-159-5607',	'518-106-1446',	'309-829-7941',	'952-363-9957',	'694-048-9003',	'486-083-6788',	'418-397-2429',	'719-235-9099',	'900-503-4301',	'243-311-1939',	'417-324-0735',	'216-241-3731',	'697-324-0449',	'339-957-5464',	'600-004-6633',	'472-143-2994',	'188-074-3542',	'129-925-7858',	'639-347-7786',	'506-477-5297',	'146-333-7811',	'511-746-5925',	'420-135-3301',	'140-879-2690',	'855-136-5960',	'135-051-8500',	'806-652-1681',	'745-756-9120',	'542-038-9496',	'508-776-6135',	'781-541-9226',	'318-122-3362',	'827-123-4632',	'416-981-5679',	'251-988-1322',	'899-313-9572',	'385-739-4742',	'546-704-3705',	'931-985-5732',	'271-346-9699',	'639-157-6088',	'910-143-6677',	'213-774-7107',	'794-802-4033',	'872-901-5112',	'335-061-5586',	'183-584-6097',	'650-569-3348',	'859-883-1818',	'982-993-0313',	'600-792-6209',	'602-832-7743',	'584-507-2742',	'943-449-6964',	'197-198-7826',	'226-493-7481',	'872-747-0773',	'868-840-0116',	'422-632-9541',	'230-310-1949',	'534-112-2897',	'758-954-2731',	'920-233-0258',	'274-089-4874',	'621-324-4665',	'298-978-8929',	'278-673-7884',	'992-333-1125',	'179-637-4758',	'362-004-0866',	'377-306-7580',	'967-361-3617',	'457-173-9615',	'497-980-7874',	'318-861-6033',	'107-528-5692',	'735-238-8423',	'982-371-6633']

#python_list = excel_list.split("\n")
#python_list = [x for x in python_list if x]

account_ids = excel_list
print(excel_list)
# Open Google Ads Editor
pyautogui.press('winleft')
time.sleep(0.5)
pyautogui.typewrite('Google Ads Editor', interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(15)

# Select the 'Accounts' tab
pyautogui.hotkey('ctrl', 'o')
time.sleep(5)
pyautogui.hotkey('shift','tab')


for account_id in account_ids:
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.1)
    pyautogui.typewrite(str(account_id), interval=0.01)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    #checkbox_x, checkbox_y = 47, 186
    checkbox_x, checkbox_y = 55, 228
    pyautogui.click(checkbox_x, checkbox_y)
    time.sleep(0.1)
    checkbox_x, checkbox_y = 1142, 78
    pyautogui.click(checkbox_x, checkbox_y)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.hotkey('del')
    time.sleep(0.1)

# Download the selected clients
#time.sleep(2)


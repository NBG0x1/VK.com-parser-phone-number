import vk
import time
import dbconnect

my_app_id = '1111111'
user_login='kyklaed'
user_password='2323232'

count_id=1000

id_num=11111  # id группы для парсинга


def parss(id_num):
    print("1")
    try:
        print("2")
        session = vk.AuthSession(my_app_id, user_login, user_password, scope='wall, messages')
        vkapi = vk.API(session, v="5.62")
        list_id = vkapi.groups.getMembers(group_id='11111111', offset=id_num, count=count_id)
    except Exception as err:
        print(err)
    print("3")
    dbase = dbconnect.Add_ids('parsdb', 'phonevk')
    print("4")
    dbase.addtable()
    print("5")

    while id_num != int(710000):
        try:
            print(list_id)
            print(len(list_id['items']))
            for i in list_id['items']:
                t = 1 #random.randint(1, 3)
                time.sleep(t)
                number_l = vkapi.users.get(user_ids=i, fields='contacts')
                #print(number_l)
                id_num += 1
                print("NUM = ", id_num)
                if 'mobile_phone' in number_l[0]:
                    if number_l[0]['mobile_phone'] != '':
                        print(number_l[0]['first_name'], number_l[0]['last_name'], number_l[0]['mobile_phone'])

                        user_n = "{0} {1}".format(number_l[0]['first_name'], number_l[0]['last_name'])
                        print(user_n, type(user_n))
                        print(number_l[0]['mobile_phone'], type(number_l[0]['mobile_phone']))
                        dbase.addid(user_n, number_l[0]['mobile_phone'])

            else:
                print("конец очереди должна начаться новая очередь")
                time.sleep(10)
                list_id = vkapi.groups.getMembers(group_id='1111111', offset=id_num, count=count_id)


        except Exception as errr:
            print(errr)
            time.sleep(10)
            list_id = vkapi.groups.getMembers(group_id='11111111', offset=id_num, count=count_id)

    else:
        print("vse")



parss(id_num)

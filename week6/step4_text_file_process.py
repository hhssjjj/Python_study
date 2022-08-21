def orderFile():

    import os

    text_data_path = 'C:\wonGit\week6\meta-data\store1'

    file_list = os.listdir(text_data_path)

    text_list = [] #day1.txt , day2.txt, day3.txt 내용이 리스트로 저장이 됨.

    for file in file_list:
        print(file)
        file_path = text_data_path + '/' + file
        try:
            if os.path.isfile(file_path) :
                f = open(file_path, 'r', encoding='utf-8')
                #f.read()  -> string
                #f.readLines() -> List
                text_list.append(f.read().split('\n'))
                print(text_list)

        except Exception as e:
            print(e)
        finally:
            pass


    order_data = dict() #key값은 menu, value값은 order_cnt(주문량)
    for data in text_list:
        for each_data in data:
            #print(each_data)
            order = each_data.split(',')
            #print(order)
            for menu_cnt in order:
                order2 = menu_cnt.split(' ')
                #print(order2[0])
                #print(order2[1])
                order_menu = order2[0]
                order_cnt = order2[1]

                if order_menu in order_data:
                    order_data[order_menu] += int(order_cnt)
                else:
                    order_data[order_menu] = int(order_cnt)

    print(order_data)

#binary file 형식으로 변수에 저장된 객체를 저장하기 때문에 객체 타입을 그대로 유지하여 파일에 저장 및 읽어올 수 있다.

def pickleFile():
    import pickle
    try:
        a_list = ['java', 'c', 'python', 'c++']
        with open('C:\wonGit\week6\object.pck', 'wb') as f:
            #바이너리 파일 생성은 dump
            pickle.dump(a_list,f)

        with open('C:\wonGit\week6\object.pck', 'rb') as f:
            data = pickle.load(f)
            print(data)
            print(type(data))
            print(len(data))

    except Exception as e:
        print(e)



def pickleFile():
    import pickle
    try:
        class Book:
            def __init__(self, title, writer, price, publisher):
                self.title = title
                self.writer = writer
                self.price = price
                self.publisher = publisher

        book1 = Book('인어공주', '안데르센', 7000, '문학동네')
        book2 = Book('장화신은 고양이', '샤를페로', 10000, '문학동네')

        #.pck.pickle
        with open('C:\wonGit\week6\object.pck', 'wb') as f:
            #바이너리 파일 생성은 dump
            pickle.dump(book1,f)
            pickle.dump(book2,f)

        with open('C:\wonGit\week6\object.pck', 'rb') as f:
            data = pickle.load(f)
            print(type(data))
            print(data.title , data.writer, data.price, data.publisher)
            data2 = pickle.load(f)
            print(data2.title , data2.writer, data2.price, data2.publisher)

    except Exception as e:
        print(e)

pickleFile()




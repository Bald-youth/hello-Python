#author : Sping
def tip():
    print("[1]添加学生信息")
    print("[2]删除学生信息")
    print("[3]修改学生信息")
    print("[4]查询学生信息")
    print("[5]查看所有信息")
    print("[0]退出系统")
def add_message():
    Student_message = {}
    Student_message["s_id"] = int(input("请输入学号："))
    Student_message["s_name"] =input("请输入姓名：")
    Student_message["s_sex"] =input("请输入性别：")
    Student_message["s_age"] =input("请输入年龄：")
    print("-"*30)
    List_message.append(Student_message)
    #print(List_message)
def del_message():
    i =0
    stu_list()
    stu_id = int(input("请输入要删除对象的学号："))
    for item in List_message:
        i+=1;
        if (item.get("s_id")==stu_id):
            del List_message[i-1];
            print("已经成功删除目标！！！")
            print("-" * 30)
            break
        else:
            print("出错啦！！！")
            print("-" * 30)
    stu_list()
def alter():
    if(len(List_message))>0:
        s_id = int(input("请输入学号："))
        for item in List_message:
            if s_id == item["s_id"]:
                query_message(s_id)
                new_id = int(input("请输入修改的学号:"))
                new_name = input("请输入修改的姓名:")
                new_sex = input("请输入修改的性别:")
                new_age = int(input("请输入修改的年龄:"))
                item["s_id"] = new_id
                item["s_name"] = new_name
                item["s_sex"] = new_sex
                item["s_age"] = new_age
                print("修改完成！！")
                print("-" * 30)
                stu_list()
                break
            else:
                print("修改出现问题。")
    else:
        print("目前数据为空！！！")
        print("-"*30)
def query_message(stu_id):
    if len(List_message)> 0:
        stu_id = int(input("请输入学号："))
        #stu_str = 's_id'
        list_tem = []
        for item in List_message:
            if (item.get("s_id")==stu_id):
                list_tem.append(item)
                #tem ={}
                tem=list_tem[0]
                print("学号：%d\t姓名：%s\t性别：%s\t年龄：%d"
                      % (int(tem["s_id"]),tem["s_name"]
                         , tem["s_sex"], int(tem["s_age"])))
                break
            else:
                print("抱歉未找到该学号的学生")
        print("-"*30)
    else:
        print("查询失败，当前数据库为空！！！")
        print("-" * 30)
def stu_list():
    if(len(List_message))>0:
        for item in List_message:
            #print(item)
            print("学号：%d\t姓名：%s\t性别：%s\t年龄：%d"
                  % (int(item["s_id"]), item["s_name"]
                     , item["s_sex"], int(item["s_age"])))
            print("-"*30)
    else:
         print("当前数据库为空！！")
         print("-" * 30)

if __name__ == '__main__':
    print("欢迎进入初代学生信息查询系统")
    print("-"*30)
    List_message=[]  #数据存储在列表中
    # Student_message ={}
    while 1:
        try:
            tip()
            print("-"*30)
            num = int(input("输入所要选择的功能序号\n按回车键结束："))
            print("-" * 30)
            if num == 1:
                add_message()
            if num == 2:
                del_message()
            if num == 3:
                alter()
            if num == 4:
                query_message(stu_id=0)
            if num == 5:
                stu_list()
            if num == 0:
                exit("成功退出系统")
        except ValueError:
            print("数据类型错误!请重新输入正确的序号！！")






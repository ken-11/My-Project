from people import People
docs = []


def add_people_info():
    L = People.input_People()
    docs.extend(L)


# "| 2) 显示学生信息
def show_people_info():
    People.output_People(docs)


# "| 3) 修改学生成绩
def modify_people_score():
    People.alter_People(docs)


# | 4) 删除学生信息
def del_people_info():
    People.del_People(docs)


# "| 5) 按成绩从高至低打印学生信息
def order_by_score_desc():
    People.output_People(sorted(docs, key=People.get_score, reverse=True))


# "| 6) 按成绩从低至高打印学生信息
def order_by_score():
    People.output_People(sorted(docs, key=People.get_score))


# "| 7) 按年龄从高至低打印学生信息
def order_by_age_desc():
    People.output_People(sorted(docs, key=People.get_age, reverse=True))


# "| 8) 按年龄从低至高打印学生信息
def order_by_age():
    People.output_People(sorted(docs, key=People.get_age))


# "| 9)　保存数据到文件(si.txt)
def save_to_txt():
    People.save_to_txt(docs)


# "|10)从文件中读取数据（si.txt）
def read_from_txt():
    People.output_People(People.read_from_txt())


# |11)保存csv到文件（infos.csv）
def save_to_csv():
    People.save_to_csv(docs)


# "|12)从csv文件中读取数据(infos.csv)
def read_from_csv():
    People.output_People(People.read_from_csv())

#print("|13) 保存到数据库|")
def save_to_mysql():
    People.save_stu_mysql(docs)

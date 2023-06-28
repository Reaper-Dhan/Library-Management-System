import mysql.connector
from datetime import date
import os

fine_per_day = 10.0

def clear():
  for _ in range(1):
    print

def add_book():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  title = input('Enter Book Title: ')
  author = input('Enter Book Author: ')
  publisher = input('Enter Book Publisher: ')
  pages = input('Enter Book Pages: ')
  price = input('Enter Book Price: ')
  edition = input('Enter Book Edition: ')
  copies  = int(input('Enter copies: '))
  sql = 'insert into book(title,author,price,pages,publisher,edition,status) values ( "' + \
       title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'
  for _ in range(0,copies):
    cursor.execute(sql)
  conn.close()
  print('\nNew Book added successfully')
  wait = input('\n\nPress any key to continue....\n')

def add_member():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  name = input('Enter Member Name: ')
  clas = input('Enter Member Class & Section: ')
  address = input('Enter Member Address: ')
  phone = input('Enter Member Phone: ')
  email = input('Enter Member Email: ')
  sql = 'insert into member(name,class,address,phone,email) values ( "' + \
      name + '","' + clas+'","'+address+'","'+phone + \
        '","'+email+'");'
  cursor.execute(sql)
  conn.close()
  print('\nNew Member added successfully')
  wait = input('\n\nPress any key to continue....\n')

def modify_book():
  while True:
    conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
    cursor = conn.cursor()
    clear()
    print("*"*60)
    print('\n\t\tModify BOOK Details Screen\n')
    print("*"*60)
    print('1. Book Title')
    print('2. Book Author')
    print('3. Book Publisher')
    print('4. Book Pages')
    print('5. Book Price')
    print('6. Book Edition')
    print('7. Go back to Main Menu')
    print('\n')
    choice = int(input('Enter your choice: '))
    print("\n")
    field = ''
    if choice == 1:
      field = 'title'
    if choice == 2:
      field = 'author'
    if choice == 3:
      field = 'publisher'
    if choice == 4:
      field = 'pages'
    if choice == 5:
      field = 'price'
    if choice == 6:
      field = 'edition'
    if choice == 7:
      break
    book_id = input('Enter Book ID: ')
    value = input('Enter new value: ')
    if field =='pages' or field == 'price':
      sql = 'update book set ' + field + ' = '+value+' where id = '+book_id+';'
    else:
      sql = 'update book set ' + field + ' = "'+value+'" where id = '+book_id+';'
    cursor.execute(sql)
    print('\nBook details Updated.....')
    conn.close()
    wait = input('\n\nPress any key to continue....\n')

def modify_member():
  while True:
    conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
    cursor = conn.cursor()
    clear()
    print("*"*60)
    print('\n\t\tModify Member Information Screen\n')
    print("*"*60)
    print('1. Name')
    print('2. Class')
    print('3. Address')
    print('4. Phone')
    print('5. Email')
    print('6. Go back to Main Menu')
    print('\n')
    choice = int(input('Enter your choice: '))
    print("\n")
    field =''
    if choice == 1:
      field ='name'
    if choice == 2:
      field = 'class'
    if choice ==3:
      field ='address'
    if choice == 4:
      field = 'phone'
    if choice == 5:
      field = 'email'
    if choice == 6:
      break
    mem_id =input('Enter member ID: ')
    value = input('Enter new value: ')
    sql = 'update member set '+ field +' = "'+value+'" where id = '+mem_id+';'
    cursor.execute(sql)
    print('Member details Updated.....')
    conn.close()
    wait = input('\n\nPress any key to continue....\n')

def mem_issue_status(mem_id):
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  sql ='select * from transaction where m_id ='+mem_id +' and dor is NULL;'
  cursor.execute(sql)
  results = cursor.fetchall()
  return results

def book_status(book_id):
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  sql = 'select * from book where id ='+book_id + ';'
  cursor.execute(sql)
  result = cursor.fetchone()
  return result[5]

def book_issue_status(book_id,mem_id):
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  sql = 'select * from transaction where b_id ='+book_id + ' and m_id ='+ mem_id +' and dor is NULL;'
  cursor.execute(sql)
  result = cursor.fetchone()
  return result

def issue_book():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tBOOK ISSUE SCREEN\n')
  print("*"*60)
  book_id = input('Enter Book ID: ')
  mem_id  = input('Enter Member ID: ')
  result = book_status(book_id)
  result1 = mem_issue_status(mem_id)
  today = date.today()
  if len(result1) == 0:
    if result == 'available':
      sql = 'insert into transaction(b_id, m_id, doi) values('+book_id+','+mem_id+',"'+str(today)+'");'
      sql_book = 'update book set status="issue" where id ='+book_id + ';'
      cursor.execute(sql)
      cursor.execute(sql_book)
      print('\nBook issued successfully')
    else:
      print('\nBook is not available for ISSUE...')
  else:
    if len(result1)<1:
      sql = 'insert into transaction(b_id, m_id, doi) values(' + \
             book_id+','+mem_id+',"'+str(today)+'");'
      sql_book = 'update book set status="issue" where id ='+book_id + ';'
      cursor.execute(sql)
      cursor.execute(sql_book)
      print('\nBook issued successfully')
    else:
      print('\nMember already have book from the Library')
  conn.close()
  wait = input('\n\nPress any key to continue....\n')

def return_book():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  global fine_per_day
  clear()
  print("*"*60)
  print('\n\t\tBOOK RETURN SCREEN\n')
  print("*"*60)
  book_id = input('Enter Book ID: ')
  mem_id = input('Enter Member ID: ')
  today =date.today()
  result = book_issue_status(book_id,mem_id)
  if result==None:
    print('Book was not issued...Check Book ID and Member ID again..')
  else:
    sql='update book set status ="available" where id ='+book_id +';'
    din = (today - result[3]).days
    fine = din * fine_per_day
    sql1 = 'update transaction set dor ="'+str(today)+'" , fine='+str(fine)+' where b_id='+book_id +' and m_id='+mem_id+' and dor is NULL;'
    cursor.execute(sql)
    cursor.execute(sql1)
    print('\nBook returned successfully')
  conn.close()
  wait = input('\n\nPress any key to continue....\n')

def search_book(field):
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tBOOK SEARCH SCREEN\n')
  print("*"*60)
  msg ='Enter '+ field +' Value: '
  title = input(msg)
  sql ='select * from book where '+ field + ' like "%'+ title+'%"'
  cursor.execute(sql)
  records = cursor.fetchall()
  clear()
  print('Search Result for: ',field,' : ' ,title)
  print('-'*120)
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue....\n')

def search_menu():
  while True:
    clear()
    print("*"*60)
    print('\n\t\tS E A R C H   M E N U\n')
    print("*"*60)
    print("1. Book Title")
    print('2. Book Author')
    print('3. Publisher')
    print('4. Go back to Main Menu')
    print('\n')
    choice = int(input('Enter your choice ... '))
    print("\n")
    field =''
    if choice == 1:
      field='title'
    if choice == 2:
      field = 'author'
    if choice == 3:
      field = 'publisher'
    if choice == 4:
      break
    search_book(field)

def report_book_list():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tREPORT - BOOK TITLES\n')
  print("*"*60)
  sql ='select * from book'
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_issued_books():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tREPORT - BOOK TITLES - Issued\n')
  print("*"*60)
  sql = 'select * from book where status = "issue";'
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_available_books():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tREPORT - BOOK TITLES - Available\n')
  print("*"*60)
  sql = 'select * from book where status = "available";'
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_weed_out_books():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tREPORT - BOOK TITLES - Weed Out\n')
  print("*"*60)
  sql = 'select * from book where status = "weed-out";'
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_stolen_books():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tREPORT - BOOK TITLES - Stolen\n')
  print("*"*60)
  sql = 'select * from book where status = "stolen";'
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_lost_books():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tREPORT - BOOK TITLES - lost\n')
  print("*"*60)
  sql = 'select * from book where status = "lost";'
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_member_list():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  clear()
  print("*"*60)
  print('\n\t\tREPORT - Members List\n')
  print("*"*60)
  sql = 'select * from member'
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record)
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_fine_collection():
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  sql ='select sum(fine) from transaction where dor ="'+str(date.today())+'";'
  cursor.execute(sql)
  result = cursor.fetchone()
  clear()
  print("*"*60)
  print('\n\t\tFINE COLLECTION\n')
  print("*"*60)
  print('Total fine collected Today :',result[0])
  print('\n')
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def report_menu():
  while True:
    clear()
    print("*"*60)
    print('\n\t\tR E P O R T    M E N U\n')
    print("*"*60)
    print("1. Book List")
    print('2. Member List')
    print('3. Issued Books')
    print('4. Available Books')
    print('5. Weed out Book')
    print('6. Stolen Book')
    print('7. Lost Book')
    print('8. Fine Collection')
    print('9. Go back to Main Menu')
    print('\n')
    choice = int(input('Enter your choice... '))
    print("\n")
    if choice == 1:
      report_book_list()
    if choice == 2:
      report_member_list()
    if choice == 3:
      report_issued_books()
    if choice == 4:
      report_available_books()
    if choice == 5:
      report_weed_out_books()
    if choice == 6:
      report_stolen_books()
    if choice == 7:
      report_lost_books()
    if choice == 8:
      report_fine_collection()
    if choice == 9:
      break

def change_book_status(status,book_id):
  conn = mysql.connector.connect(host=host, database=database, user=user, password=passwd)
  cursor = conn.cursor()
  sql = 'update book set status = "'+status +'" where id ='+book_id + ' and status ="available"'
  cursor.execute(sql)
  print('Book status changed to ',status)
  print('\n')
  conn.close()
  wait = input('\n\nPress any key to continue.....\n')

def special_menu():
  while True:
    clear()
    print("*"*60)
    print('\n\t\tS P E C I A L     M E N U\n')
    print("*"*60)
    print("1. Book Stolen")
    print('2. Book Lost')
    print('3. Book Weed out')
    print('4. Go back to Main Menu')
    print('\n')
    choice = int(input('Enter your choice... '))
    status=''
    if choice == 1:
       status ='stolen'
    if choice == 2:
       status = 'lost'
    if choice == 3:
       status = 'weed-out'
    if choice == 4:
       break
    book_id = input('Enter book id: ')
    change_book_status(status,book_id)

def main_menu():
  while True:
    clear()
    print("*"*60)
    print('\n\t\tL I B R A R Y    M E N U\n')
    print("*"*60)
    print("1. Add Books")
    print('2. Add Member')
    print('3. Modify Book Information')
    print('4. Modify Member Information')
    print('5. Issue Book')
    print('6. Return Book')
    print('7. Search Menu')
    print('8. Report Menu')
    print('9. Special Menu')
    print('0. Close application')
    print('\n')
    choice = int(input('Enter your choice... '))
    print("\n")
    if choice == 1:
      add_book()
    if choice == 2:
      add_member()
    if choice == 3:
      modify_book()
    if choice == 4:
      modify_member()
    if choice == 5:
      issue_book()
    if choice == 6:
      return_book()
    if choice == 7:
      search_menu()
    if choice == 8:
      report_menu()
    if choice == 9:
      special_menu()
    if choice == 0:
      break

def requirements():
  os.system('cmd /c "pip3 install mysql-connector-python"')

if __name__ == "__main__":
  requirements()
  global host
  host = input("Enter Host Address of MySQL: ")
  global user
  user = input("Enter User Name of MySQL: ")
  global passwd
  passwd = input("Enter Password of User Name: ")
  global database
  database = input("Enter Database Name: ")
  print("\nYour connection with the Database has been established!!\n\n")
  main_menu()
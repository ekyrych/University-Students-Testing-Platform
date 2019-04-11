import shelve,sys,sqlite3

def redirect(link) :
    sys.stdout.write('<script language="javascript" type="text/javascript">document.location.href="%s"</script>'%link)
"""
def show(link):
    sys.stdout.write('<script language="javascript" type="text/javascript">alert("%s");</script>'%link)
"""
def Add_User(user):
    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", user)
#------------------------------------------------------------------------------
# aq.py (Section 10.1)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2021, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle
import decimal
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cur = con.cursor()

BOOK_TYPE_NAME = "UDT_BOOK"
QUEUE_NAME = "BOOKS"
QUEUE_TABLE_NAME = "BOOK_QUEUE_TABLE"

# Cleanup
cur.execute(
    """begin
         dbms_aqadm.stop_queue('""" + QUEUE_NAME + """');
         dbms_aqadm.drop_queue('""" + QUEUE_NAME + """');
         dbms_aqadm.drop_queue_table('""" + QUEUE_TABLE_NAME + """');
         execute immediate 'drop type """ + BOOK_TYPE_NAME + """';
         exception when others then
           if sqlcode <> -24010 then
             raise;
           end if;
       end;""")

# Create a type
print("Creating books type UDT_BOOK...")
cur.execute("""
        create type %s as object (
            title varchar2(100),
            authors varchar2(100),
            price number(5,2)
        );""" % BOOK_TYPE_NAME)

# Create queue table and queue and start the queue
print("Creating queue table...")
cur.callproc("dbms_aqadm.create_queue_table",
        (QUEUE_TABLE_NAME, BOOK_TYPE_NAME))
cur.callproc("dbms_aqadm.create_queue", (QUEUE_NAME, QUEUE_TABLE_NAME))
cur.callproc("dbms_aqadm.start_queue", (QUEUE_NAME,))

booksType = con.gettype(BOOK_TYPE_NAME)
queue = con.queue(QUEUE_NAME, booksType)

# Enqueue a few messages
print("Enqueuing messages...")

BOOK_DATA = [
    ("The Fellowship of the Ring", "Tolkien, J.R.R.", decimal.Decimal("10.99")),
    ("Harry Potter and the Philosopher's Stone", "Rowling, J.K.",
            decimal.Decimal("7.99"))
]

for title, authors, price in BOOK_DATA:
    book = booksType.newobject()
    book.TITLE = title
    book.AUTHORS = authors
    book.PRICE = price
    print(title)
    queue.enqOne(con.msgproperties(payload=book))
    con.commit()

# Dequeue the messages
print("\nDequeuing messages...")
queue.deqOptions.wait = cx_Oracle.DEQ_NO_WAIT
while True:
    props = queue.deqOne()
    if not props:
        break
    print(props.payload.TITLE)
    con.commit()

print("\nDone.")

#sqlite_backend.py
from sqlite3 import OperationalError, IntegrityError, ProgrammingError


def connect(func):
    """Decorator to (re)open a sqlite database connection when needed.

    A database connection must be open when want to perform a database query
    but we are in one of the following situations:
    1) there is no connection
    2) the connection is closed

    Paremetres
    ----------------------------------
    func: function
    function which performs the database query

    Returns
    _____-------------------------------
    inner func : function
    """

    def inner_func(conn, *args, **kwargs):
        try:
            #I don´t know if this is the simplest and faster query to try.
            conn.execute('SELECT name FROM sqlite_temp_master WHERE type="table;"')
        except (AttributeError, ProgrammingError):
            conn = connect_to_db(DB_name)
        return func(conn, *args, **kwargs)
    return inner_func

    #sqlite_backend.py
    def disconnect_from_db(db=None, conn=None):
        if db is not DB_name:
            print("You are trying to disconnect from a wrong DB")
        if conn is not None:
            conn.close()

    @connect
    def create_table(conn, table_name):
        sql = 'CREATE TABLE {} (rowid INTEGER PRIMARY KEY AUTOINCREMENT,' \
        'name TEXT INIQUE, price REAL, quantity INTEGER)'.format(table_name)

        try:
            conn.execute(sql)
        except OperationalError as e:
            print(e)



    def scrub(input_string):
        """Clean an input(to prevent SQL infection).
        Parameters
        --------------------
        input_string : str
        Returns
        --------------------
        str
        """

        return ''.join(k for k in input_string if k.isalnum())

    @connect
    def create_table(conn, table_name):
        table_name = scrub(table_name)
        sql = 'CREATE TABLE {} (rowid INTEGER PRIMARY KEY AUTOINCREMENT, role1 TEXT UNIQUE, role2 TEXT, conflito INTEGER'.format(table_name)
        try:
            conn.execute(sql)
        except OperationalError as e:
            print(e)

    @connect
    def insert_one(conn, role1, role2, conflito, table_name):
        table_name = scrub(table_name)
        sql = "INSERT INTO {} ('role1', 'role2', 'conflito') VALUES (?, ?, ?)".format(table_name)
        try:
            conn.execute(sql, (role1, role2, conflito))
            conn.commit()
        except IntegrityError as e:
            raise mvc_exc.ItemAlreadyStored('{}: "{}" already in table "{}"'.format(e, role1, table_name)
            )

    @connect
    def insert_many(conn, items, table_name):
        table_name = scrub(table_name)
        sql = "INSERT INTO {} ('role1', 'role2', 'conflito') VALUES(?, ?, ?)".format(table_name)
        entries = list()
        for x in items:
            entries.append((x['role1'], x['role2'],x['quantity']))
        try:
            conn.executemany(sql, entries)
            conn.commit()
        except IntegrityError as e:
            print('{}: at least one in {} was already stored in table "{}"'.format(e, [x['role1'] for x in items], table_name))



    def tuple_to_dict(mytuple):
        mydict = dict()
        mydict['id'] = mytuple[0]
        mydict['role1'] = mytuple[1]
        mydict['role2'] = mytuple[2]
        mydict['conflito'] = mytuple[3]
        return mydict

    # sqlite_backend.py
    @connect
    def select_one(conn, item_name, table_name):
        table_name = scrub(table_name)
        item_name = scrub(item_name)
        sql = 'SELECT * FROM {} WHERE role1="{}"'.format(table_name, item_name)
        c = conn.execute(sql)
        result = c.fetchone()
        if result is not None:
            return tuple_to_dict(result)
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored in table "{}"'.format(item_name, table_name))
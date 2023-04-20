import pymysql
import mysecrets
import hashlib

class baseObject:
    def setup(self,tn):
        self.tn = tn
        self.conn = None
        self.cur = None
        self.fields = []
        self.pk = None
        self.data = [] #data is a list of dictionaries representing rows in our table
        self.establishConnection()
        self.getFields()
    def establishConnection(self):

        self.conn = pymysql.connect(host=mysecrets.db_host, port=3306, user=mysecrets.db_user,
                       passwd=mysecrets.db_passwd, db=mysecrets.db_name, autocommit=True)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    def set(self,d):
        self.data.append(d)

    def getVotes(self):
            # query the total number of votes for each nominee, grouped by award category
        sql = """
            SELECT n.nid, n.nomineename, n.awardcategory, n.nominatedyear, n.musicname, 
                COUNT(v.voteid) AS total_votes
            FROM vmas_nominee n
            LEFT JOIN vmas_votes v ON n.nid = v.nid
            GROUP BY n.nid, n.nomineename, n.awardcategory, n.nominatedyear, n.musicname
            ORDER BY n.awardcategory;
            """

        self.cur.execute(sql)
        nominee_results = self.cur.fetchall()

        # make dictionary of dictionaries from the results
        nominee_results_dict = {}

        # parse the results
        if nominee_results is not None:
            for row in nominee_results:
                award_category = row['awardcategory']
                if award_category not in nominee_results_dict:
                    nominee_results_dict[award_category] = []
                new_row = {}
                new_row['nid'] = row['nid']
                new_row['nomineename'] = row['nomineename']
                new_row['nominatedyear'] = row['nominatedyear']
                new_row['musicname'] = row['musicname']
                new_row['total_votes'] = row['total_votes']
                nominee_results_dict[award_category].append(new_row)
        else:
            nominee_results_dict['No results found'] = []

        return nominee_results_dict


    def checkSignedIn(self, email, password):
        # Hash the password
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()

        # Check if the user exists and the password is correct
        self.cur.execute("SELECT * FROM vmas_user WHERE email = %s AND password = %s", (email, hashed_password))
        user = self.cur.fetchone()

        return user


    def getFields(self):
        sql = f'''DESCRIBE `{self.tn}`;'''
        self.cur.execute(sql)
        for row in self.cur:
            if 'auto_increment' in row['Extra']:
                self.pk = row['Field']
            else:
                self.fields.append(row['Field'])
    def insert(self,n=0):
        count = 0
        vals = []
        sql = f"INSERT INTO `{self.tn}` ("
        for field in self.fields:
            sql += f"`{field}`,"
            vals.append(self.data[n][field])
            count +=1
        sql = sql[0:-1] + ') VALUES ('
        tokens = ("%s," * count)[0:-1]
        sql += tokens + ');'
        #print(sql,vals)
        self.cur.execute(sql,vals)
        self.data[n][self.pk] = self.cur.lastrowid

    def getById(self,id):
        sql = f"Select * from `{self.tn}` where `{self.pk}` = %s" 
        print(sql,id)
        self.cur.execute(sql,(id))
        self.data = []
        for row in self.cur:
            self.data.append(row)
            
    def createBlank(self):
        d = {}
        for field in self.fields:
            d[field] = ''
        self.set(d)
       
    def getAll(self):
        sql = f"Select * from `{self.tn}`" 
        self.cur.execute(sql)
        self.data = []
        for row in self.cur:
            self.data.append(row)
    # UPDATE [tablename] SET [col] = [val] , .... WHERE [pk] = [our objects pk] 
    def update(self,n=0):
        vals=[]
        fvs=''
        for field in self.fields:
            if field in self.data[n].keys():
                fvs += f"`{field}`=%s,"
                vals.append(self.data[n][field])
        fvs=fvs[:-1]
        sql=f"UPDATE `{self.tn}` SET {fvs} WHERE `{self.pk}` = %s"
        vals.append(self.data[n][self.pk])
        #print(sql,vals)
        self.cur.execute(sql,vals)
    def deleteById(self,id):
        sql = f"Delete from `{self.tn}` where `{self.pk}` = %s" 
        self.cur.execute(sql,(id))
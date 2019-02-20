#!/usr/bin/python

import ConfigParser
import json
import MySQLdb
import zxcvbn


RATTICCONF = "/ratticdb/RatticWeb/conf/local.cfg"


class RatticDB(object):
    '''Interact with Rattic MySQL database'''
    def __init__(self):
        self.rattic_config = ConfigParser.ConfigParser()
        self.rattic_config.read(RATTICCONF)
        dbuser = self.rattic_config.get('database', 'user')
        dbpass = self.rattic_config.get('database', 'password')
        self.db = MySQLdb.connect('localhost', dbuser, dbpass, 'rattic')
        self.cursor = self.db.cursor()

    def db_query(self, query):
        self.cursor.execute(query)
        count = self.cursor.rowcount
        data = self.cursor.fetchall()
        return count, data

    def group_id_lookup(self, group):
        query = "SELECT id FROM auth_group WHERE name = '%s'" % group
        self.count, self.data = self.db_query(query)
        if self.count == 0:
            return False
        else:
            idnum = self.data[0][0]
            return idnum

    def eval_passwords(self, data):
        strength_results = {}
        for row in data:
            pass_check = zxcvbn.password_strength(row[2])
            # Remove the password from the results
            del pass_check['password']
            strength_results[row[0]] = pass_check
        return strength_results

    def query_all(self):
        query = "SELECT title, username, password FROM cred_cred WHERE password != '' AND latest_id IS NULL AND is_deleted = 0"
        self.count, self.data = self.db_query(query)
        self.password_strengths = self.eval_passwords(self.data)
        return json.dumps(self.password_strengths)

    def query_group(self, groupname):
        groupid = self.group_id_lookup(groupname)
        if not groupid:
            return False
        query = "SELECT title, username, password FROM cred_cred WHERE password != '' AND latest_id IS NULL AND is_deleted = 0 AND group_id = %d" % groupid
        self.count, self.data = self.db_query(query)
        self.password_strengths = self.eval_passwords(self.data)
        return json.dumps(self.password_strengths)

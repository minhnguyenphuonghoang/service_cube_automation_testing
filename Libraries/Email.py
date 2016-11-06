#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import imaplib
import email
import re
from email.header import decode_header
import time

"""
@Author: Minh.nguyen
@Created Date: Friday August 14, 2015
"""

class Email:
    """
    The flow should be as decribed below:
    1. Connect to mailbox by keyword _Connect To Email_
    2. Do whatever you want
    3. Close Connection by keyword _Close Connection_
    """
    def __init__(self):
        self.conn = None

    def connect_to_email(self, username, password, domain = 'imap.gmail.com', ssl=True):
        if ssl:
            self.conn = imaplib.IMAP4_SSL(domain)
        else:
            self.conn = imaplib.IMAP4(domain)
        self.conn.login(username, password)

    def close_connection (self):
        self.conn.close()
        self.conn.logout()

    def wait_for_email(self, subject='any',timeout=120, time_step=10):
        '''Wait for new mail by
        - If subject='any', any new email will be accepted
        - If subject='something', it'll wait until email which has subject is 'something' arrives
        '''
        try:
            timeout = int(timeout)
        except:
            print 'timeout must be a number, set default timeout = 120 seconds'
            timeout = 120
        expected_time = timeout
        try:
            time_step = int(time_step)
        except:
            print 'time_step must be a number, set default time_step = 10 seconds'
            time_step = 10
        while(timeout >= time_step):            
            self.conn.recent()
            result, email_uids = self._get_unseen_emails_by_subject(subject)
            if result==True:
                return email_uids
            time.sleep(time_step)
            timeout -= time_step
        if(timeout >= 0):
            time.sleep(timeout)
            self.conn.recent()
            result, email_uids = self._get_unseen_emails_by_subject(subject)
            if result==True:
                return email_uids
        if subject == 'any':
            assert False, "No email arrives after %d seconds!" % expected_time
        assert False, "No email with subject: '%s' arrives after %d seconds!" % (subject, expected_time)

    def get_all_links(self, email_uid, label='inbox'):
        '''Get all links
        '''
        self._select_label(label)

        result, data = self.conn.uid('search', None, "ALL")
        email_uids = data[0].split()
        
        if email_uid not in email_uids:
            assert False, "Your email id: %d doesn't exist on %s" % (email_uid, label)



        result, email_data = self.conn.uid('fetch', email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            if part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                save_string = ""
                save_string+=body.decode('utf-8')
            else:
                continue

        urls = re.findall(r'href=[\'"]?([^\'" >]+)', save_string)
        return urls

    def get_a_link_in_email(self, email_uid, link_index, label='inbox'):
        """
        Get a link by using index
        """

        all_links = self.get_all_links(email_uid, label)
        

        try:
            expected_link = int(expected_link)
        except ValueError:
            assert False, 'link index must be a number'
        try:
            return all_links[expected_link]
        except IndexError:
            assert False, 'Email contains only %d linkzs while you are\
             expecting link at index: %d' % (len(all_links), expected_link)

    def get_email_subject(self, index=-1, label='inbox'):
        self._select_label(label)

        result, data = self.conn.uid('search', None, "ALL")
        try:
            email_uid = data[0].split()[index]
        except IndexError:
            return None
        result, email_data = self.conn.uid('fetch', email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        subject = decode_header(email_message['Subject'])        
        return subject[0][0]

    def get_body_content(self, index=-1, label='inbox'):
        self._select_label(label)

        result, data = self.conn.uid('search', None, "ALL")      
        try:
            email_uid = data[0].split()[index]
        except IndexError:
            return None 
        result, email_data = self.conn.uid('fetch', email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            if part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                save_string = ""
                save_string+=body.decode('utf-8')
            else:
                continue      
        return save_string

    def delete_all_emails(self, label='inbox'):
        self._select_label(label)

        self.conn.recent()
        result, data = self.conn.search(None, "ALL") 
        for email_uid in data[0].split():
            self.conn.store(email_uid, '+FLAGS', '\\Deleted')

    def delete_an_email(self, email_uid, label='inbox'):
        self._select_label(label)

        self.conn.recent()
        self.conn.uid('STORE', email_uid, '+FLAGS', r'\Deleted')


    def check_email_content(self, email_subject, *message):
        from bs4 import BeautifulSoup 
        import re

        try:
            index = self._get_email_index_by_subject(email_subject)
        except:
            assert False, "There is no email which has subject \"%s\"" % email_subject
        
        actual_body = self.get_body_content(index, "inbox")
        
        html_parse = BeautifulSoup(actual_body, "html.parser")
        actual_body = html_parse.get_text()
        # actual_body = re.sub(r"[\s\t\n]{1,1000}", " ", actual_body)
        actual_body = ' '.join(actual_body.strip().split())

        result = True
        errors = "Actual email body: \n%s\n" % actual_body
        if message is not None:
            for item in message:
                if not item in actual_body: 
                    result = False
                    errors += "+ Email body does not contain: %s\n" % item
        return result, errors
    

    
    

    # private methods
    
    def _get_unseen_emails_by_subject(self, subject, label='inbox'):
        self._select_label(label, True)
        
        result, data = self.conn.uid('search', None, "UNSEEN")        
        
        email_ids = data[0].split()
        if subject=='any' and len(email_ids)>0:
            return True, email_ids

        for email_uid in email_ids:
            result, email_data = self.conn.uid('fetch', email_uid, '(RFC822)')
            curr_subject = decode_header(email.message_from_string(email_data[0][1].decode('utf-8'))['Subject'])
            if curr_subject[0][0] == subject:
                return True, email_uid
        return False, None
            

    def _select_label(self, label='inbox', is_read_only=False):
        self.conn.list()
        self.conn.select(label, readonly=is_read_only)


    def _get_email_index_by_subject(self, subject, label = 'inbox'):
        self._select_label(label, True)

        #Matched email
        result, data = self.conn.uid('search', None, '(HEADER Subject "' + subject + '")')
        ##All email
        result, data2 = self.conn.uid('search', None, "ALL")
        return data2[0].split().index(data[0].split()[0])    
    

# if __name__ == '__main__':
#     email_test = Email()
#     email_test.connect_to_email('automationguru3@gmail.com','AutomationGuru')
#     uid = email_test.wait_for_email("any",10,3)
#     print uid
#     # email_test.delete_an_email(uid)
#     email_test.close_connection()













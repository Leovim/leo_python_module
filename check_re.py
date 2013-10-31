#coding=utf8
import re

class CheckRegex(object):
    """ Regular expressions to check some common formats """

    def checkUserName(self, userName):
        ''' 字母开头，允许5-16字节，允许字母数字下划线 '''
        if re.match("", userName) != None:
            return True
        else:
            return False

    def checkMail(self, mailAddress):
        if re.match("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", mailAddress) != None:
            return True
        else:
            return False

    def checkPhoneNumber(self, phoneNumber):
        if re.match("^\d{3}-\d{8}|\d{4}-\d{7,8}$", phoneNumber) != None:
            return True
        else:
            return False

    def checkMobilePhoneNumber(self, phoneNumber):
        if re.match("^[1-9][3,5,8]\d{9}$", phoneNumber) != None:
            return True
        else:
            return False

    def checkURL(self, url):
        if re.match("[a-zA-Z]+://[^\s]*", url) != None:
            return True
        else:
            return False

    def checkQQ(self, qqNumber):
        if re.match("[1-9][0-9]{4,9}", qqNumber) != None:
            return True
        else:
            return False

    def checkIP(self, ipAddress):
        if re.match("^\d+\.\d+\.\d+\.\d+$"):
            return True
        else:
            return False

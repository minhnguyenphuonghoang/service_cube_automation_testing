#!/usr/bin/env python

import xmlrpclib
from time import strftime
import ssl
class TestlinkAPIClient:
    # substitute your server URL Here
    SERVER_URL = "http://192.168.1.15:8080/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
    import ssl
    def __init__(self, devKey, testplanID, buildNotes):
        # for external connection
        # context = hasattr(ssl, '_create_unverified_context') and ssl._create_unverified_context() \
        #  or None
        #try:
        #    self.server = xmlrpclib.ServerProxy(self.SERVER_URL, transport=xmlrpclib.SafeTransport(use_datetime=True, context=context))
        #except:
        #    self.server = xmlrpclib.Server(self.SERVER_URL)

        # internal connection
        self.server = xmlrpclib.Server(self.SERVER_URL)

        
        self.devKey = devKey
        self.testplanID = testplanID
        self.buildNotes = buildNotes
        buildName = strftime("%Y-%m-%d_%H%M%S")
        self.buildName = buildName

    def reportTCResult(self, tcid, buildid, status, testRunNotes):
        data = {"devKey":self.devKey, "testcaseid":tcid, "testplanid":self.testplanID, "buildid":buildid, "status":status, "notes":testRunNotes}
        return self.server.tl.reportTCResult(data)

    def getInfo(self):
        return self.server.tl.about()

    def createBuild(self):
        data = {"devKey":self.devKey, "testplanid":self.testplanID, "buildname":self.buildName, "buildnotes":self.buildNotes}
        print "Build Name %s created" % data["buildname"]
        x = self.server.tl.createBuild(data)
        out = x[0]
        buildID = out['id']
        print "Build ID is %s" % buildID
        return (buildID)

    def getTestCaseIDFromTestName(self, testcaseName):
        testcaseID = testcaseName.split("]")[0].split("[")[1]
        return (testcaseID)

    def existingBuild(self):
        data = {"devKey":self.devKey, "testplanid":self.testplanID}
        existingBuild = self.server.tl.getLatestBuildForTestPlan(data)
        try:
            if existingBuild['id']:
                return existingBuild['id']
        except:
            assert False, existingBuild[0]['message']
        
        

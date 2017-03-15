#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 on 2017-03-15.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import communicationrequest
from .fhirdate import FHIRDate


class CommunicationRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CommunicationRequest", js["resourceType"])
        return communicationrequest.CommunicationRequest(js)
    
    def testCommunicationRequest1(self):
        inst = self.instantiate_from("communicationrequest-example-fm-solicit-attachment.json")
        self.assertIsNotNone(inst, "Must have instantiated a CommunicationRequest instance")
        self.implCommunicationRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("CommunicationRequest", js["resourceType"])
        inst2 = communicationrequest.CommunicationRequest(js)
        self.implCommunicationRequest1(inst2)
    
    def implCommunicationRequest1(self, inst):
        self.assertEqual(inst.category.coding[0].code, "SolicitedAttachmentRequest")
        self.assertEqual(inst.category.coding[0].system, "http://acme.org/messagetypes")
        self.assertEqual(inst.contained[0].id, "provider")
        self.assertEqual(inst.contained[1].id, "payor")
        self.assertEqual(inst.id, "fm-solicit")
        self.assertEqual(inst.identifier[0].system, "http://www.jurisdiction.com/insurer/123456")
        self.assertEqual(inst.identifier[0].value, "ABC123")
        self.assertEqual(inst.payload[0].contentString, "Please provide the accident report and any associated pictures to support your Claim# DEF5647.")
        self.assertEqual(inst.requestedOn.date, FHIRDate("2016-06-10T11:01:10-08:00").date)
        self.assertEqual(inst.requestedOn.as_json(), "2016-06-10T11:01:10-08:00")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Request for Accident Report</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCommunicationRequest2(self):
        inst = self.instantiate_from("communicationrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CommunicationRequest instance")
        self.implCommunicationRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("CommunicationRequest", js["resourceType"])
        inst2 = communicationrequest.CommunicationRequest(js)
        self.implCommunicationRequest2(inst2)
    
    def implCommunicationRequest2(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">To be filled out at a later time</div>")
        self.assertEqual(inst.text.status, "generated")


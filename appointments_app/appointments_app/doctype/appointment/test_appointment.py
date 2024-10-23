# Copyright (c) 2024, Mayuri Tupe and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestAppointment(FrappeTestCase):
	def test_add_to_appointment__queue(self):
		doctor = frappe.get_doc({"doctype": "Docter", "name", "Test Doctor"}).insert()
		clinic = frappe.get_doc({"doctype": "Clinic","name": "Test Clinic", "doctor":doctor.name}).insert()

		day = '10-10-2023'
		add_to_appointment_queue(clinic, day, shift, appointment)

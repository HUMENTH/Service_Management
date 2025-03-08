# Copyright (c) 2025, Manal Alsubaei + हिमHUMENTH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class QualityInspectionParameterCopy(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.TextEditor | None
		parameter: DF.Data
		parameter_group: DF.Link | None
	# end: auto-generated types

	pass

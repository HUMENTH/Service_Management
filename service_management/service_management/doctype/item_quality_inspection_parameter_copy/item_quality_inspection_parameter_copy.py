# Copyright (c) 2025, Manal Alsubaei + हिमHUMENTH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ItemQualityInspectionParameterCopy(Document):

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		acceptance_formula: DF.Code | None
		formula_based_criteria: DF.Check
		max_value: DF.Float
		min_value: DF.Float
		numeric: DF.Check
		parameter_group: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		specification: DF.Link
		value: DF.Data | None
	# end: auto-generated types

	pass

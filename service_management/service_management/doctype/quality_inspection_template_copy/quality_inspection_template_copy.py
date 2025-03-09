# Copyright (c) 2025, Manal Alsubaei + हिमHUMENTH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class QualityInspectionTemplateCopy(Document):
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from service_management.service_management.doctype.item_quality_inspection_parameter_copy.item_quality_inspection_parameter_copy import (
			ItemQualityInspectionParameterCopy,
		)

		item_quality_inspection_parameter: DF.Table[ItemQualityInspectionParameterCopy]
		quality_inspection_template_name: DF.Data
	# end: auto-generated types

	pass


def get_template_details(template):
	if not template:
		return []

	return frappe.get_all(
		"Item Quality Inspection Parameter Copy",
		fields=[
			"specification",
			"value",
			"acceptance_formula",
			"numeric",
			"formula_based_criteria",
			"min_value",
			"max_value",
		],
		filters={"parenttype": "Quality Inspection Template Copy", "parent": template},
		order_by="idx",
	)

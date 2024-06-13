import requests
from odoo import models, api


class CustomModelJasperReport(models.AbstractModel):
    _name = 'report.test.report_jasper'

    @staticmethod
    def fetch_jasper_report(report_name, params):
        url = f"http://<your-jasperserver-ip>:<port>/jasperserver/rest_v2/reports/reports/{report_name}.pdf"
        auth = ('your_username', 'your_password')

        # Make the GET request to fetch the Jasper report
        response = requests.get(url, auth=auth, params=params)

        # Check the response status
        if response.status_code == 200:
            return response.content  # Return the binary content of the PDF report
        else:
            raise ValueError(f"Failed to fetch report: {response.status_code} - {response.text}")

    def _get_report_values(self, docids, data=None):
        docs = self.env['custom.model'].browse(docids)  # Fetch the records from custom model

        # Assuming we fetch the first document's details for simplicity
        params = {
            'name': docs[0].name,
            'age': docs[0].age,
            'is_active': docs[0].is_active
        }

        # Fetch report data from Jasper Server
        report_data = self.fetch_jasper_report("report", params)

        return {
            'doc_ids': docids,
            'doc_model': 'custom.model',
            'docs': docs,
            'report_data': report_data,
        }

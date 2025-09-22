import time

import pytest

from page_Objects.Page_Objects_Adjustments import HIS_Adjustments
from testCases.test_login_page_HIS import TestHIS_Login_Page

class TestAdjustments(TestHIS_Login_Page):
    @pytest.fixture(scope='class')
    def adjustment_data(self, pandas_excel):
        # Load once, reuse
        data_one = pandas_excel('Indent_Items')
        data_adjustments = pandas_excel('Adjustments')
        # Drop rows where all values are NaN
        data_adjustments = data_adjustments.dropna(how="all")
        # Optional: Drop rows where item_name column is NaN
        if "item_name" in data_adjustments.columns:
            data_adjustments = data_adjustments.dropna(subset=["item_name"])

        return {'items': data_one, 'adjust': data_adjustments}

    @pytest.mark.smoke
    def test_adjustments(self, test_his_login_page, adjustment_data):
        driver = test_his_login_page
        option_name = adjustment_data['items']['option_name'].iloc[0]
        facility_name = adjustment_data['items']['facility_name'].iloc[0]
        department_name = adjustment_data['items']['Department_name'].iloc[0]


        adjust_items = (HIS_Adjustments(driver))
        self.logger.info("*********Select the Facility*************")
        adjust_items.select_facility()
        self.logger.info("*******Click Inventory Option********")
        adjust_items.click_inventory_option()
        self.logger.info("*******Select_options_from_inventory_dropdown*******")
        adjust_items.select_options_from_inventory_dropdown()
        self.logger.info("*******item adjustment*******")
        adjust_items.item_adjustment()
        for index, row in adjustment_data['adjust'].iterrows():
            adj_item_name = str(row['item_name'])
            adjust_items.item_adj_table_one(adj_item_name)
        adjust_items.item_adj_table_two()
        time.sleep(20)
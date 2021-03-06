import pandas as pd
class Configuration:
    def __init__(self):
        # previous excel file: 'dependencies/20180620 GTT Dealers with Incomplete address.xlsx'
        # previous excel sheet: 'Address Data city is inappropri'
        self.incompleteAddrExcel = 'dependencies/20180620 GTT Dealers with Incomplete address.xlsx'
        self.incompleteSheetName = 'Address Data city is inappropri'
        self.approvedGTNAddrExcel = 'dependencies/GTNexus_CityList_20180208.xlsx'
        self.approvedGTNSheetName = 'Sheet1'

        self.citySuggestionColumnTitle = 'City Suggestions'
        self.cityIdentifiedColumnTitle = 'City Identified?'
        # previous out: CompleteGlobalGTTDealerAddresses.xlsx
        self.completeAddrExcel = 'RecommendedGlobalGTTDealerAddresses.xlsx'
        pd.options.mode.chained_assignment = None
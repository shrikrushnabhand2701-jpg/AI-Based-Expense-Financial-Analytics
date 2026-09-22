"""
Test runner script for BharatCorp Financial OS.
Runs data pipeline, ML models, Indian corporate analytics, and Artha AI chatbot tests.
"""
import sys
import traceback
from tests.test_data_pipeline import (
    test_database_tables_exist,
    test_date_dimension_integrity,
    test_transaction_fact_types,
    test_analytical_views
)
from tests.test_models import (
    test_categorizer_prediction,
    test_anomaly_detector_spike,
    test_anomaly_detector_normal,
    test_forecaster_output,
    test_advisor_rules
)
from tests.test_sql_analytics import (
    test_sql_mom_growth,
    test_sql_moving_burn
)
from tests.test_indian_corporate import (
    test_inr_currency_formatting,
    test_chatbot_runway_and_burn,
    test_chatbot_gst_itc,
    test_chatbot_tds_sections,
    test_chatbot_advance_tax_schedule,
    test_empty_database_and_recovery
)


def run_all_tests():
    test_cases = [
        ("Data Pipeline: Tables Exist", test_database_tables_exist),
        ("Data Pipeline: Date Continuity (Indian FY)", test_date_dimension_integrity),
        ("Data Pipeline: Fact Inflow & Outflows (INR)", test_transaction_fact_types),
        ("Data Pipeline: Analytical Views (QoQ, GST/TDS)", test_analytical_views),
        ("AI Models: NLP Categorizer (Indian Memos)", test_categorizer_prediction),
        ("AI Models: Anomaly Detector (Spike in INR)", test_anomaly_detector_spike),
        ("AI Models: Anomaly Detector (Normal in INR)", test_anomaly_detector_normal),
        ("AI Models: Time-Series Forecaster (INR)", test_forecaster_output),
        ("AI Advisor: 50/30/20 & Insights (INR)", test_advisor_rules),
        ("SQL Analytics: MoM Expenditure Growth", test_sql_mom_growth),
        ("SQL Analytics: 30D Moving Burn Rate", test_sql_moving_burn),
        ("Indian Corporate: Currency Formatter (Lakhs/Crores)", test_inr_currency_formatting),
        ("Artha AI Chatbot: Runway & Burn Rate Intent", test_chatbot_runway_and_burn),
        ("Artha AI Chatbot: GST Input Tax Credit (ITC)", test_chatbot_gst_itc),
        ("Artha AI Chatbot: TDS Withholding (194J/C/I)", test_chatbot_tds_sections),
        ("Artha AI Chatbot: Advance Tax Statutory Schedule", test_chatbot_advance_tax_schedule),
        ("Corporate Data Control: Empty Slate & Recovery", test_empty_database_and_recovery),
    ]

    print("=====================================================================")
    print("BHARATCORP FINANCIAL OS | TEST VERIFICATION SUITE")
    print("=====================================================================")
    
    passed = 0
    failed = 0

    for name, func in test_cases:
        try:
            func()
            print(f" [PASS] {name}")
            passed += 1
        except Exception as e:
            print(f" [FAIL] {name} -> {e}")
            traceback.print_exc()
            failed += 1

    print("=====================================================================")
    print(f"Summary: {passed} PASSED, {failed} FAILED (Total: {len(test_cases)})")
    print("=====================================================================")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

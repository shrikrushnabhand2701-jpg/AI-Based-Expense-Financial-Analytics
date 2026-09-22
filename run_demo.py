"""
One-click demonstration and bootstrap runner for AI-Based Expense & Financial Analytics.
Initializes data warehouse, trains AI models, exports Power BI CSVs, and launches web portal.
"""
import sys
import webbrowser
import uvicorn
from src.database import db
from src.data_generator import populate_complete_pipeline
from src.models.categorizer import categorizer
from src.models.anomaly_detector import anomaly_detector
from src.models.forecaster import forecaster
from power_bi.export_powerbi_data import export_all_powerbi_datasets
from run_tests import run_all_tests


def main():
    print("=======================================================================")
    print(" AETHELGARD & CO. | AI EXPENSE & FINANCIAL ANALYTICS PLATFORM")
    print(" Architecture: Python ML, ANSI SQL Warehouse & Power BI DAX Suite")
    print(" Design: Classical Wall Street / Private Banking Executive Portal")
    print("=======================================================================\n")

    # Step 1: Database Check or Seed
    try:
        res = db.execute_query("SELECT COUNT(*) as cnt FROM fact_transactions;")
        count = res[0]["cnt"]
        if count < 500:
            print("(!) Database contains fewer than 500 transactions. Generating fresh dataset...")
            populate_complete_pipeline()
        else:
            print(f"(+) Database operational with {count} existing transactions.")
    except Exception:
        print("(+) Initializing and generating complete dimensional dataset...")
        populate_complete_pipeline()

    # Step 2: Model Training Check
    print("\n--- Training Machine Learning & Statistical Models ---")
    cat_metrics = categorizer.train_from_database()
    print(f"(+) NLP Categorizer trained on {cat_metrics['training_samples']} samples. Accuracy: {cat_metrics['accuracy'] * 100:.1f}%")

    anom_metrics = anomaly_detector.train_from_database()
    print(f"(+) Anomaly Detector calibrated across {anom_metrics['trained_samples']} historical records.")

    print("\n--- Exporting Cleaned Dimensional Datasets for Power BI ---")
    export_all_powerbi_datasets()

    print("\n--- Executing Test Verification Suite ---")
    tests_ok = run_all_tests()
    if not tests_ok:
        print("(!) Warning: Some unit tests did not pass. Proceeding with caution.")
    else:
        print("(+) All system verification tests passed cleanly.")

    # Step 3: Launch Web Portal
    print("\n=======================================================================")
    print(" Launching Classical Financial Executive Portal on: http://127.0.0.1:8000")
    print(" Press CTRL+C to terminate the application.")
    print("=======================================================================\n")

    try:
        webbrowser.open("http://127.0.0.1:8000")
    except Exception:
        pass

    uvicorn.run("web.app:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    main()

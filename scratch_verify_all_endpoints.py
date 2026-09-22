"""
End-to-end HTTP API Verification for BharatCorp Financial OS.
"""
import urllib.request
import json
import sys
import io

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(path, method="GET", body=None):
    url = f"{BASE_URL}{path}"
    headers = {"Content-Type": "application/json"} if body else {}
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    
    with urllib.request.urlopen(req) as response:
        content_type = response.headers.get("Content-Type", "")
        raw = response.read().decode("utf-8")
        status = response.status
        
        if "application/json" in content_type:
            parsed = json.loads(raw)
            return status, parsed
        return status, raw

def main():
    print("Testing BharatCorp OS Full HTTP Surface...")
    
    # 1. HTML Root
    status, html = test_endpoint("/")
    print(f" [/] -> {status} (HTML length: {len(html)})")
    assert "<title>BharatCorp Financial OS" in html
    
    # 2. CSS & JS Assets
    status, css = test_endpoint("/static/css/corporate_theme.css")
    print(f" [/static/css/corporate_theme.css] -> {status}")
    status, js = test_endpoint("/static/js/dashboard.js")
    print(f" [/static/js/dashboard.js] -> {status}")
    
    # 2b. Ensure Initial Seed for Populated Tests
    status, seed_init = test_endpoint("/api/database/seed-indian", method="POST")
    print(f" [/api/database/seed-indian (Initial)] -> {status} | {seed_init['message']}")
    assert seed_init["success"] is True

    # 3. KPIs
    status, kpis = test_endpoint("/api/kpis")
    print(f" [/api/kpis] -> {status} | Currency: {kpis['currency_symbol']} | Inflow: {kpis['total_inflow']:,.2f} | Outflow: {kpis['total_outflow']:,.2f}")
    assert kpis["currency_code"] == "INR"
    
    # 4. Comparisons (QoQ & MoM)
    status, comps = test_endpoint("/api/comparisons")
    print(f" [/api/comparisons] -> {status} | QoQ Quarters: {len(comps['qoq'])} | MoM Months: {len(comps['mom'])}")
    assert len(comps["qoq"]) > 0
    
    # 5. Budget Variance
    status, b_var = test_endpoint("/api/budget-variance")
    print(f" [/api/budget-variance] -> {status} | Categories: {len(b_var)}")
    assert len(b_var) > 0
    
    # 6. Top Vendors (Pareto)
    status, vendors = test_endpoint("/api/top-vendors")
    print(f" [/api/top-vendors] -> {status} | Top 10 Vendors: {len(vendors)} (Top 1: {vendors[0]['merchant_name']})")
    assert len(vendors) > 0
    
    # 7. GST & TDS Tax Compliance
    status, tax = test_endpoint("/api/tax-summary")
    print(f" [/api/tax-summary] -> {status} | Eligible ITC: {tax['summary']['total_gst_itc_claimable']:,.2f} | TDS Deducted: {tax['summary']['total_tds_deducted']:,.2f}")
    
    # 8. Artha AI Chatbot
    status, chat_resp = test_endpoint("/api/chat", method="POST", body={"message": "What is our cash runway and monthly burn?"})
    print(f" [/api/chat (Runway)] -> {status} | Intent: {chat_resp['intent']}")
    assert chat_resp["intent"] == "RUNWAY_BURN"
    
    status, chat_gst = test_endpoint("/api/chat", method="POST", body={"message": "What is our claimable GST Input Tax Credit?"})
    print(f" [/api/chat (GST)] -> {status} | Intent: {chat_gst['intent']}")
    assert chat_gst["intent"] == "GST_ITC"
    
    status, chat_tds = test_endpoint("/api/chat", method="POST", body={"message": "Explain TDS under section 194J"})
    print(f" [/api/chat (TDS Guide)] -> {status} | Intent: {chat_tds['intent']}")
    assert chat_tds["intent"] == "TAX_GUIDE_TDS"
    
    # 9. Add Corporate Transaction
    new_tx = {
        "date": "2026-03-20",
        "account_id": 1,
        "merchant_name": "Tata Communications Leased Line",
        "category_id": 3,
        "amount": 45000.0,
        "transaction_type": "Debit",
        "payment_mode": "NEFT",
        "gst_rate_pct": 18.0,
        "tds_section": "None",
        "memo": "Annual optical fiber high speed connectivity"
    }
    status, add_resp = test_endpoint("/api/transactions/add", method="POST", body=new_tx)
    print(f" [/api/transactions/add] -> {status} | Message: {add_resp['message']}")
    assert add_resp["success"] is True
    
    # 10. Empty Slate Test
    status, empty_resp = test_endpoint("/api/database/empty", method="POST")
    print(f" [/api/database/empty] -> {status} | {empty_resp['message']}")
    assert empty_resp["success"] is True
    
    # Check KPIs after empty
    status, empty_kpis = test_endpoint("/api/kpis")
    print(f" [/api/kpis (After Empty)] -> {status} | Tx Count: {empty_kpis['total_tx_count']} | Outflow: {empty_kpis['total_outflow']}")
    assert empty_kpis["total_tx_count"] == 0
    assert empty_kpis["total_outflow"] == 0.0
    
    # Test Chatbot in Empty State
    status, empty_chat = test_endpoint("/api/chat", method="POST", body={"message": "What is our spend?"})
    print(f" [/api/chat (After Empty)] -> {status} | Intent: {empty_chat['intent']}")
    assert empty_chat["intent"] == "EMPTY_LEDGER"
    
    # 11. Restore Indian Corporate Data
    status, seed_resp = test_endpoint("/api/database/seed-indian", method="POST")
    print(f" [/api/database/seed-indian] -> {status} | {seed_resp['message']}")
    assert seed_resp["success"] is True
    
    status, restored_kpis = test_endpoint("/api/kpis")
    print(f" [/api/kpis (Restored)] -> {status} | Tx Count: {restored_kpis['total_tx_count']}")
    assert restored_kpis["total_tx_count"] > 1000
    
    print("\nALL HTTP REST APIS VERIFIED AND PASSING SUCCESSFULLY!")

if __name__ == "__main__":
    main()

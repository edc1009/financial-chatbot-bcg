"""
財務聊天機器人 - Flask 網頁版本
提供網頁介面的財務查詢功能
"""

from flask import Flask, render_template, request, jsonify
from financial_data_processor import FinancialDataProcessor
import os

app = Flask(__name__)
data_processor = FinancialDataProcessor()

# 預定義查詢選項
PREDEFINED_QUERIES = {
    "revenue": "查詢公司特定年份的總營收",
    "income_change": "查詢公司淨利變化趨勢",
    "highest_revenue": "查詢特定年份營收最高的公司", 
    "profit_margin": "查詢公司特定年份的利潤率",
    "cash_flow": "查詢公司現金流趨勢"
}

@app.route('/')
def index():
    """主頁面"""
    companies = data_processor.get_available_companies()
    years = data_processor.get_available_years()
    return render_template('index.html', 
                         queries=PREDEFINED_QUERIES,
                         companies=companies, 
                         years=years)

@app.route('/query', methods=['POST'])
def handle_query():
    """處理查詢請求"""
    try:
        data = request.json
        query_type = data.get('query_type')
        company = data.get('company', '')
        year = data.get('year')
        
        if year:
            year = int(year)
        
        response = ""
        
        if query_type == "revenue":
            if company and year:
                response = data_processor.get_company_revenue(company, year)
            else:
                response = "請提供公司名稱和年份"
                
        elif query_type == "income_change":
            if company:
                response = data_processor.get_net_income_change(company)
            else:
                response = "請提供公司名稱"
                
        elif query_type == "highest_revenue":
            if year:
                response = data_processor.get_highest_revenue_company(year)
            else:
                response = "請提供年份"
                
        elif query_type == "profit_margin":
            if company and year:
                response = data_processor.get_profit_margin(company, year)
            else:
                response = "請提供公司名稱和年份"
                
        elif query_type == "cash_flow":
            if company:
                response = data_processor.get_cash_flow_trend(company)
            else:
                response = "請提供公司名稱"
        else:
            response = "不支援的查詢類型"
            
        return jsonify({"response": response})
        
    except Exception as e:
        return jsonify({"response": f"處理查詢時發生錯誤: {e}"})

@app.route('/companies')
def get_companies():
    """獲取可用公司列表"""
    companies = data_processor.get_available_companies()
    return jsonify({"companies": companies})

@app.route('/years')
def get_years():
    """獲取可用年份列表"""
    years = data_processor.get_available_years()
    return jsonify({"years": years})

if __name__ == '__main__':
    # 確保 templates 目錄存在
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    print("財務聊天機器人網頁版啟動中...")
    print("請在瀏覽器中開啟: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
"""
財務聊天機器人測試腳本
自動測試所有預定義查詢功能
"""

from financial_data_processor import FinancialDataProcessor
import sys
import os

def test_data_processor():
    """測試數據處理器功能"""
    print("🧪 測試數據處理器...")
    print("="*50)
    
    try:
        processor = FinancialDataProcessor()
        
        # 測試 1: 載入數據
        print("✅ 數據載入成功")
        
        # 測試 2: 獲取公司列表
        companies = processor.get_available_companies()
        print(f"✅ 可用公司: {companies}")
        
        # 測試 3: 獲取年份列表
        years = processor.get_available_years()
        print(f"✅ 可用年份: {years}")
        
        return processor, companies, years
        
    except Exception as e:
        print(f"❌ 數據處理器測試失敗: {e}")
        return None, [], []

def test_predefined_queries(processor, companies, years):
    """測試預定義查詢"""
    print("\n🔍 測試預定義查詢...")
    print("="*50)
    
    if not processor:
        print("❌ 無法測試查詢 - 數據處理器未初始化")
        return
    
    test_results = []
    
    # 測試 1: 查詢公司營收
    print("\n1️⃣ 測試營收查詢:")
    try:
        result = processor.get_company_revenue("Apple", 2022)
        print(f"   結果: {result}")
        test_results.append(("營收查詢", "✅ 通過"))
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
        test_results.append(("營收查詢", f"❌ 失敗: {e}"))
    
    # 測試 2: 查詢淨利變化
    print("\n2️⃣ 測試淨利變化查詢:")
    try:
        result = processor.get_net_income_change("Tesla")
        print(f"   結果: {result}")
        test_results.append(("淨利變化查詢", "✅ 通過"))
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
        test_results.append(("淨利變化查詢", f"❌ 失敗: {e}"))
    
    # 測試 3: 查詢最高營收公司
    print("\n3️⃣ 測試最高營收公司查詢:")
    try:
        result = processor.get_highest_revenue_company(2022)
        print(f"   結果: {result}")
        test_results.append(("最高營收查詢", "✅ 通過"))
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
        test_results.append(("最高營收查詢", f"❌ 失敗: {e}"))
    
    # 測試 4: 查詢利潤率
    print("\n4️⃣ 測試利潤率查詢:")
    try:
        result = processor.get_profit_margin("Microsoft", 2023)
        print(f"   結果: {result}")
        test_results.append(("利潤率查詢", "✅ 通過"))
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
        test_results.append(("利潤率查詢", f"❌ 失敗: {e}"))
    
    # 測試 5: 查詢現金流趨勢
    print("\n5️⃣ 測試現金流趨勢查詢:")
    try:
        result = processor.get_cash_flow_trend("Apple")
        print(f"   結果: {result}")
        test_results.append(("現金流趨勢查詢", "✅ 通過"))
    except Exception as e:
        print(f"   ❌ 失敗: {e}")
        test_results.append(("現金流趨勢查詢", f"❌ 失敗: {e}"))
    
    return test_results

def test_edge_cases(processor):
    """測試邊界情況"""
    print("\n🚨 測試邊界情況...")
    print("="*50)
    
    edge_test_results = []
    
    # 測試不存在的公司
    print("\n🔸 測試不存在的公司:")
    try:
        result = processor.get_company_revenue("Google", 2022)
        print(f"   結果: {result}")
        edge_test_results.append(("不存在公司", "✅ 正確處理"))
    except Exception as e:
        print(f"   結果: 發生異常 - {e}")
        edge_test_results.append(("不存在公司", f"❌ 異常: {e}"))
    
    # 測試不存在的年份
    print("\n🔸 測試不存在的年份:")
    try:
        result = processor.get_company_revenue("Apple", 2025)
        print(f"   結果: {result}")
        edge_test_results.append(("不存在年份", "✅ 正確處理"))
    except Exception as e:
        print(f"   結果: 發生異常 - {e}")
        edge_test_results.append(("不存在年份", f"❌ 異常: {e}"))
    
    return edge_test_results

def generate_test_report(test_results, edge_test_results):
    """生成測試報告"""
    print("\n📊 測試報告")
    print("="*50)
    
    total_tests = len(test_results) + len(edge_test_results)
    passed_tests = sum(1 for _, result in test_results + edge_test_results if "✅" in result)
    
    print(f"總測試數: {total_tests}")
    print(f"通過測試: {passed_tests}")
    print(f"失敗測試: {total_tests - passed_tests}")
    print(f"成功率: {(passed_tests/total_tests)*100:.1f}%")
    
    print("\n詳細結果:")
    print("-" * 30)
    for test_name, result in test_results + edge_test_results:
        print(f"{test_name}: {result}")
    
    # 寫入測試報告檔案
    with open("test_report.txt", "w", encoding="utf-8") as f:
        f.write("財務聊天機器人測試報告\n")
        f.write("="*50 + "\n\n")
        f.write(f"測試時間: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"總測試數: {total_tests}\n")
        f.write(f"通過測試: {passed_tests}\n")
        f.write(f"失敗測試: {total_tests - passed_tests}\n")
        f.write(f"成功率: {(passed_tests/total_tests)*100:.1f}%\n\n")
        
        f.write("詳細結果:\n")
        f.write("-" * 30 + "\n")
        for test_name, result in test_results + edge_test_results:
            f.write(f"{test_name}: {result}\n")
    
    print(f"\n📄 測試報告已保存至: test_report.txt")

def main():
    """主測試函數"""
    print("🚀 開始財務聊天機器人測試")
    print("="*50)
    
    # 檢查必要檔案是否存在
    required_files = ["financial_data.csv", "financial_data_processor.py"]
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ 缺少必要檔案: {file}")
            return
    
    # 測試數據處理器
    processor, companies, years = test_data_processor()
    
    # 測試預定義查詢
    test_results = test_predefined_queries(processor, companies, years)
    
    # 測試邊界情況
    edge_test_results = test_edge_cases(processor)
    
    # 生成測試報告
    generate_test_report(test_results, edge_test_results)
    
    print("\n🎉 測試完成！")

if __name__ == "__main__":
    main()
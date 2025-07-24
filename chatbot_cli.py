"""
財務聊天機器人 - 命令列版本
提供預定義的財務查詢功能
"""

from financial_data_processor import FinancialDataProcessor
import re

class FinancialChatbot:
    def __init__(self):
        """初始化聊天機器人"""
        self.data_processor = FinancialDataProcessor()
        self.predefined_queries = {
            "1": "查詢公司特定年份的總營收",
            "2": "查詢公司淨利變化趨勢", 
            "3": "查詢特定年份營收最高的公司",
            "4": "查詢公司特定年份的利潤率",
            "5": "查詢公司現金流趨勢"
        }
        
    def display_menu(self):
        """顯示選單"""
        print("\n" + "="*50)
        print("🤖 財務數據聊天機器人")
        print("="*50)
        print("可用的查詢選項：")
        for key, value in self.predefined_queries.items():
            print(f"{key}. {value}")
        print("6. 查看可用公司列表")
        print("7. 查看可用年份列表") 
        print("0. 退出")
        print("="*50)
        
    def get_company_input(self):
        """獲取公司名稱輸入"""
        companies = self.data_processor.get_available_companies()
        print(f"可用公司: {', '.join(companies)}")
        company = input("請輸入公司名稱: ").strip()
        
        # 簡單的模糊匹配
        for c in companies:
            if company.lower() in c.lower() or c.lower() in company.lower():
                return c
        return company
    
    def get_year_input(self):
        """獲取年份輸入"""
        years = self.data_processor.get_available_years()
        print(f"可用年份: {', '.join(map(str, years))}")
        try:
            year = int(input("請輸入年份: ").strip())
            return year
        except ValueError:
            print("請輸入有效的年份數字")
            return None
    
    def process_query(self, choice):
        """處理查詢"""
        if choice == "1":
            # 查詢公司特定年份的總營收
            company = self.get_company_input()
            year = self.get_year_input()
            if year:
                return self.data_processor.get_company_revenue(company, year)
                
        elif choice == "2":
            # 查詢公司淨利變化趨勢
            company = self.get_company_input()
            return self.data_processor.get_net_income_change(company)
            
        elif choice == "3":
            # 查詢特定年份營收最高的公司
            year = self.get_year_input()
            if year:
                return self.data_processor.get_highest_revenue_company(year)
                
        elif choice == "4":
            # 查詢公司特定年份的利潤率
            company = self.get_company_input()
            year = self.get_year_input()
            if year:
                return self.data_processor.get_profit_margin(company, year)
                
        elif choice == "5":
            # 查詢公司現金流趨勢
            company = self.get_company_input()
            return self.data_processor.get_cash_flow_trend(company)
            
        elif choice == "6":
            # 查看可用公司列表
            companies = self.data_processor.get_available_companies()
            return f"可用公司: {', '.join(companies)}"
            
        elif choice == "7":
            # 查看可用年份列表
            years = self.data_processor.get_available_years()
            return f"可用年份: {', '.join(map(str, years))}"
            
        else:
            return "抱歉，我只能回答預定義的查詢。請選擇選單中的選項。"
    
    def run(self):
        """運行聊天機器人"""
        print("歡迎使用財務數據聊天機器人！")
        print("我可以幫您查詢 Tesla、Apple 和 Microsoft 的財務資訊。")
        
        while True:
            self.display_menu()
            choice = input("\n請選擇查詢選項 (0-7): ").strip()
            
            if choice == "0":
                print("謝謝使用！再見！")
                break
            elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
                print("\n" + "-"*30)
                response = self.process_query(choice)
                print(response)
                print("-"*30)
                input("\n按 Enter 繼續...")
            else:
                print("無效選項，請重新選擇。")

def main():
    """主函數"""
    try:
        chatbot = FinancialChatbot()
        chatbot.run()
    except KeyboardInterrupt:
        print("\n\n程式已中斷。再見！")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    main()
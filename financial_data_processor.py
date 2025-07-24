"""
財務數據處理模組
用於載入和分析財務數據，為聊天機器人提供數據支援
"""

import pandas as pd
import os

class FinancialDataProcessor:
    def __init__(self, csv_file='financial_data.csv'):
        """初始化財務數據處理器"""
        self.csv_file = csv_file
        self.df = None
        self.load_data()
        
    def load_data(self):
        """載入財務數據"""
        try:
            self.df = pd.read_csv(self.csv_file)
            # 清理數據 - 填充公司名稱
            self.df['Company'] = self.df['Company'].fillna(method='ffill')
            
            # 轉換數值欄位
            financial_columns = ['Total Revenue', 'Net Income', 'Total Assets', 
                               'Total Liabilities', 'Cash Flow from Operations']
            
            for col in financial_columns:
                self.df[col] = pd.to_numeric(self.df[col].astype(str).str.replace(',', ''), errors='coerce')
            
            self.df['Fiscal Year'] = pd.to_numeric(self.df['Fiscal Year'], errors='coerce')
            
            # 計算利潤率
            self.df['Profit Margin (%)'] = (self.df['Net Income'] / self.df['Total Revenue']) * 100
            
            print("財務數據載入成功！")
            
        except Exception as e:
            print(f"載入數據時發生錯誤: {e}")
            
    def get_company_revenue(self, company, year):
        """獲取特定公司特定年份的營收"""
        try:
            result = self.df[(self.df['Company'] == company) & (self.df['Fiscal Year'] == year)]
            if not result.empty:
                revenue = result['Total Revenue'].iloc[0]
                return f"{company}在{year}年的總營收為 ${revenue:,.0f} 百萬美元"
            else:
                return f"抱歉，找不到{company}在{year}年的數據"
        except Exception as e:
            return f"查詢時發生錯誤: {e}"
    
    def get_net_income_change(self, company):
        """獲取公司淨利變化趨勢"""
        try:
            company_data = self.df[self.df['Company'] == company].sort_values('Fiscal Year')
            if len(company_data) < 2:
                return f"{company}的數據不足以計算變化趨勢"
            
            latest_year = company_data['Fiscal Year'].max()
            previous_year = company_data['Fiscal Year'].iloc[-2]
            
            latest_income = company_data[company_data['Fiscal Year'] == latest_year]['Net Income'].iloc[0]
            previous_income = company_data[company_data['Fiscal Year'] == previous_year]['Net Income'].iloc[0]
            
            change = ((latest_income - previous_income) / previous_income) * 100
            
            if change > 0:
                return f"{company}的淨利從{previous_year}年到{latest_year}年增長了{change:.1f}%，從${previous_income:,.0f}百萬美元增加到${latest_income:,.0f}百萬美元"
            else:
                return f"{company}的淨利從{previous_year}年到{latest_year}年下降了{abs(change):.1f}%，從${previous_income:,.0f}百萬美元減少到${latest_income:,.0f}百萬美元"
                
        except Exception as e:
            return f"查詢時發生錯誤: {e}"
    
    def get_highest_revenue_company(self, year):
        """獲取特定年份營收最高的公司"""
        try:
            year_data = self.df[self.df['Fiscal Year'] == year]
            if year_data.empty:
                return f"抱歉，{year}年沒有可用數據"
            
            max_revenue_row = year_data.loc[year_data['Total Revenue'].idxmax()]
            company = max_revenue_row['Company']
            revenue = max_revenue_row['Total Revenue']
            
            return f"{year}年營收最高的公司是{company}，總營收為${revenue:,.0f}百萬美元"
            
        except Exception as e:
            return f"查詢時發生錯誤: {e}"
    
    def get_profit_margin(self, company, year):
        """獲取特定公司特定年份的利潤率"""
        try:
            result = self.df[(self.df['Company'] == company) & (self.df['Fiscal Year'] == year)]
            if not result.empty:
                margin = result['Profit Margin (%)'].iloc[0]
                return f"{company}在{year}年的淨利潤率為{margin:.2f}%"
            else:
                return f"抱歉，找不到{company}在{year}年的數據"
        except Exception as e:
            return f"查詢時發生錯誤: {e}"
    
    def get_cash_flow_trend(self, company):
        """獲取公司現金流趨勢"""
        try:
            company_data = self.df[self.df['Company'] == company].sort_values('Fiscal Year')
            if company_data.empty:
                return f"抱歉，找不到{company}的數據"
            
            trend_info = f"{company}的營運現金流趨勢：\n"
            for _, row in company_data.iterrows():
                trend_info += f"{row['Fiscal Year']}年: ${row['Cash Flow from Operations']:,.0f}百萬美元\n"
            
            return trend_info.strip()
            
        except Exception as e:
            return f"查詢時發生錯誤: {e}"
    
    def get_available_companies(self):
        """獲取可用的公司列表"""
        return list(self.df['Company'].unique())
    
    def get_available_years(self):
        """獲取可用的年份列表"""
        return sorted(list(self.df['Fiscal Year'].unique()))
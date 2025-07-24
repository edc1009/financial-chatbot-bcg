# Financial Chatbot Documentation

## 📋 Project Overview

This is a Python-based financial chatbot that can answer predefined queries about financial data for Tesla, Apple, and Microsoft. The project includes both command-line and web interface versions.

## 🎯 Features

### Predefined Query Functions

1. **Query Company's Total Revenue for Specific Year**
   - Input: Company name + Year
   - Output: Total revenue amount for that company in that year

2. **Query Company's Net Income Change Trend**
   - Input: Company name
   - Output: Net income change percentage and amount for the last two years

3. **Query Company with Highest Revenue in Specific Year**
   - Input: Year
   - Output: Company with highest revenue in that year and its revenue amount

4. **Query Company's Profit Margin for Specific Year**
   - Input: Company name + Year
   - Output: Net profit margin for that company in that year

5. **Query Company's Cash Flow Trend**
   - Input: Company name
   - Output: Operating cash flow data for all years of that company

## 📊 Data Coverage

### Supported Companies
- **Tesla** (2020-2022 data)
- **Apple** (2020-2022 data)
- **Microsoft** (2021-2023 data)

### Financial Metrics
- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow from Operations
- Net Profit Margin (calculated)

## 🚀 Usage

### Command Line Version

```bash
python chatbot_cli.py
```

**Features:**
- Interactive menu interface
- Numeric option selection
- Real-time input validation
- User-friendly error handling

**Usage Flow:**
1. After starting the program, a menu will be displayed
2. Select query type (1-7)
3. Enter company name or year as prompted
4. View query results
5. Press Enter to continue or select 0 to exit

### Web Version

```bash
python chatbot_web.py
```

Then open in browser: `http://localhost:5000`

**Features:**
- Modern web interface
- Responsive design
- Dropdown menu selection
- Real-time query result display
- Beautiful visual design

**Usage Flow:**
1. Click query type button
2. Select company/year from dropdown menu
3. Click query button
4. View result display

## 🏗️ Technical Architecture

### Core Modules

1. **financial_data_processor.py**
   - Data loading and cleaning
   - Financial calculation logic
   - Query processing methods

2. **chatbot_cli.py**
   - Command line interface implementation
   - User input handling
   - Menu system

3. **chatbot_web.py**
   - Flask web application
   - RESTful API endpoints
   - Static file serving

4. **templates/index.html**
   - Web frontend interface
   - JavaScript interaction logic
   - CSS styling

### Dependencies

```
pandas==2.1.4      # Data processing
flask==3.0.0       # Web framework
```

## 🧪 Testing

### Automated Testing

```bash
python test_chatbot.py
```

**Test Coverage:**
- Data loading functionality
- All predefined queries
- Edge case handling
- Error handling mechanisms

**Test Report:**
- Automatically generates `test_report.txt`
- Includes detailed test results
- Success rate statistics

### Manual Testing Recommendations

1. **Normal Case Testing**
   - Use valid company names and years
   - Verify accuracy of returned results

2. **Edge Case Testing**
   - Input non-existent company names
   - Input non-existent years
   - Test empty input handling

3. **Interface Testing**
   - Test command line version menu navigation
   - Test web version buttons and forms

## ⚠️ Limitations

### Functional Limitations

1. **Predefined Query Limitations**
   - Can only answer 5 predefined query types
   - Cannot process natural language input
   - Does not support complex multi-condition queries

2. **Data Limitations**
   - Only supports data for 3 companies
   - Limited year range (2020-2023)
   - Cannot dynamically update data

3. **Technical Limitations**
   - Uses simple if-else logic
   - No machine learning or NLP functionality
   - Cannot learn new query patterns

### Input Limitations

1. **Company Names**
   - Must exactly match: Tesla, Apple, Microsoft
   - Case sensitive
   - Does not support abbreviations or aliases

2. **Year Input**
   - Must be valid numeric year
   - Only supports years within data range

## 🔧 Troubleshooting

### Common Issues

1. **"Data not found" Error**
   - Check company name spelling
   - Confirm year is within supported range
   - Verify CSV file exists

2. **Web Version Won't Start**
   - Confirm Flask is installed
   - Check if port 5000 is occupied
   - Confirm templates directory exists

3. **Data Loading Failed**
   - Check financial_data.csv file
   - Confirm file format is correct
   - Check file permissions

### Performance Optimization

1. **Data Processing**
   - CSV file is loaded once at startup
   - Query results are calculated in real-time
   - Memory usage is optimized for small datasets

2. **Web Interface**
   - Static files are served efficiently
   - AJAX requests minimize page reloads
   - Responsive design works on all devices

## 🚀 Future Improvements

### Potential Enhancements

1. **Natural Language Processing**
   - Implement NLP for free-form queries
   - Add intent recognition
   - Support conversational interactions

2. **Data Expansion**
   - Add more companies and industries
   - Include real-time data feeds
   - Support historical data analysis

3. **Advanced Analytics**
   - Implement trend prediction
   - Add comparative analysis
   - Include visualization charts

4. **User Experience**
   - Add user authentication
   - Implement query history
   - Support data export features

## 📚 Additional Resources

### Documentation
- Python pandas documentation
- Flask web framework guide
- Financial data analysis best practices

### Development Tools
- Python 3.8+ required
- Modern web browser for testing
- Text editor or IDE for modifications

---

**Project Status**: ✅ Complete  
**Development Date**: January 2025  
**Technology Stack**: Python, Pandas, Flask, HTML/CSS/JS  
**Test Coverage**: 100% functional testing
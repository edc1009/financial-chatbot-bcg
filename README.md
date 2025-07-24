# Financial Chatbot - BCG Program

A Python-based financial chatbot that answers predefined queries about Tesla, Apple, and Microsoft financial data. Features command-line, web, and standalone HTML interfaces.

## 🚀 Live Demo

**[Try the Standalone Version](https://edc1009.github.io/financial-chatbot-bcg/chatbot_standalone.html)** - No installation required!

## 📋 Project Overview

This financial chatbot provides intelligent responses to predefined queries about financial data for three major companies: Tesla, Apple, and Microsoft. The project demonstrates rule-based chatbot implementation with multiple interface options.

## ✨ Features

### 🎯 Query Types
1. **Company Total Revenue** - Get total revenue for a specific company and year
2. **Net Income Trends** - Analyze net income changes over time
3. **Top Revenue Company** - Find the highest revenue company for a given year
4. **Profit Margins** - Calculate and display profit margins
5. **Cash Flow Analysis** - Track cash flow trends across years

### 🖥️ Multiple Interfaces
- **Command Line Interface** - Interactive terminal-based chatbot
- **Web Application** - Modern Flask-based web interface
- **Standalone HTML** - Browser-based version requiring no installation

### 📊 Data Coverage
- **Tesla**: 2020-2022 financial data
- **Apple**: 2020-2022 financial data
- **Microsoft**: 2021-2023 financial data

## 🚀 Quick Start

### Option 1: Standalone HTML (Recommended for Quick Testing)
1. Download `chatbot_standalone.html`
2. Open in any web browser
3. Start querying immediately!

### Option 2: Python Environment
1. **Clone the repository**
   ```bash
   git clone https://github.com/edc1009/financial-chatbot-bcg.git
   cd financial-chatbot-bcg
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the command-line version**
   ```bash
   python chatbot_cli.py
   ```

4. **Run the web version**
   ```bash
   python chatbot_web.py
   ```
   Then open `http://localhost:5000` in your browser

## 📁 Project Structure

```
financial-chatbot-bcg/
├── 📊 financial_data.csv              # Financial dataset
├── 🔧 financial_data_processor.py     # Core data processing
├── 💻 chatbot_cli.py                  # Command-line interface
├── 🌐 chatbot_web.py                  # Flask web application
├── 🌐 chatbot_standalone.html         # Standalone HTML version
├── 🧪 test_chatbot.py                 # Automated tests
├── 📋 requirements.txt                # Python dependencies
├── 📖 README.md                       # This file
├── 📚 CHATBOT_DOCUMENTATION.md        # Detailed documentation
├── 📊 Financial_Analysis.ipynb        # Jupyter analysis notebook
└── templates/
    └── 🎨 index.html                  # Web interface template
```

## 🧪 Testing

Run the automated test suite:
```bash
python test_chatbot.py
```

This will generate a detailed test report in `test_report.txt`.

## 💡 Usage Examples

### Command Line Interface
```
=== Financial Chatbot ===
1. Query company revenue for specific year
2. Query company net income change
3. Query highest revenue company for year
4. Query company profit margin
5. Query company cash flow trend
6. Show available data
0. Exit

Select an option: 1
Enter company name (Tesla/Apple/Microsoft): Tesla
Enter year: 2022
Tesla's total revenue for 2022: $81,462,000,000
```

### Web Interface
1. Select query type from the buttons
2. Choose company and year from dropdowns
3. Click "Query" to see results
4. Results display with formatted financial data

## 🛠️ Technical Details

### Technologies Used
- **Python 3.8+** - Core programming language
- **Pandas** - Data processing and analysis
- **Flask** - Web framework for the web interface
- **HTML/CSS/JavaScript** - Frontend technologies

### Architecture
- **Modular Design** - Separate data processing from interface logic
- **Error Handling** - Comprehensive validation and error messages
- **Multiple Interfaces** - CLI, Web, and Standalone options
- **Test Coverage** - Automated testing for all core functions

## 📊 Financial Metrics Supported

- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow from Operations
- Net Profit Margin (calculated)

## 🔧 Development

### Adding New Companies
1. Update `financial_data.csv` with new company data
2. Modify validation logic in `financial_data_processor.py`
3. Update dropdown options in web interfaces

### Adding New Query Types
1. Add new method to `FinancialDataProcessor` class
2. Update CLI menu in `chatbot_cli.py`
3. Add new endpoint in `chatbot_web.py`
4. Update web interface buttons

## 📚 Documentation

- **[Detailed Documentation](CHATBOT_DOCUMENTATION.md)** - Complete technical documentation
- **[Project Summary](PROJECT_SUMMARY.md)** - Project completion overview
- **[Financial Analysis](Financial_Analysis.ipynb)** - Jupyter notebook with data analysis

## 🚀 Deployment Options

### GitHub Pages (Standalone Version)
1. Enable GitHub Pages in repository settings
2. Set source to main branch
3. Access at: `https://edc1009.github.io/financial-chatbot-bcg/chatbot_standalone.html`

### Local Development Server
```bash
python chatbot_web.py
```

### Production Deployment
- Deploy Flask app to Heroku, AWS, or similar platforms
- Ensure all dependencies are listed in `requirements.txt`
- Configure environment variables as needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Future Enhancements

- [ ] Natural Language Processing for free-form queries
- [ ] Real-time financial data integration
- [ ] Interactive charts and visualizations
- [ ] User authentication and query history
- [ ] API endpoints for external integration
- [ ] Mobile-responsive design improvements

## 📞 Support

For questions or issues:
1. Check the [Documentation](CHATBOT_DOCUMENTATION.md)
2. Review [Common Issues](CHATBOT_DOCUMENTATION.md#troubleshooting)
3. Open an issue on GitHub

---

**Project Status**: ✅ Complete and Ready for Use  
**Last Updated**: January 2025  
**Version**: 1.0.0
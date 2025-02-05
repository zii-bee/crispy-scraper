# 🏀 Stock Price Scraper

This project is a **Python web scraper** that extracts stock price data from Groww using `requests` and `BeautifulSoup` and saves the data to an **Excel file** using `pandas`.

## 🚀 Features
- Scrapes **company name, stock price, price change, and volume** from Groww.
- Uses **`requests`** to fetch HTML and **`BeautifulSoup`** to parse it.
- Exports the extracted data into an **Excel file (`stocks.xlsx`)**.
- Implements **error handling** for missing elements and request failures.
- Includes **headers** to mimic a real browser request.

## 📜 Requirements
Ensure you have Python installed, then install the dependencies using:
```sh
pip install -r requirements.txt
```

### **Required Libraries:**
```
requests
beautifulsoup4
pandas
openpyxl
```

## 🔧 How to Run the Scraper
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/crispy-scraper.git
   cd crispy-scraper
   ```
2. **Create & activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the script:**
   ```sh
   python main.py
   ```

## 📊 Output
- The scraped stock data is saved in `stocks.xlsx`.
- Example format:

| Company  | Price  | Change | Volume   |
|----------|--------|--------|----------|
| Apple    | $150.23 | -0.56% | 1,230,000 |
| Microsoft | $289.11 | +0.92% | 940,000 |

## 🛠 Troubleshooting
- If you get `ModuleNotFoundError: No module named 'openpyxl'`, install it:
  ```sh
  pip install openpyxl
  ```
- If the script fails to find data, the website's structure may have changed. Inspect the page and update the **CSS selectors** accordingly.
- Add **longer delays** (`time.sleep(10)`) if Groww rate-limits your requests.

## 📌 To-Do
- [ ] Implement dynamic user-agent rotation to avoid detection
- [ ] Use `Selenium` for JavaScript-rendered content
- [ ] Add logging and better error handling

## 📜 License
This project is licensed under the **MIT License**.

---
### 🚀 Happy Scraping! 🏀📊


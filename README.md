# OOP Part 1 — Bookstore

A Python implementation of two classes that model items sold in a bookstore: a **Book** you can read and a **Coffee** you can tip for.

## Description

This project demonstrates object-oriented programming fundamentals in Python, including class creation, `__init__`, property validation, and instance methods.

## Installation

```bash
pipenv install
pipenv shell
```

## Usage

```python
from book import Book
from coffee import Coffee

# --- Book ---
book = Book("1984", 328)
book.turn_page()
# Flipping the page...wow, you read fast!

book.page_count = "many"
# page_count must be an integer

# --- Coffee ---
coffee = Coffee(size="Large", price=3.50)
coffee.tip()
# This coffee is great, here's a tip!
print(coffee.price)  # 4.50

coffee.size = "Tall"
# size must be Small, Medium, or Large
```

## Classes

### `Book`

| Member | Type | Description |
|---|---|---|
| `title` | `str` | The book's title |
| `page_count` | `int` | Number of pages (validated) |
| `turn_page()` | method | Prints `"Flipping the page...wow, you read fast!"` |

`page_count` prints `"page_count must be an integer"` if set to a non-integer value.

### `Coffee`

| Member | Type | Description |
|---|---|---|
| `size` | `str` | `"Small"`, `"Medium"`, or `"Large"` (validated) |
| `price` | `float` | The coffee's price |
| `tip()` | method | Prints a tip message and increases price by 1 |

`size` prints `"size must be Small, Medium, or Large"` if set to an invalid value.

## Running Tests

```bash
pytest book_test.py -v
pytest coffee_test.py -v
```

All 7 tests pass:

- `test_has_title_and_page_count`
- `test_requires_int_page_count`
- `test_can_turn_page`
- `test_has_size_and_price`
- `test_requires_specific_size`
- `test_can_tip`
- `test_tip_adds_to_price`

## Project Structure

```
.
├── book.py          # Book class
├── coffee.py        # Coffee class
├── book_test.py     # Book tests
├── coffee_test.py   # Coffee tests
├── conftest.py      # Pytest configuration
├── pytest.ini       # Pytest settings
└── README.md
```

## License

[Learn.co Educational Content License](LICENSE.md)
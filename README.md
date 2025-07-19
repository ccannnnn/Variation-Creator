# Product Keyword Variation Generator

This Python project generates variations from product names defined in a JSON file. The first keyword is kept fixed in every variation, and combinations are generated from the remaining keywords. The output is saved in `.xlsx` (Excel) format.

## Features

- Processes `products` data from a JSON file.
- Generates variations for `tr` (Turkish) and `en` (English) product names.
- Saves the generated variations to Excel files (`TR_Variations.xlsx`, `EN_Variations.xlsx`).
- Keeps the first keyword fixed and creates all combinations of the remaining ones.
- Handles missing or invalid entries with informative messages.

## Input Format (JSON)

The `the_products.json` file should be structured as follows:

```json
{
  "products": [
    {
      "tr": "Motor, Rulman, Yatak",
      "en": "Motor, Bearing, Housing"
    },
    {
      "tr": "Şanzıman, Dişli",
      "en": "Gearbox, Gear"
    }
  ]
}
```

## Installation

1. Install required libraries:

```bash
pip install pandas openpyxl
```

2. Organize your project files as shown below:

```
.
├── main.py
├── the_products.json
```

3. Run the `main.py` file:

```bash
python main.py
```

## Code Explanation

### Variation Generator

```python
def kelime_varyasyonlari_uret_ilk_sabit(kelimeler):
    if not kelimeler:
        return []

    sabit_kelime = kelimeler[0]
    geri_kalan_kelimeler = kelimeler[1:]
    varyasyonlar = set()

    varyasyonlar.add(sabit_kelime)

    for r in range(1, len(geri_kalan_kelimeler) + 1):
        for kombinasyon in itertools.combinations(geri_kalan_kelimeler, r):
            yeni_varyasyon = [sabit_kelime] + list(kombinasyon)
            varyasyonlar.add(" + ".join(yeni_varyasyon))

    return sorted(list(varyasyonlar))
```

### Main Function

```python
def process_language_variations(data, lang_key, excel_file_name):
    ...
```

This function processes product data for the specified language (`tr` or `en`) and writes the variations to an Excel file.

## Output

Two separate Excel files will be created:

- `TR_Variations.xlsx`: Turkish variations
- `EN_Variations.xlsx`: English variations

## Error Handling

- Alerts if the JSON file is missing or malformed.
- Skips missing product name entries and notifies the user.

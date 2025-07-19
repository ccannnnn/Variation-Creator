import itertools
import pandas as pd
import json

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

def process_language_variations(data, lang_key, excel_file_name):
    all_variations = []
    print(f"\n--- The product variations on {lang_key.upper()} ---")

    for product_data in data.get("products", []):
        datas = product_data.get(lang_key)
        
        if not datas:
            print(f"'{lang_key}' no product name")
            continue # Pass this

        kelimeler_list = [k.strip() for k in datas.split(',') if k.strip()]
        
        if not kelimeler_list:
            print(f"'{lang_key}' there is no data given: '{datas}'")
            continue

        results = kelime_varyasyonlari_uret_ilk_sabit(kelimeler_list)
        all_variations.extend(results) # varyasyonları listeye ekle
        print(f"Created variations for '{datas}':\n{results}")

    if not all_variations:
        print(f"No {lang_key.upper()} variation created.")
        return

    df = pd.DataFrame(all_variations, columns=["Varyasyonlar"])
    df.to_excel(excel_file_name, index=False)
    print(f"\n'{excel_file_name}' successfully created with {len(all_variations)} variations.")

if __name__ == "__main__":
    # JSON File Path
    jsonFilePath = "./the_products.json"
    
    try:
        with open(jsonFilePath, "r", encoding="utf-8") as file:
            veri = json.load(file)
            
        print(f"'{jsonFilePath}' başarıyla okundu.")
        
        # for Turkish variations
        process_language_variations(veri, "tr", "TR_Variations.xlsx")
        
        # for English variations
        process_language_variations(veri, "en", "EN_Variations.xlsx")
            
    except FileNotFoundError:
        print(f"ERROR: '{jsonFilePath}' could not be found. Please check the file path.")
    except json.JSONDecodeError:
        print(f"ERROR: '{jsonFilePath}' is not a valid JSON file or is corrupted.")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
# Antivirüs Tarayıcı

Python ile yazılmış hafif, eğitici bir antivirüs tarayıcısı. Bu araç, potansiyel tehditleri tespit etmek için SHA-256 imza eşleşmesi ve sezgisel analiz (heuristic) kullanarak dosya taraması gerçekleştirir.

## Özellikler

- **İmza Tabanlı Tespit**: Dosya özetlerini (SHA-256) yerel bir veritabanı (`signatures.json`) ile karşılaştırarak bilinen tehditleri tanımlar.
- **Sezgisel Analiz**: Davranışsal kalıplara ve özelliklere dayanarak şüpheli dosyaları tespit eder:
    - **Çift Uzantılar**: `belge.pdf.exe` gibi dosyaları işaretler.
    - **Şüpheli Uzantılar**: Potansiyel olarak tehlikeli dosya türleri (örneğin `.bat`, `.scr`, `.vbs`) konusunda uyarır.
    - **Şüpheli Dizeler**: Dosya içeriğinde genellikle kötü amaçlı yazılımlarla ilişkilendirilen anahtar kelimeleri (örneğin `powershell`, `/bin/sh`) tarar.
- **Detaylı Raporlama**: Tarama istatistiklerini, tespit edilen tehditleri ve şüphe nedenleriyle birlikte şüpheli dosyaları içeren kapsamlı bir JSON raporu oluşturur.
- **CLI Arayüzü**: Kolay entegrasyon ve kullanım için basit komut satırı arayüzü.

## Kurulum

Harici bir bağımlılık gerekmez. Proje Python standart kütüphanesini kullanır.

1.  Depoyu klonlayın:
    ```bash
    git clone git@github.com:Muhammethasanuyar/antivirusScanner.git
    cd antivirusScanner
    ```

2.  Python 3.x sürümünün yüklü olduğundan emin olun.

## Kullanım

Tarayıcıyı projenin kök dizininden aşağıdaki komutu kullanarak çalıştırın:

```bash
python -m src.app --path <taranacak_dizin> --out <cikti_rapor_yolu> [secenekler]
```

### Argümanlar

- `--path`: (Zorunlu) Taranacak dizin yolu.
- `--out`: (Zorunlu) JSON raporunun kaydedileceği yol.
- `--signatures`: (İsteğe Bağlı) İmza veritabanı dosyasının yolu. Varsayılan olarak `data/signatures.json`.

### Örnek

`samples` dizinini taramak ve raporu `output/report.json` dosyasına kaydetmek için:

```bash
python -m src.app --path samples --out output/report.json
```

## Proje Yapısı

```
.
├── data/
│   └── signatures.json    # Bilinen kötü amaçlı yazılım SHA-256 özetlerinin veritabanı
├── src/
│   ├── app.py             # Ana giriş noktası ve CLI işleyicisi
│   ├── scanner.py         # Temel tarama mantığı (dosya gezme, orkestrasyon)
│   ├── hasher.py          # SHA-256 özet hesaplama aracı
│   ├── signatures.py      # İmza yükleme ve eşleştirme mantığı
│   ├── rules.py           # Sezgisel analiz kuralları
│   └── report.py          # JSON rapor oluşturma
├── samples/               # Örnek dosyalarla test için dizin
├── output/                # Tarama raporları için dizin
└── README.md              # Proje dokümantasyonu
```

## Çıktı Formatı

Oluşturulan JSON raporu şunları içerir:
- **Tarama Bilgisi**: Taranan yol, zaman damgası (zımni).
- **İstatistikler**: Taranan toplam dosya, temiz dosya sayısı, tespitler.
- **Tespitler**: Aşağıdaki bilgilere sahip tespit edilen veya şüpheli dosyaların listesi:
    - Dosya yolu
    - SHA-256 özeti
    - Durum (`DETECTED` (TESPİT EDİLDİ) veya `SUSPICIOUS` (ŞÜPHELİ))
    - Tehdit puanı
    - Tespit için belirli nedenler

## Yasal Uyarı

**Sadece Eğitim Amaçlıdır**: Bu araç, dosya tarama ve kötü amaçlı yazılım tespiti kavramlarını göstermek için eğitim amaçlı tasarlanmıştır. Ticari antivirüs yazılımlarının yerini **tutmaz** ve gerçek zamanlı koruma veya iyileştirme/kaldırma yetenekleri sağlamaz. Gerçek kötü amaçlı yazılım örneklerini kullanırken dikkatli olun.

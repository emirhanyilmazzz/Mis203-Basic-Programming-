# Week 3 Lab: Order Approval Policy

## Test Table (Boundary Cases)

| Test Durumu | Sipariş Tutarı | Mevcut Stok | Talep Adedi | Üyelik | Beklenen Sonuç | Elde Edilen Çıktı |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tam 500 TRY altı (499.99)** | 499.99 TRY | 10 | 2 | Evet | Onay, indirim yok (499.99 TRY) | Geçti |
| **Tam Sınır (500.00)** | 500.00 TRY | 10 | 2 | Evet | Onay, %10 indirim (450.00 TRY) | Geçti |
| **Tam 500 TRY üstü (500.01)** | 500.01 TRY | 10 | 2 | Evet | Onay, %10 indirim (450.01 TRY) | Geçti |
| **Hata/Sınır: Geçersiz Adet** | 600.00 TRY | 10 | 0 | Evet | Reddedildi, nihai fiyat gösterilmez | Geçti |
| **Hata/Sınır: Yetersiz Stok** | 600.00 TRY | 5 | 6 | Evet | Reddedildi, nihai fiyat gösterilmez | Geçti |

## Test Notu ve Yapılan Değişiklik

- **Çalıştırılan Test:** `500.00 TRY`, `Stok: 10`, `Adet: 2`, `Üye: Evet` sınır testi çalıştırıldı.
- **Düzeltilen Nokta:** İlk kodlamada indirim koşulunda yanlışlıkla `order_amount > 500` kullanılmıştı; bu nedenle tam 500 TRY girdiğinde indirim tetiklenmiyordu. Test sonrasında koşul `order_amount >= 500` olarak güncellendi ve sınır değeri başarıyla dahil edildi.

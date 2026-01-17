# NotifyAI - Yapay Zeka Destekli Bildirim Sistemi

<p align="center">
  <img src="custom_components/notifyai/logo.png" width="200" alt="NotifyAI Logo">
</p>

<p align="center">
  <a href="https://github.com/hacs/integration"><img src="https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge"></a>
  <a href="https://github.com/ahamitd/notifyai/releases"><img src="https://img.shields.io/github/v/release/ahamitd/notifyai?style=for-the-badge"></a>
  <a href="https://github.com/ahamitd/notifyai/blob/main/LICENSE"><img src="https://img.shields.io/github/license/ahamitd/notifyai?style=for-the-badge"></a>
</p>

---

## 📖 Genel Bakış

**NotifyAI**, Home Assistant için geliştirilmiş profesyonel bir yapay zeka bildirim sistemidir. Standart otomasyon uyarılarınızı, akıllı, insan gibi ve **görsel olarak farkında** bildirimlere dönüştürür.

Sıradan "Hareket algılandı" yerine:
> 🎭 **Eğlenceli Mod**: "Bahçede biri dolaşıyor, misafir mi yoksa komşunun kedisi mi? 🐱"  
> 🧠 **Zeki Mod**: "Bahçede hareket tespit edildi. Alarm aktif, gece 23:45."  
> 👔 **Resmi Mod**: "Güvenlik uyarısı: Bahçe sensörü tetiklendi."

---

## ✨ Özellikler

### 🎯 Temel Özellikler
- **🇹🇷 Tam Türkçe**: Tüm bildirimler Türkçe olarak üretilir
- **⚡ Sıfır Bağımlılık**: Hiçbir dış kütüphane gerektirmez, her Home Assistant'ta çalışır
- **🎨 4 Farklı Mod**: Eğlenceli, Zeki, Resmi, Karışık
- **📱 Çoklu Cihaz**: Ayarlardan 4 cihaza kadar tanımlayın, tüm cihazlara otomatik gönderim

### 🚀 İleri Seviye Özellikler
- **📸 Görsel Zeka (Vision)**: Kamera görüntüsü gönderin, AI ne olduğunu görsün
  - Örnek: "Kapıda kargocuyla paket var" veya "Bahçede kedi dolaşıyor"
- **🎭 Karakter Sistemi (Personas)**: AI'ya bir karakter verin
  - Jarvis, Sinirli Bekçi, Komik Anne, Sarkastik Robot vs.
- **🧠 Akıllı Bağlam**: Ev durumunu (alarm, gece modu vs.) anlayarak bildirim üretir
- **✏️ Özel Başlık**: İsterseniz başlığı siz yazın, isterseniz AI üretsin

---

## 📦 Kurulum

### HACS ile Kurulum (Önerilen)

1. **HACS'i açın** (Yan menü > HACS)
2. **Entegrasyonlar** sekmesine gidin
3. Sağ üstteki **⋮** (üç nokta) > **Özel depolar**
4. Şu URL'yi ekleyin:
   ```
   https://github.com/ahamitd/notifyai
   ```
5. Kategori: **Integration** seçin
6. **Ekle** butonuna tıklayın
7. HACS'te **"NotifyAI"** arayın
8. **İndir** butonuna tıklayın
9. **Home Assistant'ı yeniden başlatın**

### Manuel Kurulum

1. Bu repoyu indirin (Code > Download ZIP)
2. `custom_components/notifyai` klasörünü Home Assistant'ınızın `config/custom_components/` dizinine kopyalayın
3. Home Assistant'ı yeniden başlatın

---

## ⚙️ Yapılandırma

### 1. Entegrasyonu Ekleyin

1. **Ayarlar** > **Cihazlar & Hizmetler** > **Entegrasyon Ekle**
2. **"NotifyAI"** arayın
3. **Google Gemini API Anahtarınızı** girin
   - Ücretsiz API anahtarı almak için: [Google AI Studio](https://aistudio.google.com/apikey)
   - Günlük limit çok yüksek, normal kullanımda asla dolmaz

### 2. Bildirim Cihazlarını Tanımlayın (Opsiyonel)

1. **Ayarlar** > **Cihazlar & Hizmetler** > **NotifyAI** kartını bulun
2. **Yapılandır** butonuna tıklayın
3. 4 cihaza kadar bildirim servisi ekleyin:
   - Örnek: `notify.mobile_app_iphone`
   - Örnek: `notify.mobile_app_android`
   - Örnek: `notify.salon_tv`

Artık otomasyonlarda `notify_service` belirtmeden tüm cihazlara otomatik gönderim yapılır!

---

## 🎮 Kullanım

### Basit Kullanım

```yaml
service: notifyai.generate
data:
  event: "Bahçe kapısı açıldı"
  mode: "fun"
```

**Sonuç**:
- **Başlık**: "Kapı Açıldı! 🚪"
- **Mesaj**: "Bahçe kapısı açıldı, misafir mi geldi yoksa kedi mi kaçtı? 🐱"

---

### Tüm Parametreler

```yaml
service: notifyai.generate
data:
  event: "Hareket algılandı"              # Zorunlu: Ne olduğunu yazın
  custom_title: "🚨 Güvenlik Uyarısı"     # Opsiyonel: Özel başlık
  context: "Alarm aktif, gece modu açık"  # Opsiyonel: Ev durumu
  mode: "smart"                           # Opsiyonel: fun, smart, formal, mixed
  persona: "Jarvis"                       # Opsiyonel: AI karakteri
  image_path: "/config/www/kapi.jpg"      # Opsiyonel: Görsel analizi
  notify_service: "notify.mobile_app"     # Opsiyonel: Belirli cihaz
```

---

## 📸 Görsel Zeka Örneği

Kamera görüntüsünü analiz ederek bildirim üretir:

```yaml
service: notifyai.generate
data:
  event: "Kapıda biri var"
  image_path: "/config/www/doorbell_snapshot.jpg"
  mode: "smart"
```

**AI'nın Göreceği**: Görüntüdeki kişi, nesne, durum  
**Üretilen Bildirim**: "Kapıda kargocuyla paket var, imzalı teslimat bekliyor."

---

## 🎭 Karakter Sistemi Örnekleri

### Jarvis (Iron Man'in AI'ı)
```yaml
service: notifyai.generate
data:
  event: "Bulaşık makinesi bitti"
  persona: "Jarvis"
```
**Sonuç**: "Efendim, bulaşıklar temizlendi. Mutfak görevleri tamamlandı."

### Sarkastik Robot
```yaml
service: notifyai.generate
data:
  event: "Çöp kutusu dolu"
  persona: "Sarkastik Robot"
```
**Sonuç**: "Çöp kutusu dolmuş, ama tabii acele etmeyin, ben sadece bir robotum. 🤖"

---

## 🔧 Gelişmiş Kullanım

### Otomasyonda Kullanım

```yaml
automation:
  - alias: "Akıllı Kapı Bildirimi"
    trigger:
      - platform: state
        entity_id: binary_sensor.kapi
        to: "on"
    action:
      - service: notifyai.generate
        data:
          event: "Ön kapı açıldı"
          context: "Evde kimse yok"
          mode: "smart"
```

### Görsel Analiz ile Otomasyon

```yaml
automation:
  - alias: "Kapı Zili - Görsel Analiz"
    trigger:
      - platform: state
        entity_id: binary_sensor.doorbell
        to: "on"
    action:
      - service: camera.snapshot
        target:
          entity_id: camera.kapi
        data:
          filename: "/config/www/doorbell_snapshot.jpg"
      - delay: "00:00:02"
      - service: notifyai.generate
        data:
          event: "Kapı zili çaldı"
          image_path: "/config/www/doorbell_snapshot.jpg"
```

---

## 🎨 Mod Açıklamaları

| Mod | Açıklama | Örnek |
|-----|----------|-------|
| **fun** | Eğlenceli, şakacı, emoji kullanır | "Kapı açıldı, misafir mi geldi yoksa kedi mi kaçtı? 🐱" |
| **smart** | Zeki, bilgilendirici, net | "Ön kapı açıldı. Alarm aktif, saat 23:45." |
| **formal** | Resmi, profesyonel, emoji yok | "Güvenlik uyarısı: Ön kapı sensörü tetiklendi." |
| **mixed** | Rastgele mod seçer | Her seferinde farklı ton |

---

## ❓ Sık Sorulan Sorular

### Ücretli mi?
Hayır! Google Gemini API ücretsiz. Günlük limit çok yüksek, normal kullanımda asla dolmaz.

### OpenAI destekliyor mu?
Hayır, sadece Google Gemini. Protobuf çakışması olmadan çalışması için REST API kullanıyoruz.

### Bildirimler nereye gider?
Ayarlarda tanımladığınız cihazlara otomatik gider. Veya `notify_service` parametresiyle belirli bir cihaza gönderebilirsiniz.

### Görsel analizi nasıl çalışır?
Kamera görüntüsünü Google Gemini'ye gönderir, AI görseli analiz eder ve bildirimi ona göre üretir.

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

---

## 📄 Lisans

MIT License - Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 🙏 Teşekkürler

- Google Gemini API
- Home Assistant Community
- HACS

---

<p align="center">
  Made with ❤️ for Home Assistant
</p>

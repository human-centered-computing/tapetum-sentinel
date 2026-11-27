# Tapetum Sentinel

[English](README.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [العربية](README.ar.md)

Tapetum Sentinel, drone ve saha görüntüleri için tasarlanan açık kaynak, insan merkezli video analizi platformudur. Görüntüleri iyileştirir, göreve özgü nesne tespiti yapar, kanıt içeren üstveriyi saklar ve analiz edilmiş videolar üzerinde yerel, çevrimdışı soru-cevap sağlar.

## Temel ilkeler

- İnsan merkezli dönüşüm
- Varsayılan açık kaynak
- Yerel öncelikli, çevrimdışı çalışabilme
- Modelden bağımsız mimari
- Kanıta dayalı yanıtlar
- Doğrulanmış geri bildirimle sürekli iyileştirme

## İş hattı

```text
Video / Drone Feed
        |
        v
Retinex Tapetum Enhancement
        |
        v
Task-Specific YOLO Detection
        |
        v
Tracking + Metadata Fusion
        |
        v
Local Database + Evidence Index
        |
        v
Local LLM / RAG Question Answering
```

## Depo yapısı

- `apps/`: Masaüstü ve API uygulamaları
- `services/`: İyileştirme, tespit, izleme, bilgi ve yerel LLM servisleri
- `training/`: Colab odaklı eğitim ve değerlendirme
- `feedback/`: Etiketleme, doğrulama ve veri kümesi dışa aktarma
- `model-registry/`: Kullanıcı görevlerinin modellere eşlenmesi
- `database/`: Şemalar ve geçişler
- `docker/`: Docker varlıkları
- `docs/`: Mimari ve karar kayıtları

## Model dağıtımı

Kaynak kod GitHub'da tutulur. Eğitilmiş kontrol noktaları ve model kartlarının Hugging Face'te yayımlanması planlanır. Uygulama, afet veya tarım analizi gibi görevleri model kaydı üzerinden sürümlü modellere eşler.

## Durum

İlk mimari iskelet. Bileşenler, kararlı servis sözleşmeleri arkasında aşamalı gerçekleştirilecektir.

## Lisans

GNU Affero General Public License v3.0 (AGPL-3.0). [LICENSE](LICENSE) dosyasına bakın. Ağ üzerinden sunulan değiştirilmiş kapsamdaki yazılımlar için AGPL kaynak erişilebilirliği hükümleri geçerlidir.

graph TD
    subgraph Donanim_Girdileri [Donanım & Sensörler]
        S[Kan Şekeri Sensörü] -->|Elektriksel Sinyal| A[Sensör Veri Analizörü]
    end

    subgraph Yazilim_Islem_Katmani [Yazılım Mantığı ve Denetleyici]
        A -->|Glikoz Seviyesi| C[İnsülin Doz Hesaplayıcı]
        C -->|Gerekli Doz Miktarı| P[Pompa Sinyal Oluşturucu]
        
        K[Sistem Saati / Zamanlayıcı] -->|Periyodik Tetikleme| A
        LOG[(Doz Kayıt Veritabanı)] <--- P
    end

    subgraph Donanim_Ciktilari [Eylemciler & İkaz Sistemleri]
        P -->|Atım Sinyali| Pump[İnsülin Pompası]
        P -->|Limit Aşımı / Hata| Alarm[Sesli & Görsel Alarm]
        P -->|Bilgi| Display[Ekran / Gösterge]
    end

    style S fill:#f9f,stroke:#333,stroke-width:2px
    style Pump fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px

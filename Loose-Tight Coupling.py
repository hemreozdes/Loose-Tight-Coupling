from abc import ABC, abstractmethod

# Doğrudan somut sınıfa bağımlılık
class EpostaGondericiTight:
    def eposta_gonder(self, mesaj):
        print(f"E-posta gönderildi: {mesaj}")
    
class BildirimServisiTight:
    def __init__(self):
        # Sıkı bağlılık: BildirimServisi kendi içinde EpostaGonderici'yi üretiyor
        self.eposta = EpostaGondericiTight()
        
    def bildirim_yap(self, mesaj):
        self.eposta.eposta_gonder(mesaj)

# 1. Soyut Arayüz (Contract)
class IBildirimKanalı(ABC):
    @abstractmethod
    def gonder(self, mesaj: str):
        pass

# 2. Somut Uygulamalar
class EpostaGonderici(IBildirimKanalı):
    def gonder(self, mesaj: str):
        print(f"E-posta: {mesaj}")

class SmsGonderici(IBildirimKanalı):
    def gonder(self, mesaj: str):
        print(f"SMS: {mesaj}")

# 3. Gevşek Bağlı Servis
class BildirimServisi:
    def __init__(self, kanal: IBildirimKanalı):
        # Gevşek bağlılık: Servis somut sınıfa değil, arayüze bağımlıdır
        self.kanal = kanal

    def bildirim_yap(self, mesaj: str):
        self.kanal.gonder(mesaj)

# Kullanım:
sms_kanali = SmsGonderici()
servis = BildirimServisi(sms_kanali)  # İstediğimiz kanalı dışarıdan enjekte edebiliriz
servis.bildirim_yap("Siparişiniz kargoya verildi.")

email_kanali = EpostaGonderici()
servis_email = BildirimServisi(email_kanali)  # Farklı bir kanal ile aynı servisi kullanabiliriz
servis_email.bildirim_yap("Siparişiniz teslim edildi.")

tight_servis = BildirimServisiTight()  # Sıkı bağlı servis
tight_servis.bildirim_yap("Sıkı bağlı bildirim.")  # Sıkı bağlı servisin kullanımı, kanal değiştirilemez.




    
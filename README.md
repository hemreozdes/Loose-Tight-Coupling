## Mimari Diyagramı (UML Sınıf Diyagramı)

Aşağıdaki diyagramda, sıkı bağlılık (Tight Coupling) ile gevşek bağlılık (Loose Coupling / Dependency Inversion) arasındaki mimari fark gösterilmektedir:

```mermaid
classDiagram
    namespace Tight_Coupling_Siki_Baglilik {
        class TightOrderProcessor {
            -EmailSender email_sender
            +process_order(order_details)
        }
        class EmailSender {
            +send_email(message)
        }
    }

    namespace Loose_Coupling_Gevsek_Baglilik {
        class NotificationService {
            <<Interface / Abstract Class>>
            +send(message)*
        }
        class EmailNotificationService {
            +send(message)
        }
        class SMSNotificationService {
            +send(message)
        }
        class LooseOrderProcessor {
            -NotificationService notification_service
            +process_order(order_details)
        }
    }

    %% Bağımlılık İlişkileri
    TightOrderProcessor --> EmailSender : Doğrudan Bağımlı (Somut Sınıf)
    
    EmailNotificationService ..|> NotificationService : Implements
    SMSNotificationService ..|> NotificationService : Implements
    LooseOrderProcessor --> NotificationService : Soyutlamaya Bağımlı (Interface/ABC)
```

### Yapısal Açıklama:
1. **Sıkı Bağlılık (Tight Coupling):** `TightOrderProcessor`, e-posta göndermek için doğrudan somut `EmailSender` sınıfına bağlıdır. Başka bir bildirim yöntemine geçmek için kod değişikliği ve refactoring gerekir.
2. **Gevşek Bağlılık (Loose Coupling):** `LooseOrderProcessor`, somut sınıflar yerine `NotificationService` soyutlamasına (Interface / Abstract Class) bağlıdır. `EmailNotificationService` veya `SMSNotificationService` sınıfları bu arayüzü uyguladığı için sisteme yeni bir bildirim yöntemi eklemek var olan kodu değiştirmeyi gerektirmez (Open/Closed Principle).
